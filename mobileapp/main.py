from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Program now knows of the .kv file
Builder.load_file('design.kv')

class LoginScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        # A method of App already
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()

