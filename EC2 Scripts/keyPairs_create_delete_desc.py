# To create new key pair 
# To Descibe key pair
# To Delete a key pair

# AUTHOR: Yogananda - 18/01/2021

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs() # To descibe the key pairs
print(response)

response1 = ec2.create_key_pair(KeyName='devKeyPair') # To create new key pair
print(response1)

response2 = ec2.delete_key_pair(KeyName='devKeyPair') # To delete an existing key pair
print(response2)

