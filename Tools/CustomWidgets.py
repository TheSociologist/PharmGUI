from MainApp import White
from Tools.ScreenManager import sm
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import NoTransition, SlideTransition


class ReturnButton(Button, RelativeLayout):
    def __init__(self):
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

        Button.__init__(self)
        RelativeLayout.__init__(self)
        self.background_normal = ''
        self.background_color = White
        self.bind(on_press=GoBack)
