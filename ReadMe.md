# Step for creating CI/CD Cross-Account ECS BLUE Green Deploy



## Step 1 : Create CI/CD in own Acccount 

- Create AWS Resources and Task using own cloudformation template

```
aws cloudformation deploy --template-file pipelinecf.yaml --stack-name pipeline-build --parameter-overrides Key1=Value1 Key2=Value2 --tags Key1=Value1 Key2=Value2

aws cloudformation update-stack-instances --stack-set-name my-awsconfig-stackset --parameter-overrides ParameterKey=MaximumExecutionFrequency,ParameterValue=TwentyFour_Hours\\,Twelve_Hours --operation-preferences FailureToleranceCount=0,MaxConcurrentCount=1 --accounts '["012345678901"]' --regions '["eu-west-1", "us-west-2"]'

```
BranchName: master
ContainerPort  : 80 
RepositoryName: calci-app
Stage: poc

```
aws cloudformation deploy --template-file Fargate-Cluster.yaml --stack-name poc-dk-ecs-cluster --parameter-overrides Key1=Value1 Key2=Value2 --tags Key1=Value1 Key2=Value2

```

image uri(ecr latest):
container-port: 




Above cmd will Create following infrastructure :
- Build Docker image , 
- Create and push image to ECR repo 
- Auto Docker build using code pipeline
- Create ECS Cluster 

Note: there is error in cloudformation templete the container-image ecr image path is wrong so need to create a new version 

```
dev-548593215839-ecr-repository:7d4414f
```

- Create new version of Task Defination where ecr path is latest 


Note: There are some limitation in cloudformation template there is no provision for roll-back update and blue-green update. 

So we have to manually need to 

- Delete the pervious ECS Service 
- Create new ECS Service with update policy blue-green which automatically create CodeDeploy Task 

    Follow the link how to create BlueGreen-ECS-Service 

- Create ECR BlueGreen Pipeline using below artical 
    Note: use source artifacts than build artifacts

    https://catalog.us-east-1.prod.workshops.aws/workshops/4b59b9fb-48b6-461c-9377-907b2e33c9df/en-US/devopspipeline/ecswithec2/codepipeline

    https://aws.plainenglish.io/aws-codepipeline-for-amazon-ecs-part-2-a-blue-green-deployment-type-c162fd73be91

    https://github.com/polovyivan/aws-ecs-pipeline-with-blue-green-deployment



