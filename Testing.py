from kivy import Config
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.listview import ListView
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from functools import partial
import pickle
import datetime
from datetime import datetime
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.uix.screenmanager import ScreenManager, Screen

class Pharm(App):
    def build(self):
        grid = BoxLayout()
        simple_list_adapter = SimpleListAdapter(
            data=["Item #{0}".format(i) for i in range(100)],
            cls=Label)

        list_view = ListView(adapter=simple_list_adapter)
        grid.add_widget(list_view)
        return grid
Pharm().run()
