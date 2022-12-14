import kivy
from kivy.app import App
from kivy.uix.label import Label

# Replace this with your
# current version
kivy.require('2.0.0')
# To find your kivy version use,
#print(kivy.__version__)

class MyFirstKivyApp(App):



    # Function that returns

    # the root widget

    def build(self):



        # Label with text Hello World is

        # returned as root widget

        return Label(text ="Hello World !")

myApp = MyFirstKivyApp()
myApp.run()
