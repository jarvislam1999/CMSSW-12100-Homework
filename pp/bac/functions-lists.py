def F1(i, j) :
    print("F1({}, {})".format(i, j))
    F2(j, i+j)
    print("F1: i = {}, j = {}".format(i, j))
    

def F2(i, j) :
    print("    F2({}, {})".format(i, j))
    k = F3(i, j)
    print("    F2: i = {}, j = {}, k = {}".format(i, j, k))
    

def F3(i, j) :
    print("        F3({}, {})".format(i, j))
    i = i+j
    j = i+2*j
    k = 2*i+3*j
    print("        F3: i = {}, j = {}, k = {}".format(i, j, k))
    return k
    

print("Warmup exercise 1:")
F1(1, 1)
print()
print()


def mystery1(l):
    rv = []
    for x in l:
        rv = [x] + rv
    return rv

print("Warmup exercise 2:")
l = [0, 1, 2, 3, 4]
nl = mystery1(l)
print("l: ", l)
print("nl: ", nl)
print()
print()

def mystery2(l):
    rv = []
    for i in range(len(l)-1, -1, -1):
        rv.append(l[i])
    return rv

print("Warmup exercise 3:")
l = [0, 1, 2, 3, 4]
nl = mystery2(l)
print("l: ", l)
print("nl: ", nl)
print()
print()

def mystery3(l):
    n = len(l)
    for i in range(n // 2):
        t = l[i]
        l[i] = l[n-i-1]
        l[n-i-1] = t


print("Challenge exercise:")
l = [0, 1, 2, 3, 4]
mystery3(l)
print("l: ", l)
print()
print()
