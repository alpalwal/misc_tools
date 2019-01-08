# D9-sns-to-elasticsearch
Send events from SNS to AWS Elasticsearch
 
Adapted from AWS' project on this: https://github.com/awslabs/amazon-elasticsearch-lambda-samples

## Setup
- Create a new Lambda function with a blank template
- Set your SNS topic as the trigger
- Paste in the code from index.js - be sure to update the variables with the details of your cluster
- Set up your IAM role so that the function has permissions to send events to ES
- Save it and you're good to go!

## To Do
- Rewrite with serverless wrapper
- Break the message into JSON for better parsing
