import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph()
f= open('dis.txt','r')
last_line =f.readline()
dis = {}
withbraces = last_line
line = withbraces.split('{')[1]
parts = line.split(',')
parts[-1] = parts[-1].split('}')[0]
for p in parts:
	value = p.split(':')[0]
	value = p.split('\'')[1]
	dis[value]=int(p.split(':')[1])
nodename_to_num= dis
# nodename_to_num={'lack': 221, 'devine': 83, 'unrest': 170, 'protest': 4, 'hate': 65, 'children': 215, 'dera': 361, 'suicide': 339, 'punjab': 366, 'anshul': 354, 'finally': 91, 'lord': 81, 'sakshi': 367, 'woman': 87, 'assam': 335, 'facebook': 186, 'aaye': 345, 'dhruv': 359, 'temple': 102, 'salute': 47, 'maharaj': 368, 'sauda': 363, 'brave': 403, 'pledge': 35, 'tricolor': 48, 'sign': 284, 'second': 265, 'blue': 181, 'rapist': 348, 'deeply': 112, 'rohtak': 387, 'indian': 217, 'supplier': 207, 'supplies': 218, 'bharat': 31, 'appeal': 381, 'celebrates': 394, 'public': 198, 'nazis': 23, 'dahi': 370, 'hours': 139, 'tragedy': 214, 'wait': 137, 'great': 149, 'kids': 199, 'daughter': 383, 'harminder': 384, 'borussia': 282, 'berke': 136, 'action': 166, 'love': 63, 'family': 69, 'manohar': 353, 'brought': 294, 'fake': 262, 'armed': 404, 'satyagraha': 409, 'standing': 125, 'cherishing': 417, 'khan': 260, 'nehru': 398, 'hospital': 208, 'indians': 204, 'tricolour': 140, 'next': 104, 'makhan': 374, 'https': 75, 'films': 316, 'today': 55, 'baba': 253, 'afford': 258, 'company': 202, 'flag': 49, 'virtue': 418, 'benefits': 344, 'shetty': 325, 'shraddha': 306, 'rights': 38, 'challenge': 183, 'following': 74, 'saheeb': 390, 'beautiful': 304, 'violence': 59, 'trump': 18, 'links': 189, 'mataram': 34, 'india': 44, 'high': 419, 'rape': 356, 'native': 123, 'unpaid': 232, 'breaking': 143, 'till': 267, 'amazing': 169, 'rathee': 360, 'youhappy': 405, 'hoisting': 331, 'blood': 113, 'coming': 127, 'sentencing': 389, 'purchase': 247, 'liquid': 229, 'candles': 176, 'guru': 84, 'coutinho': 280, 'chief': 219, 'jail': 98, 'shraddhakapoor': 314, 'tyohar': 378, 'finalized': 323, 'move': 51, 'wishing': 28, 'years': 167, 'signs': 281, 'police': 53, 'thank': 107, 'clashes': 39, 'charlottesville': 1, 'followers': 364, 'anushka': 299, 'sachha': 362, 'happened': 93, 'good': 54, 'crash': 26, 'bans': 180, 'hardik': 190, 'largest': 172, 'handi': 371, 'nation': 153, 'gurmeet': 349, 'shameful': 401, 'schools': 334, 'panchkula': 388, 'killed': 56, 'bigger': 146, 'name': 119, 'oxygen': 206, 'always': 148, 'arrested': 178, 'bless': 99, 'satyagrah': 242, 'shortage': 213, 'surat': 103, 'modi': 194, 'heyer': 115, 'bills': 228, 'encephalitis': 246, 'signing': 278, 'everyone': 29, 'neil': 318, 'hare': 16, 'related': 132, 'challenges': 341, 'celebrating': 396, 'year': 73, 'special': 201, 'kapoor': 307, 'trending': 326, 'trooper': 86, 'mata': 32, 'cause': 155, 'announced': 287, 'pakistans': 407, 'million': 165, 'recd': 327, 'assures': 239, 'wanted': 100, 'bates': 117, 'exposing': 355, 'days': 177, 'thing': 92, 'shree': 252, 'disturbed': 380, 'place': 57, 'janma': 85, 'think': 156, 'first': 64, 'janmasthami': 12, 'clause': 290, 'done': 134, 'city': 157, 'story': 133, 'festival': 14, 'leading': 302, 'white': 6, 'pakistani': 406, 'released': 196, 'defends': 369, 'churane': 375, 'lover': 82, 'aazadi': 241, 'sentenced': 97, 'hamara': 414, 'supremacist': 10, 'teenagers': 337, 'mishra': 227, 'need': 109, 'orders': 160, 'prosperity': 203, 'forces': 296, 'singh': 244, 'committing': 340, 'citizens': 37, 'valverde': 289, 'english': 402, 'paid': 67, 'nitin': 319, 'aakhri': 350, 'pair': 315, 'america': 19, 'payment': 224, 'proud': 175, 'judiciary': 358, 'joining': 88, 'saying': 70, 'bhaiyo': 193, 'bring': 77, 'soilders': 415, 'principal': 225, 'mubarak': 377, 'indiansalute': 410, 'iskcon': 101, 'state': 52, 'going': 76, 'announce': 301, 'banned': 342, 'massacre': 223, 'despite': 297, 'celebrate': 13, 'krishna': 17, 'earn': 416, 'amid': 58, 'remove': 188, 'release': 231, 'azaadi': 408, 'nandlal': 376, 'ousmane': 270, 'resmi': 295, 'fail': 230, 'baris': 372, 'movie': 309, 'datenone': 329, 'please': 159, 'achaa': 413, 'mcauliffe': 42, 'fans': 292, 'various': 336, 'reading': 248, 'conditions': 333, 'notice': 343, 'rajeev': 226, 'pained': 379, 'news': 9, 'cities': 173, 'shubhkamnaye': 191, 'career': 322, 'many': 94, 'planned': 162, 'glorious': 397, 'pakistan': 237, 'supply': 220, 'mafia': 357, 'better': 36, 'asks': 184, 'dortmund': 275, 'patrolling': 197, 'sare': 411, 'much': 110, 'hindi': 400, 'compensating': 328, 'helicopter': 60, 'troopers': 154, 'sacha': 386, 'life': 130, 'tiger': 391, 'lives': 24, 'last': 144, 'spirit': 234, 'independence': 30, 'case': 255, 'welcoming': 305, 'bill': 233, 'governor': 5, 'near': 27, 'country': 111, 'sabhi': 192, 'player': 285, 'harsh': 332, 'media': 245, 'make': 89, 'member': 121, 'speech': 195, 'sarkar': 261, 'grand': 250, 'inch': 324, 'gets': 68, 'disappointment': 330, 'injured': 61, 'jassi': 385, 'driver': 71, 'protesters': 20, 'cullen': 116, 'sisters': 46, 'whale': 182, 'supremacists': 7, 'euro': 293, 'well': 171, 'without': 147, 'mother': 269, 'know': 138, 'money': 210, 'actress': 313, 'shaant': 352, 'death': 126, 'lady': 303, 'kerala': 254, 'lets': 393, 'parents': 161, 'teenager': 346, 'hind': 142, 'whatsapp': 187, 'real': 129, 'rahim': 347, 'march': 131, 'emergency': 106, 'government': 105, 'read': 164, 'delhi': 256, 'virginia': 0, 'game': 151, 'vande': 33, 'nationalists': 43, 'birth': 80, 'govt': 222, 'disappointed': 311, 'county': 122, 'fortune': 79, 'night': 145, 'security': 200, 'kyun': 259, 'google': 185, 'crowd': 3, 'people': 21, 'stern': 240, 'back': 128, 'dead': 22, 'hindustan': 235, 'home': 8, 'provided': 257, 'lead': 312, 'haryana': 264, 'opposite': 308, 'contributing': 50, 'saaho': 300, 'jugador': 277, 'burn': 365, 'jahan': 412, 'murdered': 124, 'sixty': 216, 'prabhas': 298, 'getting': 236, 'freedom': 141, 'yogiadityanath': 249, 'slams': 174, 'plus': 268, 'celebrations': 251, 'gorakhpur': 209, 'political': 150, 'nothing': 90, 'right': 2, 'sarkaar': 351, 'zinda': 392, 'neymar': 288, 'deal': 274, 'transfer': 286, 'dembele': 271, 'long': 95, 'fight': 152, 'start': 66, 'racist': 108, 'died': 118, 'forward': 276, 'happy': 15, 'link': 135, 'congratulations': 310, 'cylinders': 212, 'wish': 168, 'official': 279, 'signed': 283, 'fuhar': 373, 'agree': 273, 'teen': 338, 'nationalist': 40, 'deaths': 62, 'rahi': 263, 'harmony': 205, 'candle': 266, 'rally': 11, 'hospitals': 243, 'film': 321, 'heather': 114, 'dying': 238, 'deadly': 72, 'peace': 120, 'yogi': 211, 'interested': 395, 'star': 291, 'brothers': 45, 'congress': 382, 'delivered': 399, 'welcome': 163, 'update': 179, 'sujeeth': 320, 'terry': 41, 'sides': 25, 'bcoz': 317, 'happening': 78, 'confirm': 158, 'barcelona': 272, 'time': 96}
no_to_nodename={}
for n in nodename_to_num.items():
	#print n[1]
	no_to_nodename[n[1]]=n[0]
# print no_to_nodename[1]
#no_to_nodename[0] = "xyz"

fd=open("sample_input.txt","rw+")

# to skip the values to the proper details
while fd.readline()!="\n":
	pass

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
fd1=open("ans1.txt","rw+")
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

#print lis

start=-1
color=["green","red","blue","yellow","pink","black","white"]
#print color_list
s=set()
cnt=-1
for line in lis:
	parts=line
	if int(parts[0]) == start:
		k = cnt%7
		s.add(int(parts[1]))
		color_list[int(parts[1])]=str(color[k])
		# print color[k]
	else:
		cnt = cnt + 1
		start=parts[0]
		k = cnt%7
		# print color[k]
		

		if len(s)>3:
			# print s
			nodes=[]
			fd = open("sample_input.txt","rw+")
			while fd.readline()!="\n":
				pass
			line = fd.readline()
			gg = nx.Graph()
			while line:
				line = line.strip()
				parts=line.split()
				n=[]
				if int(parts[0]) in s and int(parts[1]) in s:			
					# print parts[0],
					# print parts[1]
					# if int(parts[0])!=0 and int(parts[1])!=0:
					a = str(no_to_nodename[int(parts[0])])
					b = str(no_to_nodename[int(parts[1])])
					gg.add_edge(str(a),str(b))	
					if (str(a)) not in nodes:
						nodes.append(str(a))
					if (str(parts[1])) not in nodes:
						nodes.append(str(b))
					
					# elif int(parts[1])==0 :
					# 	a = str(no_to_nodename[int(parts[0])])
					# 	b = str(no_to_nodename[int(parts[0])])
					# 	gg.add_edge(str(a),str(b))	
					# 	if (str(a)) not in nodes:
					# 		nodes.append(str(a))
					# 	if (str(parts[1])) not in nodes:
					# 		nodes.append(str(b))

					# elif int(parts[0])==0 :
					# 	a = str(no_to_nodename[int(parts[1])])
					# 	b = str(no_to_nodename[int(parts[1])])
					# 	gg.add_edge(str(a),str(b))	
					# 	if (str(a)) not in nodes:
					# 		nodes.append(str(a))
					# 	if (str(parts[1])) not in nodes:
					# 		nodes.append(str(b))
			
				line = fd.readline()
			
			# print nodes
			#gg.info("mani")
			gg.add_nodes_from(nodes)
			nx.draw(gg,node_color="red",node_size=4000,with_labels=True)
			plt.draw()
			plt.show()				



		s=set()
		# s.add(int(parts[0]))
		s.add(int(parts[1]))
		# color_list[int(parts[0])]=str(color[k])
		color_list[int(parts[1])]=str(color[k])

if len(s)>3:
			#print s
			nodes=[]
			fd = open("sample_input.txt","rw+")
			while fd.readline()!="\n":
				pass
			line = fd.readline()
			gg = nx.Graph()
			while line:
				line = line.strip()
				parts=line.split()
				n=[]
				if int(parts[0]) in s and int(parts[1]) in s:			
					# print parts[0],
					# print parts[1]
					# if int(parts[0])!=0 and int(parts[1])!=0:
					a = str(no_to_nodename[int(parts[0])])
					b = str(no_to_nodename[int(parts[1])])
					gg.add_edge(str(a),str(b))	
					if (str(a)) not in nodes:
						nodes.append(str(a))
					if (str(parts[1])) not in nodes:
						nodes.append(str(b))
					
					# elif int(parts[1])==0 :
					# 	a = str(no_to_nodename[int(parts[0])])
					# 	b = str(no_to_nodename[int(parts[0])])
					# 	gg.add_edge(str(a),str(b))	
					# 	if (str(a)) not in nodes:
					# 		nodes.append(str(a))
					# 	if (str(parts[1])) not in nodes:
					# 		nodes.append(str(b))

					# elif int(parts[0])==0 :
					# 	a = str(no_to_nodename[int(parts[1])])
					# 	b = str(no_to_nodename[int(parts[1])])
					# 	gg.add_edge(str(a),str(b))	
					# 	if (str(a)) not in nodes:
					# 		nodes.append(str(a))
					# 	if (str(parts[1])) not in nodes:
					# 		nodes.append(str(b))
			
				line = fd.readline()
			# print nodes
			#gg.info("mani")
			gg.add_nodes_from(nodes)
			nx.draw(gg,node_color="green",node_size=4000,with_labels=True)
			plt.draw()
			plt.show()				



	
#print s
#print node_list
#color_node=color_list
