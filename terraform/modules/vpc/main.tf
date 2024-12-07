resource "aws_vpc" "main" {
  cidr_block           = var.cidr_block
  enable_dns_support   = true
  enable_dns_hostnames = true
}

resource "aws_subnet" "public" {
  count             = 2
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 4, count.index)
  vpc_id            = aws_vpc.main.id
  map_public_ip_on_launch = true
}

resource "aws_subnet" "private" {
  count      = 2
  cidr_block = cidrsubnet(aws_vpc.main.cidr_block, 4, count.index + 2)
  vpc_id     = aws_vpc.main.id
}

