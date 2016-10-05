import kivy
kivy.require('1.0.5')

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.actionbar import ActionBar
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty



class main(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'

class LeftColumn(BoxLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

class LeftColumnMarket(BoxLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

class CenterColumn(BoxLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

class CenterColumnBottomPane(BoxLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

class RightColumn(BoxLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

class MenuBar(BoxLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

class MainApp(App):

    def build(self):
        return main(info='Hello world')

if __name__ == '__main__':
    MainApp().run()