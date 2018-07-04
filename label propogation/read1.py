fd2 = open("input1.txt","rw+")
line = fd2.readline()
list=[[]]
cnt = 1
while line:
	parts = line.strip("(")
	parts = parts[0:-2]
	parts = parts.split(",")
	#print parts
	parts[0] = int(parts[0])
	parts[1] = int(parts[1])
	parts[2] = int(parts[2])
	list.append(parts)
	cnt = cnt + 1
	line = fd2.readline()
list.sort()
length = len(list)
list = list[1:length]
#list = list[0:14]
#print list
freq = 1
tt = [0,0,0]
p = [0,0,0]
q=[0,0,0]


for n in list:
	q = n
	#print tt
	#print q
	if tt!=q and q!=[]:
		##print p
		##print q
		if tt[0] == q[0]:
			if tt[1] != q[1]:
				#print "if"
				p.append(0)
				p.append(0)
				k=len(p)
				p[k-2] = int(freq)
				p[k-1] = int(q[1])
				freq = 1
				#print p
				tt = q
			else:
				#print "ifif"
				freq = freq + 1
		else:
			#print "else"
			p.append(0)
			k = len(p)
			#print k
			p[k-1] = int(freq)
			print p
			p = p[0:3]
			p[0] = int(q[0])
			p[1] = int(q[2])
			p[2] = int(q[1])
			#tt = tt[0:3]
			tt = q
			# tt[0] = q[0]
			# tt[1] = q[1]
			# tt[2] = q[2]
			#print tt
			#print p
			freq = 1
	else:
		#print "elseelse"
		freq=freq+1

if tt == q:
	k = len(p)
	p.append(0)
	p[k] = int(freq)
	print p
