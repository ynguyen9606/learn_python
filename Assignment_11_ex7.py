class Battery:
    def __init__(self):
        self.__energy = 10

    def getEnergy(self):
        return self.__energy
    
    def setEnergy(self, energy):
        if 0 <= energy <= 100:
            self.__energy = energy
        elif energy > 100:
            self.__energy = 100
        else:
            self.__energy = 0

    def decreaseEnergy(self):
        if self.__energy >= 2:
            self.__energy -= 2
        else:
            self.__energy = 0

class FlashLamp:
    def __init__(self):
        self.__status = False
        self.__battery = None

    def getBatteryInfo(self):
        if self.__battery is not None:
            return self.__battery.getEnergy()
        else:
            return "k co pin"
    
    def setBattery(self, b):
        self.__battery = b
    
    def turnOn(self):
        self.__status = True
        if self.__battery is not None and self.__battery.getEnergy() > 0:
            print("Đen sang")
        else:
            print("Đen k sang")

    def turnOff(self):
        self.__status = False
        print("den tat")

class TestFlashLamp:
    def main():
        battery = Battery()

        lamp = FlashLamp()

        lamp.setBattery(battery)

        for i in range(10):
            lamp.turnOn()
            lamp.turnOff()
        
        print("Nang lung pin con lai: ", battery.getEnergy())

TestFlashLamp.main()