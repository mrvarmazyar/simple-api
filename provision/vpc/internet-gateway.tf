resource "aws_internet_gateway" "api-vpc-internet-gateway" {
  vpc_id = "${aws_vpc.api-vpc.id}"

  tags {
    Name = "api-vpc-internet-gateway"
  }
}
