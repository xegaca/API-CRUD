variable "app_name" {
  description = "Name of the application"
}

variable "vpc_id" {
  description = "VPC ID"
}

variable "public_subnets" {
  description = "List of public subnet IDs"
  type        = list(string)
}

variable "private_subnets" {
  description = "List of private subnet IDs"
  type        = list(string)
}
