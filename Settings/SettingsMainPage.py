from Design.Fonts import DefaultFont
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, NoTransition, SlideTransition
from Tools.ScreenManager import sm
from Settings.Notifications import NotificationsMainScreen
from Settings.Security import SecurityPage
from Settings.Accessibility import AccessibilityPage
from Settings.Dispensing import DispensingPage

Black = (0, 0, 0, 1)
White = (1, 1, 1, 1)
Gray = (0, 0, 0, 0.5)
Red = (1, 132/255, 10/255, 1)


class SettingsMainPage:
    def build(self):
        SettingsScreen = Screen(name="settings")
        sm.add_widget(NotificationsMainScreen.build(self))
        sm.add_widget(SecurityPage.build(self))
        sm.add_widget(AccessibilityPage.build(self))
        sm.add_widget(DispensingPage.build(self))


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
        SettingsScreenLayout = BoxLayout(orientation='vertical', size_hint_y=None, height=1000, pos=(0, 25),
                                         padding=10)

        NotificationsButton = Button(text="Notifications", color=White, font_size=40,
                                     font_name=DefaultFont,
                                     size_hint_y=None,
                                     height=60,
                                     background_color=Black)
        NotificationsButton.bind(on_press=GoTonotifications)
        SecurityButton = Button(text="Security", color=White, font_size=40,
                                font_name=DefaultFont,
                                size_hint_y=None,
                                height=60,
                                background_color=Black)
        SecurityButton.bind(on_press=GoTosecurity)
        DispensingButton = Button(text="Dispensing", color=White, font_size=40,
                                  font_name=DefaultFont,
                                  size_hint_y=None,
                                  height=60,
                                  background_color=Black)
        DispensingButton.bind(on_press=GoTodispensing)
        AccessibilityButton = Button(text="Accessibility", color=White, font_size=40,
                                     font_name=DefaultFont,
                                     size_hint_y=None,
                                     height=60,
                                     background_color=Black)
        AccessibilityButton.bind(on_press=GoToaccessibility)

        SettingsScreenLayout.add_widget(NotificationsButton)
        SettingsScreenLayout.add_widget(SecurityButton)
        SettingsScreenLayout.add_widget(DispensingButton)
        SettingsScreenLayout.add_widget(AccessibilityButton)
        SettingsScreen.add_widget(SettingsScreenLayout)

        return SettingsScreen







