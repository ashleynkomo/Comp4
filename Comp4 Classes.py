class VirtualPet:
    #This is the constructor, it runs the automatically on instaniation
    def __init__(self, name):
        self.name = name
        self.energy = 9000
        self.mood = "Proud"
        self.bowel = 0
        print("I HAVE THE POWER, {0}".format(self.name))

    def eat(self,food):
        if food == "chow":
            self.energy = self.energy + 50
            self.bladder = self.bowel + 2
            print("Schlek!! Schlek!!")
        elif food == "stray dogs":
            self.energy = self.energy + 100
            self.bladder = self.bowel + 50
            print("OMNOM!! OMNOM!!")
        elif food == "fish food":
            self.energy = self.energy - 30
            self.bladder = self.bowel + 100 
            self.mood = "ill"
            print("why, master, why!! you give me kryptonite!!")
        elif food == "stray dogs":
            self.energy = self.energy + 100
            self.bladder = self.bladder + 50
            print("OMNOM!! OMNOM!!")


#Object creation
pet_one = VirtualPet("HE-MAN")#instantiating a class into an object
