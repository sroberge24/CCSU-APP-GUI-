from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
# -------------------------
# Window setup
# -------------------------
root = Tk()
root.title('CCSU App')
root.geometry("500x650")
root.resizable(0, 0)
root.configure(bg='light blue')
# -------------------------
# Make white in logo transparent and show it
# -------------------------
img = Image.open('logo1.PNG')
# Pillow>=10 changed ANTIALIAS; this keeps it compatible
try:
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((100, 100), Image.ANTIALIAS)
img = img.convert("RGBA")
data = img.getdata()
newData = []
for item in data:
    # if pixel is white make it transparent; else keep it
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
img.putdata(newData)
img.save("transparent.png")
logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = Label(root, image=logo, bg='light blue')
logoLabel.place(x=1, y=1)
    # -------------------------
data = pd.read_csv("examfilehere.csv")
    # Label used to display results
lb = Label(root, justify="left", bg="light blue", anchor="w")
lb.place(x=130, y=180)
# -------------------------
# button 1: calendar
def calender():
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=180)
# button 2: buildings
def building():
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=180)
# button 3: faculty
def faculty():
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=180)


def school_of_business():
    Majors = ['Accounting', 'Finance', 'Management & Organization','Marketing', 'MIS','Business Analytics']
    col_text = "\n".join(Majors)

    lb.config(text=col_text, justify="left")
    lb.place(x=20, y=250)


def  mis_department():
    Classes = ['Intro to MIS', 'Database Management','Systems Analysis and Design','Business Analytics/Data Visualization ', 'network and Information Security', 'Project Management' ]
    col_text = "\n".join(Classes)
    lb.config(text=col_text, justify="left")
    lb.place(x=20, y=250)
# -------------------------

button1 = Button(root, text='Calender', command=calender, bg="dark blue",fg="white")
button1.place(x=50, y=110)
button2 = Button(root, text='Buildings', command=building, bg="dark blue", fg="white")
button2.place(x=150, y=110)
button3 = Button(root, text='Faculty', command=faculty, bg="dark blue", fg="white")
button3.place(x=250, y=110)
button4 = Button(root, text= 'School of Business', command=school_of_business, bg="dark blue", fg="white" )
button4.place(x=50, y=150)
button5 = Button(root, text='MIS Department', command=mis_department, bg="dark blue", fg="white")
button5.place(x=250, y=150)

mainloop()