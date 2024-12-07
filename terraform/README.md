# API-CRUD

### Bootcamp de DevOps. Entrega Sprint10. Parte 3 - Infraestructura como código.

Este proyecto implementa una infraestructura en AWS utilizando Terraform. La infraestructura está diseñada para soportar una aplicación escalable basada en contenedores, con una base de datos relacional gestionada y una red configurada para garantizar seguridad y rendimiento.

## Recursos Implementados

1.	VPC (Virtual Private Cloud):
	- Red privada para alojar recursos de AWS.
	- Subredes públicas y privadas para organizar los recursos:
    	- Subredes públicas: Alojamiento de recursos accesibles desde Internet.
    	- Subredes privadas: Alojamiento de recursos sensibles, como la base de datos.
2.	ECS (Elastic Container Service):
	- Gestión de contenedores para aplicaciones escalables.
	- Contenedor configurado con `nginx` para servir una aplicación web.
	- Definición de tareas y roles IAM necesarios para la ejecución segura de las tareas.
3.	RDS (Relational Database Service):
	- Base de datos relacional PostgreSQL gestionada.
	- Configuración de subredes privadas para la seguridad de la base de datos.
	- Grupo de seguridad para permitir acceso controlado a la base de datos.

## Requisitos Previos

- [Terraform](https://www.terraform.io/downloads.html) instalado en tu máquina.
- Credenciales de AWS configuradas en tu máquina.
- Acceso a la consola de AWS para revisar los recursos desplegados.

## Estructura del Proyecto

```
├── main.tf                # Archivo principal de Terraform que configura los módulos.
├── outputs.tf             # Definición de salidas del proyecto (endpoints y ARN).
├── terraform.tfvars       # Variables personalizables del proyecto.
├── variables.tf           # Declaración de variables globales.
├── modules/
    ├── vpc/               # Configuración del módulo VPC.
    │   ├── main.tf        # Implementación de la VPC y subredes.
    │   ├── outputs.tf     # Salidas del módulo VPC.
    │   ├── variables.tf   # Variables para la VPC.
    ├── ecs/               # Configuración del módulo ECS.
    │   ├── main.tf        # Implementación de ECS Cluster, servicios y roles.
    │   ├── outputs.tf     # Salidas del módulo ECS.
    │   ├── variables.tf   # Variables para ECS.
    ├── rds/               # Configuración del módulo RDS.
        ├── main.tf        # Implementación de la base de datos RDS.
        ├── outputs.tf     # Salidas del módulo RDS.
        ├── variables.tf   # Variables para RDS.
```

## Cómo Usar este Proyecto

1.	Clonar el repositorio:

git clone https://github.com/xegaca/API-CRUD.git
cd API-CURL/terraform


2.	Inicializar Terraform:

```bash
terraform init
```

3.	Revisar el plan de ejecución:

```bash
terraform plan
```

4.	Aplicar los cambios:

```bash
terraform apply
```

5.	Obtener las salidas:
Al finalizar la ejecución, Terraform mostrará los valores importantes, como:
	- Endpoint de la base de datos RDS.
	- ARN del servicio ECS.
	- ID de la VPC creada.

## Variables Personalizables

Las variables se configuran en el archivo `terraform.tfvars`. Algunas variables clave incluyen:

- `region`: Región de AWS donde se desplegarán los recursos. Por defecto: `us-east-1`.
- `cidr_block`: Bloque CIDR para la red VPC. Por defecto: `10.0.0.0/16`.
- `app_name`: Nombre de la aplicación (para ECS). Por defecto: `scalable-app`.

## Salidas Principales

El proyecto genera las siguientes salidas visibles tras la ejecución de Terraform:
- `vpc_id`: ID de la VPC creada.
- `ecs_service_arn`: ARN del servicio ECS.
- `rds_endpoint`: Endpoint de la base de datos RDS.

## Notas Importantes

- La base de datos RDS tiene acceso restringido mediante un grupo de seguridad; asegúrate de conectar desde las instancias correctas.
- El contenedor utiliza la imagen `nginx`, pero puede ser reemplazada por cualquier otra imagen adaptada a tu aplicación.
- Las credenciales para RDS (`username` y `password`) están configuradas como variables en el código y deben protegerse adecuadamente.

## Posibles Extensiones

- **Escalado automático**: Configurar políticas de escalado en ECS para manejar cargas variables.
- **Balanceador de carga**: Integrar un Elastic Load Balancer (ELB) para distribuir tráfico hacia los contenedores.
- **Almacenamiento adicional**: Conectar un bucket S3 para gestionar archivos estáticos.

## Licencia

Este proyecto está licenciado bajo la `MIT License`.

## Autor

Jesús Gallego