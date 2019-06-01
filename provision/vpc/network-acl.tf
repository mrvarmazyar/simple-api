resource "aws_network_acl" "api-vpc-network-acl" {
    vpc_id = "${aws_vpc.api-vpc.id}"
    subnet_ids = ["${aws_subnet.api-vpc-subnet1.id}", "${aws_subnet.api-vpc-subnet2.id}"]

    egress {
        protocol   = "-1"
        rule_no    = 100
        action     = "allow"
        cidr_block = "0.0.0.0/0"
        from_port  = 0
        to_port    = 0
    }

    ingress {
        protocol   = "-1"
        rule_no    = 100
        action     = "allow"
        cidr_block = "0.0.0.0/0"
        from_port  = 0
        to_port    = 0
    }

    tags {
        Name = "api-vpc-network-acl"
    }
}
