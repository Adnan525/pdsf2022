import tkinter as tk

# embedding code followed from https://matplotlib.org/3.1.1/gallery/user_interfaces/embedding_in_tk_sgskip.html
# plot function followed from https://stackoverflow.com/questions/31440167/placing-plot-on-tkinter-main-window-in-python

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import util

# this will help to create the initial empty plot
# when we start the program it will have an empty plot
# this will make the GUI look better, also the quit button is not at the center
x = []
y = []
root = tk.Tk()
root.wm_title("Question 8")
root.geometry("700x600")

# left frame
leftFrame = tk.Frame(root, background="white", height=root.winfo_screenheight(), width=root.winfo_screenwidth() / 4)
leftFrame.pack(side=tk.LEFT)
# frame label
selectDataLab = tk.Label(leftFrame, text="Please select a dataset", background="white")
selectDataLab.place(relx=0.5, rely=0.4, anchor="center")
# figure widget to embed matplotlib pplot
fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
# plotting empty plot
fig.add_subplot(111).scatter(x, y, color="red")
# showing empty plot
canvas.draw()

# variable to hold the data file name
# will use with the drop down menu
choice = tk.StringVar()
choice.set("blue_2d.txt")


# gets called everytime we select a dataset
def onClickChoice(event):
    name = choice.get()
    df = util.read_multi_dim_data(name)
    df = util.genCoord(df)
    global x, y
    # generating x, y value for scatter plot
    x, y = util.helper(df)
    # plotting on fig and canvas
    util.plotInFig(x, y, fig, canvas)


# drop down widget with 3 options
# default value blue_2d.txt
dropDown = tk.OptionMenu(leftFrame, choice, "blue_2d.txt", "red_2d.txt", "unknown_2d.txt", command=onClickChoice)
dropDown.config(width=25)
dropDown.place(relx=0.5, rely=0.5, anchor="center")

# quit button added from matplotlib documentattion
def _quit():
    root.quit()  # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

# adding the button to root
button = tk.Button(root, text="Quit", command=_quit)
button.place(relx=0.4, rely=0.9, anchor="center")

tk.mainloop()
