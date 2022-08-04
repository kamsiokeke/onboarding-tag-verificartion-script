'''a = open("holly_hunt_ver.txt", "r")
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
'''
a = open("org_ver.txt", "r")
missing =[]
def backup_tags():
    c = open("tag_compliance_check.txt", "r")
    d = c.read().split('\n')
    e = list(dict.fromkeys(d))
    onboarded_vms = a.read().split('\n')
    for i in onboarded_vms:
        if any(f"{i}".lower() in d.lower() for d in e):
            pass
        else:
            missing.append(i)
    if len(missing) == 0:
        print('success, all instances have backup tags')
    else:
        print(f"the folllowing instnaces do not have backuop tags {missing}")

backup_tags()