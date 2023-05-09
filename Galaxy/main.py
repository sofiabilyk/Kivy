# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:26:04 2023

@author: Sofi Bilyk
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

class MainWidget(Widget):
    perspective_points_x = NumericProperty(0)
    perspective_points_y = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        print("INIT W:" + str(self.width) + " H:" + str(self.height))

class GalaxyApp(App):
    pass


GalaxyApp().run()
