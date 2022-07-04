# Step for creating CI/CD Cross-Account ECS BLUE Green Deploy

##

## Step 1 : Create CI/CD in own Acccount 

- Create AWS Resources and Task using own cloudformation template

```
aws cloudformation deploy --template-file pipelinecf.yaml --stack-name pipeline-build --parameter-overrides Key1=Value1 Key2=Value2 --tags Key1=Value1 Key2=Value2

```
Parameters of cloudformation 

- BranchName: master
- ContainerPort  : 80 
- RepositoryName: calci-app
- Stage: poc

Above cmd will Create following infrastructure :
- Build Docker image , 
- Create and push image to ECR repo 
- Auto Docker build using code pipeline
- Create ECS Cluster 

Note: there is error in cloudformation(pipelinecf.yaml) templete the container-image ecr image path is wrong so need to create a new version 

```
ERROR: image uri:  dev-548593215839-ecr-repository:7d4414f
```

- Create new version of Task Defination where ecr path is latest

> ERROR in pipelinecf.yaml:
>
>    - Update the Task Defination 
>        - change container image to  "dev-548593215839-ecr-repository:latest"
>        - Copy "Task definatin ARN" and "container-name" to appspec.json file
>        - Copy "Task defination JSON" to "taskdef.json"
>    - Delete older version of Task Defination



Note: There are some limitation in cloudformation template there is no provision for roll-back update and blue-green update. 

So we have to manually need to update the ECS-Cluster

```
- Delete the pervious ECS Service 
- Create new ECS Service with update policy blue-green which automatically create CodeDeploy Task
    - Delete old Service 
    - Create New Service 
       - select new task which is created 
       - seletct blue green deployment  
            - Select blue green deploy method 
                - AllatOnce  [ Not 10% for very 10 mints, 15 mints, 20 mints]
        - Application load balancer 
            - select port : 80 (NO TESTING)
            - select load balancer : 
                - select Target Group 
                - Create New Target Group in drop down menu
    - Save Service (Automaticaly Create new CodeDeploy (Application, DeployGroup)
        - Test 
            - Go to DeployGroup 
                - online editor upload appspec.yaml 
                - test deploy 

- Your Deployment is SUCESSFULL

```
```
- Create a PIPELINE 
    - Add Source code and build 
    - In Deploy select : ECS(BLUE/GREEN)
      either select (source or build artifact) and upload the artifacts


- Your Pipeline is SUCESSFULL 
```

    Follow the link how to create BlueGreen-ECS-Service 

- Create ECR BlueGreen Pipeline using below artical 
    Note: use source artifacts than build artifacts

    https://catalog.us-east-1.prod.workshops.aws/workshops/4b59b9fb-48b6-461c-9377-907b2e33c9df/en-US/devopspipeline/ecswithec2/codepipeline

    https://aws.plainenglish.io/aws-codepipeline-for-amazon-ecs-part-2-a-blue-green-deployment-type-c162fd73be91

    https://github.com/polovyivan/aws-ecs-pipeline-with-blue-green-deployment

Extra 

```
aws cloudformation deploy --template-file Fargate-Cluster.yaml --stack-name poc-dk-ecs-cluster --parameter-overrides Key1=Value1 Key2=Value2 --tags Key1=Value1 Key2=Value2

```

