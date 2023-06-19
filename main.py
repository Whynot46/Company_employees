from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.uix.popup import Popup
from kivymd.uix.dialog.dialog import MDDialog
from kivy.config import Config
from kivymd.uix.datatables.datatables import MDDataTable

Window.size = (sp(700), sp(310))
Config.set('graphics', 'resizable', False)

class Main_Screen(Screen):
    def add_people(self): pass

    def delete_people(self): pass

class Data_base(Screen):
    pass


class Staff_info(Screen):
    def show_info(self):
        self.dialog = MDDialog(text='Информация о сотруднике')
        self.dialog.open()
    


class Company_employees(MDApp):
    def build(self):
        global SM
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.load_kv('company_employees.kv')
        SM = ScreenManager()
        SM.add_widget(Main_Screen(name='Main_Screen'))
        SM.add_widget(Data_base(name='Data_base'))
        SM.add_widget(Staff_info(name='Staff_info'))
        return SM


if __name__ == '__main__':
    Company_employees().run()