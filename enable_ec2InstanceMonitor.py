# To Enable and Disable monitoring on ec2 instances, Pass the instance id as argument to script

# AUTHOR: Yogananda - 18/01/2021

import sys
import boto3


ec2 = boto3.client('ec2')
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
print(response)
