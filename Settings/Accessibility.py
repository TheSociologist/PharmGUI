from kivy.uix.screenmanager import Screen


class AccessibilityPage:
    def build(self):
        AccessibilityScreen = Screen(name='accessibility')
        return AccessibilityScreen
