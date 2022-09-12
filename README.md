# cr-onboarding-verification

Tool used to automate the verification process of isntance onboarding.
A complete setup will:
- Create compare the list of onboarded instances with available chef nodes.
- Validate if the of the onboarded instances have patching group tags.

## Initial setup

* Ensure you have any of the following versions of python 3.9.10 3.8.12 3.7.11 3.6.6
* Set up [Roller](https://github.com/cloudreach-coreops/roller) to access the customer environment via the CLI
* roller --profile default --account <aws_account_number> --role CloudreachAdminRole --name <account_name>

## Configuration


### Common tags

CloudreachSupport: BaseSupport
CloudreachSupport: PlatformOnly
Cloudreach Backup Group: <custom_value>
Cloudreach Backup Ignore: <custom_value>
Cloudreach Patching Event: <custom_value>
Cloudreach Patching Phase: <custom_value>
Cloudreach Patching Group: <custom_value>
Cloudreach Patching Ignore: <custom_value>

# Steps
> Paste the below code to pull this repo into your desktop directory and call it onboarding_verification
cd ~/desktop; git clone https://github.com/kamsiokeke/onboarding-tag-verificartion-script.git onboarding_verification
> Populate the org_ver.txt file with the onboarded instances names or instance ids from the associated onboarding-tracking sheet.
> Assuming that your chef_orgs dir is located here at this path ~/repos/chef_orgs, if not modify the path in chef_checker.sh to reflect your path, then execute the following:
./chef_checker.sh <chef_org_name>
> This will iterate through the instaces and check if there is a chef node for that instance and populate chef_onboarded_nodes with the output.
> onboarded_nodes_recipies.txt is also created and populated with the recipies of the successfully onboarded instances, if blank then the associated instance was not onboarded correctly, and needs to be reonboarded.
> chef_ver_script.py is also run and outputs a list of all instances without corresponding chef nodes.

> To validate supprt, patching and backup tags, firstly use roller to assume a role in the customer account
    roller --profile default --account xxxxxxxxxxxxx --role CloudreachAdminRole --name <aws_account_name>

## Authors

- Kamsi Okeke (Cloudreach Managaed Services)
