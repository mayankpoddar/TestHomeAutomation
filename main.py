from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.network.urlrequest import UrlRequest
from kivy.uix.popup import Popup

class IntroPage(GridLayout):
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.label = Label(text="Hey there! \n This Phone belongs to Mayank of House Poddar, \n First of His Name, \n King of the Andals and the First Men, \n Lord of the Seven Kingdoms, \n and Protector of the Realm.", halign="center", valign="middle", font_size=30)
        self.label.size_hint_y = None
        self.label.height = Window.size[1]*0.9
        self.add_widget(self.label)

        self.button = Button(text="Proceed")
        self.button.bind(on_press=self.clicked)
        self.add_widget(self.button)

     def clicked(self, instance):
        myapp.screenmanager.current = "Tabs" 

class TabsPage(GridLayout):
     def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text="", size_hint_y=None, height=Window.size[1]*0.1))

        self.lightButtonON = Button(text="Switch Light ON")
        self.lightButtonON.size_hint_y = None
        self.lightButtonON.height = Window.size[1]*0.1
        self.lightButtonON.bind(on_press=self.toggleLight)

        self.add_widget(self.lightButtonON)

        self.add_widget(Label(text="", size_hint_y=None, height=Window.size[1]*0.05))

        self.lightButtonOFF = Button(text="Switch Light OFF")
        self.lightButtonOFF.size_hint_y = None
        self.lightButtonOFF.height = Window.size[1]*0.1
        self.lightButtonOFF.bind(on_press=self.toggleLight)

        self.add_widget(self.lightButtonOFF)

        self.add_widget(Label(text="", size_hint_y=None, height=Window.size[1]*0.05))

        self.fanButtonON = Button(text="Switch Fan ON")
        self.fanButtonON.size_hint_y = None
        self.fanButtonON.height = Window.size[1]*0.1
        self.fanButtonON.bind(on_press=self.toggleFan)

        self.add_widget(self.fanButtonON)

        self.add_widget(Label(text="", size_hint_y=None, height=Window.size[1]*0.05))

        self.fanButtonOFF = Button(text="Switch Fan OFF")
        self.fanButtonOFF.size_hint_y = None
        self.fanButtonOFF.height = Window.size[1]*0.1
        self.fanButtonOFF.bind(on_press=self.toggleFan)

        self.add_widget(self.fanButtonOFF)

        self.add_widget(Label(text="", size_hint_y=None, height=Window.size[1]*0.05))

        self.unlockButton = Button(text="Unlock Door")
        self.unlockButton.size_hint_y = None
        self.unlockButton.height = Window.size[1]*0.1
        self.unlockButton.bind(on_press=self.toggleLock)

        self.add_widget(self.unlockButton)

        self.add_widget(Label(text="", size_hint_y=None, height=Window.size[1]*0.05))

        self.lockButton = Button(text="Lock Door")
        self.lockButton.size_hint_y = None
        self.lockButton.height = Window.size[1]*0.1
        self.lockButton.bind(on_press=self.toggleLock)

        self.add_widget(self.lockButton)

        self.add_widget(Label(text="", size_hint_y=None, height=Window.size[1]*0.05))

     def toggleLight(self, instance):
        if instance.text == "Switch Light ON":
            req = UrlRequest("http://192.168.0.123/LED=ON")
        else:
            req = UrlRequest("http://192.168.0.123/LED=OFF")

     def toggleFan(self, instance):
        if instance.text == "Switch Fan ON":
            req = UrlRequest("http://192.168.0.124/FAN=ON")
        else:
            req = UrlRequest("http://192.168.0.124/FAN=OFF")

     def toggleLock(self, instance):
        if instance.text == "Unlock Door":
            req = UrlRequest("http://192.168.0.123/DOORLOCK=OFF")
        else:
            req = UrlRequest("http://192.168.0.123/DOORLOCK=ON")

class MyApp(App):

    def build(self):
        self.screenmanager = ScreenManager()

        self.intropage = IntroPage()
        screen = Screen(name="Intro")
        screen.add_widget(self.intropage)
        self.screenmanager.add_widget(screen)

        self.tabspage = TabsPage()
        screen = Screen(name="Tabs")
        screen.add_widget(self.tabspage)
        self.screenmanager.add_widget(screen)

        return self.screenmanager

if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
