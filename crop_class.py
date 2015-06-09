class Crop:
    """A generic food crop""" #Doc string to tell python what class is for
    #Constructor
    def __init__(self,growth_rate,light_need,water_need):
        #Set attributes with initial value
        self._growth = 0
        self._day_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        #These attributes were public, they could have been used directly by programs outside class
        #I've made them prive by adding underscore after (Self.)

def main():
    new_crop = Crop(1,4,3)
    print(new_crop._status)
    print(new_crop._light_need)
    print(new_crop._water_need)

if __name__ == "__main__":
    main()
