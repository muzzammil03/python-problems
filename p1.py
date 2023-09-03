
# Convert input string into lower case in Desktop applications

from tkinter import *
root=Tk()
root.geometry("400x300")
def get_user_str():
    user_s =entry.get()
    if user_s.islower():
        Label(root,text="Already in lower case").pack()
    else:
        lower_user_s =user_s.lower()
        Label(root,text="String is coverted to lowercase "+str(lower_user_s)).pack()
    

entry=Entry(root,width=40)
entry.pack(pady=4)
btn=Button(root,text="Enter",command=get_user_str)
btn.pack()
root.mainloop()