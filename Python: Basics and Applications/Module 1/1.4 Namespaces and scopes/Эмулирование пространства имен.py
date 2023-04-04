def elem(ns, var):
    if var in namespaces.get(ns):
        return ns
    elif ns != 'global':
        return elem(namespaces.get(ns)[0], var)
    else:
        return None


namespaces = {
    'global': [],
}
for _ in range(int(input())):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        namespaces[namesp] = []
        namespaces[namesp].append(arg)
        if arg in namespaces:
            namespaces[arg].append(namesp)
    elif cmd == 'add':
        if namesp in namespaces:
            namespaces[namesp].append(arg)
    elif cmd == 'get':
        print(elem(namesp, arg))
