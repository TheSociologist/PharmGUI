from kivy import Config
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
#Config.set('graphics', 'fullscreen', 'fake')
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, SlideTransition
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.recycleview import RecycleView
from kivy.adapters.listadapter import ListAdapter

import datetime
from datetime import datetime

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
        minute =  "0" + minute
    print(hour + ":" + minute)
    return hour + ":" + minute


Black = (0, 0, 0, 1)
White = (1, 1, 1, 1)
Gray = (0, 0, 0, 0.5)
Red = (1, 132/255, 10/255, 1)

ButtonFont = 'C:\Fonts\Roboto_Condensed\RobotoCondensed-Regular'

SettingsIcon = 'C:\GUIIcons\settings.png'
PillIcon = 'C:\GUIIcons\pill.png'
BackIcon = 'C:\GUIIcons\back.png'

HomeIcon = 'C:\GUIIcons\home.png'
SelectionIcon = 'C:\GUIIcons\Selection.png'
SliderBackground = "C:\GUIIcons\sliderbackground.png"

Window.size = (800, 480)
Window.clearcolor = White

def GetRecentPill():
    name = Slot1.name
    namelength = len(Slot1.name)
    length = 20 - namelength
    for i in range(length):
        name = name+"  "

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
        hours = abs(24-now.hour)
        hoursleft = hours + Slot.hour
        return str(hoursleft) +" Hours Left"
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



class Pharm(App):
    def build(self):
        OverLayout = GridLayout(rows=3)
        sm = ScreenManager()
        HomeScreen = Screen(name='home')
        HomeScreen.clearcolor = Black
        HomeScreenLayout = RelativeLayout(size_hint_x=None, width=200, size_hint_y=None, height=500)

        UpNext = Label(text="Up Next", color=Black, font_size=35, font_name=ButtonFont, pos=(-25, 10))
        PillType = Image(source=ChooseIcon(Slot12), size_hint_x=None, width=200, pos=(-50, -75))
        PillName = Label(text=GetRecentPill(), color=Red, font_size=40, font_name=ButtonFont, pos=(230, -75),
                         size_hint_x=None,
                         width=150)
        PillTime = Label(text=GetRecentPillTime(Slot12, datetime.now()), color=Black, font_size=35,
                         font_name=ButtonFont,
                         pos=(575, -75))
        PillNumber = Label(text=ChooseLabel(self, Slot12), color=Black, font_size=35,
                           font_name=ButtonFont, pos=(-35, -150))

        HomeScreenLayout.add_widget(UpNext)
        HomeScreenLayout.add_widget(PillType)
        HomeScreenLayout.add_widget(PillName)
        HomeScreenLayout.add_widget(PillTime)
        HomeScreenLayout.add_widget(PillNumber)

        HomeScreen.add_widget(HomeScreenLayout)


        def GoBack(self):
            print('activated')
            print(sm.current)
            sm.transition = NoTransition()
            if sm.current == "devicesnotes":
                sm.current = "notifications"
            elif sm.current == "phoneenotes":
                sm.current = 'notifications'
            elif sm.current == "notifications":
                sm.current = 'settings'
            elif sm.current == 'security':
                sm.current = 'settings'
            elif sm.current == 'dispensing':
                sm.current = 'settings'
            elif sm.current == 'accessibility':
                sm.current = 'settings'
            sm.transition = SlideTransition()

        class ReturnButton(Button, RelativeLayout):
            def __init__(self):
                Button.__init__(self)
                RelativeLayout.__init__(self)
                self.background_normal = ''
                self.background_color = White
                
                self.bind(on_press=GoBack)

        def GoTonotifications(self):
            sm.transition = NoTransition()
            sm.current = 'notifications'
            sm.transition = SlideTransition()
        def GoTosecurity(self):
            sm.transition = NoTransition()
            sm.current = 'security'
            sm.transition = SlideTransition()

        def GoTodispensing(self):
            sm.transition = NoTransition()
            sm.current = 'dispensing'
            sm.transition = SlideTransition()

        def GoToaccessibility(self):
            sm.transition = NoTransition()
            sm.current = 'accessibility'
            sm.transition = SlideTransition()



        #Settings
        SettingsScreen = Screen(name='settings')
        SettingsScreenLayout = BoxLayout(orientation='vertical', size_hint_y=None, height=1000, pos=(0, 25),
                                         padding=10)

        NotificationsButton = Button(text="Notifications", color=White, font_size=40,
                               font_name=ButtonFont,
                               size_hint_y=None,
                               height=60,
                               background_color=Black)
        NotificationsButton.bind(on_press=GoTonotifications)
        SecurityButton = Button(text="Security", color=White, font_size=40,
                               font_name=ButtonFont,
                               size_hint_y=None,
                               height=60,
                               background_color=Black)
        SecurityButton.bind(on_press=GoTosecurity)
        DispensingButton = Button(text="Dispensing", color=White, font_size=40,
                          font_name=ButtonFont,
                          size_hint_y=None,
                          height=60,
                          background_color=Black)
        DispensingButton.bind(on_press=GoTodispensing)
        AccessibilityButton = Button(text="Accessibility", color=White, font_size=40,
                                  font_name=ButtonFont,
                                  size_hint_y=None,
                                  height=60,
                                  background_color=Black)
        AccessibilityButton.bind(on_press=GoToaccessibility)

        SettingsScreenLayout.add_widget(NotificationsButton)
        SettingsScreenLayout.add_widget(SecurityButton)
        SettingsScreenLayout.add_widget(DispensingButton)
        SettingsScreenLayout.add_widget(AccessibilityButton)
        SettingsScreen.add_widget(SettingsScreenLayout)

        def GoToDeviceNotes(self):
            sm.transition = NoTransition()
            sm.current = 'devicesnotes'
            sm.transition = SlideTransition()

        def GoToPhoneNotes(self):
            sm.transition = NoTransition()
            sm.current = 'phonenotes'
            sm.transition = SlideTransition()

        NotificationsScreen = Screen(name="notifications")
        NotificationsScreenManager = BoxLayout(orientation='vertical', size_hint_y=None, height=1000, pos=(0, 25),
                                         padding=100, spacing=10)
        DeviceNotesButton = Button(text="Device Notifications", color=White, font_size=40,
                                  font_name=ButtonFont,
                                  size_hint_y=None,
                                  height=60,
                                  background_color=Black)
        DeviceNotesButton.bind(on_press=GoToDeviceNotes)
        PhoneNotificationsButton = Button(text="Phone Notifications", color=White, font_size=40,
                                   font_name=ButtonFont,
                                   size_hint_y=None,
                                   height=60,
                                   background_color=Black)
        PhoneNotificationsButton.bind(on_press=GoToPhoneNotes)

        NotificationsScreenManager.add_widget(DeviceNotesButton)
        DeviceNotesScreen = Screen(name='devicesnotes')

        SuperDeviceNotesLayout = GridLayout(rows=2, cols=1, pos=(10, 30) )
        DeviceNotesLayout = GridLayout(cols=2, rows=6, size_hint_y=None, height=400,
                                       row_force_default=True, col_force_default=True, col_default_width=350,
                                       row_default_height=35)

        NotificationsScreenManager.add_widget(PhoneNotificationsButton)
        NotificationsScreen.add_widget(NotificationsScreenManager)


        AlarmLabel = Label(text="Medicine Alarms", color=Black,
                           font_size=25,
                                   font_name=ButtonFont, halign='left', disabled=False)
        AlarmVolume = Label(text="Alarm Volume", color=Gray,
                           font_size=25,
                                   font_name=ButtonFont)

        MissingPillLabel = Label(text="Missed Pill Notifications", color=Black,
                                 font_size=25,
                                   font_name=ButtonFont, halign='left')
        BatteryWarningLabel = Label(text="Low Battery Notifications", color=Black,
                                    font_size=25,
                                   font_name=ButtonFont)
        ExpirationWarningLabel = Label(text="Upcoming Expiration Date Notifications",
                                       color=Black,
                                       font_size=25,
                                   font_name=ButtonFont, halign='left')
        LowPillCountLabel = Label(text="Low PIll Count Notifications", color=Black,
                                  font_size=25,
                                   font_name=ButtonFont, halign='left')

        AlarmToggle = CheckBox(color=Black)
        AlarmVolumeSlider = Slider(min=0, max=100, value=50, orientation="horizontal",
                                   cursor_size=(30,30), disabled=False)

        MissingPillWarningToggle = CheckBox(color=Black)
        BatteryWarningToggle = CheckBox(color=Black)
        ExpirationWarningToggle = CheckBox(color=Black)
        LowPillCountToggle = CheckBox(color=Black)

        DeviceNotesLayout.add_widget(AlarmLabel)
        DeviceNotesLayout.add_widget(AlarmToggle)

        DeviceNotesLayout.add_widget(AlarmVolume)
        DeviceNotesLayout.add_widget(AlarmVolumeSlider)

        DeviceNotesLayout.add_widget(MissingPillLabel)
        DeviceNotesLayout.add_widget(MissingPillWarningToggle)

        DeviceNotesLayout.add_widget(BatteryWarningLabel)
        DeviceNotesLayout.add_widget(BatteryWarningToggle)

        DeviceNotesLayout.add_widget(ExpirationWarningLabel)
        DeviceNotesLayout.add_widget(ExpirationWarningToggle)

        DeviceNotesLayout.add_widget(LowPillCountLabel)
        DeviceNotesLayout.add_widget(LowPillCountToggle)


        #SuperDeviceNotesLayout.add_widget(DeviceNotesLayout)
        SuperDeviceNotesLayout.add_widget(ReturnButton())
        DeviceNotesScreen.add_widget(SuperDeviceNotesLayout)

        def DevicerefreshAlarmState():
            if AlarmToggle.state == 'down':
                AlarmVolume.color = Black
                AlarmVolumeSlider.set_disabled(False)
            else:
                AlarmVolume.color = Gray
                AlarmVolumeSlider.set_disabled(True)
                pass

        PhoneNotesScreen = Screen(name='phonenotes')

        PhoneNotesLayout = GridLayout(cols=2, rows=6, size_hint_y=None, height=400,
                                       row_force_default=True, col_force_default=True, col_default_width=350,
                                       row_default_height=45, pos=(75, -90))

        PhoneAlarmLabel = Label(text="Medicine Alarms", color=Black,
                           font_size=25,
                           font_name=ButtonFont, halign='left', disabled=False)
        PhoneAlarmVolume = Label(text="Alarm Volume", color=Gray,
                            font_size=25,
                            font_name=ButtonFont)

        PhoneMissingPillLabel = Label(text="Missed Pill Notifications", color=Black,
                                 font_size=25,
                                 font_name=ButtonFont, halign='left')
        PhoneBatteryWarningLabel = Label(text="Low Battery Notifications", color=Black,
                                    font_size=25,
                                    font_name=ButtonFont)
        PhoneExpirationWarningLabel = Label(text="Upcoming Expiration Date Notifications",
                                       color=Black,
                                       font_size=25,
                                       font_name=ButtonFont, halign='left')
        PhoneLowPillCountLabel = Label(text="Low PIll Count Notifications", color=Black,
                                  font_size=25,
                                  font_name=ButtonFont, halign='left')

        PhoneAlarmToggle = CheckBox(color=Black)
        PhoneAlarmVolumeSlider = Slider(min=0, max=100, value=50, orientation="horizontal",
                                   cursor_size=(30, 30), disabled=False)

        PhoneMissingPillWarningToggle = CheckBox(color=Black)
        PhoneBatteryWarningToggle = CheckBox(color=Black)
        PhoneExpirationWarningToggle = CheckBox(color=Black)
        PhoneLowPillCountToggle = CheckBox(color=Black)

        PhoneNotesLayout.add_widget(PhoneAlarmLabel)
        PhoneNotesLayout.add_widget(PhoneAlarmToggle)

        PhoneNotesLayout.add_widget(PhoneAlarmVolume)
        PhoneNotesLayout.add_widget(PhoneAlarmVolumeSlider)

        PhoneNotesLayout.add_widget(PhoneMissingPillLabel)
        PhoneNotesLayout.add_widget(PhoneMissingPillWarningToggle)

        PhoneNotesLayout.add_widget(PhoneBatteryWarningLabel)
        PhoneNotesLayout.add_widget(PhoneBatteryWarningToggle)

        PhoneNotesLayout.add_widget(PhoneExpirationWarningLabel)
        PhoneNotesLayout.add_widget(PhoneExpirationWarningToggle)

        PhoneNotesLayout.add_widget(PhoneLowPillCountLabel)
        PhoneNotesLayout.add_widget(PhoneLowPillCountToggle)

        PhoneNotesScreen.add_widget(PhoneNotesLayout)

        def PhonerefreshAlarmState():
            if PhoneAlarmToggle.state == 'down':
                PhoneAlarmVolume.color = Black
                PhoneAlarmVolumeSlider.set_disabled(False)
            else:
                PhoneAlarmVolume.color = Gray
                PhoneAlarmVolumeSlider.set_disabled(True)
                pass


        SecurityScreen = Screen(name='security')
        DispensingScreen = Screen(name='dispensing')
        AccessibilityScreen = Screen(name='accessibility')

        #Pill List
        PillsScreen = Screen(name='pill')
        PillsScreenLayout = BoxLayout(size_hint_x=None, width=500, size_hint_y=None, height=500)

        data = [{'text': str(i)} for i in range(100)]

        args_converter = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_y': None,
                                                 'height': 25,
                                                 'color': Black}

        list_adapter = ListAdapter(data=data,
                                   args_converter=args_converter,
                                   cls=ListItemButton,
                                   selection_mode='single',
                                   allow_empty_selection=False)

        list_view = ListView(adapter=list_adapter)
        PillsScreenLayout.add_widget(list_view)

        PillsScreen.add_widget(PillsScreenLayout)


        sm = ScreenManager(size_hint_y=None, height=300)
        sm.add_widget(HomeScreen)
        sm.add_widget(SettingsScreen)
        sm.add_widget(PillsScreen)
        sm.add_widget(NotificationsScreen)
        sm.add_widget(SecurityScreen)
        sm.add_widget(DispensingScreen)
        sm.add_widget(AccessibilityScreen)
        sm.add_widget(PhoneNotesScreen)
        sm.add_widget(DeviceNotesScreen)



        MenuClock = Label(text="Time", color=Black, size_hint_y=None, height=30)
        ClockAnchor = AnchorLayout(anchor_y='top', anchor_x='right')
        ClockAnchor.add_widget(MenuClock)

        def timeupdate():
            MenuClock.text = GetAMTime(datetime.now())
            PillTime.text = GetRecentPillTime(Slot1, datetime.now())
            DevicerefreshAlarmState()
            PhonerefreshAlarmState()
            pass

        Clock.schedule_interval(lambda dt: timeupdate(), 0.5)

        MenuAnchor = AnchorLayout(anchor_y='bottom')
        MenuLayout = BoxLayout(orientation='horizontal', spacing=10, padding=10, size_hint_y=None, height=120)

        HomeLayout = RelativeLayout()
        SettingsLayout = RelativeLayout()
        PillLayout = RelativeLayout()

        HomeButton = Button(background_normal='', background_color=White)
        HomeImage = Image(source=HomeIcon, pos=(0, 10), color=White)
        HomeLabel = Label(text="HOME", color=Black, pos=(0, -40), font_size=20, font_name=ButtonFont)

        HomeLayout.add_widget(HomeButton)
        HomeLayout.add_widget(HomeImage)
        HomeLayout.add_widget(HomeLabel)

        SettingsButton = Button(background_normal='', background_color=White)
        SettingsImage = Image(source=SettingsIcon, pos=(0, 10), color=Gray)
        SettingsLabel = Label(text="SETTINGS", color=Gray, pos=(0, -40), font_size=20, font_name=ButtonFont)

        SettingsLayout.add_widget(SettingsButton)
        SettingsLayout.add_widget(SettingsImage)
        SettingsLayout.add_widget(SettingsLabel)

        PillButton = Button(background_normal='', background_color=White)
        PillImage = Image(source=PillIcon, pos=(0, 10), color=Gray)
        PillLabel = Label(text="PILLS", color=Gray, pos=(0, -40), font_size=20, font_name=ButtonFont)


        PillLayout.add_widget(PillButton)
        PillLayout.add_widget(PillImage)
        PillLayout.add_widget(PillLabel)

        def GotoSettings(self):
            print("Settings")
            SettingsImage.color = White
            SettingsLabel.color = Black
            HomeLabel.color = Gray
            HomeImage.color = Gray
            PillImage.color = Gray
            PillLabel.color = Gray

            if sm.current == 'home':
                sm.transition.direction = 'right'
                sm.current = 'settings'
            elif sm.current == 'pill':
                sm.transition.direction = 'right'
                sm.current = 'settings'
            else:
                sm.transition = NoTransition()
                sm.current = 'settings'
                sm.transition = SlideTransition()
            pass

        def GotoPill(self):
            print("Pills")
            SettingsImage.color = Gray
            SettingsLabel.color = Gray
            HomeLabel.color = Gray
            HomeImage.color = Gray
            PillImage.color = White
            PillLabel.color = Black
            if sm.current == 'settings':
                sm.transition.direction = 'left'
                sm.current = 'pill'
            elif sm.current == 'home':
                sm.transition.direction = 'left'
                sm.current = 'pill'
            else:
                sm.transition = NoTransition()
                sm.current = 'pill'
                sm.transition = SlideTransition()
            pass

        def GotoHome(self):
            print("Home")
            SettingsImage.color = Gray
            SettingsLabel.color = Gray
            HomeLabel.color = Black
            HomeImage.color = White
            PillImage.color = Gray
            PillLabel.color = Gray
            if sm.current == 'pill':
                sm.transition.direction = 'right'
            elif sm.current == 'settings':
                sm.transition.direction = 'left'
            else:
                sm.transition = NoTransition()
            sm.current = 'home'
            sm.transition = SlideTransition()

            pass

        HomeButton.bind(on_press=GotoHome)
        PillButton.bind(on_press=GotoPill)
        SettingsButton.bind(on_press=GotoSettings)

        MenuLayout.add_widget(SettingsLayout)
        MenuLayout.add_widget(HomeLayout)
        MenuLayout.add_widget(PillLayout)
        MenuAnchor.add_widget(MenuLayout)


        OverLayout.add_widget(ClockAnchor)
        OverLayout.add_widget(sm)
        OverLayout.add_widget(MenuAnchor)


        return OverLayout



Pharm().run()


