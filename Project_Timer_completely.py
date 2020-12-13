""" Timer """
import time
from tkinter import *
import tkinter as tk
import datetime

def timer(): # หน้าหลักสำหรับเลือก 2 ฟังก์ชัน
    main_desktop = tk.Tk()
    main_desktop.title("Timer")
    main_desktop.geometry("600x500")
    main_desktop.configure(bg = "Antiquewhite")

    def timer_counter(): # ฟังก์ชันในการนับเวลา
        global count
        count = 0
        class App():
            def reset(self): # ฟังก์ชันสำหรับresetเวลาให้กลับมาที่จุดเริ่มต้น
                global count
                count = 1
                self.lb["text"] = "00:00:00"

            def start(self): # ฟังก์ชันใช้ในการนับเวลา
                global count
                count = 0
                self.start_timer()

            def start_timer(self): # ฟังก์ชันสำหรับกด start แล้วจะเริ่มทำงาน
                global count
                self.timer()

            def stop(self): # ฟังก์ชันสำหรับหยุดเวลา
                global count
                count = 1

            def timer(self): # ฟังก์ชันแสดงเวลาตามเงื่อนไงในการนับเวลา
                global count
                if count == 0:
                    self.d = str(self.lb["text"])
                    h,m,s = map(int, self.d.split(":"))
                    h = int(h)
                    m = int(m)
                    s = int(s)
                    if s < 59:
                        s += 1
                    elif s == 59:
                        s = 0
                        if m < 59:
                            m += 1
                        elif m == 59:
                            h += 1
                            m = 0
                    if h < 10:
                        h = str(0)+str(h)
                    else:
                        h = str(h)
                    if m < 10:
                        m = str(0)+str(m)
                    else:
                        m = str(m)
                    if s < 10:
                        s = str(0)+str(s)
                    else:
                        s = str(s)
                    self.d = h+":"+m+":"+s
                    self.lb["text"] = self.d
                    if count == 0:
                        self.root.after(930, self.start_timer)

            def __init__(self): # สำหรับตกแต่งหน้าต่างที่แสดง
                self.root=Tk()
                self.root.title("Timer Counter")
                self.root.geometry("600x500")
                self.root.resizable(False, False)
                self.lb = Label(self.root, text = "00:00:00", fg = "white", bg = "lightcoral")
                self.lb.config(font = ("Courier 50 bold"))
                self.root.configure(bg = "coral")
                self.bt1 = Button(self.root, text = "Start", fg = "lime", bg = "black", command = self.start, font = ("Courier 13 bold"))
                self.bt2 = Button(self.root, text = "Stop", fg = "red", bg = "black", command = self.stop, font = ("Courier 13 bold"))
                self.bt3 = Button(self.root, text = "Reset", fg = "yellow", bg = "black", command = self.reset, font = ("Courier 13 bold"))
                self.lb.place(x = 130, y=165)
                self.bt1.place(x = 140, y=260)
                self.bt2.place(x = 265, y=260)
                self.bt3.place(x = 380, y=260)

        App()

    def timer_countdown(): # ฟังก์ชันสำหรับนับถอยหลัง
        class Countdown(tk.Frame):
            def __init__(self, master): # ฟังก์ชันที่เรียกใช้งานฟังก์ชันทั้งหมดที่ใช้ในการแสดงบนหน้าต่าง
                super().__init__(master)
                self.create_widgets()
                self.show_widgets()
                self.seconds_left = 0
                self._timer_on = False

            def show_widgets(self): # ฟังก์ชันสำหรับแสดงหน้าต่าง widget
                self.label.pack()
                self.entry.pack()
                self.start.pack()

            def create_widgets(self): # ฟังกืชันในการแสดงผลของเวลา ช่องสำหรับใส่เวลา และ ปุ่มstart
                self.label = tk.Label(self, text="0:00:00", font = ("Courier 40 bold"), fg = "blue")
                self.entry = tk.Entry(self, justify = "center",)
                self.entry.focus_set()
                self.start = tk.Button(self, text = "Start", fg = "lime", bg = "black", command = self.start_button, font = ("Courier 13 bold"))
            
            def countdown(self): # ฟังก์ชันเงื่อนไขในการนับถอยหลัง
                self.label["text"] = self.convert_seconds_left_to_time()
                if self.seconds_left:
                    self.seconds_left -= 1
                    self._timer_on = self.after(1000, self.countdown)
                else:
                    self._timer_on = False

            def start_button(self): # ฟังก์ชันที่ทำให้ปุ่มstartทำงาน
                self.seconds_left = int(self.entry.get())
                self.stop_timer()
                self.countdown()

            def stop_timer(self): # ฟังก์ชันสำหรับหยุดการนับอยหลัง
                if self._timer_on:
                    self.after_cancel(self._timer_on)
                    self._timer_on = False

            def convert_seconds_left_to_time(self): # ฟังก์สำหรับคืนค่าเวลาที่เหลืออยู่
                return datetime.timedelta(seconds = self.seconds_left)

        if __name__ == "__main__": # สำหรับตกแต่งหน้าต่าง
            root = tk.Tk()
            root.title("Timer Countdown")
            root.geometry("650x350")
            root.resizable(False, False)
            root.configure(bg = "paleturquoise")
            countdown = Countdown(root)
            countdown.pack()
            root.mainloop()

    func_btn1 = tk.Button(main_desktop, text = "Time Counter", command = timer_counter, bg = "black", fg = "orange", font = ("Courier 17 bold"))
    func_btn2 = tk.Button(main_desktop, text = "Time Countdown", command = timer_countdown,  bg = "black", fg = "cyan", font = ("Courier 17 bold"))
    func_btn1.pack()
    func_btn2.pack()
    func_btn1.place(x=200, y=140)
    func_btn2.place(x=186, y=280)
    main_desktop.mainloop()

timer()
