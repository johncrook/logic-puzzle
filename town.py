from Tkinter import *


class Town(object):
		def __init__(self, name, player):
				self.name = name

		def __str__(self):
				return self.name

class District(object):
		def __init__(self, Dnumber):
			self.number = Dnumber
			self.people = {}
			self.exits = {}
			self.buildings = {}
			#self.image = image

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


##  def __str__(self):
##      return "You are in {}. You can talk to {}. \n You can go {}.".format(self.number, self.people, self.exits)
##
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
			return t

		# adds people to their dictionary plus their text            
		def addPerson(self, name, text):
				self.text = {}
				
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


				

class Building(District):
		def __init__(self, name, people, exits):
				district.__init__(self, name, people, exits, image)



#######################################################################
#######################################################################
#create the town
Sedgewick = Town("Sedgewick", "Rick Sanchez")


#Create the Districts
D1 = District("District 1")
D2 = District("District 2")

#add stuff to district 1
D1.addPerson("bobby", bobbySpeech)
D1.addExits("east", D2)

#add stuff to district 2
D2.addPerson("steven", stevenSpeech[event])
D2.addExits("west", D1)


#####################################################################
#####################################################################
class Game(Frame):
	def __init__(self, parent, root):
		Frame.__init__(self, parent)
		#self.root = root
	
	currentDistrict = D1
	event = "wrath"
	print currentDistrict
	
	while(True):
		
		'''root = Tk()
		frame = Frame(root, width = 300, height = 300)
		root.title("cause i wanted to put a fucking title")'''
		
		action = raw_input("Player action: ")
		action = action.lower()
		player_input = action.split()
		if (action != "quit"):
			
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
						print response
					else:
						print " "
						response = "That is not a place you can go. Try north, east, south, or west."
						print response
						
				if (verb == "talk"):
					if (noun in currentDistrict.people):
						response = currentDistrict.people[noun][event]
						print response
					else:
						response = "Who dat?"
						print " "
						print response
						
			else:
				response = "I don't know what you tryna type, but I don't \n\
like it. Use actions like go, talk, or grab."
				print " "
				print response
		else:
			print " "
			print "Goodbye"
			break
	
		#root.mainloop()

#root Tk()
#g.play()
