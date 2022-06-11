import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

WIDTH = 300
HEIGHT = 200

size = str(WIDTH) + "x" + str(HEIGHT)

# root window
root = tk.Tk()
root.title('app teste')
root.wm_geometry(size)
root.resizable(True, True)

canvas = tk.Canvas(root)
canvas.pack()

# frame
frame = ttk.Frame(canvas, height=HEIGHT, width=WIDTH)

# field options
options = {'padx': 5, 'pady': 5}

# name1 label
name1_label = ttk.Label(frame, text='NomeOrigem')
name1_label.grid(column=0, row=0, sticky='W', **options)
name1_label.config(text='Nome Origem:')

# name1 entry text
name1 = tk.StringVar()
name1_entry = ttk.Entry(frame, textvariable=name1)
name1_entry.grid(column=1, row=0, **options)
name1_entry.focus()

# name2 label
name2_label = ttk.Label(frame, text='Nome Destino')
name2_label.grid(column=0, row=1, sticky='W', **options)

# name2 entry text
name2 = tk.StringVar()
name2_entry = ttk.Entry(frame, textvariable=name2)
name2_entry.grid(column=1, row=1, **options)
name2_entry.focus()

# result label
result_desc_label = ttk.Label(frame, text='resultado: ')
result_desc_label.grid(column=0, row=5, sticky='W', **options)
result_label = ttk.Label(frame)
result_label.grid(column=1, row=5, sticky='W', **options)


# copy button
def copiar():
    try:
        name2.set(name1.get() + name3.get())
        result_label.config(text=name1.get())
    except ValueError as error:
        showerror(title='Error', message=error)


btnCopiar = ttk.Button(frame, text='Copiar')
btnCopiar.grid(column=1, row=4, sticky='W', **options)
btnCopiar.configure(command=copiar)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

name3 = tk.StringVar()


# open new window
def New_window():
    window = tk.Toplevel()
    window.title('Janela 01')
    canvas2 = tk.Canvas(window, height=HEIGHT, width=WIDTH)
    
    # name3 entry text
    name3_entry = ttk.Entry(canvas2, textvariable=name3)
    name3_entry.grid(column=0, row=0, **options)
    name3_entry.focus()
    window.wm_geometry(size)
    canvas2.pack()


# open new window
btnNewwindow = tk.Button(frame, text="abrir", bg='White', fg='Black',
                         command=lambda: New_window())
btnNewwindow.grid(column=1, row=15, sticky='W', **options)

# start the app
root.mainloop()