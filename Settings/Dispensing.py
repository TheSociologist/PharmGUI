from kivy.uix.screenmanager import Screen


class DispensingPage:
    def build(self):
        DispensingScreen = Screen(name='dispensing')
        return DispensingScreen