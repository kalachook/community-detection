import sys
fd = open("final_input.txt","rw+")
line = fd.readline()
sys.stdout=open("second_input2.txt","w")
while line:
	flag=0
	line=line.strip()
	line=line.lower()	
	parts=line.split()
	if line == "president trump given white nationalists cover oxygen dream respectability" or len(parts)<6:
		flag = 1
	if flag==0:
		print line
		flag = 0
	line = fd.readline()
sys.stdout.close()
