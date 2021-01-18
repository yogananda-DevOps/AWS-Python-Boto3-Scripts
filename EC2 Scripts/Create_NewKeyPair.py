# Script to create key-pair for AWS-ec2 instance

# AUTHOR: Yogananda - 18/01/2021

import boto3

ec2_client = boto3.client("ec2")
key_pair=ec2_client.create_key_pair(KeyName="KeyPair_Dev")