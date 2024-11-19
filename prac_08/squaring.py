"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Modified as per requirements
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (400, 200)  # Updated window size to better fit the layout
        self.title = "Square Number 2"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ Handle calculation (button press), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(round(result, 2))
        except ValueError:
            self.root.ids.output_label.text = "Invalid Input"


SquareNumberApp().run()
