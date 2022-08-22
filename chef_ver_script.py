a = open("org_ver.txt", "r")
b = open("onboarded_nodes.txt", "r")
missing =[]
# This script check to see if any of the instances do not have an associated chef node and outputs any missed instances
def verification():
    onboarded_vms = a.read().split('\n')
    HM_chef_nodes = b.read().split('\n')
    nodes = ""
    for i in onboarded_vms:
        if any(f"{i}".lower() in d.lower() for d in HM_chef_nodes):
            nodes+=f"{i} \n"
        else:
            missing.append(i)
    print('Done \n')
    print(f'The following instnaces do not have an associated chef node: \n{missing}')
    #print(nodes)
    #print(len(missing))
    #print(onboarded_vms)
verification()
