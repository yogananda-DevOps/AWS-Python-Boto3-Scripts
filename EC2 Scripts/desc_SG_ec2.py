# Displays the security groups

# AUTHOR: Yogananda - 18/01/2021

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=['sg-e9495d90']) # security group id
    print(response)
except ClientError as e:
    print(e)
