'''from Design.Colors import Black
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView, ListItemButton'''
from kivy.uix.screenmanager import Screen


class PillPage:
    def build(self):
        PillsScreen = Screen(name='pill')
        '''PillsScreenLayout = BoxLayout(size_hint_x=None, width=500, size_hint_y=None, height=500)

        data = [{'text': str(i)} for i in range(100)]

        args_converter = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_y': None,
                                                 'height': 25,
                                                 'color': Black}

        list_adapter = ListAdapter(data=data,
                                   args_converter=args_converter,
                                   cls=ListItemButton,
                                   selection_mode='single',
                                   allow_empty_selection=False)

        list_view = ListView(adapter=list_adapter)
        PillsScreenLayout.add_widget(list_view)

        PillsScreen.add_widget(PillsScreenLayout)'''
        return PillsScreen
