from Design.Colors import White
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from Home.Home import MainClock
from Home.Menu import Menu
from Tools.ScreenManager import sm


Window.size = (800, 480)
Window.clearcolor = White

class Pharm(App):
    def build(self):

        OverLayout = GridLayout(rows=3)
        OverLayout.add_widget(MainClock.build(self))
        OverLayout.add_widget(sm)
        OverLayout.add_widget(Menu.build(self))

        return OverLayout



Pharm().run()


