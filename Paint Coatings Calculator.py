'''
Paint Coating Computations
Formulas:
Volume Solids VS = DFT/WFT * 100 ,unit % VS
Dry Film Thickness DFT = WFT*VS / 100 ,unit microns
Wet Film Thickness WFT = 100*DFT / VS ,unit microns
Theoretical Spreading Rate TSR = 10*VS(%) / DFT ,unit m2 per liter of paint
Practical Spreading Rate PSR = TSR x (100%-wastage%) ,unit m2 per liter of paint
Quanty of paint Q = Area / PSR, unit liter per m2

'''

from tkinter import *
from tkinter import messagebox   #pop up message for errors
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Paint Coating Calculator')
root.config(bg='slategray3')
# HEADER
Label(root, text='Please input the following data: ',
      font='Arial 15', bg='slategray3', justify='left').pack()


## Input ##

# Volume Solid
Label(root, text='Volume Solid: ', font='arial 12',
      bg='slategray3').place(x=15, y=30)
vs = StringVar()
Entry(root,textvariable = vs,font='arial 12',width=10).place(x=120,y=30)

# Dry Film Thickness
Label(root, text='DFT: ', font='arial 12', bg='slategray3').place(x=15, y=60)
dft = StringVar()
Entry(root, textvariable = dft, font='arial 12', width=10).place(x=120, y=60)

# Surface Area
Label(root, text='Area(sq.m): ', font='arial 12', bg='slategray3').place(x=15, y=90)
area = StringVar()
Entry(root, textvariable = area, font='arial 12', width=10).place(x=120, y=90)

# Loss Factor
Label(root, text='Loss Factor: ', font='arial 12',
      bg='slategray3').place(x=230, y=30)
loss_percentage = StringVar()
Entry(root, textvariable=loss_percentage, font='arial 12', width=5).place(x=325, y=30)

## Calculated Output ##
# header
Label(root, text='Calculate:', font='Arial 14', bg='slategray3').place(x=15, y=120)

# Wet Film Thickness
Label(root, text='WFT: ', font='arial 12', bg='slategray3').place(x=15, y=150)
wft = StringVar()
Label(root, textvariable=wft, font='arial 12', width=15, bg='slategray2').place(x=120, y=150)

# Theoretical Spreading Rate
Label(root, text='TSR: ', font='arial 12', bg='slategray3').place(x=15, y=180)
tsr = StringVar()
Label(root, textvariable=tsr, font='arial 12',bg='slategray2', width=15).place(x=120, y=180)

# Practical Spreading Rate
Label(root, text='PSR: ', font='arial 12', bg='slategray3').place(x=15, y=210)
psr = StringVar()
Label(root, textvariable=psr, font='arial 12', bg='slategray2', width=15).place(x=120, y=210)

# Paint Quantity
Label(root, text='Paint in Liters: ', font='arial 12',
      bg='slategray3').place(x=15, y=240)
paint = StringVar()
Label(root, textvariable=paint, bg='slategray2', font='arial 12', width=15).place(x=120, y=240)

# Reset all data to empty
def reset():
    vs.set("")
    dft.set("")
    area.set("")
    wft.set("")
    tsr.set("")
    psr.set("")
    paint.set("")
    loss_percentage.set("")


def exit():
    root.destroy()




def calculate():
    
    try:
        # Check if any input data is empty
        given = [vs.get(), dft.get(), loss_percentage.get(), area.get()]

        if '' in given:
            messagebox.showerror('Error', 'Fill all the blank areas')
            return

        # No empty data, convert to float 
        vs_val = float(vs.get())
        dft_val = float(dft.get())
        loss_percentage_val = float(loss_percentage.get())
        area_val = float(area.get())

    # pop message if invalid input
    except:
        messagebox.showerror('Invalid', 'Input integers only')

    
    # wft
    wft_val =round((100*dft_val)/vs_val,2)
    wft.set(f'{wft_val} microns')

    # tsr
    tsr_val = round((10*vs_val)/dft_val,2)
    tsr.set(f'{tsr_val} sq.m/liter')

    # psr
    psr_val = round(tsr_val*((100-loss_percentage_val)/100),2)
    psr.set(f'{psr_val} sq.m/liter')

    # paint quantity
    paint_val = round(area_val/psr_val,2)
    paint.set(f'{paint_val} liter/sq.m')

    
# Calculate Button
Button(root,text='CALCULATE',font='arial 13',
       command = calculate,bg='slategray2').place(x=15,y=290)

# Reset Button
Button(root, text='RESET', font='arial 13',
       command = reset, bg='slategray2').place(x=15, y=330)

# Exit Button
Button(root, text='EXIT', font='arial 13',
       command=exit, bg='slategray2').place(x=120, y=330)






root.mainloop()