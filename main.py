from config import *
from db.db import *
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition 
from kivy.metrics import dp
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.datatables.datatables import MDDataTable


class Main_Screen(Screen): pass


class Data_base(Screen):
    def on_enter(self):
        self.update_db()

    def update_db(self):
        self.ids.db_layout.clear_widgets()
        current_line=staff['K1'].value+2
        print(current_line)
        data_tables = MDDataTable(
            size_hint=(1, 0.75),
            check=True,
            rows_num=8,
            use_pagination=True,
            padding=20,
            column_data=[
                ("ID", dp(40)),
                ("ФИО", dp(40)),
                ("Дата рождения", dp(40)),
                ("Должность", dp(40)),
                ("Квалификация", dp(40)),
                ("Стаж", dp(40)),
            ],
            row_data=[
                (staff[f'A{i}'].value, 
                staff[f'B{i}'].value,
                staff[f'C{i}'].value,
                staff[f'D{i}'].value,
                staff[f'E{i}'].value,
                staff[f'F{i}'].value) for i in range(2, current_line)
            ],
        )
        self.ids.db_layout.add_widget(data_tables)


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