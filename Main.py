from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, BooleanProperty
#from kivy.uix.scrollview import ScrollView

class WidgetExample(GridLayout):
    my_text = StringProperty("1")
    able = BooleanProperty(False)
    text_input_str = StringProperty(("foo"))
    #slider_value = StringProperty("50")
    def on_button_click(self):
        print("Button clicked")
        if self.able : 
            self.my_text = str(int(self.my_text) + 1)
    def on_toggle_button_state(self, widget) :
        print("toggle state: " + widget.state)
        if widget.state == "normal" :
            widget.text = "OFF"
            self.able = False
        else:
            widget.text = "ON"
            self.able = True
    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))
        
    #def on_slider_value(self, widget):
     #   print("Value: " + str(int(widget.value)))
        #self.slider_value = str(int(widget.value))
    def on_text_validate(self, widget):
        self.text_input_str = widget.text
        
 
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #self.orientation = "rl-tb"
        for i in range(0, 100) :
            b = Button(text= str(i + 1), size_hint = (.2, None), height = ("80dp"))
            self.add_widget(b)

#class GridLayoutExaple(GridLayout):
 #   pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
"""

class MainWidget(Widget):
    pass

class TheLabApp(App) :
    pass

TheLabApp().run()
