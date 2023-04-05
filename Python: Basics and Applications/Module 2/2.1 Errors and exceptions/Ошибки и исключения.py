def exc(start, path=[]):
    path = path + [start]
    for node in classes[start]:
        if node not in path:
            newpath = exc(node, path)
            if newpath:
                return newpath
    return path


classes, all_req = {}, []
for _ in range(int(input())):
    s = input().split(' : ')
    if len(s) > 1:
        new_list = ''.join(s[1]).split(' ')
        classes[s[0]] = new_list
    else:
        classes[s[0]] = []
print(classes)
for _ in range(int(input())):
    rqst = input()
    if rqst not in all_req:
        all_req.append(rqst)
        if len(set(exc(rqst)) & set(all_req)) > 1:
            print(rqst)
    else:
        print(rqst)