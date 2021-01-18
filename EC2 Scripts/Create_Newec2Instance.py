# Create New instance in AWS using Python boto3

# AUTHOR: Yogananda - 18/01/2021

import boto3
client=boto3.client("ec2")

response = client.run_instances(ImageId='ami-0a9d27a9f4f5c0efc',
                     InstanceType='t2.micro',
                     MinCount=1,
                     MaxCount=1)
for instance in response['Instances']:
    instance_id = instance['InstanceId']


