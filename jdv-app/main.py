from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from app.widgets import alert
class Root(ScreenManager): pass
class Dummy(Screen): pass
class JDVApp(MDApp):
    def build(self):
        sm=Root(); sm.add_widget(Dummy(name='home'))
        return sm
if __name__=='__main__': JDVApp().run()