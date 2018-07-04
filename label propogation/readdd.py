#!/usr/bin/path
import sys
import operator
from hyperParameters import hyperParameter as hp
sys.stdout=open("input1.txt","w")
fd = open("second_input2.txt","rw+")
nodes_freq = {}
min_freq = hp.min_freq_value
nodename_to_no={}
node_no = 0
label=0
##removal_list= whatever, wishes, j&amp, maybe answer, thinking, 
##weekend, really, value, small, group, peace, looking, actually, values, groups, short, starting, quote, gives, travel, shower, interested, shower, zverev
##tomorrow, things, thoughts, think, second, three, makes, cause, tweet, words, takes, learn, please, weekend, started, antifa, learn, called, thought, another, looks, tonight, anything, thanks, gonna, giving, talking 'regards','right','everything','tells','remember','tells','ahead','unite','making','enough','early','wrong','exactly' , 'special', 'needs', 'general', 'twitter', 'wanted', 'better', 'taking', 'towards', 'first', 'already', 'everyone', 'terry', 'going','taken', 'saying', 'update','today','tommorrow','yesterday','https','happy','sunday','monday','saturday','last','night','mondaymotivation','always','along','lives','president','great','clear','never','anyone','nothing','bring','sometimes','different','getting','become','check','august','display','create','shall','knows','essence','complete','attaque','gots7e5','plots','everyon','ouagadougou','matter','unique','karti','morning']
##removal_list=['tomorrow', 'things', 'thoughts', 'think', 'second', 'three', 'makes', 'cause', 'tweet', 'words', 'takes', 'learn', 'please', 'weekend' 'started', 'antifa', 'learn', 'called', 'thought', 'another', 'looks', 'tonight', 'anything', 'thanks', 'gonna', 'giving', 'talking', 'coming', 'comes', 'spread', 'forget', 'important', 'trying', 'shami', 'calling', 'years', 'together', 'around', 'young', 'regards', 'right', 'everything', 'tells', 'ahead', 'unite', 'making', 'enough', 'early', 'exactly', 'special', 'needs', 'general', 'twitter', 'wanted', 'better', 'taking', 'towards', 'first', 'already', 'everyone', 'terry', 'going', 'taken', 'weekend', 'really', 'value', 'small', 'group', 'peace', 'looking', 'actually', 'values', 'groups', 'short', 'starting', 'quote', 'gives', 'travel', 'shower', 'interested', 'zverev', 'whatever', 'wishes', 'j&amp', 'maybe', 'answer', 'thinking', 'without', 'saying','update','today','tommorrow','yesterday','https','happy','sunday','monday','saturday','last','night','mondaymotivation','always','along','lives','president','great','clear','never','anyone','nothing','bring','sometimes','different','getting','become','check','august','display','create','shall','knows','essence','complete','attaque','gots7e5','plots','everyon','ouagadougou','matter','unique','karti']
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
node_no = 0

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
						print (int(nodename_to_no[n]),int(nodename_to_no[k]),int(label_dict[n]))
						print (int(nodename_to_no[k]),int(nodename_to_no[n]),int(label_dict[k]))
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
						if n in label_dict and k in label_dict:
							print (int(nodename_to_no[n]),int(nodename_to_no[k]),int(label_dict[n]))
							print (int(nodename_to_no[k]),int(nodename_to_no[n]),int(label_dict[k]))			
						if n in label_dict and  k not in label_dict:
							label_dict[k]=0
							#print (n,k,label_dict[n])
							##print (k,n,label_dict[k])
							print (int(nodename_to_no[n]),int(nodename_to_no[k]),int(label_dict[n]))
							print (int(nodename_to_no[k]),int(nodename_to_no[n]),int(label_dict[k]))			
						
						if k in label_dict and n not in label_dict:
							label_dict[n]=0
							#print (n,k,label_dict[n])
							##print (k,n,label_dict[k])
							print (int(nodename_to_no[n]),int(nodename_to_no[k]),int(label_dict[n]))
							print (int(nodename_to_no[k]),int(nodename_to_no[n]),int(label_dict[k]))
						if k not in label_dict and n not in label_dict:
							label_dict[n]=0
							label_dict[k]=0
							#print (n,k,label_dict[n])
							##print (k,n,label_dict[k])
							print (int(nodename_to_no[n]),int(nodename_to_no[k]),int(label_dict[n]))
							print (int(nodename_to_no[k]),int(nodename_to_no[n]),int(label_dict[k]))
	line = fd1.readline()
#uncomment below line step9	
sys.stdout.close()
sys.stdout = open('dis.txt','w')
print nodename_to_no	
sys.stdout.close()

#print nodes_freq
listt=[[]]
for n in nodes_freq.items():
	ll=[]
	ll.append(n[1])
	ll.append(n[0])
	listt.append(ll)

listt.sort()
#print listt
#print node_no
##print node
# with open('input1.txt', 'r') as f:
# 	lines = f.read().splitlines()
# 	last_line = lines[-1]
# 	newfile.write(last_line)
# 	newfile.close()




