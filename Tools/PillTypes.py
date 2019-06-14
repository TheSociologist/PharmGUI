class Pill:
    def __init__(self,
                 name,
                 slot,
                 total,
                 number,
                 hour,
                 minute,
                 information,
                 expiration,
                 filled,
                 ):
        self.name = name
        self.slot = slot
        self.total = total
        self.number = number
        self.hour = hour
        self.minute = minute
        self.information = information
        self.expiration = expiration
        self.filled = filled

    def Type(self):
        return 'solid'

    def push(self):
        print("pushing")

    def move(self):
        print("Moving to " + str(self.slot))

class Liquid:
    def __init__(self, slot, name, mass, volume, hour,
                 minute, filled):
        self.slot = slot
        self.name = name
        self.mass = mass
        self.hour = hour
        self.minute = minute
        self.volume = volume
        self.filled = filled
    def dispense(self):
        print('dispensing liquid')

    def Type(self):
        return 'liquid'




Slot1 = Pill("Tylenol", 1, 0, 5, 21, 30, "Painkiller", "9/12/2019", True)
Slot2 = Pill("", 2, 0, 0, 0, 0, "", "", False)
Slot3 = Pill("", 3, 0, 0, 0, 0, "", "", False)
Slot4 = Pill("", 4, 0, 0, 0, 0, "", "", False)
Slot5 = Pill("", 5, 0, 0, 0, 0, "", "", False)
Slot6 = Pill("", 6, 0, 0, 0, 0, "", "", False)
Slot7 = Pill("", 7, 0, 0, 0, 0, "", "", False)
Slot8 = Pill("", 8, 0, 0, 0, 0, "", "", False)
Slot9 = Pill("", 9, 0, 0, 0, 0, "", "", False)
Slot10 = Pill("", 10, 0, 0, 0, 0, "", "", False)
Slot11 = Liquid(11, "Cough Syrup", 30, 30, 12, 30, True)
Slot12 = Liquid(12, "Cough Syrup", 30, 30, 12, 30, True)
Pills = [Slot1.name,
         Slot2.name,
         Slot3.name,
         Slot4.name,
         Slot5.name,
         Slot6.name,
         Slot7.name,
         Slot8.name,
         Slot9.name,
         Slot10.name,
         Slot11.name,
         Slot12.name]