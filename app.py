from kivy.config import Config
Config.set('graphics', 'allow_screenspace_scale', '1')

from kivy.app import App
from kivy.core.window import Window
from model import TipModel
from controller import TipCalculator

scale = 60
Window.size = (9 * scale, 24 * scale) 

class TipCalculatorApp(App):
    def build(self):
        model = TipModel()
        
        # Create the glue (Controller) that links the Model and the KV View
        controller = TipCalculator(model)
        
        # Kivy automatically loads 'view.kv' because it's called in controller.py
        return controller
    
if __name__ == "__main__":
    app = TipCalculatorApp()
    app.run()
