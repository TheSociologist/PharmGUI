from Design.Colors import White, Black, Gray
from Design.Fonts import DefaultFont
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import NoTransition, SlideTransition, Screen
from kivy.uix.slider import Slider
from Tools.ScreenManager import sm


class NotificationsMainScreen:
    def build(self):

        sm.add_widget(DeviceNotificationsScreen.build(self))
        sm.add_widget(PhoneNotificationsScreen.build(self))
        def GoToDeviceNotes(self):
            sm.transition = NoTransition()
            sm.current = 'devicesnotes'
            sm.transition = SlideTransition()

        def GoToPhoneNotes(self):
            sm.transition = NoTransition()
            sm.current = 'phonenotes'
            sm.transition = SlideTransition()

        NotificationsScreen = Screen(name='notifications')
        NotificationsScreenManager = BoxLayout(orientation='vertical', size_hint_y=None, height=1000, pos=(0, 25),
                                               padding=100, spacing=10)
        DeviceNotesButton = Button(text="Device Notifications", color=White, font_size=40,
                                   font_name=DefaultFont,
                                   size_hint_y=None,
                                   height=60,
                                   background_color=Black)
        DeviceNotesButton.bind(on_press=GoToDeviceNotes)
        PhoneNotificationsButton = Button(text="Phone Notifications", color=White, font_size=40,
                                          font_name=DefaultFont,
                                          size_hint_y=None,
                                          height=60,
                                          background_color=Black)
        PhoneNotificationsButton.bind(on_press=GoToPhoneNotes)

        NotificationsScreenManager.add_widget(DeviceNotesButton)
        NotificationsScreenManager.add_widget(PhoneNotificationsButton)

        NotificationsScreen.add_widget(NotificationsScreenManager)

        return NotificationsScreen

class DeviceNotificationsScreen:
    def build(self):
        DeviceNotesScreen = Screen(name='devicesnotes')

        DeviceNotesLayout = GridLayout(cols=2, rows=6, size_hint_y=None, height=400,
                                       row_force_default=True, col_force_default=True, col_default_width=350,
                                       row_default_height=35, pos=[50,-100])

        AlarmLabel = Label(text="Medicine Alarms", color=Black,
                           font_size=25,
                           font_name=DefaultFont, halign='left', disabled=False)
        AlarmVolume = Label(text="Alarm Volume", color=Gray,
                            font_size=25,
                            font_name=DefaultFont)

        MissingPillLabel = Label(text="Missed Pill Notifications", color=Black,
                                 font_size=25,
                                 font_name=DefaultFont, halign='left')
        BatteryWarningLabel = Label(text="Low Battery Notifications", color=Black,
                                    font_size=25,
                                    font_name=DefaultFont)
        ExpirationWarningLabel = Label(text="Upcoming Expiration Date Notifications",
                                       color=Black,
                                       font_size=25,
                                       font_name=DefaultFont, halign='left')
        LowPillCountLabel = Label(text="Low Pill Count Notifications", color=Black,
                                  font_size=25,
                                  font_name=DefaultFont, halign='left')

        AlarmToggle = CheckBox(color=Black)
        AlarmVolumeSlider = Slider(min=0, max=100, value=50, orientation="horizontal",
                                   cursor_size=(30, 30), disabled=False)

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

        DeviceNotesScreen.add_widget(DeviceNotesLayout)

        def DevicerefreshAlarmState():
            if AlarmToggle.state == 'down':
                AlarmVolume.color = Black
                AlarmVolumeSlider.set_disabled(False)
            else:
                AlarmVolume.color = Gray
                AlarmVolumeSlider.set_disabled(True)
                pass
        Clock.schedule_interval(lambda dt: DevicerefreshAlarmState(), 0.5)
        return DeviceNotesScreen

class PhoneNotificationsScreen:
    def build(self):
        PhoneNotesScreen = Screen(name='phonenotes')

        PhoneNotesLayout = GridLayout(cols=2, rows=5, size_hint_y=None, height=400,
                                      row_force_default=True, col_force_default=True, col_default_width=350,
                                      row_default_height=45, pos=(75, -90))

        PhoneAlarmLabel = Label(text="Medicine Alarms", color=Black,
                                font_size=25,
                                font_name=DefaultFont, halign='left', disabled=False)
        PhoneAlarmVolume = Label(text="Alarm Volume", color=Gray,
                                 font_size=25,
                                 font_name=DefaultFont)

        PhoneMissingPillLabel = Label(text="Missed Pill Notifications", color=Black,
                                      font_size=25,
                                      font_name=DefaultFont, halign='left')
        PhoneExpirationWarningLabel = Label(text="Upcoming Expiration Date Notifications",
                                            color=Black,
                                            font_size=25,
                                            font_name=DefaultFont, halign='left')
        PhoneLowPillCountLabel = Label(text="Low Pill Count Notifications", color=Black,
                                       font_size=25,
                                       font_name=DefaultFont, halign='left')

        PhoneAlarmToggle = CheckBox(color=Black)
        PhoneAlarmVolumeSlider = Slider(min=0, max=100, value=50, orientation="horizontal",
                                        cursor_size=(30, 30), disabled=False)

        PhoneMissingPillWarningToggle = CheckBox(color=Black)
        PhoneExpirationWarningToggle = CheckBox(color=Black)
        PhoneLowPillCountToggle = CheckBox(color=Black)

        PhoneNotesLayout.add_widget(PhoneAlarmLabel)
        PhoneNotesLayout.add_widget(PhoneAlarmToggle)

        PhoneNotesLayout.add_widget(PhoneAlarmVolume)
        PhoneNotesLayout.add_widget(PhoneAlarmVolumeSlider)

        PhoneNotesLayout.add_widget(PhoneMissingPillLabel)
        PhoneNotesLayout.add_widget(PhoneMissingPillWarningToggle)

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

        Clock.schedule_interval(lambda dt: PhonerefreshAlarmState(), 0.5)
        return PhoneNotesScreen