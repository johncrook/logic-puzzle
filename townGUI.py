from Tkinter import *


class Town(object):
	def __init__(self, name, player):
		self.name = name

	def __str__(self):
		return self.name

class District(object):
	def __init__(self, Dnumber, image):
		self.number = Dnumber
		self.people = {}
		self.exits = {}
		self.buildings = {}
		self.items = {}
		self.grabbables = []
		self.image = image

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self):
		self._name = value

	@property
	def number(self):
		return self._number

	@number.setter
	def number(self, value):
		self._number = value

	@property
	def people(self):
		return self._people

	@people.setter
	def people(self, value):
		self._people = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def buildings(self):
		return self._buildings

	@buildings.setter
	def buildings(self, value):
		self._buildings = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables= value

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, value):
		self._image = value

	def play(self):

#######################################################################
		def setupGUI(self):
			# organize the GUI
			self.pack(fill=BOTH, expand=1)
			# setup the player input at the bottom of the GUI
			# the widget is a Tkinter Entry
			# set its background to white and bind the return key to the
			# function process in the class
			# push it to the bottom of the GUI and let it fill horizontally
			# give it focus so the player doesn't have to click on it
			Game.player_input = Entry(self, bg="white")
			Game.player_input.bind("<Return>", self.process)
			Game.player_input.pack(side=BOTTOM, fill=X)
			Game.player_input.focus()

			# setup the image to the left of the GUI
			# the widget is a Tkinter Label
			# don't let the image control the widget's size
			img = None
			Game.image = Label(self, width=int(WIDTH / 2), image=img)
			Game.image.image = img
			Game.image.pack(side=LEFT, fill=Y)
			Game.image.pack_propagate(False)

			# setup the text to the right of the GUI
			# first, the frame in which the text will be placed
			text_frame = Frame(self, width=WIDTH / 2)
			# the widget is a Tkinter Text
			# disable it by default
			# don't let the widget control the frame's size
			Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
			Game.text.pack(fill=Y, expand=1)
			text_frame.pack(side=RIGHT, fill=Y)
			text_frame.pack_propagate(False)
#######################################################################
		# base display    
		def __str__(self):
			# what district you're in
			t = "You are in {}.\n".format(self._number)

			# who you can talk to 
			t += "You can talk to: "
			for people in self._people.keys():
				t += people +" "
				t += "\n"

			# exits
			t += "You can go: "
			for exit in self._exits.keys():
				t += exit +" "
				t += "\n"

			t += "You see: "
			for item in self.items.keys():
				t += item + " "
				t += "\n"
			return t
#######################################################################
		#set the current room image
		def setRoomImage(self):
			if (Game.currentRoom == None):
				#if dead,set skull image
				Game.img = PhotoImage(file="skull.gif")
			else:
				Game.img = PhotoImage(file=Game.currentRoom.image)
				Game.image.config(image=Game.img)
				Game.image.image = Game.img
#######################################################################
	# adds people to their dictionary plus their text            
	def addPerson(self, name, text):
		self._people[name] = text

	# adds exits and district to correct dictionary    
	def addExits(self, exit, district):
		self.exits[exit] = district

	# adds building in districts    
	def addBuildings(self, building, main_room):
		self.buildings[building] = main_room

	# adds what image    
	def displayImage(self):
		#set screen to district image
		pass

	def addItem(self, item, desc):
		self._items[item] = desc

	def addGrabbable(self, grabbable):
		pass

	def addImage(self, image):
		self.image = image

#######################################################################
def walkLeft(event):
	print "why you want to go left?"

def walkRight(event):
	print "why you want to go right?"


class Building(District):
	def __init__(self, name, people, exits):
		district.__init__(self, name, people, exits, image)
#######################################################################
stage = 1
bobbyList = ["Thank God you are here. My wife is frigh_tend of me. She claims that I assulted her last night but I don't remember anything.",\
"Thank you for helping me straighten things out with my wife. I owe you one."]
bobbySpeech = bobbyList[stage]
#######################################################################
#print D1
#create the town
Sedgewick = Town("Sedgewick", "Rick Sanchez")
#Create the Districts
D1 = District("District 1", "District1.gif")
D2 = District("District 2", "District2.gif")
##D3 = District("District 3")
##D4 = District("District 4")
##D5 = District("District 5")
##D6 = District("District 6")
##D7 = District("District 7")
##D8 = District("District 8")
##D9 = District("District 9")

#add the district images

#add stuff to district 1
D1.addPerson("bobby", bobbySpeech)
D1.addExits("east", D2)
#D1.addExits("south", D4)
D1.addItem("cross", "It is wooden with a Latin inscription.")

#add stuff to district 2
#D2.addPerson("steven", stevenSpeech)
D2.addExits("west", D1)
#D2.addExits("east", D3)
#D2.addExits("south", D5)
D2.addItem("wheelbarrow", "It is filled with firewood.")

#add stuff to district 3
##D3.addPerson("dean", deanSpeech)
##D3.addExits("west", D2)
##D3.addExits("south", D5)
##D3.addItem("sickle", "It seems to have been put to good use.")
##
###add stuff to district 4
##D4.addPerson("charlie", charlieSpeech)
##D4.addExits("north", D1)
##D4.addExits("east", D5)
##D4.addExits("south", D7)
##D4.addItem("hammer", "It has charlie carved into the handle.")
##
###add stuff to district 5
##D5.addPerson("michael", michaelSpeech)
##D5.addExits("east", D6)
##D5.addExits("west", D4)
##D5.addExits("north", D2)
##D5.addExits("south", D8)
##D5.addItem("clock", "It is very ornate.")
##
###add stuff to district 6
##D6.addPerson("ellen", ellenSpeech)
##D6.addExits("west", D5)
##D6.addExits("north", D3)
##D6.addExits("south", D9)
##D6.addItem("wallet", "Someone must have dropped this.")
##
###add stuff to distict 7
##D7.addPerson("john", johnSpeech)
##D7.addExits("east", D8)
##D7.addExits("north", D6)
##D7.addItem("rifle", "It has two eagle feathers hanging from it.")
##
###add stuff to district 8
##D8.addPerson("charlotte", charlotteSpeech)
##D8.addExits("east", D9)
##D8.addExits("west", D7)
##D8.addExits("north", D5)
##D8.addItem("lunch", "Charlotte made this for the blacksmith.")
##
###add stuff to district 9
##D9.addPerson("phillip", phillipSpeech)
##D9.addExits("west", D8)
##D9.addExits("north", D6)
##D9.addItem("ledger", "This has the names and addresses of all the townspeople.")
#######################################################################
def Game(Frame):
	currentDistrict = D1

	while(True):

		action = raw_input("Player action: ")
		action = District.player_input.get()
		action = action.lower()
		player_input = action.split()
		if (action != "quit"):

			response = "I don't know what you tryna type, but I don't \n\
			like it. Use actions like go, look, talk, or grab."

		if (len(player_input) == 2):
			verb = player_input[0]
			noun = player_input[1]

			if (verb == "go"):
				if (noun in currentDistrict.exits):
					currentDistrict = currentDistrict.exits[noun]
					response = "District changed"
					print " "
					print currentDistrict
					print " "                       

				else:
					print " "
					response = "That is not a place you can go. Try north, east, south, or west."

			if (verb == "talk"):
				if (noun in currentDistrict.people):
					response = currentDistrict.people[noun]

			if (verb == "look"):
				response = "I don't see that item."
				if (noun in currentDistrict.items):
					response = currentDistrict.items[noun]
             
					print " "            
					print response
				else:
					break


#######################################################################
##root = Tk()
##frame = Frame(root, width= 200, height= 200)
##root.title("cause i wanted to put a fucking title")
##g = Game(root)
##root.mainloop()
WIDTH = 800
HEIGHT = 600

root = Tk()
#root.title("lel it workz")

g = Game(root)
g.play()
root.mainloop()
