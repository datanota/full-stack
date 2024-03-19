
from utilities.common import Common
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp


class KivyWidgetsContent(BoxLayout):
    pass


class KW0App(MDApp, Common):
    def __init__(self):
        super().__init__()

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        self.title = 'kivy-widgets - quick start'
        return KivyWidgetsContent()


if __name__ == '__main__':
    KW0App().run()



