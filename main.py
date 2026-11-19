from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sympy as sp

class FactorizadorApp(App):
    def build(self):
        self.title = "Factorizador de Polinomios"
        
        # Contenedor principal vertical
        layout = BoxLayout(orientation='vertical', padding=25, spacing=15)

        # Título descriptivo
        layout.add_widget(Label(
            text="Factorizar ax² + bx + c", 
            font_size=22, 
            size_hint_y=None, 
            height=40
        ))

        # Campos de entrada para a, b y c
        self.input_a = TextInput(hint_text='Coeficiente a (ej. 1)', multiline=False, input_filter='float', size_hint_y=None, height=45)
        self.input_b = TextInput(hint_text='Coeficiente b (ej. -5)', multiline=False, input_filter='float', size_hint_y=None, height=45)
        self.input_c = TextInput(hint_text='Coeficiente c (ej. 6)', multiline=False, input_filter='float', size_hint_y=None, height=45)

        layout.add_widget(self.input_a)
        layout.add_widget(self.input_b)
        layout.add_widget(self.input_c)

        # Botón para calcular
        btn_calcular = Button(
            text="Factorizar", 
            size_hint_y=None, 
            height=50,
            background_color=(0.1, 0.6, 0.8, 1)
        )
        btn_calcular.bind(on_press=self.factorizar_polinomio)
        layout.add_widget(btn_calcular)

        # Etiqueta para mostrar el resultado
        self.result_label = Label(
            text="Resultado:", 
            font_size=18,
            halign='center',
            valign='middle'
        )
        self.result_label.bind(size=self.result_label.setter('text_size'))
        layout.add_widget(self.result_label)

        return layout

    def factorizar_polinomio(self, instance):
        try:
            # Obtener valores de los inputs (si están vacíos, se asume 0)
            a = float(self.input_a.text) if self.input_a.text else 0.0
            b = float(self.input_b.text) if self.input_b.text else 0.0
            c = float(self.input_c.text) if self.input_c.text else 0.0

            if a == 0:
                self.result_label.text = "Error: El coeficiente 'a' no puede ser 0\n(no sería un polinomio de grado 2)."
                return

            # Usar SymPy para factorizar de forma algebraica exacta
            x = sp.Symbol('x')
            expr = a * x**2 + b * x + c
            factored = sp.factor(expr)

            self.result_label.text = f"Forma Factorizada:\n{str(factored)}"

        except Exception as e:
            self.result_label.text = "Por favor, ingresa números válidos."

if __name__ == '__main__':
    FactorizadorApp().run()