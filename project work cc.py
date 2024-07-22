#                                      ''' CURRENCY_CONVERTOR'''
import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, OptionMenu, Text
class currencyconvertor:
    def __init__(self):
         root = tk.Tk()
         root.title("currency convertor")
         root.resizable(width ='False', height ='False')
         root.configure(background = 'white')
         lable_one = Label(root, text ="INDIAN RUPEE",font = "Times 15 bold", fg = 'GREEN',bg = 'WHITE')
         lable_one.grid(row = 1, column = 1)
         self.entry = Entry(root,bd = 5, relief = 'groove', width = 35)
         self.entry.grid(row = 1, column = 2)         
         label_two = Label(root, text = "Select Country", font = "Times 15 bold", fg = 'RED', bg = 'WHITE')
         label_two.grid(row = 2,column = 1)
         btn = Button(root, text = "Convert", fg = "Black", font = "times 15 bold", bg = 'Gray', command = self.currency_convertor)
         btn.grid(row = 3, column = 1)
         btn = Button(root, text ="Clear ALL", fg = "black", font = "Times 15 bold", bg = "Gray",command = self.clear)
         btn.grid(row = 4, column = 1)
         self.country_name = StringVar(root) 
         self.country_name.set(None)
         self.options = {
             "USD": 0.012,
             "Australian Dollar": 0.018,
             "United Arab Emirates Dhiram": 0.044,
             "Japanese Yen": 1.78,
             "Russian ruble": 1.06 }
         self.option_menu = OptionMenu(root, self.country_name,*self.options)
         self.option_menu.grid(row = 2, column = 2, sticky = 'ew')
         self.result = Text(root,height = 2, width = 30, font = "Times 15 bold",bd = 5)
         self.result.grid(row = 3, column = 2) 
         
         root.mainloop()
    def clear(self):
        self.entry.delete(0, tk.END)
        self.result.delete('1.0', tk.END)
        self.country_name.set(None)
    def currency_convertor(self):
        try:
            amount_rs = self.entry.get()
            selected_country = self.country_name.get()
            selected_country_currency_value = self.options.get(selected_country,None)
            
            try:
                currency = float(selected_country_currency_value)
                amount = float(amount_rs)
                converted_amount = currency*amount
                self.result.delete('1.0', tk.END)
                self.result.insert(tk.INSERT,"amount In",tk.INSERT, selected_country,tk.INSERT,"=",tk.INSERT,converted_amount)
            
            except TypeError as error:
                print('Please Select target country or', error)
        except ValueError as error:
            print(error)
currencyconvertor()             
            
            
            
            
            
            
            
            
            
            
            
            
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         