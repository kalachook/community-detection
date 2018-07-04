import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph()

fd=open("output_1.txt","rw+")
line = fd.readline()
node_count=set()
while line:
	line = line.strip()
	parts=line.split()
	if int(parts[0]) not in node_count:
		node_count.add(int(parts[0]))
	if int(parts[1]) not in node_count:
		node_count.add(int(parts[1]))	
	# print parts
	g.add_edge(int(parts[0]),int(parts[1]))	
	line = fd.readline()

total = len(node_count)
i=0
node_list=[]
color_list=[]
while i<total:
	node_list.append(int(i))
	color_list.append("")
	i=i+1
g.add_nodes_from(node_list)

fd.close()

# print lis


#print total
colour=["red",]
fd1=open("ans_1.txt","rw+")
line = fd1.readline()
lis=[]
while line:
	parts=line.split("--")
	l=[]
	l.append(int(parts[1]))
	l.append(int(parts[0]))
	lis.append(l)
	line = fd1.readline()
lis.sort()
# print lis

print lis
start=-1
color=["green","red","blue","yellow","pink","black","white", "orange", "maroon", "cyan", "indigo", "violet", "gray", "gold"]
#print color_list
s=set()
cnt=-1
for line in lis:
	parts=line
	if int(parts[0]) == start:
		k = cnt%7
		s.add(int(parts[1]))
		print parts[1]
		color_list[int(parts[1])]=str(color[k])
		# print color[k]
	else:
		cnt = cnt + 1
		start=parts[0]
		k = cnt%7
		# print color[k]
		if len(s)!=0:
			print s
		s=set()
		# s.add(int(parts[0]))
		s.add(int(parts[1]))
		# color_list[int(parts[0])]=str(color[k])
		color_list[int(parts[1])]=str(color[k])

print s
print color_list
#color_node=color_list
nx.draw(g,node_color=color_list,with_label=True,node_size=1000)
plt.draw()
plt.show()
