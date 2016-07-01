#!/usr/bin/env python

import Tkinter
import os
import time
import tkMessageBox
import thread

def show_alarm():
	while 1:
		result = tkMessageBox.askyesno(title=u"It's time", message="please check roaster", detail=u"yes to check roaster", icon="warning")
		if result: os.system('bash /home/www/shells/roaster_status.sh 2>&1')
		time.sleep(7200)

def main_window():

	top = Tkinter.Tk()
	top.title('Roaster Alarms')
	top.geometry('250x100')

	label = Tkinter.Label(top, text='Timer for checking roaster!', font='Helvetica -18 bold')
	label.pack()

	thread.start_new_thread(show_alarm, ())

	quit = Tkinter.Button(top, text='Quit',
		command=top.quit, bg='white', fg='red')
	quit.pack(fill=Tkinter.X, expand=0)

	Tkinter.mainloop()


if __name__ == '__main__':
	main_window()