import datetime
from datetime import datetime
from Design.Colors import Black, Red
from Design.Fonts import DefaultFont
from Tools.PillTypes import Pill, Liquid
from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen


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


class HomePage:
    def build(self):
        def GetRecentPill():
            name = Slot1.name
            namelength = len(Slot1.name)
            length = 20 - namelength
            for i in range(length):
                name = name + "  "

            return name.upper()

        def GetRecentPillTime(Slot, now):
            hour = Slot.hour
            minute = Slot.minute
            hoursleft = hour - now.hour
            if hoursleft == 0:
                minutesleft = minute - now.minute
                if minutesleft < 0:
                    hoursleft = 24
                    return str(hoursleft) + " Hours Left"
                else:
                    return str(minutesleft) + " Minutes Left"
            elif hoursleft < 0:
                hours = abs(24 - now.hour)
                hoursleft = hours + Slot.hour
                return str(hoursleft) + " Hours Left"
            elif hoursleft == 1:
                return str(hoursleft) + " Hour Left"
            else:
                return str(hoursleft) + " Hours Left"

        def ChooseIcon(Slot):
            SolidPillTypeIcon = 'C:\GUIIcons\PillType.png'
            LiquidTypeIcon = 'C:\GUIIcons\LiquidType.png'
            if Slot.Type() == "solid":
                return SolidPillTypeIcon
            else:
                return LiquidTypeIcon

        def ChooseLabel(self, Slot):
            if Slot.Type() == 'solid':
                if Slot.number == 1:
                    return str(Slot.number) + ' Pill'
                else:
                    return str(Slot.number) + " Pills"
            else:
                if Slot.volume == 1:
                    return str(Slot.volume) + ' mL'
                else:
                    return str(Slot.volume) + " mL"
        HomeScreen = Screen(name='home')
        HomeScreen.clearcolor = Black
        HomeScreenLayout = RelativeLayout(size_hint_x=None, width=200, size_hint_y=None, height=500)

        UpNext = Label(text="Up Next", color=Black, font_size=35, font_name=DefaultFont, pos=(-25, 10))
        PillType = Image(source=ChooseIcon(Slot12), size_hint_x=None, width=200, pos=(-50, -75))
        PillName = Label(text=GetRecentPill(), color=Red, font_size=40, font_name=DefaultFont, pos=(230, -75),
                         size_hint_x=None,
                         width=150)
        PillTime = Label(text=GetRecentPillTime(Slot12, datetime.now()), color=Black, font_size=35,
                         font_name=DefaultFont,
                         pos=(575, -75))
        PillNumber = Label(text=ChooseLabel(self, Slot12), color=Black, font_size=35,
                           font_name=DefaultFont, pos=(-35, -150))

        HomeScreenLayout.add_widget(UpNext)
        HomeScreenLayout.add_widget(PillType)
        HomeScreenLayout.add_widget(PillName)
        HomeScreenLayout.add_widget(PillTime)
        HomeScreenLayout.add_widget(PillNumber)

        HomeScreen.add_widget(HomeScreenLayout)
        return HomeScreen

class MainClock:
    def build(self):
        def GetAMTime(now):
            hour = now.hour
            minute = str(now.minute)
            Sub = " AM"
            if now.minute < 10:
                minute = "0" + minute
            if now.hour > 12:
                hour = now.hour - 12
                Sub = " PM"
            elif now.hour < 12:
                Sub = " AM"
            hour = str(hour)
            return hour + ":" + minute + Sub

        def GetTwentyFourTime(now):
            print('Getting 24 Hour Time')
            hour = str(now.hour)
            minute = str(now.minute)
            if now.minute < 10:
                minute = "0" + minute
            print(hour + ":" + minute)
            return hour + ":" + minute
        MenuClock = Label(text="Time", color=Black, size_hint_y=None, height=30)
        ClockAnchor = AnchorLayout(anchor_y='top', anchor_x='right')
        ClockAnchor.add_widget(MenuClock)

        def timeupdate():
            MenuClock.text = GetAMTime(datetime.now())
            pass

        Clock.schedule_interval(lambda dt: timeupdate(), 0.5)

        return ClockAnchor
