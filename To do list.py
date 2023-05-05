'''
Simple python to-do list

-Can add a task and delete it when its done.
-I will be using a Python package called Tkinter used for Python GUI library


'''

from tkinter import *
from tkinter import messagebox

# Create To-do list application window
window = Tk()
window.title('To-do List App')
#window.geometry('600x290')
#window.resizable(0,0)
window.config(bg='#F9E2AF')

label = Label(window, text='To-Do list for Today:',font='Montserrat 20', bg='#F9E2AF').pack(anchor='nw')

#Frame widget to hold listbox and scrollbar
frame_task = Frame(window).pack(side='left')

#to hold items in a listbox
listbox_task = Listbox(frame_task, bg='#009FBD', height=15,
                       width=50, font='helvetica', selectforeground='black',selectbackground='DodgerBlue2')
listbox_task.pack(side='left',padx=3,pady=3)


##Scrolldown in case the total list exceeds the size of the window
    # create a scroll widget under parent widget frame_task
scrollbar_task = Scrollbar(frame_task)
    #Tells scrollbar_task to be packed on the right side of frame_task, and to fill the vertical(Y) space.
scrollbar_task.pack(side='right',fill=Y)
    # Configures listbox_task to use scrollbar_task for scrolling when needed.
listbox_task.config(yscrollcommand=scrollbar_task.set)
    # Configures scrollbar_task to control the vertical scrolling of listbox_task
scrollbar_task.config(command = listbox_task.yview) 


def entertask():
    #A new window to pop up to take input

    
    #input_text = ''

    def add():
        #store your input text
        input_text = entry_task.get(1.0, 'end-1c')
        #get() method takes two parameters: start and end. These parameters specify the range of characters to be retrieved from the Text widget.
        #1.0, which means that the first character in the first line of the Text widget will be included.
        #end-1c', which means that all characters up to the last character in the Text widget will be included, 
        # except for the last character. The - 1c specifies that the last character should be excluded, because it is a newline character that is automatically added to the end of the Text widget when the user presses the Enter key.
        if input_text == '':
            messagebox.showwarning(
                title="Warning!", message="Please Enter some Text")
        else:
            listbox_task.insert(END, input_text)
            #close the root1 window
            root1.destroy()

    root1 = Tk()
    root1.title("Add Task")
    entry_task = Text(root1, width=40, height=4,font='helvetica', bg='#F9E2AF')
    entry_task.pack()
    button_temp = Button(root1, text='Add Task', command=add)
    button_temp.pack()
    root1.mainloop()


#function to facilitate the delete tsak from the Listbox
def deletetask():
    #selects the selected item and then deletes it
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])

#Executes this to mark completed
def markcompleted():
    #store the index of currect selected item in listbox_task
    marked = listbox_task.curselection()
    #index 
    temp = marked
    
    #store the text of selected item in a string
    temp_marked = listbox_task.get(marked)
    #update it
    temp_marked = temp_marked+' ✔'
    #delete current text then insert the updated text
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


#Button widget
entry_button = Button(window, text='Add Task',bg='#009FBD', width=20, command=entertask)
entry_button.pack(padx=3, pady=3)

delete_button = Button(window, text='Delete selected task', bg='#009FBD',width=20, command=deletetask)
delete_button.pack(padx=3,pady=3)

mark_button = Button(window, text='Mark as completed', bg='#009FBD', width=20, command=markcompleted)
mark_button.pack(padx=3,pady=3)

print(listbox_task)
    

window.mainloop()

