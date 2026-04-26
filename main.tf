module "vpc" {
  source     = "./modules/vpc"
  vpc_cidr   = var.vpc_cidr
  aws_region = var.aws_region
  tags       = var.common_tags
}

module "lambda" {
  source     = "./modules/lambda"
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnet_ids
  tags       = var.common_tags
}