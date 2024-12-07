resource "aws_db_instance" "main" {
  vpc_security_group_ids = [aws_security_group.rds.id] 
  allocated_storage      = 20
  instance_class         = "db.t3.micro" 
  engine                 = "postgres"
  engine_version         = "11.22"
  identifier             = "mydb-instance" 
  username               = "admin_user"
  password               = "password"
  db_name                = "mydb"
  skip_final_snapshot    = true
  publicly_accessible    = false
  db_subnet_group_name   = aws_db_subnet_group.main.name  
}

resource "aws_security_group" "rds" {
  name        = "rds-security-group"
  description = "Allow access to RDS"
  vpc_id      = var.vpc_id  # Usar el ID de VPC correcto

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_subnet_group" "main" {
  name       = "my-db-subnet-group"
  subnet_ids = var.private_subnets

  tags = {
    Name = "My DB Subnet Group"
  }
}
