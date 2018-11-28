# Warm-up exercise a
x = 7
y = 5.0
z = 10.0
w = x % 2 + y / z + z + y / (z + z)
print("w evaluates to " + str(w))

# Warm-up exercise b
c = True
d = False
c = c and d
c = not c or d
print("c evaluates to " + str(c))

# Warm-up exercise c
d = 0
for p in range(0, 5):
    if p % 4 == 0:
        d = d + (p-1) * 25;
    else:
        d = d + 100;
print("$" + str(d//100) + "." + str(d % 100))





