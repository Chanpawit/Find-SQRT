import math
from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.geometry('800x500')
GUI.title('Find SQRT By Ryu')
GUI.wm_iconbitmap('math.ico')

FONT1 = ('Cooper Black', 20)
allresult = []

L = ttk.Label(GUI, text='Enter SQRT Down Here', font=FONT1)
L.pack(pady=10)

def CheckSQRT(event=None):
	global allresult
	for rs in allresult:
		rs.destroy()
	allresult = []
	
	sqrt = v_sqrt.get()
	print("Message:",sqrt)

	for q in sqrt:
		try:
			text = math.sqrt(float(sqrt))
			print(text)

		except:
			print('Error')
			pass
			text = '{} Is Not Defined'.format(sqrt)

	L1 = ttk.Label(GUI, text=text, font=FONT1)
	allresult.append(L1)
	L1.pack(pady=10)


	v_sqrt.set('')

v_sqrt = StringVar()

E1 = ttk.Entry(GUI, textvariable=v_sqrt, font=FONT1)
E1.pack(pady=20)

E1.bind('<Return>', CheckSQRT)

B1 = ttk.Button(GUI, text='Check SQRT', command=CheckSQRT)
B1.pack(ipady=10, ipadx=10)

def Showmessagebox(event=None):
	messagebox.showinfo('System','This Program Is For Find SQRT In Input\n  Develop by Ryu')

L2 = ttk.Label(GUI, text='Press F1 for more Information', font=FONT1, foreground='green')
L2.pack(side=BOTTOM)

GUI.bind('<F1>', Showmessagebox)

GUI.mainloop()