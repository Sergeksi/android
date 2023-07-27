# importing modules

# it will allow us to get time
import time

# The App class is the base for
# creating Kivy applications
from kivy.app import App

# it will allow us to make interval calls
from kivy.clock import Clock

# Label widget will be used to render text
from kivy.uix.label import Label

# we will be using this to resize app window
from kivy.core.window import Window

# it will allow us to create layouts
from kivy.uix.boxlayout import BoxLayout

# declaring window size
Window.size = (700, 400)


# clock class


class myclock(Label):
    def update(self, *args):
        # get the current local time
        #self.text = time.asctime()[10:]
        self.text = time.asctime()[:-5]
        number_mapping = {
            "Mon": "Понедельник",
            "Tue": "Вторник",
            "Wed": "Среда",
            "Thu": "Четверг",
            "Fri": "Пятница",
            "Sat": "Субота",
            "Sun": "Воскресенье"
        }

        replaced_text = ""
        textList = self.text.split(' ')
        textList.pop(1)
        self.text = ' '.join(number_mapping.get(k, k) for k in textList)


# App class


class TimeApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        # it will create vertical layouts in app

        # calling clock class for time
        clock1 = myclock()

        # updates time with the interval of 1 sec
        Clock.schedule_interval(clock1.update, 1)

        # adding layout to the screen
        layout.add_widget(clock1)

        return layout


root = TimeApp()
root.run()  # running the app