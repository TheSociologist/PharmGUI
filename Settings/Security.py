from kivy.uix.screenmanager import Screen


class SecurityPage:
    def build(self):
        SecurityScreen = Screen(name='security')
        return SecurityScreen