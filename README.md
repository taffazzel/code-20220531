# CI/CD pipeline 
A CI/CD pipeline with docker images scheduled and executed by Airflow

![CI-CD-4](https://user-images.githubusercontent.com/17614336/172147450-714fe9ff-acbd-4ce6-9774-4e0f6a8f531a.jpg)


The pipeline shows when a developer upadtes any code in their local machine and committs to github, creates pull request and triggers a azure ci/cd pipline which puts the uploads to S3 and builds docker images and pushes into ECR(AWS managed docker repository).

## Use case
