#responsable de gestionar el ciclo de vida de la aplicación, como su inicio y cierre.
from kivy.app import App
# es un contenedor de diseño en Kivy que organiza sus widgets 
from kivy.uix.boxlayout import BoxLayout
#es un widget que muestra texto en la interfaz de usuario
from kivy.uix.label import Label
# es un widget que permite al usuario ingresar texto o números. 
from kivy.uix.textinput import TextInput
#es un widget que representa un botón interactivo.
from kivy.uix.button import Button
        

class App_porcentaje(App):

    def build(self):
        #Creamos un BoxLayout llamado pantalla con orientación vertical. Este será el diseño principal de nuestra aplicación
        pantalla = BoxLayout(orientation='vertical')
        #Creamos dos widgets de TextInput para que el usuario pueda ingresar un número y un porcentaje.
        self.numero = TextInput(hint_text="Ingrese el numero ")
        self.porcentaje = TextInput(hint_text="Ingrese el porcetaje ")
        self.resultado = Label(text="Resultado: ")
        #Creamos un botón llamado boton_calcular con el texto "Calcular porcentaje" y vinculamos el evento on_press
        boton_calcular = Button(text='Calcular porcentaje', on_press=self.porsentaje_num)

        #Agregamos estos widgets al BoxLayout pantalla.
        pantalla.add_widget(self.numero)
        pantalla.add_widget(self.porcentaje)
        pantalla.add_widget(self.resultado)
        pantalla.add_widget(boton_calcular)
        return pantalla
    
    def porsentaje_num(self, instance):
        # self accede a los numero ingresados, mientras que instace accede a los windget
        
        #Dentro del bloque try, se coloca el código que se espera que pueda generar una excepción (error).
        try: 
            #Intentamos convertir el texto ingresado en los campos de texto a números de punto flotante (float).
            numero = float(self.numero.text)
            porcentaje = float(self.porcentaje.text)
            porcentaje_resultado = numero * (porcentaje / 100)
            #Actualizamos el texto del widget resultado con el resultado calculado, formateado con dos decimales.
            self.resultado.text = f"Resultado: {porcentaje_resultado:.2f}"
        
        #Si se produce una excepción ValueError (por ejemplo, si el usuario ingresa texto no numérico), mostramos un mensaje de error en el widget resultado.
        except ValueError:
            self.resultado.text = "Ingrese valores validos"

#Este bloque se ejecuta cuando ejecutas el script directamente, no cuando se importa como un módulo.
#Crea una instancia de la clase App_porcentaje y llama al método run() para iniciar la aplicación.
if __name__ == '__main__':
    App_porcentaje().run()
