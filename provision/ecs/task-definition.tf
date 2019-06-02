resource "aws_ecs_task_definition" "api-sample-definition" {
    family                = "api-sample-definition"
    #container_definitions = "${file("./ecs/api.json")}"
    container_definitions = "${template_file.api-template.rendered}"
}
