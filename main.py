from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.title = "آلة حاسبة بايثون"
        
        # تخزين العمليات الحسابية
        self.formula = ""
        
        # التصميم الرئيسي (عمودي)
        root_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # شاشة العرض (TextInput)
        self.solution = TextInput(
            font_size=40,
            readonly=True,
            halign="right",
            multiline=False,
            size_hint=(1, 0.25)
        )
        root_layout.add_widget(self.solution)
        
        # أزرار الآلة الحاسبة وترتيبها في شبكة
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(
                    text=label,
                    font_size=30,
                    background_color=(0.1, 0.5, 0.8, 1) if label != "C" else (0.8, 0.2, 0.2, 1)
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            root_layout.add_widget(h_layout)
            
        # زر اليساوي (=) في الأسفل
        equals_button = Button(
            text="=",
            font_size=35,
            background_color=(0.2, 0.7, 0.3, 1),
            size_hint=(1, 0.2)
        )
        equals_button.bind(on_press=self.on_solution)
        root_layout.add_widget(equals_button)
        
        return root_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "C":
            self.formula = ""
            self.solution.text = ""
        else:
            if current and (current[-1] in "+-*/." and button_text in "+-*/."):
                return # منع تكرار العمليات الحسابية ورا بعض
            self.formula += button_text
            self.solution.text = self.formula

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                # حساب النتيجة باستخدام eval بأمان نسبي
                res = str(eval(self.formula))
                self.solution.text = res
                self.formula = res
            except Exception:
                self.solution.text = "خطأ"
                self.formula = ""

if __name__ == "__main__":
    CalculatorApp().run()
