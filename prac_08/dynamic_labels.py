from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App to dynamically create Labels based on a list of names."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Define the data (list of names)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Label widgets dynamically and add them to the GUI."""
        for name in self.names:
            # Create a Label for each name
            label = Label(text=name, font_size=20, size_hint_y=None, height=40)
            # Add the Label to the BoxLayout with id 'main'
            self.root.ids.main.add_widget(label)


if __name__ == "__main__":
    DynamicLabelsApp().run()
