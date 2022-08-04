a = open("org_ver.txt", "r")
b = open("HH_chefnodes.txt", "r")
missing =[]


def verification():
    #print(type(a.read()))
    onboarded_vms = a.read().split('\n')
    #print(len(onboarded_vms))
    HM_chef_nodes = b.read().split('\n')
    #print(HM_chef_nodes)
    nodes = ""
    for i in onboarded_vms:
        if any(f"{i}".lower() in d.lower() for d in HM_chef_nodes):
            nodes+=f"{i} \n"
        else:
            missing.append(i)
    #print('Done \n')

    #print(f'The following instnaces are missing from HM {missing}')
    #print(nodes)
    #print(len(missing))

    #print(onboarded_vms)
verification()
