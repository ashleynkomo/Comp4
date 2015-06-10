import random

class Crop:
    """A generic food crop""" #Doc string to tell python what class is for
    #Constructor
    def __init__(self,growth_rate,light_need,water_need):
        #Set attributes with initial value
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        #These attributes were public, they could have been used directly by programs outside class
        #I've made them private by adding underscore after (Self.) to only be used in the class
        #this is called ENCAPSULATION

    def needs(self):#when creating method you must pass self as a parameter
        #Dictionary works different from list as the values stored are in pairs(key:value)
        #this meas you can define key and use it foind associated value
        return {"light need":self._light_need,"water need":self._water_need}
    
    def report(self):
        return{"type":self._type,"status":self._status,"growth":self._growth,"days growing":self._days_growing}
    
    def update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Yound"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

    def auto_grow(crop,days):
        for day in range(days):
            light = random.randint(1,10)
            water = random.randint(1,10)
            crop.grow(light,water)

    
def main():
    #instaniate the class
    new_crop = Crop(1,4,3)
    #this is a test to see if it works or nahh
    print(new_crop.needs())#["light"] inside outer brackets to get specific value
    print(new_crop.report())#don't need to pass self its done automatically
    auto_grow(new_crop,30)
    #new_crop.grow(4,4)
    print(new_crop.report())


if __name__ == "__main__":
    main()
