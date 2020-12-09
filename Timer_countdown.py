import tkinter as tk
import datetime

class Countdown(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False

    def show_widgets(self):

        self.label.pack()
        self.entry.pack()
        self.start.pack()

    def create_widgets(self):

        self.label = tk.Label(self, text="0:00:00", font=("Courier 50 bold"), fg="blue")
        self.entry = tk.Entry(self, justify="center")
        self.entry.focus_set()
        self.start = tk.Button(self, text="Start", fg="lime", bg="black", command=self.start_button, font=("Courier 13 bold"))
    
    def countdown(self):
        self.label["text"] = self.convert_seconds_left_to_time()

        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else:
            self._timer_on = False

    def start_button(self):
        self.seconds_left = int(self.entry.get())
        self.stop_timer()
        self.countdown()

    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def convert_seconds_left_to_time(self):

        return datetime.timedelta(seconds=self.seconds_left)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Countdown")
    root.geometry("400x250")
    root.resizable(False, False)
    root.configure(bg="silver")
    countdown = Countdown(root)
    countdown.pack()
    root.mainloop()
