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
        try:
            pocetni_dan = self.ids.dan_pocetak.text
            pocetni_mesec = self.ids.mesec_pocetak.text
            pocetna_godina = self.ids.godina_pocetak.text
            zavrsni_dan = self.ids.dan_kraj.text
            zavrsni_mesec = self.ids.mesec_kraj.text
            zavrsna_godina = self.ids.godina_kraj.text

            date_1 = datetime(int(pocetna_godina), int(pocetni_mesec), int(pocetni_dan))
            date_2 = datetime(int(zavrsna_godina), int(zavrsni_mesec), int(zavrsni_dan))

            # Get the interval between two dates
            diff = relativedelta.relativedelta(date_2, date_1)
            # ('Complete Difference between two dates: ')
            self.label_result = f"{diff.years} godina {diff.months} meseci {diff.days} dana"
        except:
            self.label_result = "Morate uneti sve ispravne vrednosti"



class DatumarApp(App):
    def build(self):
        return DatumarWidget()

if __name__ == "__main__":
    DatumarApp().run()
