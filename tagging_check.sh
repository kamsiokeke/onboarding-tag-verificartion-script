#!/bin/bash

# This script will automate the process of verification of the presence of chef nodes

set -eu
# Fetch customer account role from config

# Grab the tag values
cat chef_onboarded_nodes.txt | grep -oG "i-0.*" > org_ver_2.txt
cat ~/Desktop/onboarding_verification/regions.txt | while read line
do 
    aws resourcegroupstaggingapi get-resources --region="$line" --resource-type-filters ec2:instance\
    --tag-filters Key="Cloudreach Backup Group",Values=$1 | grep "Value" >> ~/Desktop/onboarding_verification/tag_compliance_check.txt
done

# python3 verification_script.py
python3 patching_verification.py