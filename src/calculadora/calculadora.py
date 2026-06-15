# Imports
import os

# Tcl/Tk environment variables for AppImage
def _setup_tcl_tk_env():
    tcl_paths = [
        '/usr/share/tcltk/tcl8.6',
        '/usr/share/tcl8.6',
        '/usr/lib/tcl8.6',
        '/usr/lib64/tcl8.6',
        '/usr/share/tcltk/tcl8.5',
        '/usr/share/tcl8.5',
        '/usr/lib/tcl8.5'
    ]
    tk_paths = [
        '/usr/share/tcltk/tk8.6',
        '/usr/share/tk8.6',
        '/usr/lib/tk8.6',
        '/usr/lib64/tk8.6',
        '/usr/share/tcltk/tk8.5',
        '/usr/share/tk8.5',
        '/usr/lib/tk8.5'
    ]
    
    if 'TCL_LIBRARY' not in os.environ or not os.path.exists(os.path.join(os.environ['TCL_LIBRARY'], 'init.tcl')):
        for path in tcl_paths:
            if os.path.exists(os.path.join(path, 'init.tcl')):
                os.environ['TCL_LIBRARY'] = path
                break
                
    if 'TK_LIBRARY' not in os.environ or not os.path.exists(os.path.join(os.environ['TK_LIBRARY'], 'tk.tcl')):
        for path in tk_paths:
            if os.path.exists(os.path.join(path, 'tk.tcl')):
                os.environ['TK_LIBRARY'] = path
                break

_setup_tcl_tk_env()

from tkinter import *

# Colors
background = "#202020"
text = "#ffffff"
onSuface = "#383838"
onSufaceVariant = "#323232"
selected = "#4d4d4d"
accentColor = "#327DA6"
accentColorSelected = "#419ED1"
black = "#000000"

# Fonts
fontTitle = "Arial 24" 
fontButton = "Arial 11 bold"

# Screen Size
width = 348
height = 348

# Window
window = Tk()
try:
    window.iconbitmap("./assets/img/icon.ico") # Icon
except Exception:
    pass
window.title("Sample Calculator")
window.geometry(f"{int(width)}x{int(height)}")
window.resizable(False, False) # Non resizable
window.config(bg=background)

# Frames
frameDisplay = Frame(window, width=int(width), height=int(height * 1/6), bg=background)
frameDisplay.pack(side="top", fill="x")

frameKeyboard = Frame(window, width=int(width), height=int(height * 5/6), bg=background)
frameKeyboard.pack(side="bottom", fill="both", expand=True)

# Functions
showValue = StringVar()
values = ''

## Update Display
def updateDisplay(text_to_show):
    length = len(text_to_show)

    if length > 20:
        display_text = text_to_show[:17] + "..."
    else:
        display_text = text_to_show
        
    showValue.set(display_text)

## Input Value
def inputValue(event):
    global values
    if values == "Error":
        values = ""
    if event == '%':
        try:
            current_val = float(eval(values))
            values = str(current_val / 100)
        except Exception:
            pass
    else:
        values = values + str(event)
    ### Displays the result on the screen
    updateDisplay(values)

## Calculate
def calculate():
    global values
    try:
        result = eval(values)
        updateDisplay(str(result))
        values = str(result)
    except ZeroDivisionError:
        updateDisplay("Error")
        values = "Error"
    except SyntaxError:
        updateDisplay("Error")
        values = "Error"
    except Exception:
        updateDisplay("Error")
        values = "Error"

## Clean
def clean():
    global values
    values = ''
    updateDisplay('')

# Label
labelScreen = Label(frameDisplay, textvariable=showValue, bg=background, fg=text, font=(fontTitle), width=16, padx=8, pady=40, justify="right", anchor="e", relief="flat")
labelScreen.pack()

# Buttons

## Row 0
btnClean = Button(frameKeyboard, command = clean, text="C", width=19, height=2, bg=onSufaceVariant, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnClean.grid(row=0, column=0, columnspan=2)

btnPerce = Button(frameKeyboard, command = lambda: inputValue('%'), text="%", width=8, height=2, bg=onSufaceVariant, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnPerce.grid(row=0, column=2)

btnDiv = Button(frameKeyboard, command = lambda: inputValue('/'), text="/", width=8, height=2, bg=onSufaceVariant, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnDiv.grid(row=0, column=3)

## Row 1
btnSeven = Button(frameKeyboard, command = lambda: inputValue('7'), text="7", width=8, height=2, bg=onSuface, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnSeven.grid(row=1, column=0)

btnEight = Button(frameKeyboard, command = lambda: inputValue('8'), text="8", width=8, height=2, bg=onSuface, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnEight.grid(row=1, column=1)

btnNine = Button(frameKeyboard, command = lambda: inputValue('9'), text="9", width=8, height=2, bg=onSuface, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnNine.grid(row=1, column=2)

btnMult = Button(frameKeyboard, command = lambda: inputValue('*'), text="x", width=8, height=2, bg=onSufaceVariant, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnMult.grid(row=1, column=3)

## Row 2
btnFour = Button(frameKeyboard, command = lambda: inputValue('4'), text="4", width=8, height=2, bg=onSuface, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnFour.grid(row=2, column=0)

btnFive = Button(frameKeyboard, command = lambda: inputValue('5'), text="5", width=8, height=2, bg=onSuface, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnFive.grid(row=2, column=1)

btnSix = Button(frameKeyboard, command = lambda: inputValue('6'), text="6", width=8, height=2, bg=onSuface, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnSix.grid(row=2, column=2)

btnSub = Button(frameKeyboard, command = lambda: inputValue('-'), text="-", width=8, height=2, bg=onSufaceVariant, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnSub.grid(row=2, column=3)

## Row 3
btnOne = Button(frameKeyboard, command = lambda: inputValue('1'), text="1", width=8, height=2, bg=onSuface, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnOne.grid(row=3, column=0)

btnTwo = Button(frameKeyboard, command = lambda: inputValue('2'), text="2", width=8, height=2, bg=onSuface, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnTwo.grid(row=3, column=1)

btnTree = Button(frameKeyboard, command = lambda: inputValue('3'), text="3", width=8, height=2, bg=onSuface, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnTree.grid(row=3, column=2)

btnPlus = Button(frameKeyboard, command = lambda: inputValue('+'), text="+", width=8, height=2, bg=onSufaceVariant, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnPlus.grid(row=3, column=3)

## Row 4
btnZero = Button(frameKeyboard, command = lambda: inputValue('0'), text="0", width=19, height=2, bg=onSuface, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnZero.grid(row=4, column=0, columnspan=2)

btnDot = Button(frameKeyboard, command = lambda: inputValue('.'), text=".", width=8, height=2, bg=onSuface, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=selected, activeforeground=text, highlightthickness=0, borderwidth=0)
btnDot.grid(row=4, column=2)

btnEqual = Button(frameKeyboard, command = calculate, text="=", width=8, height=2, bg=accentColor, fg=text, font=(fontButton), relief="flat", overrelief="raised", activebackground=accentColorSelected, activeforeground=black, highlightthickness=0, borderwidth=0)
btnEqual.grid(row=4, column=3)

# -----

def main():
    window.mainloop()

if __name__ == "__main__":
    main()
