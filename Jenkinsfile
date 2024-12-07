pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'xegaca/API-CRUD-IMG' 
    }
    stages {
        stage('Clonar código fuente') {
            steps {
                // Clona el repositorio desde GitHub
                git branch: 'main', url: 'https://github.com/xegaca/API-CRUD.git' 
            }
        }
        stage('Instalar dependencias') {
            steps {
                script {
                    // Instala las dependencias usando pip
                    sh 'pip install --no-cache-dir -r requirements.txt'
                }
            }
        }
        stage('Ejecutar Tests') {
            steps {
                script {
                    // Ejecuta pytest con cobertura
                    def coverageOutput = sh(script: 'pytest --cov=app --cov-report=term-missing', returnStdout: true).trim()
                    echo coverageOutput
                    
                    // Extrae el porcentaje de cobertura de la salida
                    def coverageMatch = coverageOutput =~ /TOTAL\s+\d+\s+\d+\s+(\d+)%/
                    if (coverageMatch.find()) {
                        def coverage = coverageMatch[0][1] as Integer
                        echo "Cobertura de código: ${coverage}%"
                        if (coverage < 80) {
                            error "La cobertura de código (${coverage}%) es inferior al 80%. Se detiene la ejecución del pipeline."
                        }
                    } else {
                        error "No se pudo determinar la cobertura de código. Se detiene la ejecución del pipeline."
                    }
                }
            }
        }
        stage('Linting') {
            steps {
                script {
                    // Ejecuta flake8 para verificar el estilo del código
                    try {
                        sh 'flake8 --max-line-length=79'
                        echo "No se encontraron errores de linting."
                    } catch (Exception e) {
                        error "Se encontraron errores de linting. Se detiene la ejecución del pipeline."
                    }
                }
            }
        }
        stage('Construir Imagen Docker') {
            steps {
                script {
                    // Construye la imagen Docker
                    sh 'docker build -t ${DOCKER_IMAGE}:${env.BUILD_ID} .'
                }
            }
        }
        stage('Subir Imagen a Docker Registry') {
            when {
                branch 'main'
            }
            steps {
                script {
                    // Inicia sesión en Docker Hub
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        // Subir la imagen Docker
                        sh 'docker push ${DOCKER_IMAGE}:${env.BUILD_ID}'
                    }
                }
            }
        }
    }
    post {
        always {
            echo "Pipeline finalizado."
        }
        success {
            echo "Pipeline completado con éxito."
        }
        failure {
            echo "Pipeline falló. Revisa los logs para más detalles."
        }
    }
}