import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-042e8287309f5df03',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='Firstkey'
 )