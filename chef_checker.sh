#!/bin/bash

# This script will automate the process of verification of the presence of chef nodes

set -eu
cd ~/repos/chef_orgs/$1
cat ~/Desktop/onboarding_verification/org_ver.txt | while read line ; do knife node list | grep $line >> ~/Desktop/onboarding_verification/chef_onboarded_nodes.txt; done
cat ~/Desktop/onboarding_verification/onboarded_nodes.txt | while read line ; do knife node show | grep Recipe >> ~/Desktop/onboarding_verification/onboarded_nodes_recipies.txt; done
python3 chef_ver_script.py
echo "Next steps:
Validation of patching and backup tags on instances, use Roller to assume a role in the customer account
e.g. roller --profile default --account xxxxxxxxxxxxx --role CloudreachAdminRole --name <aws_account_name>"