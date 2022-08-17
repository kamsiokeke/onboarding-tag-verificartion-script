import boto3
import botocore
import test
from verification_script import backup_tags
regions = open("regions.txt", "r")
aws_regions = regions.read().split('\n')
prod= []
devtest= []
errors =[]
supported_instances=[]
instances = backup_tags.onboarded_vms
backup_supported_vms=[]
patching_supported_vms=[]
# checking for patching tags compliance
for i in aws_regions:
    client = boto3.client('ec2', region_name=aws_regions)
    for i in instances:
        try:
            response = client.describe_instances(
                InstanceIds=[i]
            )
        except botocore.exceptions.ClientError:
            errors.append(f'error calling DescribeInstnace on {i}. It may not exist within this region:{aws_regions}!')
            pass
        key,value=[],[]
        a = (response["Reservations"][0]["Instances"][0]["Tags"])
        for j in a:
            key.append(j["Key"].lower())
            value.append(j["Value"].lower())
            
            #print(f'{j["Key"]}:{j["Value"]}')
        #print(key)
        #print(value)
        if "cloudreachsupport" in key and "basesupport" in value:
            if "Cloudreach Backup Group".lower() in key:
                if "Cloudreach Patching Event".lower() and "Cloudreach Patching Phase".lowe() and "Cloudreach Patching Group".lower() in key:
                    backup_supported_vms.append(i)
                    patching_supported_vms.append(i)

        '''if "env" in key:
            if "dev" in value:
                devtest.append(i)
            elif "test" in value:
                devtest.append(i)
            elif "prod" in value:
                prod.append(i)
        
        if any("dev" in word for word in response["Reservations"][0]["Instances"][0]["Tags"]):
            devtest.append(i)
        elif any("test" in word for word in response["Reservations"][0]["Instances"][0]["Tags"]):
            devtest.append(i)
        elif any("prod" in word for word in response["Reservations"][0]["Instances"][0]["Tags"]):
            prod.append(i)'''

    # Checking for CloudreachSupport:BaseSupport Compliance
    crsupport_tags=[]
    cr_support_tag_values= open("tagging_validation/cr_support_tag_values.txt", "r")
    cr_tag_values = cr_support_tag_values.read().split('\n')

    for i in cr_tag_values:
        try:
            tag_test = client.describe_instances(
                Filters=[
                    {
                        'Name': 'tag:CloudreachSupport',
                        'Values': [i]
                    }

                ]
            )
        except botocore.exceptions.ClientError:
            errors.append(f'error calling DescribeInstnacs.')

        for i in tag_test['Reservations']:
            supported_instances.append(i['Instances'][0]['InstanceId'])
        #print(f'{len(supported_instances)}')
        non_base_support = [i for i in supported_instances if i not in instances]
        print(f'Of the instances to be onboarded, the following do not have the CloudreachSupport:BaaseSupport tag:\n{non_base_support}')

    #print(f'Length of devtest: {len(devtest)})') 
    #print(f'devtest instances: \n{devtest}\n')
    #print(f'Length of prod: {len(prod)}')
    #print(f'prod instnaces \n{prod}\n')
    #print(errors)

    #prod1= prod[:16]
    #prod2= prod[16:32]
    #prod3= prod[32::]

    # Add test patching tags to test instances

    '''for dev in devtest:
        devtest = client.create_tags(
            DryRun=False,
            Resources=[dev],
            Tags=[
                {
                    'Key': 'Cloudreach Patching Ignore',
                    'Value': 'True'
                }
            ]
        )
    for pro1 in prod:
        devtest = client.create_tags(
            DryRun=False,
            Resources=[pro1],
            Tags=[
                {
                    'Key': 'Cloudreach Patching Ignore',
                    'Value': 'True'
                }
            ]
        )


    # Add prod patching tags to prod instances

    for dev in devtest:
        devtest = client.delete_tags(
            DryRun=False,
            Resources=[dev],
            Tags=[
                {
                    'Key': 'Cloudreach Patching Ignore',
                    'Value': 'True'
                }
            ]
        )
    for pro1 in prod:
        devtest = client.delete_tags(
            DryRun=False,
            Resources=[pro1],
            Tags=[
                {
                    'Key': 'Cloudreach Patching Ignore',
                    'Value': 'True'
                }
            ]
        )'''
