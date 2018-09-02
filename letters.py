import copy

letters=list(["F","W","N","G","M","N","U","T","A","U","F","G"])
musthave=list(["A","U"])
invalidcombies=list(["UU","AA","FW","FN","FG","FM","WW","WF","WN","WG","WM","WT","NW","GF","GG","GT"])
wlen=5
positions=list()

class position (object):
	def __init__(self,letterlist):
		self.__letterlist=letterlist
		self.__follow_position=None
		self.__current_letterpos=0
		self.__completed_once=False
		
	def set_follower(self,follower):
		self.__follow_position=follower

	def next(self):
		if self.__current_letterpos+1 == len(self.__letterlist):
			self.__current_letterpos=0
			self.__follow_position.next()
			self.__completed_once=True
		else:
			self.__current_letterpos+=1

	def get(self):
		return self.__letterlist[self.__current_letterpos]

class word(object):
	def __init__(self,letters,positions,musthave,invalidcombies):
		self.__letterlist=letters
		self.__positions=positions
		self.__musthaves=musthave
		self.__invalidcombies=invalidcombies
	def __validate(self,word):
		tmpletterlist=copy.copy(self.__letterlist)
		for char in word:
			try:
				tmpletterlist.remove(char)
			except ValueError:
				return False	
		return True

	def __checkmusthaves(self,word):
		for musthave in self.__musthaves:
			if not musthave in word:
				return False
		return True

	def __checkinvalidcombies(self,word):
		for invalidcombie in self.__invalidcombies:
			if invalidcombie in word:
				return False
		return True
				
	def next(self):
		word=""
		for position in self.__positions:
			word+=position.get()
		if self.__validate(word) and self.__checkmusthaves(word) and self.__checkinvalidcombies(word):
			print ("Wort:", word)
		self.__positions[0].next()		
	
for i in range(wlen):
	posindex=i-1
	positions.append(position(letters))	
	#if i < wlen and posindex>0:
	if posindex>0:
		positions[posindex-1].set_follower(positions[posindex])
positions[len(positions)-2].set_follower(positions[len(positions)-1])
	

while True:
	masterword=word(letters,positions,musthave,invalidcombies)
	masterword.next()
#while True:
#	word=""
#	for position in positions:
#		word+=position.get()
#	print (word)
#	positions[0].next()
