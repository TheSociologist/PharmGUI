from Design.Colors import Black, White
from Design.Fonts import DefaultFont
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class SecurityPage:
    def build(self):
        def SecuritySwitcher(option):
            print(option)


        SecurityScreen = Screen(name='security')
        SecurityLayout = BoxLayout(orientation='horizontal')

        GridLayout(cols=2, rows=5, size_hint_y=None, height=400,
                                      row_force_default=True, col_force_default=True, col_default_width=350,
                                      row_default_height=45, pos=(75, -90))

        SecurityMethod = Label(text="Security Method", color=Black,
                                font_size=25,
                                font_name=DefaultFont, halign='left', disabled=False)
        SecurityMethodDropDown = DropDown()

        FingerprintOpButton = Button(text="Fingerprint", color=Black, font_size=40,
                                     font_name=DefaultFont,
                                     size_hint_y=None,
                                     height=10,
                                     background_color=Black)
        FingerprintOpButton.bind(on_press=lambda: SecurityMethodDropDown.select(FingerprintOpButton.text))

        PINOpButton = Button(text="PIN", color=White, font_size=40,
                                     font_name=DefaultFont,
                                     size_hint_y=None,
                                     height=10,
                                     background_color=Black)
        PINOpButton.bind(on_press=lambda: SecurityMethodDropDown.select(PINOpButton.text))

        PasswordOpButton = Button(text="Password", color=Black, size_hint_y=None,
                                     height=10)
        PINOpButton.bind(on_press=lambda: SecurityMethodDropDown.select(PasswordOpButton.text))

        MasterButton = Button(text="Options", size=(30,30), pos=(0, 0))
        MasterButton.bind(on_press= SecurityMethodDropDown.open)


        SecurityMethodDropDown.add_widget(FingerprintOpButton)
        SecurityMethodDropDown.add_widget(PINOpButton)
        SecurityMethodDropDown.add_widget(PasswordOpButton)

        #SecurityLayout.add_widget(SecurityMethod)
        SecurityLayout.add_widget(MasterButton)
        SecurityScreen.add_widget(SecurityLayout)


        return SecurityScreen