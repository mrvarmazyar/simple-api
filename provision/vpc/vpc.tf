resource "aws_vpc" "api-vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = "true"

  tags {
    Name = "api-vpc"
  }
}

output "id" {
  value = "${aws_vpc.api-vpc.id}"
}
