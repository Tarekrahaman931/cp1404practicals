from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

# Conversion constant
MILES_TO_KM = 1.60934

class ConvertMilesApp(App):
    # Property to update output label text
    output_text = StringProperty()

    def build(self):
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        # Set initial output text
        self.update_output()
        return self.root

    def handle_increment(self, increment):
        try:
            # Get current miles value
            miles = float(self.root.ids.miles_input.text)
        except ValueError:
            # If the input is not a valid number, set miles to 0
            miles = 0.0
        # Increment miles value
        miles += increment
        # Update miles input field
        self.root.ids.miles_input.text = str(miles)
        # Update output label
        self.update_output()

    def handle_convert(self):
        self.update_output()

    def update_output(self):
        try:
            # Get miles value from input field
            miles = float(self.root.ids.miles_input.text)
        except ValueError:
            # If the input is not a valid number, set miles to 0
            miles = 0.0
        # Calculate kilometers
        kilometers = miles * MILES_TO_KM
        # Update output label text
        self.output_text = f"{kilometers:.2f} km"

if __name__ == "__main__":
    ConvertMilesApp().run()

