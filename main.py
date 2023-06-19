import config
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition 
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.uix.popup import Popup
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.datatables.datatables import MDDataTable


class Main_Screen(Screen):
    def add_people(self): pass

    def delete_people(self): pass


class Data_base(Screen):
    pass


class Staff_info(Screen):
    def show_info(self):
        self.dialog = MDDialog(title='Информация о сотруднике',
                               text='Очень важная информация')
        self.dialog.open()
    

class Company_employees(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.load_kv('company_employees.kv')
        self.SM = ScreenManager(transition=FadeTransition())
        self.SM.add_widget(Main_Screen(name='Main_Screen'))
        self.SM.add_widget(Data_base(name='Data_base'))
        self.SM.add_widget(Staff_info(name='Staff_info'))
        return self.SM
    
    def set_dark_theme(self):
        self.theme_cls.theme_style = "Dark"

    def set_light_theme(self):
        self.theme_cls.theme_style = "Light"

    def go_to_main(self):
        self.SM.current = 'Main_Screen'


if __name__ == '__main__':
    Company_employees().run()