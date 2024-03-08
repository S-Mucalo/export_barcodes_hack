# -*- coding: utf-8 -*-
"""
Created on Sun Mar 8 18:53:03 2023

@author: spm119
"""

import tkinter as tk
from tkinter import filedialog as fd
from fpdf import FPDF
from barcode import Code128
from barcode.writer import ImageWriter
import csv


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Barcode PDF Generator')
        self.geometry('300x200')
        self.frame = ConverterFrame(self)
        self.frame.pack()

class ConverterFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.csv_file = None
        self.barcode_data = {}
        # self.room_sublocation = {}
        self.create_widgets()

    def create_widgets(self):
        self.select_button = tk.Button(self, text="Select CSV", command=self.select_csv)
        self.select_button.pack()

        self.generate_button = tk.Button(self, text="Generate PDF", command=self.generate_pdf)
        self.generate_button.pack()

    def select_csv(self):
        self.csv_file = fd.askopenfilename(filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        self.load_infile()
        
        # Read CSV and extract barcode data - populate self.barcode_data
    
    def load_infile(self):
        with open(self.csv_file, newline='') as csv_infile:
            reader = csv.DictReader(csv_infile)
            for row in reader:
                self.barcode_data[row['Room'] + '-' + row['Sub-location']] = row['Bar Code']  
                # print(row['Bar Code'], row['Site'], row['Building'], row['Floor'], row['Room'], row['Sub-location Path'], row['Sub-location'])


    def generate_pdf(self):
        
        if self.csv_file:
           self.pdf_file = fd.asksaveasfilename(defaultextension=".pdf", filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
           self.generate_images()
           self.save_pdf()
           tk.messagebox.showinfo("Success", "PDF generated successfully!")
        else:
           tk.messagebox.showerror("Error", "Please select a CSV file first.")

    def generate_images(self):
        for name, bcode in self.barcode_data.items():
           # Generate barcode image using python-barcode library
           code128 = Code128(bcode, writer=ImageWriter())
                        
           code128.save(f"temp_barcode_{name}", options={'font_size': 5}, text=name,)      
        
        
    def save_pdf(self):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Times", size=16) 
        pdf.add_page()
            
        # with pdf.table() as table:
        #     for data_row in :
        columns  = 2
        rows = len(self.barcode_data)//columns+1
        keys =  list(self.barcode_data.keys())
        with pdf.table(borders_layout="NONE") as table:
            row = table.row()
            for i in range(rows):
                  row = table.row()
                  for j in range(columns):
                      if keys[i+j] in self.barcode_data:
                          row.cell(img=f"temp_barcode_{keys[i+j]}.png", img_fill_width=True)


        pdf.output(self.pdf_file)
 
if __name__ == "__main__":
    app = Application()
    app.mainloop()
