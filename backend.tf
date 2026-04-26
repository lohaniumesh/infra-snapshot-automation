terraform {
  required_version = ">= 1.0.0"
  # Replace with your S3 bucket and DynamoDB table
  # backend "s3" {
  #   bucket         = "my-terraform-state"
  #   key            = "ec2-cleaner/terraform.tfstate"
  #   region         = "us-east-1"
  #   dynamodb_table = "terraform-lock"
  # }
}
