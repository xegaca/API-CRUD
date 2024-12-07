provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source    = "./modules/vpc"
  cidr_block = "10.0.0.0/16"
}

module "ecs" {
  source         = "./modules/ecs"
  app_name       = "my-scalable-app"
  vpc_id         = module.vpc.vpc_id  
  public_subnets = module.vpc.public_subnets
  private_subnets = module.vpc.private_subnets
}

module "rds" {
  source         = "./modules/rds"
  vpc_id         = module.vpc.vpc_id 
  private_subnets = module.vpc.private_subnets
}
