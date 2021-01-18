
# To delete a security group

# The Argument is SG -ID

# AUTHOR: Yogananda - 18/01/2021

import boto3
from botocore.exceptions import ClientError

# Create EC2 client
ec2 = boto3.client('ec2')

# Delete security group
try:
    response = ec2.delete_security_group(GroupId='sg-0dc28699c6a9d5a9b')  # SECURITY_GROUP_ID
    print('Security Group Deleted')
except ClientError as e:
    print(e)
