# The program lists all the ec2 instances and stops if any instance is running

# AUTHOR: Yogananda - 18/01/2021

import boto3
ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    print(
        "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
            instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
        )
    )
    print('Instance with ID {} is  {}'  .format(
        instance.id, instance.state["Name"]))
    if(instance.state["Name"] == 'running'):
        ec2.Instance(instance.id).stop()
