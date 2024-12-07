variable "region" {
  default = "us-east-1"
}

variable "cidr_block" {
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "app_name" {
  description = "Application name"
  default     = "scalable-app"
}
