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
                 filled):
        self.name = name
        self.slot = slot
        self.total = total
        self.number = number
        self.hour = hour
        self.minute = minute
        self.information = information
        self.expiration = expiration
        self.filled = filled

    def push(self):
        print("pushing")

    def move(self):
        print("Moving to " + str(self.slot))


Slot1 = Pill("", 1, 0, 0, 0, 0, "", "", False)
Slot2 = Pill("", 2, 0, 0, 0, 0, "", "", False)
Slot3 = Pill("", 3, 0, 0, 0, 0, "", "", False)
Slot4 = Pill("", 4, 0, 0, 0, 0, "", "", False)
Slot5 = Pill("", 5, 0, 0, 0, 0, "", "", False)
Slot6 = Pill("", 6, 0, 0, 0, 0, "", "", False)
Slot7 = Pill("", 7, 0, 0, 0, 0, "", "", False)
Slot8 = Pill("", 8, 0, 0, 0, 0, "", "", False)
Slot9 = Pill("", 9, 0, 0, 0, 0, "", "", False)
Slot10 = Pill("", 10, 0, 0, 0, 0, "", "", False)


def CreatePill(self):
    print("activated")
    while True:
        if not Slot1.filled:
            Slot1.move()
            Slot1.filled = True
            break
        if not Slot2.filled:
            Slot2.move()
            Slot2.filled = True
            break
        if not Slot3.filled:
            Slot3.move()
            Slot3.filled = True
            break
        if not Slot4.filled:
            Slot4.move()
            Slot4.filled = True
            break
        if not Slot5.filled:
            Slot5.move()
            Slot5.filled = True
            break
        if not Slot6.filled:
            Slot6.move()
            Slot6.filled = True
            break
        if not Slot7.filled:
            Slot7.move()
            Slot7.filled = True
            break
        if not Slot8.filled:
            Slot8.move()
            Slot8.filled = True
            break
        if not Slot9.filled:
            Slot9.move()
            Slot9.filled = True
            break
        if not Slot10.filled:
            Slot10.move()
            Slot10.filled = True
            break
        print("Every Slot is Filled")
        break
