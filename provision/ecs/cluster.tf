resource "aws_ecs_cluster" "api-ecs-cluster" {
    name = "${var.ecs-cluster-name}"
}
