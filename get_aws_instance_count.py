#!/usr/bin/env python
#Python script for getting a list of all instances in ALL regions in an AWS account. 
#This runs on the default CLI profile by default. If you want to change that, run 'export AWS_PROFILE=<yourProfileName>' before executing the script
#Taken from here: https://stackoverflow.com/questions/40164786/determine-how-many-aws-instances-are-in-a-zone

import boto.ec2

for region in [r for r in boto.ec2.regions() if r.name not in ['cn-north-1', 'us-gov-west-1']]:
  conn = boto.ec2.connect_to_region(region.name)
  reservations = conn.get_all_instances()
  for r in reservations:
    for i in r.instances:
      print region.name, i.id, i.tags, i.state
