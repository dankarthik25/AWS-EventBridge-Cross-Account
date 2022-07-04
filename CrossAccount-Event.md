
# How to Add Eventbridge to Infrastructure AWS-Account

Go to developer AWS Account <<Developer-Account-Id>> where sourcecode(git code) is push or uploaded
Follow the steps 
- Navigate to the Rules in EventBridge 
  -In EventBridge console Left-SideBar Under =Events=  select =Event Buses=
  
- Create Rule and Start the default EventBus
  - Default *event bus* name= =default= Select =ACTION= and start =Discovery=
  - Select =default= Event bus and create Rule
- Create rule with  =Event Pattern=  *Rule with an event pattern*
  - In *Sample event -optional* select
    - *Enter my own*
  - In *Event pattern* select
    - *Custom pattern (JSON editor)* and past below code
      - In repalce ="resources"= value with CodeCommit Repo *ANR*
      - Replace <<branch-name>> with your own branch name
```
      {
        "detail-type": ["CodeCommit Repository State Change"],
        "resources": ["arn:aws:codecommit:<<Region>>:<<DEV-ACCOUNT-ID>>:<<Codecommit-Repo>>"],
        "source": ["aws.codecommit"],
        "detail": {
          "referenceType": ["branch"],
          "event": ["referenceCreated", "referenceUpdated"],
          "referenceName": ["<<branch-name>>"]
        }
      }
``` 
- You have CREATED RULE for EventBridge

- Select the target
- In the Select targets panel:
    - For Target, select Event bus in a  different account <<Infrastructure-Account-Id>>  or Region.
      I have created =Eventbus= name: =mybus= here is the [link](https://us-east-1.console.aws.amazon.com/events/home?region=us-east-1#/eventbus/mybus "link1") and its ANR=arn:aws:schemas:us-east-1:548593215839:discoverer/events-event-bus-mybus
      
    - For Event Bus, enter the ARN =arn:aws:schemas:us-east-1:548593215839:discoverer/events-event-bus-mybus=  of the target event bus.
      
    - Keep the selected option Create a new role for this specific resource. This creates the necessary IAM permissions to allow the rule to put events on the target bus.
	
  [![adsfas](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2021/04/12/crossregion2.png "adsfas")](https://d2908q01vomqb2.cloudfront.net/1b6453892473a467d07372d45eb05abc2031647a/2021/04/12/crossregion2.png "adsfas")

Go to <<Infrastructure-Accound-Id>  EventBuses name : mybus
- For EventBus : =mybus= give Permissions to <<Developer-Account-Id>> to =putEvents=
  - Replace [DEV-ACCOUNT-ID] with your AWS-Account Id
```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "allow_account_to_put_events",
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::918175365727:root"
      "AWS": "arn:aws:iam::[DEV-ACCOUNT-ID]:root"
    },
    "Action": "events:PutEvents",
    "Resource": "arn:aws:events:us-east-1:548593215839:event-bus/mybus"
  }, {
    "Sid": "allow_account_to_manage_rules_they_created",
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::918175365727:root"
      "AWS": "arn:aws:iam::[DEV-ACCOUNT-ID]:root"
    },
    "Action": ["events:PutRule", "events:PutTargets", "events:DeleteRule", "events:RemoveTargets", "events:DisableRule", "events:EnableRule", "events:TagResource", "events:UntagResource", "events:DescribeRule", "events:ListTargetsByRule", "events:ListTagsForResource"],
    "Resource": "arn:aws:events:us-east-1:548593215839:rule/mybus",
    "Condition": {
      "StringEqualsIfExists": {
        "events:creatorAccount": "arn:aws:iam::918175365727:root"
        "events:creatorAccount": "arn:aws:iam::[DEV-ACCOUNT-ID]:root"
      
      }
    }
  }]
}
```    
- Create Event Pattern Rules
  - paste codecommit EventBridge Rule in <<DEV-ACCOUND-ID>> to <<Infrastructure-Account-Id>>
      - In repalce ="resources"= value with CodeCommit Repo *ANR*
      - Replace <<branch-name>> with your own branch name   
```      {
        "detail-type": ["CodeCommit Repository State Change"],
        "resources": ["arn:aws:codecommit:<<Region>>:<<DEV-ACCOUNT-ID>>:<<Codecommit-Repo>>"],
        "source": ["aws.codecommit"],
        "detail": {
          "referenceType": ["branch"],
          "event": ["referenceCreated", "referenceUpdated"],
          "referenceName": ["<<branch-name>>"]
        }
      }
```

- You have CREATED RULE for EventBridge
- You can Choose Target like CodeBuild, Codedeploy, CodePipeline
  -Chose ECS (Bluegreen/Green) CodePipeline 
