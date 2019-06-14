from Design.Colors import Black, White, Gray
from Design.Fonts import DefaultFont
from Design.Icons import HomeIcon, SettingsIcon, PillIcon
from Home.Home import HomePage
from PillList.RecyclerView import PillPage
from Settings.SettingsMainPage import SettingsMainPage
from Tools.ScreenManager import sm
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import NoTransition, SlideTransition


class Menu:
    def build(self):
        sm.add_widget(HomePage.build(self))
        sm.add_widget(SettingsMainPage.build(self))
        sm.add_widget(PillPage.build(self))

        MenuAnchor = AnchorLayout(anchor_y='bottom')
        MenuLayout = BoxLayout(orientation='horizontal', spacing=10, padding=10, size_hint_y=None, height=120)

        HomeLayout = RelativeLayout()
        SettingsLayout = RelativeLayout()
        PillLayout = RelativeLayout()

        HomeButton = Button(background_normal='', background_color=White)
        HomeImage = Image(source=HomeIcon, pos=(0, 10), color=White)
        HomeLabel = Label(text="HOME", color=Black, pos=(0, -40), font_size=20, font_name=DefaultFont)

        HomeLayout.add_widget(HomeButton)
        HomeLayout.add_widget(HomeImage)
        HomeLayout.add_widget(HomeLabel)

        SettingsButton = Button(background_normal='', background_color=White)
        SettingsImage = Image(source=SettingsIcon, pos=(0, 10), color=Gray)
        SettingsLabel = Label(text="SETTINGS", color=Gray, pos=(0, -40), font_size=20, font_name=DefaultFont)

        SettingsLayout.add_widget(SettingsButton)
        SettingsLayout.add_widget(SettingsImage)
        SettingsLayout.add_widget(SettingsLabel)

        PillButton = Button(background_normal='', background_color=White)
        PillImage = Image(source=PillIcon, pos=(0, 10), color=Gray)
        PillLabel = Label(text="PILLS", color=Gray, pos=(0, -40), font_size=20, font_name=DefaultFont)

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

        return MenuAnchor