import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph()
def getKey(item):
     return item[1]
nodename_to_num={}
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
f.close()
# nodename_to_num={'lack': 283, 'devine': 100, 'unrest': 223, 'protest': 5, 'follow': 386, 'hate': 72, 'children': 278, 'dera': 487, 'suicide': 455, 'punjab': 492, 'riots': 77, 'anshul': 479, 'finally': 109, 'lord': 98, 'sakshi': 493, 'woman': 104, 'kuda': 411, 'assam': 447, 'facebook': 244, 'welcoming': 397, 'aaye': 470, 'dhruv': 485, 'leader': 46, 'independence': 33, 'maharaj': 494, 'sauda': 489, 'brave': 532, 'pledge': 38, 'tricolor': 53, 'sign': 368, 'second': 345, 'video': 132, 'pass': 452, 'blue': 238, 'rapist': 473, 'deeply': 138, 'paralegal': 149, 'supplied': 309, 'rohtak': 515, 'waiting': 258, 'indian': 279, 'supplier': 269, 'supplies': 280, 'bharat': 34, 'appeal': 508, 'celebrates': 523, 'public': 257, 'nazis': 26, 'dahi': 497, 'philippe': 385, 'never': 129, 'shankar': 426, 'hundreds': 161, 'hours': 179, 'following': 86, 'tragedy': 276, 'wait': 170, 'great': 193, 'kids': 259, 'daughter': 510, 'conviction': 513, 'harminder': 511, 'borussia': 366, 'berke': 169, 'action': 217, 'makes': 73, 'love': 70, 'family': 78, 'manohar': 478, 'replace': 200, 'county': 152, 'chunky': 431, 'stern': 305, 'armed': 533, 'announced': 372, 'standing': 155, 'cherishing': 547, 'khan': 340, 'nehru': 527, 'hospital': 270, 'indians': 265, 'tricolour': 182, 'next': 123, 'makhan': 501, 'call': 127, 'https': 90, 'films': 419, 'today': 61, 'baba': 330, 'milyon': 382, 'afford': 338, 'company': 262, 'flag': 54, 'virtue': 548, 'benefits': 464, 'shetty': 437, 'women': 206, 'shraddha': 399, 'rights': 41, 'challenge': 241, 'sabu': 428, 'growing': 131, 'saheeb': 519, 'beautiful': 396, 'admired': 410, 'months': 294, 'trump': 19, 'links': 247, 'give': 226, 'mataram': 37, 'india': 49, 'high': 549, 'want': 172, 'cows': 313, 'rape': 481, 'native': 153, 'monitoring': 234, 'democracy': 187, 'unpaid': 297, 'heroine': 391, 'breaking': 186, 'till': 350, 'amazing': 221, 'expecting': 413, 'economy': 336, 'plant': 323, 'youhappy': 534, 'tied': 235, 'hoisting': 443, 'blood': 140, 'coming': 157, 'sentencing': 517, 'court': 331, 'purchase': 320, 'liquid': 293, 'candles': 231, 'guru': 101, 'coutinho': 364, 'chief': 281, 'jihadism': 467, 'jail': 117, 'ambulance': 315, 'shraddhakapoor': 414, 'tyohar': 505, 'cute': 406, 'finalized': 435, 'move': 57, 'wishing': 31, 'years': 218, 'signs': 365, 'police': 59, 'thank': 130, 'madhie': 425, 'mamata': 466, 'clashes': 42, 'creations': 404, 'charlottesville': 1, 'followers': 490, 'main': 329, 'anushka': 390, 'sachha': 488, 'happened': 111, 'good': 60, 'crash': 29, 'bans': 239, 'hardik': 248, 'largest': 227, 'judiciary': 484, 'handi': 498, 'nation': 198, 'disrupted': 324, 'comitting': 460, 'schools': 446, 'panchkula': 516, 'killed': 62, 'bigger': 190, 'name': 147, 'oxygen': 267, 'always': 192, 'university': 56, 'arrested': 233, 'bless': 118, 'satyagrah': 311, 'stopped': 285, 'shortage': 275, 'surat': 122, 'modi': 252, 'heyer': 142, 'bills': 292, 'encephalitis': 318, 'mean': 196, 'signing': 362, 'everyone': 32, 'neil': 422, 'hare': 17, 'related': 163, 'challenges': 458, 'celebrating': 525, 'year': 85, 'special': 261, 'really': 171, 'kapoor': 400, 'trending': 438, 'trooper': 103, 'mata': 35, 'cause': 202, 'salute': 52, 'pakistans': 536, 'million': 216, 'recd': 439, 'assures': 304, 'wanted': 119, 'care': 174, 'bates': 144, 'exposing': 480, 'sahoo': 398, 'days': 232, 'thing': 110, 'shree': 328, 'disturbed': 507, 'place': 63, 'janma': 102, 'vijay': 430, 'think': 203, 'first': 71, 'dont': 236, 'janmasthami': 13, 'clause': 376, 'shameful': 530, 'done': 166, 'president': 66, 'lakhs': 268, 'city': 204, 'story': 164, 'festival': 15, 'leading': 394, 'player': 370, 'attack': 84, 'white': 7, 'pakistani': 535, 'murder': 82, 'released': 255, 'believe': 126, 'youth': 459, 'churane': 502, 'lover': 99, 'arun': 429, 'aazadi': 310, 'sentenced': 116, 'counter': 4, 'hamara': 543, 'supremacist': 11, 'turned': 25, 'teenagers': 449, 'mishra': 290, 'need': 134, 'nazi': 167, 'orders': 210, 'prosperity': 264, 'agency': 308, 'officers': 181, 'take': 175, 'forces': 384, 'truck': 352, 'singh': 314, 'committing': 457, 'citizens': 40, 'valverde': 374, 'english': 531, 'paid': 75, 'nitin': 423, 'aakhri': 475, 'nothing': 108, 'america': 20, 'payment': 287, 'medical': 263, 'proud': 230, 'upset': 180, 'brought': 381, 'khattar': 482, 'fact': 335, 'joining': 105, 'saying': 80, 'bhaiyo': 251, 'bring': 92, 'soilders': 545, 'principal': 288, 'ehsaan': 427, 'mubarak': 504, 'indiansalute': 539, 'iskcon': 120, 'fans': 379, 'going': 91, 'combo': 417, 'announce': 393, 'casted': 407, 'banned': 462, 'massacre': 286, 'watch': 165, 'bharatiya': 544, 'despite': 387, 'celebrate': 14, 'krishna': 18, 'earn': 546, 'amid': 64, 'remove': 246, 'greene': 151, 'release': 296, 'azaadi': 537, 'nandlal': 503, 'ousmane': 354, 'college': 115, 'resmi': 383, 'fail': 295, 'best': 388, 'defends': 495, 'baris': 499, 'farmers': 456, 'movie': 402, 'datenone': 441, 'please': 209, 'achaa': 542, 'mcauliffe': 45, 'state': 58, 'various': 448, 'paise': 317, 'reading': 322, 'conditions': 445, 'notice': 463, 'august': 220, 'rajeev': 289, 'pained': 506, 'boss': 347, 'news': 10, 'cities': 228, 'shubhkamnaye': 249, 'career': 434, 'many': 112, 'pushpa': 307, 'planned': 212, 'glorious': 526, 'pakistan': 302, 'gurmeet': 474, 'supply': 282, 'sweet': 421, 'mafia': 483, 'expensive': 369, 'speak': 184, 'better': 39, 'asks': 242, 'west': 89, 'patrolling': 256, 'three': 94, 'sare': 540, 'much': 135, 'hindi': 529, 'compensating': 440, 'helicopter': 67, 'troopers': 201, 'sacha': 514, 'life': 160, 'tiger': 520, 'finished': 468, 'lives': 27, 'last': 188, 'spirit': 299, 'case': 333, 'marcha': 48, 'bill': 298, 'governor': 6, 'cast': 432, 'near': 30, 'country': 137, 'study': 469, 'cylinder': 319, 'convine': 465, 'sabhi': 250, 'shame': 178, 'someone': 225, 'confirmed': 254, 'harsh': 444, 'media': 316, 'make': 107, 'unite': 177, 'member': 150, 'speech': 253, 'harmony': 266, 'grand': 326, 'inch': 436, 'gets': 76, 'disappointment': 442, 'injured': 68, 'jassi': 512, 'blames': 208, 'driver': 81, 'yesterday': 214, 'protesters': 21, 'moment': 87, 'cullen': 143, 'sisters': 51, 'whale': 240, 'supremacists': 8, 'euro': 380, 'well': 224, 'person': 207, 'without': 191, 'mother': 353, 'know': 173, 'violence': 65, 'money': 272, 'actress': 412, 'violent': 79, 'shaant': 477, 'death': 156, 'disappointed': 408, 'bullshit': 453, 'kerala': 332, 'arrest': 124, 'lets': 522, 'parents': 211, 'teenager': 471, 'innocent': 95, 'hind': 185, 'ohhh': 405, 'whatsapp': 245, 'save': 291, 'excited': 176, 'real': 159, 'rahim': 472, 'march': 162, 'emergency': 128, 'government': 125, 'read': 215, 'delhi': 334, 'virginia': 0, 'game': 195, 'vande': 36, 'nationalists': 47, 'birth': 97, 'govt': 284, 'buyout': 375, 'lady': 395, 'jugador': 361, 'fortune': 96, 'lost': 145, 'misskyra': 416, 'journalist': 518, 'night': 189, 'become': 136, 'security': 260, 'kyun': 339, 'google': 243, 'crowd': 3, 'people': 22, 'fake': 342, 'back': 158, 'dead': 23, 'hindustan': 300, 'home': 9, 'provided': 337, 'lead': 409, 'confirm': 205, 'satyagraha': 538, 'literally': 321, 'opposite': 401, 'contributing': 55, 'saaho': 392, 'convict': 496, 'temple': 121, 'burn': 491, 'jahan': 541, 'murdered': 154, 'found': 451, 'sixty': 277, 'bhii': 348, 'post': 106, 'super': 222, 'prabhas': 389, 'getting': 301, 'freedom': 183, 'yogiadityanath': 325, 'slams': 229, 'plus': 351, 'dortmund': 359, 'kmii': 349, 'celebrations': 327, 'protests': 24, 'film': 433, 'gorakhpur': 271, 'political': 194, 'kbiir': 450, 'pair': 418, 'right': 2, 'sarkaar': 476, 'zinda': 521, 'neymar': 373, 'deal': 358, 'transfer': 371, 'dembele': 355, 'long': 113, 'fight': 197, 'start': 74, 'fought': 88, 'racist': 133, 'bcoz': 420, 'forward': 360, 'happy': 16, 'complete': 377, 'link': 168, 'filed': 306, 'true': 139, 'congratulations': 403, 'cylinders': 274, 'wish': 219, 'official': 363, 'signed': 367, 'paired': 415, 'fuhar': 500, 'agree': 357, 'teen': 454, 'nationalist': 43, 'deaths': 69, 'rahi': 343, 'chal': 461, 'candle': 346, 'rally': 12, 'hospitals': 312, 'sarkar': 341, 'heather': 141, 'dying': 303, 'deadly': 83, 'peace': 148, 'yogi': 273, 'interested': 524, 'sick': 199, 'star': 378, 'brothers': 50, 'congress': 509, 'delivered': 528, 'welcome': 213, 'update': 237, 'sujeeth': 424, 'terry': 44, 'sides': 28, 'died': 146, 'happening': 93, 'haryana': 344, 'barcelona': 356, 'rathee': 486, 'time': 114}
no_to_nodename={}
for n in nodename_to_num.items():
	#print n[1]
	no_to_nodename[n[1]]=n[0]
# print no_to_nodename
node_list=[]
color_list=[]
# print lis
#print total

#colour=["red",]
fd1=open("ans1.txt","rw+")
line = fd1.readline()
lis=[]
#lis1=[]
while line:
	parts=line.split("--")
	l=[]
	l.append(no_to_nodename[int(parts[0])])
	l.append(int(parts[1]))
	lis.append(l)
	line = fd1.readline()

lis.sort(key=getKey)
#sort(lis, key = lambda element : elem[1])
# print lis

#print lis
#start="xyz"
#color=["green","red","blue"]
#print color_list
#s1=set()
#s2=set()
#s3=()
#start=1
#cnt=-1
for line in lis:
	parts=line
        #sort(parts[1])
        # print parts
	if int(parts[1]) == 1:
		#k = cnt%2
		#s1.add(str(parts[0]))
		#print parts[1]
                node_list.append(str(parts[0]))
                #g.add_node(str(parts[0]))
		#color_list[int(parts[1])]=str(color[k])
                color_list.append('red')
		# print color[k]
	if int(parts[1]) == 2:
		#k = cnt%2
		node_list.append(str(parts[0]))
                #g.add_node(str(parts[0]))
		#color_list[int(parts[1])]=str(color[k])
                color_list.append('blue')
        if int(parts[1]) == 3:
                #k = cnt%2
		node_list.append(str(parts[0]))
                #g.add_node(str(parts[0]))
		#color_list[int(parts[1])]=str(color[k])
                color_list.append('green')
	
g.add_nodes_from(node_list)
g.nodes()	
# print node_list
# print color_list
#nx.draw_networkx_nodes(g,nodelist=node_list,node_color=color_list,node_size=2000,alpha=0.5)

#color_node=color_list
fd=open("sample_input.txt","rw+")

# to skip the line to the value where we neede the answer

while fd.readline()!="\n":
	pass


line = fd.readline()
# print line
#node_count=set()
while line:
	line = line.strip()
	parts=line.split()
	a=str(no_to_nodename[int(parts[0])]) 
	b=str(no_to_nodename[int(parts[1])]) 
	g.add_edge(a,b)	
	line = fd.readline()

#total = len(node_count)         
fd.close()
nx.draw(g,node_color=color_list,node_size=2000,with_labels=True)
plt.draw()
plt.show()

