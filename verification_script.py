def backup_tags():
    a = open("org_ver_2.txt", "r")
    missing =[]
    c = open("tag_compliance_check.txt", "r")
    d = c.read().split('\n')
    e = list(dict.fromkeys(d))
    backup_tags.onboarded_vms = a.read().split('\n')
    for i in backup_tags.onboarded_vms:
        if any(f"{i}".lower() in d.lower() for d in e):
            pass
        else:
            missing.append(i)
    if len(missing) == 0:
        print('success, all instances have backup tags')
    else:
        print(f"the folllowing instnaces do not have backup tags {missing}")

backup_tags()