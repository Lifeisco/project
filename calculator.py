from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import math


class CalculScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        self.txt = Label(text="0", font_size=50, color=(1, 1, 1, 1))
        self.formula = "0"
        gl = GridLayout(cols=4, spacing=5, size_hint=(1, 0.8))
        bl = BoxLayout(orientation="vertical", spacing=5)

        buttons = [
            "C", "%", "√", "DEL",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "/", "0", ".", "="
        ]

        for button_text in buttons:
            gl.add_widget(Button(text=button_text, on_press=self.button_pressed,
                                 background_color=(0.4, 0.4, 0.4, 1),
                                 color=(1, 1, 1, 1)))

        bl.add_widget(self.txt)
        bl.add_widget(gl)
        self.add_widget(bl)

    def button_pressed(self, instance):
        button_text = instance.text

        if button_text == '=':
            try:
                self.formula = str(eval(self.formula))
                self.txt.text = self.formula
            except Exception:
                self.formula = ''
                self.txt.text = 'Error'
        elif button_text == 'C':
            self.formula = ''
            self.txt.text = '0'
        elif button_text == 'DEL':
            self.formula = self.formula[:-1]
            self.txt.text = self.formula if self.formula else '0'
        elif button_text == '√':
            try:
                result = math.sqrt(float(self.formula))
                self.formula = str(result)
                self.txt.text = self.formula
            except ValueError:
                self.formula = ''
                self.txt.text = 'Error'
        elif button_text == '.':
            if '.' not in self.formula:
                self.formula += button_text
                self.txt.text = self.formula
        else:
            if self.txt.text == '0':
                self.formula = button_text
            else:
                self.formula += button_text
            self.txt.text = self.formula


class CalculApp(App):
    def build(self):
        Window.clearcolor = (0.2, 0.2, 0.2, 1)
        sm = ScreenManager()
        sm.add_widget(CalculScr(name='second'))
        return sm


app = CalculApp()
app.run()
