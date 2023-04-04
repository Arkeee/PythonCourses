def subclass(start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    elif start not in classes:
        return None
    for node in classes[start]:
        if node not in path:
            newpath = subclass(node, end, path)
            if newpath:
                return newpath
    return None


classes = {}
for _ in range(int(input())):
    s = input().split(' : ')
    if len(s) > 1:
        new_list = ''.join(s[1]).split(' ')
        classes[s[0]] = new_list
    else:
        classes[s[0]] = []
for _ in range(int(input())):
    s = input().split(" ")
    if subclass(s[1], s[0]):
        print("Yes")
    else:
        print("No")
