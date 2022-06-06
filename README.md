# CI/CD pipeline 
A CI/CD pipeline with docker images scheduled and executed by Airflow

![CI-CD-4](https://user-images.githubusercontent.com/17614336/172147450-714fe9ff-acbd-4ce6-9774-4e0f6a8f531a.jpg)


The pipeline shows when a developer upadtes any code in their local machine and committs to github, creates pull request and triggers a azure ci/cd pipline which puts the uploads to S3 and builds docker images and pushes into ECR(AWS managed docker repository).

## Sections of the use case:
We can logically divide the use case into this below sections:

1. Developer develops/updates application code in test driven approach.
2. CI/CD triggers
3. Docker images built and pushed to ECR
4. AWS managed Docker (ECS) get executed by AWS managed Airflow DAG.

