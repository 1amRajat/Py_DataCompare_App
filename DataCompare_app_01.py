import difflib
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

def validate():
    try:
        report_file_sample = str(report_name.get())
        source_file = str(source_file.get())
        target_file = str(target_file.get())

        if report_file_sample[-1] == "$\$":
            report_file_test = report_file_sample + 'ReportFile.html'
        else:
            report_file_test = report_file_sample + '\ReportFile.html'
        report_file = report_file_test

        print(report_file)
        print(source_file)
        print(target_file)
        print('Validation Starting!')

        srcLines = open(source_file).readlines()
        tarLines = open(target_file).readlines()
        print(srcLines)

        difference = difflib.HtmlDiff().make_file(srcLines,tarLines,source_file,target_file)
        final_report = open(report_file,'w')
        final_report.write(difference)
        final_report.close()
        print('Validation Completed!')
        messagebox.showinfo("Validation Status", "Validation Completed!")

    except:
        print('Validation Incomplete, check the file path')
        messagebox.showinfo('Validation Status', 'Validation Incomplete, check the file path')


root = tk.Tk()

root.configure(background = 'light blue')
root.title("Py Data Comparison")

source_name = tk.StringVar()
target_name = tk.StringVar()
report_name = tk.StringVar()

heading = Label(root, text="Py Data Compare", bg = "light blue", font='Helvetica 15 bold italic')
heading.pack()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill = "both")

name_label = ttk.Label(input_frame, text = ' Source File Name with Path:', font ='Helvetica 8 bold')
name_label.pack(side='left', padx=(0,10))
name_entry = ttk.Entry(input_frame, width=35, textvariable = source_name)
name_entry.pack(side = "left",expand = True)
name_entry.focus()

name_label = ttk.Label(input_frame, text = ' Target File Name with Path:', font ='Helvetica 8 bold')
name_label.pack(side='left', padx=(0,10))
name_entry = ttk.Entry(input_frame, width=35, textvariable = target_name)
name_entry.pack(side = "left",expand = True)
name_entry.focus()

name_label = ttk.Label(input_frame, text = ' Provide output report path:', font ='Helvetica 8 bold')
name_label.pack(side='left', padx=(0,10))
name_entry = ttk.Entry(input_frame, width=35, textvariable = report_name)
name_entry.pack(side = "left",expand = True)
name_entry.focus()

buttons = ttk.Frame(root, padding = (20,10))
buttons.pack(fill='both')

greet_button = ttk.Button(buttons, text = "Validate", command = validate)
greet_button.pack(side= 'left', fill='x', expand=True)

quit_button = ttk.Button(buttons, text = "Quit", command = root.destroy)
quit_button.pack(side= 'right', fill='x', expand=True)

root.mainloop()

