from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from model import TipModel

Builder.load_file('view.kv')

class TipCalculator(BoxLayout):
    bill_input = StringProperty()
    people_input = StringProperty("1")
    tip_output = StringProperty()
    
    __model: TipModel

    def __init__(self, model):
        super().__init__()    
        self.__model = model

    def btn_click_calc_tip(self, tip_percent):
        try:
            self.__model.bill_amount = float(self.bill_input)
            self.__model.tip_percent = float(tip_percent)
            self.__model.num_people = int(self.people_input) 

            self.tip_output = f"Each Pays: ${self.__model.total_per_person:.2f}"

        except ValueError as ex:
            self.tip_output = "Invalid Input!"
            print(f"Error: {ex}")
