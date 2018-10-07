# Examples for lists and loops lab

l0 = []
l1 = [1, "abc", 5.7, [1, 3, 5]]
l2 = [10, 11, 12, 13, 14, 15, 16]
l3 = [7, -5, 6, 27, -3, 0, 14]
l4 = [0, 1, 1, 3, 2, 4, 6, 1, 7, 8]

all_pos = True
for i in l3:
	if i <0:
		all_pos = False

pos_only = []
for i in l3:
	if i >0:
		pos_only.append(i)

is_pos_0 = []
for i in l3:
	if i >0:
		is_pos_0.append(True)
	else:
		is_pos_0.append(False)

is_pos_1 = []
for i in range(0,len(l3)):
	if l3[i] >0:
		is_pos_1.append(True)
	else:
		is_pos_1.append(False)

maxl4 = max(l4)

counts = []
for i in l4:
	icount = 0
	for j in l4:
		if j == i:
			icount = icount+1
	counts.append(icount)

