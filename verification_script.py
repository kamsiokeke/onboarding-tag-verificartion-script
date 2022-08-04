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