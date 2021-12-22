from datetime import datetime
from dateutil import relativedelta
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.properties import StringProperty

Builder.load_file('./datumar.kv')
Window.size = (350,550)

class DatumarWidget(Widget):
    label_result = StringProperty()
    def result(self):
        date_1 = datetime(2002, 12, 1)
        date_2 = datetime(2021, 10, 1)
        # Get the interval between two dates
        diff = relativedelta.relativedelta(date_2, date_1)
        #('Complete Difference between two dates: ')
        #diff.years, ' years, ', diff.months, ' months and ', diff.days, ' days')
        self.label_result = f"{diff.years} godina {diff.months} meseci {diff.days} dana"

class DatumarApp(App):
    def build(self):
        return DatumarWidget()

if __name__ == "__main__":
    DatumarApp().run()
