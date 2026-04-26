This README provides the documentation for infra-snapshot-automation. I have used modular approach to mimic the code with production grade IaC.

1. Chosen IaC Tool: I choose Terraform because it is cloud agnostic tool and modular.

2. How to Execute the IaC:
Initiate Terraform by executing below command

terraform init

Then run a dry run by executing

terraform plan

Once everything looks good in plan execute it by running 

terraform apply


3. How to Deploy the Lambda Function Code: Lambda function will also be deployed with Terrafrom execution along with infra creation. Since IaC follows idempotent principal, any code changes in Lambda later will only apply to Lambda.

4. How to configure the Lambda function to run within the VPC: The Lambda is configured to run inside the VPC using the vpc_config block:
Subnet IDs: It is assigned to the Private Subnet created by the VPC module.
Security Group IDs: A dedicated Security Group allows the Lambda to send outbound traffic on Port 443 to reach the EC2 VPC Interface Endpoint.

5. Assumptions
Region: The project defaults to us-east-1, you can change the region by updating the entry in terraform.tfvars
I have created backend.tf but commented for now to make the execution simpler. This code wil create the tfstate file locally but in actual enterprise environments we need to update the file for tfstate file management through S3 and Dynamo DB, in case of Terraform enterprise we need to update it accordingly.

6. Monitoring
CloudWatch Logs: Every action is logged. You can view these in the Log Group: /aws/lambda/snapshot-cleaner.
CloudWatch Metrics: You can track the invocations count and errors in the Lambda dashboard to ensure the daily trigger is working.

7. Design Diagram
Please refer design.png