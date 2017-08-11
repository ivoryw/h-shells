import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import poly
from cmath import pi, sqrt, exp
from math import factorial, sin, cos
import threading
import random

global bohrRad
bohrRad = 5.2917721067E-11

class MyApp:
	def __init__(self, parent):
		self.myParent = parent
		
		self.myContainer1 = ttk.Frame(parent)
		self.myContainer1.pack()
		
		# Layout constants #
		button_width = 6
		buttons_padx= "2m"
		buttons_pady = "1m"
		buttons_frame_padx = "6m"
		buttons_frame_pady = "2m"
		buttons_frame_ipadx = "3m"
		buttons_frame_ipady = "1m"

		self.output_frame = ttk.Frame(self.myContainer1)
		self.output_frame.pack()

		self.outputPlot = tk.Canvas(self.output_frame)
		self.outputPlot.configure(
			height='650',
			width = '650',
			bg='#1D1D1D',
			bd=0
			)
		self.outputPlot.pack(side=tk.LEFT)
		
		self.img = tk.PhotoImage(file = 'sidebar.gif')
		self.sidebar = ttk.Label(self.output_frame, image=self.img)
		self.sidebar.pack(side=tk.LEFT)
		self.labelFrame = ttk.Frame(self.output_frame)
		self.labelFrame.pack(side=tk.LEFT, fill=tk.Y)
		
		self.sideLabel0 = ttk.Label(self.labelFrame, text="24a₀")
		self.sideLabel0.pack(side=tk.TOP)
		self.sideLabel2 = ttk.Label(self.labelFrame, text="-24a₀")
		self.sideLabel2.pack(side=tk.BOTTOM)

		self.input_frame = ttk.Frame(self.myContainer1)
		self.input_frame.pack(side=tk.BOTTOM,
			ipadx=buttons_frame_ipady,
			ipady=buttons_frame_ipady,
			padx=buttons_frame_padx,
			pady=buttons_frame_pady,
			fill=tk.X)

		self.nLabel = ttk.Label(self.input_frame, text="Principal (n):")
		self.nLabel.pack(side=tk.LEFT)
		self.nInput = ttk.Entry(self.input_frame)
		self.nInput.configure(
			width=3,
			validate='key',
			#Add validation for values#
			validatecommand='')
		self.nInput.pack(side=tk.LEFT)

		self.lLabel = ttk.Label(self.input_frame, text="   Orbital (l):")
		self.lLabel.pack(side=tk.LEFT)
		self.lInput = ttk.Entry(self.input_frame)
		self.lInput.configure(
			width=3,
			validate='key',
			#Validation
			validatecommand='')
		self.lInput.pack(side=tk.LEFT)

		self.mlLabel = ttk.Label(self.input_frame, text = "   Magnetic (m):")
		self.mlLabel.pack(side=tk.LEFT)
		self.mlInput = ttk.Entry(self.input_frame)
		self.mlInput.configure(
			width=3)
		self.mlInput.pack(side=tk.LEFT)

		self.iterationLabel = ttk.Label(self.input_frame, text="   Iterations (x1000):")
		self.iterationLabel.pack(side=tk.LEFT)
		self.iterationInput = ttk.Entry(self.input_frame)
		self.iterationInput.configure(
			width=6)
		self.iterationInput.pack(side=tk.LEFT)

		self.goButton = ttk.Button(self.input_frame, text='Go!', command=self.goClick)
		self.goButton.pack(side=tk.LEFT)
	
	def goClick(self):
		self.outputPlot.delete('all')
		l = int(self.lInput.get())
		n = int(self.nInput.get())
		m = int(self.mlInput.get())
		i = int(self.iterationInput.get()) * 1000

		if(n<1):
			messagebox.showwarning("Warning","Your value for n is too small.\nn must be a positive integer.")
			return
		if(l>(n-1)):
			messagebox.showwarning("Warning","Your value for l is too large.\nl must be at least 1 less than n")
			return
		if(m>(l)):
			messagebox.showwarning("Warning","Your value for m is too large.\nm cannot be greater than l")
			return
		if(m<(-1 * l)):
			messagebox.showwarning("Warning","Your value for n is too small.\nm cannot be less than -l")
			return

		j=0
		points={}
		
		while(j < i):
			r = random.random() * bohrRad * 48
			theta = random.random() * 2 * pi
			rho = 2*r/(n*bohrRad)
			normalizationConst = sqrt((2/(n*bohrRad))**3 * factorial(n-l-1)/(2*n*factorial(n+l))) * exp(-1 * rho/2) * rho**l

			radialEigenfunc = poly.laguerrePoly(n-l-1, 2*l+1, rho) *  normalizationConst

			sphericalEigenfunc = (-1)**m * sqrt(((2*l-1)/(4*pi)) * (factorial(l-m)/factorial(l+m))) * poly.legendrePoly(l, m, cos(theta)) 
			wavefunc = radialEigenfunc * sphericalEigenfunc
			expectValue= abs(wavefunc ** 2) * 5E-28

			if(expectValue >= random.random()):
				x1 = r * 325 * sin(theta) /(48 * bohrRad)- 1 + 325
				y1 = r * 325 * cos(theta) /(48 * bohrRad)- 1 + 325
				x2 = r * 325 * sin(theta) /(48 * bohrRad)+ 1 + 325
				y2 = r * 325 * cos(theta) /(48 * bohrRad)+ 1 + 325
				self.outputPlot.create_rectangle(x1,y1,x2,y2, fill='white', width=0, activefill='red')
			
			j += 1
		
		self.outputPlot.create_text(650,650, anchor=tk.SE, text='('+', '.join(map(str,[n,l,m]))+')', fill='white')
		return

root = tk.Tk()
root.title('Hydrogen Shells')
root.resizable(width=False, height=False)
myapp = MyApp(root)
root.mainloop()
