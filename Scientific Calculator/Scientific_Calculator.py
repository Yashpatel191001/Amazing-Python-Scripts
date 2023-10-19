import tkinter as tk
import customtkinter
from math import *
 
# used to switch between units of rad, and deg
convert_constant = 1
inverse_convert_constant = 1

#Functions for the buttons
def fsin(arg):
    return sin(arg * convert_constant)
 
 
def fcos(arg):
    return cos(arg * convert_constant)
 
 
def ftan(arg):
    return tan(arg * convert_constant)
 
 
def arcsin(arg):
    return inverse_convert_constant * (asin(arg))
 
 
def arccos(arg):
    return inverse_convert_constant * (acos(arg))
 
 
def arctan(arg):
    return inverse_convert_constant * (atan(arg))
 
 
# Here are the methods inside class for all the Buttons in the Scientific Calculator.
class Calculator:
    def __init__(self, master):

        # expression that will be displayed on screen
        self.expression = ""
        # be used to store data in memory
        self.recall = ""
        # self.answer
        self.sum_up = ""
        # create string for text input
        self.text_input = customtkinter.StringVar()
        # assign instance to master
        self.master = master
        # set frame showing inputs and title
        top_frame = customtkinter.CTkFrame(master, width=650, height=10)
        top_frame.pack()
        # set frame showing all buttons
        bottom_frame = customtkinter.CTkFrame(master, width=650, height=470)
        bottom_frame.pack()
       
        # Here is the code for Display of Calculator.
        # entry interface for inputs
        txt_display = customtkinter.CTkEntry(top_frame, font=('arial', 36),textvariable=self.text_input, width=600,justify='right')
        txt_display.pack()

 
        # row 0
        # left bracket button
        self.btn_left_brack = customtkinter.CTkButton(
            bottom_frame, text="(", command=lambda: self.btn_click('('))
        self.btn_left_brack.grid(row=0, column=0)
        # right bracket button
        self.btn_right_brack = customtkinter.CTkButton(
            bottom_frame, text=")", command=lambda: self.btn_click(')'))
        self.btn_right_brack.grid(row=0, column=1)
        # takes e to some exponent that you insert into the function
        self.btn_exp = customtkinter.CTkButton(
            bottom_frame, text="exp", command=lambda: self.btn_click('exp('))
        self.btn_exp.grid(row=0, column=2)
        # constant pi
        self.btn_pi = customtkinter.CTkButton(
            bottom_frame, text="π", command=lambda: self.btn_click('pi'))
        self.btn_pi.grid(row=0, column=3)
        # square root
        self.btn_sqrt = customtkinter.CTkButton(
            bottom_frame, text="sqrt", command=lambda: self.btn_click('sqrt('))
        self.btn_sqrt.grid(row=0, column=4)
        # clears self.expression
        self.btn_clear = customtkinter.CTkButton(
            bottom_frame, text="AC", command=self.btn_clear_all)
        self.btn_clear.grid(row=0, column=5)
        # deletes last string input
        self.btn_del = customtkinter.CTkButton(
            bottom_frame, text="C", command=self.btn_clear1)
        self.btn_del.grid(row=0, column=6)
        # inputs a negative sign to the next entry
        self.btn_change_sign = customtkinter.CTkButton(
            bottom_frame, text="+/-", command=self.change_signs)
        self.btn_change_sign.grid(row=0, column=7)
        # division
        self.btn_div = customtkinter.CTkButton(
            bottom_frame, text="/", command=lambda: self.btn_click('/'))
        self.btn_div.grid(row=0, column=8)

 
        # row 1
        # changes trig function outputs to degrees
        self.btn_Deg = customtkinter.CTkButton(bottom_frame, text="Deg", command=self.convert_deg)
        self.btn_Deg.grid(row=1, column=0)
        # changes trig function outputs to default back to radians
        self.btn_Rad = customtkinter.CTkButton(bottom_frame,text="Rad", command=self.convert_rad)
        self.btn_Rad.grid(row=1, column=1)
        # cubes a value
        self.cube = customtkinter.CTkButton(bottom_frame, text=u"x\u00B3", command=lambda: self.btn_click('**3'))
        self.cube.grid(row=1, column=2)
        # takes the absolute value of an expression
        self.btn_abs = customtkinter.CTkButton(
            bottom_frame, text="abs", command=lambda: self.btn_click('abs' + '('))
        self.btn_abs.grid(row=1, column=3)
        # 'memory clear' button. Wipes self.recall to an empty string
        self.btn_MC = customtkinter.CTkButton(
            bottom_frame, text="MC", command=self.memory_clear)
        self.btn_MC.grid(row=1, column=4)
        # seven
        self.btn_7 = customtkinter.CTkButton(bottom_frame, text="7", command=lambda: self.btn_click(7))
        self.btn_7.configure()
        self.btn_7.grid(row=1, column=5)
        # eight
        self.btn_8 = customtkinter.CTkButton(bottom_frame, text="8", command=lambda: self.btn_click(8))
        self.btn_8.configure()
        self.btn_8.grid(row=1, column=6)
        # nine
        self.btn_9 = customtkinter.CTkButton(bottom_frame, text="9", command=lambda: self.btn_click(9))
        self.btn_9.configure()
        self.btn_9.grid(row=1, column=7)
        # multiplication
        self.btn_mult = customtkinter.CTkButton(bottom_frame, text="x", command=lambda: self.btn_click('*'))
        self.btn_mult.grid(row=1, column=8)
 
        # row 2
        # sin function that returns value from -1 to 1 by default
        self.btn_sin = customtkinter.CTkButton(
            bottom_frame, text="sin", command=lambda: self.btn_click('fsin('))
        self.btn_sin.grid(row=2, column=0)
        # cos function that returns value from -1 to 1 by default
        self.btn_cos = customtkinter.CTkButton(
            bottom_frame, text="cos", command=lambda: self.btn_click('fcos('))
        self.btn_cos.grid(row=2, column=1)
        # tan function
        self.btn_tan = customtkinter.CTkButton(bottom_frame, text="tan", command=lambda: self.btn_click('ftan('))
        self.btn_tan.grid(row=2, column=2)
        #
        self.btn_log = customtkinter.CTkButton(bottom_frame, text="log", command=lambda: self.btn_click('log('))
        self.btn_log.grid(row=2, column=3)
        # outputs what is in self.recall
        self.btn_MR = customtkinter.CTkButton(bottom_frame, text="MR", command=self.memory_recall)
        self.btn_MR.grid(row=2, column=4)
        # four
        self.btn_4 = customtkinter.CTkButton(bottom_frame, text="4", command=lambda: self.btn_click(4))
        self.btn_4.configure()
        self.btn_4.grid(row=2, column=5)
        # five
        self.btn_5 = customtkinter.CTkButton(bottom_frame, text="5", command=lambda: self.btn_click(5))
        self.btn_5.configure()
        self.btn_5.grid(row=2, column=6)
        # six
        self.btn_6 = customtkinter.CTkButton(bottom_frame, text="6", command=lambda: self.btn_click(6))
        self.btn_6.configure()
        self.btn_6.grid(row=2, column=7)
        # subtraction
        self.btnSub = customtkinter.CTkButton(bottom_frame, text="-", command=lambda: self.btn_click('-'))
        self.btnSub.grid(row=2, column=8)
 
        # row 3
        # sin inverse function
        self.btn_sin_inverse = customtkinter.CTkButton(bottom_frame, text=u"sin-\u00B9", command=lambda: self.btn_click('arcsin('))
        self.btn_sin_inverse.grid(row=3, column=0)
        # cos inverse function
        self.btn_cos_inverse = customtkinter.CTkButton(bottom_frame, text=u"cos-\u00B9", command=lambda: self.btn_click('arccos('))
        self.btn_cos_inverse.grid(row=3, column=1)
        # tan inverse function
        self.btn_tan_inverse = customtkinter.CTkButton(bottom_frame, text=u"tan-\u00B9", command=lambda: self.btn_click('arctan('))
        self.btn_tan_inverse.grid(row=3, column=2)
        # takes the natural log
        self.btn_ln = customtkinter.CTkButton(bottom_frame, text="ln", command=lambda: self.btn_click('log1p('))
        self.btn_ln.grid(row=3, column=3)
        # adds current self.expression to self.recall string
        self.btn_M_plus = customtkinter.CTkButton(bottom_frame, text="M+", command=self.memory_add)
        self.btn_M_plus.grid(row=3, column=4)
        # one
        self.btn_1 = customtkinter.CTkButton(bottom_frame, text="1", command=lambda: self.btn_click(1))
        self.btn_1.configure()
        self.btn_1.grid(row=3, column=5)
        # two
        self.btn_2 = customtkinter.CTkButton(bottom_frame, text="2", command=lambda: self.btn_click(2))
        self.btn_2.configure()
        self.btn_2.grid(row=3, column=6)
        # three
        self.btn_3 = customtkinter.CTkButton(bottom_frame, text="3", command=lambda: self.btn_click(3))
        self.btn_3.configure()
        self.btn_3.grid(row=3, column=7)
        # addition
        self.btn_add = customtkinter.CTkButton(
            bottom_frame, text="+", command=lambda: self.btn_click('+'))
        self.btn_add.grid(row=3, column=8)
 
        # row 4
        # factorial function
        self.btn_fact = customtkinter.CTkButton(bottom_frame, text="n!", command=lambda: self.btn_click('factorial('))
        self.btn_fact.grid(row=4, column=0)
        # square function
        self.btn_sqr = customtkinter.CTkButton(bottom_frame, text=u"x\u00B2", command=lambda: self.btn_click('**2'))
        self.btn_sqr.grid(row=4, column=1)
        # to the power of function
        self.btn_power = customtkinter.CTkButton(bottom_frame, text="x^y", command=lambda: self.btn_click('**'))
        self.btn_power.grid(row=4, column=2)
        # stores previous expression as an answer value
        self.btn_ans = customtkinter.CTkButton(bottom_frame, text="ans", command=self.answer)
        self.btn_ans.grid(row=4, column=3)
        # comma to allow for more than one parameter!
        self.btn_comma = customtkinter.CTkButton(bottom_frame, text=",", command=lambda: self.btn_click(','))
        self.btn_comma.grid(row=4, column=4)
        # zero
        self.btn_0 = customtkinter.CTkButton(bottom_frame, text="0", command=lambda: self.btn_click(0))
        self.btn_0.configure(width=7)
        self.btn_0.grid(row=4, column=5, columnspan=2)
        # equals button
        self.btn_eq = customtkinter.CTkButton(bottom_frame, text="=", command=self.btn_equal)
        self.btn_eq.configure()
        self.btn_eq.grid(row=4, column=7)
        # decimal to convert to float
        self.btn_dec = customtkinter.CTkButton(bottom_frame, text=".", command=lambda: self.btn_click('.'))
        self.btn_dec.grid(row=4, column=8)
 
 
    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)
        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)
 
 
    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)
 
 
    def change_signs(self):
        self.expression = self.expression + '-'
        self.text_input.set(self.expression)
 
 
    def memory_clear(self):
        self.recall = ""
 
 
    def memory_add(self):
        self.recall = self.recall + '+' + self.expression
 

 
    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_input.set(self.expression)

 
    def memory_recall(self):
        if self.expression == "":
            self.text_input.set('0' + self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)
 
 
    def convert_deg(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = pi / 180
        inverse_convert_constant = 180 / pi

 
    def convert_rad(self):
        global convert_constant
        global inverse_convert_constant
        convert_constant = 1
        inverse_convert_constant = 1

 

 
    def btn_clear_all(self):
        self.expression = ""
        self.text_input.set("")
 

 
    def btn_equal(self):
        self.sum_up = (eval(self.expression))
        self.text_input.set(self.sum_up)
        self.expression = self.sum_up
 
 
# tkinter layout
root = customtkinter.CTk()
b = Calculator(root)
root.title("Scientific Calculator")
root.geometry("1400x400+50+50")
root.resizable(True, True)
root.mainloop()