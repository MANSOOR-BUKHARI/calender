# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 23:10:06 2023

@author: Mansoor
"""

from tkinter import *
import calendar

# Create the main application window
tk = Tk()
tk.title("Calendar")
tk.geometry('350x470')

frame = Frame(tk)
frame.pack()

label = Label(frame, text="Calculator", font=('Arial', 30, 'bold'))
label.pack()

# Create frame for getting input month and year
frame1 = Frame(tk)
frame1.pack()

# Create a label to instruct the user
label1 = Label(frame1, bg='black', fg='white', borderwidth=5, text="Enter Year:", font=('Arial', 10, 'bold'), width=11)
label1.grid(column=0, row=0, padx=5, pady=2)  # Adjust padx and pady as needed

# Create an Entry widget for text input
yearEntry = Entry(frame1, fg='black', bg='white', width=17, borderwidth=5, font=('Arial', 15, 'bold'))
yearEntry.grid(row=0, column=1, padx=5, pady=2)  # Adjust padx and pady as needed

label2 = Label(frame1, bg='black', fg='white', borderwidth=5, text="Enter Month:", font=('Arial', 10, 'bold'), width=11)
label2.grid(column=0, row=1, padx=5, pady=2)  # Adjust padx and pady as needed

# Create an Entry widget for text input
monthEntry = Entry(frame1, width=17, font=('Arial', 15, 'bold'), borderwidth=5, fg='black', bg='white')
monthEntry.grid(row=1, column=1, padx=5, pady=2)  # Adjust padx and pady as needed

def restart():
    for row in range(1, num_rows):
        for column in range(num_columns):
            buttons[row][column]['text'] = ''

# Function to retrieve the input when a button is clicked and display calendar
def generateCalendar():
    global month,year,i
    i+=1
    year = int(yearEntry.get())
    month = int(monthEntry.get())
    length = 7
    restart()
    try:
        cal_text = calendar.month(year, month)
        cal_lines = cal_text.split('\n')
        month_year = cal_lines[0].strip().split(' ')  # Extract the month and year
       
        # Display the month and year on the calendar
        monthYear.config(text=month_year)
        month = month_year[0]
        # Display the calendar values on the buttons
        day_values = [line.split() for line in cal_lines[2:]]
        row = 1
        col = 0
        for values in day_values:
            rowLength = int(len(values))
            if rowLength < length and row == 1:
                col = (length - rowLength)

            for value in values:
                buttons[row][col].config(text=value)

                col += 1
                if col >= num_columns:
                    col = 0
                    row += 1
    except IndexError:
        pass

# Frame for month and year
frame2 = Frame(tk)
frame2.pack()
month = ''
year = ''
# Create a button to display the month and year and trigger the calendar generation
monthYear = Button(frame2, bg='white', fg='black', width=24, borderwidth=5, text="Submit",
                   font=("Helvetica", 16), command=generateCalendar)
monthYear.grid(row=0, column=0, columnspan=8)

# Bind the button's hover event to change its text to "Submit" when hovered
def on_hover(event):
    monthYear.config(text="Submit")
    monthYear['bg'] = 'black'
    monthYear['fg'] = 'white'

i = 0
def on_leave(event):
    if i==0:
        return
    monthYear['bg'] = 'white'
    monthYear['fg'] = 'black'
    monthYear.config(text=f"{month}, {year}")

monthYear.bind("<Enter>", on_hover)
monthYear.bind("<Leave>", on_leave)

# Define the number of rows and columns for the calendar
num_rows = 7
num_columns = 7

# Create a 2D list to hold the buttons
buttons = [[None for _ in range(num_columns)] for _ in range(num_rows)]
fgColor = ['red', 'blue', 'white', 'green', 'brown', 'yellow', 'orange']

# Create and grid the buttons using nested loops
for row in range(num_rows):
    for column in range(num_columns):
        button = Button(frame2, bg='black', fg=fgColor[column], text=' ', width=3, borderwidth=5, height=1,
                        font=("Helvetica", 11, 'bold'))
        button.grid(row=row + 1, column=column)
        buttons[row][column] = button  # Store the button in the 2D list

# Display the days of the week in the first row
days_of_week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
for col, day in enumerate(days_of_week):
    buttons[0][col]['text'] = day

# Start the Tkinter event loop
tk.mainloop()
