import tkinter as tk
import subprocess
from tkinter import filedialog

root = tk.Tk()
root.title('Backup tool')
root.geometry('750x200')
def choose_backup_locate():
    global data
    data = str(filedialog.askdirectory())
    Backup_Locate_Entry.insert(0,data)
    Backup_Locate_Entry.config(state="readonly")
    data=list(data)
def choose_save_locate():
    global save_locate
    save_locate = str(filedialog.askdirectory())
    Save_Locate_Entry.insert(0,save_locate)
    Save_Locate_Entry.config(state="readonly")
    save_locate=list(save_locate)
def Backup_Start():
    datatmp=""
    for i in data:
        if i=="/":
            datatmp+="\\"
        else:
            datatmp+=i
    savetmp=""
    for i in save_locate:
        if i=="/":
            savetmp+="\\"
        else:
            savetmp+=i
    command="xcopy \""+datatmp+"\" \""+savetmp+"\" /e /h /c /i"
    subprocess.run(["powershell.exe", command])
Backup_Locate_Label=tk.Label(root,text="Choose the directory that you want to backup:")
Backup_Locate_Label.grid(row=0,column=0)
Backup_Locate_Entry=tk.Entry(root)
Backup_Locate_Entry.grid(row=0,column=1)
Backup_Locate_Entry.config(width="60")
Backup_Locate_Button=tk.Button(root,text="Choose",command=choose_backup_locate)
Backup_Locate_Button.grid(row=0,column=2)
Save_Locate_Label=tk.Label(root,text="Choose the location for save Save data:")
Save_Locate_Label.grid(row=1,column=0)
Save_Locate_Entry=tk.Entry(root)
Save_Locate_Entry.config(width="60")
Save_Locate_Entry.grid(row=1,column=1)
Save_Locate_Button=tk.Button(root,text="Choose",command=choose_save_locate)
Save_Locate_Button.grid(row=1,column=2)
Backup=tk.Button(text="Backup",command=Backup_Start)
Backup.grid(row=2,column=1)
root.mainloop()
# root.withdraw()

