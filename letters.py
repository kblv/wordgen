import copy
import argparse

letters=list()
musthave=list()
invalidcombies=list()
wlen=int()
positions=list()

class position (object):
	def __init__(self,letterlist):
		self.__letterlist=letterlist
		self.__follow_position=None
		self.__current_letterpos=0
		
	def set_follower(self,follower):
		self.__follow_position=follower

	def next(self):
		if self.__current_letterpos+1 == len(self.__letterlist):
			self.__current_letterpos=0
			self.__follow_position.next()
		else:
			self.__current_letterpos+=1

	def get(self):
		return self.__letterlist[self.__current_letterpos]

class words(object):
	def __init__(self,letters,wlen,musthave,invalidcombies):
		self.__letterlist=letters
		#Is some work around - set makes the whole thing uniq, but positions class 
		#uses indexes and set does not support does -> that's why it becomes list
		#again
		self.__uniqletterlist=list(set(self.__letterlist))
		self.__positions=list()
		self.__musthaves=musthave
		self.__invalidcombies=invalidcombies
		self.__wlen=wlen

		for i in range(self.__wlen):
			posindex=i-1
			self.__positions.append(position(self.__uniqletterlist))	
			if posindex>0:
				self.__positions[posindex-1].set_follower(self.__positions[posindex])
		self.__positions[len(self.__positions)-2].set_follower(self.__positions[len(self.__positions)-1])


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
			print (word)
		self.__positions[0].next()		
	
	

class parameters(object):
	def __init__(self):
		self.__parser=argparse.ArgumentParser("Simple wordlist generator")
		self.__parser.add_argument("-c",required=True, dest="letters",nargs="+",help="Characters - Specifies all allowed characters - if letter is allowed twice, it needs to be given twice. \n Letters need to be given with spaces in between -> -c A B C")
		self.__parser.add_argument("-l",required=True, dest="wlen",type=int,action="store",help="Length - Length of the word")
		self.__parser.add_argument("-m", dest="musthave",default="", nargs="+",help="Musthave - List of charactersequences/characters which need to appear. \n Single sequences separated by space.")
		self.__parser.add_argument("-n", dest="invalidcombies",default="",nargs="+",help="Not - List of charactersequences which should be excluded \n Single sequences separated by space.")
	def export(self):
		global letters
		global musthave
		global invalidcombies 
		global wlen
		arguments=self.__parser.parse_args()
		letters=arguments.letters
		musthave=arguments.musthave
		invalidcombies=arguments.invalidcombies
		wlen=arguments.wlen
		

parameters().export()
masterword=words(letters,wlen,musthave,invalidcombies)
while True:
	#If all positions have been checked the last position will call its next-method
	#resulting in AttributeError as follower will be None
	#Not the cleanest way to signal all possible combinations have been checked -
	#but the fastest :)
	try:
		masterword.next()
	except AttributeError:
		exit()	
