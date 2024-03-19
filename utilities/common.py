
import webbrowser
import datetime


class Common:
    def __init__(self):
        self.project = 'Datanota-Prototypes'

    @staticmethod
    def dn_demo(web_address):
        webbrowser.open(web_address)
