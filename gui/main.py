
import kivy
kivy.require('1.0.5')

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.actionbar import ActionBar
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty


# Declare all of our classes used by our layout so we can reference them in the .kv file
class main(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    label_wid = ObjectProperty()
    info = StringProperty()

class LeftColumn(BoxLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

class LeftColumnMarket(BoxLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

class CenterColumn(BoxLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

class ShipFitting(BoxLayout):
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

class StatsPaneHeader(ButtonBehavior, BoxLayout):
    pass

class StatsPaneInfo(BoxLayout):
    pass

class StatsPane(RelativeLayout):
    def on_press(self):
        for child in self.children:
            if isinstance(child, StatsPaneInfo):
                if child.disabled:
                    child.y = child.saved_y
                    child.size_hint = (1, 1)
                    child.disabled = False
                else:
                    child.saved_y = child.y
                    child.y = 5000000000000
                    child.size_hint = (None, None)
                    child.disabled = True
                    child.width = 0
                    child.height = 0

class StatPaneQuick(BoxLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

class StatPaneFitting(BoxLayout):
    label_wid = ObjectProperty()
    info = StringProperty()

class UpdateStats():
    pass

class MainApp(App):

    def build(self):
        return main(info='Hello world')

if __name__ == '__main__':
    MainApp().run()
