from Tkinter import *

#THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST
#THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST
#THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST
#THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST
#THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST THE BEST

#this class creates the town
class Town(object):
        #this funtion gives the town a name
        def __init__(self, name, player):
                self.name = name
        #this function returns the town name
        def __str__(self):
                return self.name

#the district class is an object that the player can move around the screen on
class District(object):

        #each distict has a number, people, exits, items, grabbables, and an image
        def __init__(self, districtNum, image):
                self.districtNum = districtNum
                self.people = {}
                self.exits = {}
                self.items = {}
                self.grabbables = []
                self.image = image

        #this is an accessor
        @property
        def districtNum(self):
                return self._districtNum

        #this is a mutator
        @districtNum.setter
        def districtNum(self, value):
                self._districtNum = value

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
                self._image = value

        # base display    
        def __str__(self):
        # what district you're in
                t = "You are in {}.\n".format(self.districtNum)
            
                # who you can talk to 
                t += "You can talk to: "
                for people in self._people.keys():
                        t += people +" "
                t += "\n"
	
                # exits in the District
                t += "You can go: "
                for exit in self._exits.keys():
                        t += exit +" "
                t += "\n"

                #items in the District 
                t += "You see: "
                for item in self.items.keys():
                        t += item + " "
                return t

          

        # adds people to their dictionary plus their text            
        def addPerson(self, name, text):
                self._people[name] = text

        # adds exits and district to correct dictionary    
        def addExits(self, exit, district):
                self.exits[exit] = district

        # adds what image    
        #def displayImage(self):
                #set screen to district image
                #pass

        #add items to the district
        def addItem(self, item, desc):
                self._items[item] = desc


#the game is the object that is the game iteself which is a frame in tkinter               
class Game(Frame):
        #the constructer which gets its atributes from the frame class from tkinter
        def __init__(self, parent):
                Frame.__init__(self, parent)
        #this function calls the other functions inside the game class to run the game
        def play(self):
                #self.setPersonText()
                self.createDistricts()
                self.setupGUI()
                self.districtImage()
                self.setStatus("")

        #this function gives all of the CPU's speech
        #def setPersonText(self):
                #the event counter changes base off of how far you are in the game which determines the speech of each charater
                
        #this function is responsible for creating the districts and everything contained in them
        def createDistricts(self):
                #create the town
                Sedgewick = Town("Sedgewick", "Rick Sanchez")

                event = 0
                bobbyList = ["Thank God you are here. My wife is frigh_tend of me. She claims that I assulted her last night but I don't remember anything."]
                bobbySpeech = bobbyList[event]

                #Create the Districts
                D1 = District("District 1", "District1.gif")
                D2 = District("District 2", "District2.gif")
                D3 = District("District 3", "room3.gif")
                D4 = District("District 4", "room4.gif")
                D5 = District("District 5", "room5.gif")
                D6 = District("District 6", "room6.gif")
                D7 = District("District 7", "skull.gif")
                D8 = District("District 8", "GameOver.gif")
                D9 = District("District 9", "District1.gif")

                #add stuff to district 1
                D1.addPerson("bobby", bobbySpeech)
                D1.addExits("east", D2)
                D1.addExits("south", D4)
                D1.addItem("cross", "It is wooden with a Latin inscription.")

                #add stuff to district 2
                D2.addPerson("steven", "I , wanna be a real boy.")
                D2.addExits("west", D1)
                D2.addExits("east", D3)
                D2.addExits("south", D5)
                D2.addItem("wheelbarrow", "It is filled with firewood.")

                #add stuff to district 3
                D3.addPerson("dean", "My dad went on a hunting trip, he hasn't been home in a few days.")
                D3.addExits("west", D2)
                D3.addExits("south", D5)
                D3.addItem("sickle", "It seems to have been put to good use.")

                #add stuff to district 4
                D4.addPerson("charlie", "I am the town blacksmith.")
                D4.addExits("north", D1)
                D4.addExits("east", D5)
                D4.addExits("south", D7)
                D4.addItem("hammer", "It has charlie carved into the handle.")

                #add stuff to district 5
                D5.addPerson("michael", "My family has lived in this town for three generations.")
                D5.addExits("east", D6)
                D5.addExits("west", D4)
                D5.addExits("north", D2)
                D5.addExits("south", D8)
                D5.addItem("clock", "It is very ornate.")

                #add stuff to district 6
                D6.addPerson("ellen", "My husband owns the bank.")
                D6.addExits("west", D5)
                D6.addExits("north", D3)
                D6.addExits("south", D9)
                D6.addItem("wallet", "Someone must have dropped this.")

                #add stuff to distict 7
                D7.addPerson("john", "I just got back into town, I'm Dean's father.")
                D7.addExits("east", D8)
                D7.addExits("north", D6)
                D7.addItem("rifle", "It has two eagle feathers hanging from it.")

                #add stuff to district 8
                D8.addPerson("charlotte", "The blacksmith is my husband.")
                D8.addExits("east", D9)
                D8.addExits("west", D7)
                D8.addExits("north", D5)
                D8.addItem("lunch", "Charlotte made this for the blacksmith.")

                #add stuff to district 9
                D9.addPerson("phillip", "Hello! I am the mayor of Sedgewick!")
                D9.addExits("west", D8)
                D9.addExits("north", D6)
                D9.addItem("ledger", "This has the names and addresses of all the townspeople.")

                Game.currentDistrict = D1

        #this function sets up the window for the GUI
        def setupGUI(self):
                self.pack(fill = BOTH, expand = 1)
                
                Game.player_input = Entry(self, bg = "white")
                Game.player_input.bind("<Return>", self.process)
                Game.player_input.pack(side = BOTTOM, fill = X)
                Game.player_input.focus()
                
                img = None
                Game.image = Label(self, width = 800, height = 600, image = img)
                Game.image.image = img
                Game.image.pack(side = LEFT, fill = Y)
                Game.image.pack_propagate(False)
                
                text_frame = Frame(self, width = 200)
                Game.text = Text(text_frame, bg = "lightgrey", fg="blue", state = DISABLED)
                Game.text.pack(fill = Y, expand = 1)
                text_frame.pack(side = RIGHT, fill = Y)
                text_frame.pack_propagate(False)

        def districtImage(self):
                Game.img = PhotoImage(file = Game.currentDistrict.image)
                Game.image.config(image = Game.img)
                Game.image.image = Game.img

        def setStatus(self, status):
                Game.text.config(state = NORMAL)
                Game.text.delete("1.0", END)
                Game.text.insert(END, str(Game.currentDistrict) + "\nYour status is:" + status)
                Game.text.config(state = DISABLED)

        def process(self, event):
                #action = raw_input("Player action: ")
                action = Game.player_input.get()
                action = action.lower()
                player_input = action.split()
                #if (action != "quit"):
                response = "I don't know what you tryna type, but I don't like it. \n Use actions like go, look, talk, or grab."
                if (action == "quit" or action == "exit" or action == "bye" \
                    or action == "sionara!"):
                        exit(0)
                if (len(player_input) == 2):
                        verb = player_input[0]
                        noun = player_input[1]
                        if (verb == "go"):
                            if (noun in Game.currentDistrict.exits):
                                Game.currentDistrict = Game.currentDistrict.exits[noun]
                                response = "District changed"
                                print " "
                                print Game.currentDistrict
                                print " "                       
                            else:
                                print " "
                                response = "That is not a place you can go. Try north, east, south, or west."
                        elif (verb == "talk"):
                            if (noun in Game.currentDistrict.people):
                                response = Game.currentDistrict.people[noun]
                        elif (verb == "look"):
                                response = "I don't see that item."
                                if (noun in Game.currentDistrict.items):
                                        response = Game.currentDistrict.items[noun]                    
                    #print " "            
                    #print response
                #else:
                    #pass

                self.setStatus(response)
                self.districtImage()
                Game.player_input.delete(0, END)
  
##root = Tk()
##frame = Frame(root, width= 200, height= 200)
##root.title("cause i wanted to put a title")
##g = Game(root)
##root.mainloop()
WIDTH = 1000
HEIGHT = 1000
window = Tk()
window.title("motha fukin title /Vigga")
g = Game(window)
g.play()
window.mainloop()

