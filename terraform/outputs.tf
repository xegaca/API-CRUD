output "vpc_id" {
  value = module.vpc.vpc_id
}

output "ecs_service_arn" {
  value = module.ecs.service_arn
}

output "rds_endpoint" {
  value = module.rds.db_instance_endpoint
}
