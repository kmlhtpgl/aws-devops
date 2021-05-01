import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-04444dfca0de5b704').stop()