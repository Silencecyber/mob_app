from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import datetime


class SimpleApp(App):
    def build(self):
        # Create a BoxLayout to hold the Label and Buttons

        with open('db.txt', 'r') as file:
            line = file.readline().split(',')

            totals = line[0]
            current_time = line[1]
        layout = BoxLayout(orientation='vertical')

        if current_time == "NONE":
            # Create a Label
            hours=int(totals)/60/60
            text = f"Total generator time in hours: {hours}"
        else:
            text = "Generator is still working. Click stop button!"
        self.label = Label(text=text)

        # Create Buttons
        button_click = Button(text="Start generator")
        button_click.bind(on_press=self.on_button_click)

        button_reset = Button(text="Stop generator")
        button_reset.bind(on_press=self.on_button_reset)

        # Add the Label and Buttons to the layout
        layout.add_widget(self.label)
        layout.add_widget(button_click)
        layout.add_widget(button_reset)

        return layout

    def on_button_click(self, instance):
        # Change the text of the label when the button is clicked

        with open('db.txt', 'r') as file:
            line = file.readline().split(',')

            totals = line[0]
            current_time = [line[1]]

        with open('db.txt', 'w') as f:
            curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            line = f'{totals},{curr_time}'
            f.writelines(line)

        self.label.text = "Generator was started in " + str(curr_time)

    def on_button_reset(self, instance):
        # Reset the text of the label when the reset button is clicked
        with open('db.txt', 'r') as file:
            line = file.readline().split(',')

            totals = line[0]
            current_time = [line[1]]

        new_time = datetime.datetime.now()
        current_time = datetime.datetime.strptime(current_time[0], '%Y-%m-%d %H:%M:%S')
        totals = int((new_time - current_time).total_seconds()) + int(totals)
        with open('db.txt', 'w') as f:
            line = f'{totals},NONE'
            f.writelines(line)
        hours = int(totals) / 60 / 60
        self.label.text = f"Generator was stopped! The generator's total time in hours: {hours}"


if __name__ == '__main__':
    SimpleApp().run()
