#!/usr/bin/path
import sys
import operator
from hyperParameters import hyperParameter as hp
#sys.stdout=open("input1.txt","w")
fd = open("second_input2.txt","rw+")
nodes_freq = {}
min_freq = hp.min_freq_value
nodename_to_no={}
node_no = 1
label=0
nodes=set() 
line = fd.readline()
while line:
	##print line
	parts = line.split()
	for node in parts:
		if node in nodes:
			temp = nodes_freq[str(node)]
			temp = temp + 1
			nodes_freq[str(node)]  = temp
		else:
			nodes_freq[str(node)] = 1
			nodes.add(node)
	line = fd.readline()
fd.close()
##print nodes
##print nodes_freq

fd1 = open("second_input2.txt","rw+")
line = fd1.readline()
#stores all nodes whose edges has already form
prev = set()
label = 0
label_dict={}
nodename_to_no={}
node_no = 1
while line:
	#print line
	parts1 = line.split()
	s = set()
	s1 = set()
	s2=set()
	dict_freq={}

	node_list=[]
	parts=[]
	for n in parts1:
		if len(n)>3 and  nodes_freq[n]>min_freq:
			parts.append(n)
	#print parts1
	for n in parts:
		dict_freq[str(n)]=nodes_freq[str(n)]
	size1=len(parts)	

	#print parts
	##print dict_freq
	min = hp.max_value
 	dict_greater={}
	for n in dict_freq.items():
		if n[1]>min:
			dict_greater[n[0]]=n[1]

	##print dict_greater
	# sort= sorted(dict_freq.items(),key=operator.itemgetter(1))
	# #print "dict_freq",
	# #print dict_freq
	##print parts
	
	li1 =[]
 	
	list_temp = []
	
	for n in parts:
		list_temp.append(n)
	
	size = len(s1)
	#flag is for checking whether that whole tweet line is new or not
	#based on this we assign the value of the label
	

	flag=0
	##print list_temp
	##print prev
	
	for n in parts:
	 	if n not in label_dict:
	 		flag=1
	 	else:
	 		flag=0
	 		break

	

	if flag == 1:
		##print "1"
		##print line
		if len(dict_greater)!=0:
			label = label + 1
		# #print label
		# #print nodename_to_no
		##print nodename_to_no
		# #print parts
		# #print dict_greater
		
		for n in parts:
			##print n
			if n in dict_greater:
				for k in parts:
					label_dict[n]=label
					label_dict[k]=label
					if n!=k:
						# #print n,
						# #print k
						if n not in nodename_to_no:
							nodename_to_no[n]=node_no
							node_no = node_no + 1
						if k not in nodename_to_no:
							nodename_to_no[k]=node_no
							node_no = node_no + 1
						#print (n,k,label_dict[n])
						##print (k,n,label_dict[k])	
						# print (int(nodename_to_no[n]),int(nodename_to_no[k]),int(label_dict[n]))
						# print (int(nodename_to_no[k]),int(nodename_to_no[n]),int(label_dict[k]))
	else:
		##print nodename_to_no
		# #print "0"
		# #print parts
		# #print dict_greater
		for n in parts:
			##print n
			if n in dict_greater:
				for k in parts:
					if n!=k:
						# #print n,
						# #print k
						if n not in nodename_to_no:
							nodename_to_no[n]=node_no
							node_no = node_no + 1
						if k not in nodename_to_no:
							nodename_to_no[k]=node_no
							node_no = node_no + 1	
						# if n in label_dict and k in label_dict:
							# print (int(nodename_to_no[n]),int(nodename_to_no[k]),int(label_dict[n]))
							# print (int(nodename_to_no[k]),int(nodename_to_no[n]),int(label_dict[k]))			
						# if n in label_dict and  k not in label_dict:
						# 	label_dict[k]=0
						# 	#print (n,k,label_dict[n])
							##print (k,n,label_dict[k])
							# print (int(nodename_to_no[n]),int(nodename_to_no[k]),int(label_dict[n]))
							# print (int(nodename_to_no[k]),int(nodename_to_no[n]),int(label_dict[k]))			
						
						# if k in label_dict and n not in label_dict:
						# 	label_dict[n]=0
						# 	#print (n,k,label_dict[n])
						# 	##print (k,n,label_dict[k])
						# 	print (int(nodename_to_no[n]),int(nodename_to_no[k]),int(label_dict[n]))
						# 	print (int(nodename_to_no[k]),int(nodename_to_no[n]),int(label_dict[k]))
						# if k not in label_dict and n not in label_dict:
						# 	label_dict[n]=0
						# 	label_dict[k]=0
						# 	#print (n,k,label_dict[n])
						# 	##print (k,n,label_dict[k])
						# 	print (int(nodename_to_no[n]),int(nodename_to_no[k]),int(label_dict[n]))
						# 	print (int(nodename_to_no[k]),int(nodename_to_no[n]),int(label_dict[k]))
	line = fd1.readline()
#uncomment below line step9	

#print nodename_to_no																																																																																																																																																																																																																																																	
listt=[[]]
for n in nodes_freq.items():
	ll=[]
	ll.append(n[1])
	ll.append(n[0])
	listt.append(ll)

listt.sort()
#print label_dict
#print listt
#print nodes_freq
#print node_no
##print node
nodeno_and_freq={}
#print nodename_to_no
for n in nodename_to_no:
	if n in nodes_freq:
	#	print n
		a = str(n)
		nodeno_and_freq[nodename_to_no[a]]=nodes_freq[a]

#print nodeno_and_freq

for n in nodeno_and_freq.items():
	print int((n[0]))-1,
	print int(n[1])
#sys.stdout.close()

#rint ("\n")
print ("")
fd2 = open("input3.txt","rw+")
line = fd2.readline()
while line:
	l = len(line)
	#print line
	line = line[1:l-2]
	parts = line.split(",")
	l = len(parts)
	# print "[",
	# for i in range(l):
	# 	if i==2:
	# 		print (",[["),
	# 	if i!=2 and i!=0 and i%2==0:
	# 		print ("],["),
	# 	print int(parts[i]),
	# 	if i%2==0:
	# 		print (","),
	#print "]]]"
	
	i = 2
	while i<l:
		if int(parts[0])!=0:
			print (int(parts[0])),
			#print (""),
			print (int(parts[i])),
			#print (""),
			print (int(parts[i+1]))
		i = i + 2
	line = fd2.readline()

