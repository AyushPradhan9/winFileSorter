import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tkinter import *

win = Tk()
win.title("File Sorter")
win.geometry("500x500")
win.configure(bg="Gray15")
Label(win,text="Welcome to the File Sorter",font=("Times",17),height=5,bg="Gray15",fg="White").grid(row=0,column=1,padx=0,pady=10)

current_path = os.getcwd()

track = open("listFiles.txt", 'w+')
reader = track.readlines(1)
if not reader:
    track.write("Sorted files are placed under the following folder:\n\n")
    track.write("\tImage Files:\n\n")
    track.write("\tVideo Files:\n\n")
    track.write("\tDocument Files:\n\n")
    track.write("\tCompressed Files:\n\n")
    track.write("\tDatabase Files:\n\n")
    track.write("\tExecutable Files:\n\n")
    track.write("\tProgramming Files:\n\n")
    track.write("\tSystem Files:\n\n")
    track.write("\tOther Files:\n\n")
track.close()

extension = ''

executable = ['.apk', '.bat', '.bin', '.exe', '.jar', '.py']
images = ['.ico', '.png', '.jpeg', '.gif', '.tiff', '.psd', '.raw', '.jpg']
videos = ['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.mpeg', '.mpg', '.3gp']
document = ['.doc', '.pdf', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt']
compressed = ['.7z', '.zip', '.rar', '.z', '.zip', '.iso']
database = ['.csv', '.dat', '.db', '.dbf', '.sql', 'xml']
program = ['.c', '.class', '.cpp', '.cs', '.h', '.java', '.swift', '.vb', '.sh']
system = ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.ini', '.msi', '.sys', '.tmp', '.ini']

def staticOne():

    file = [f for f in os.listdir(current_path) if os.path.isfile(f)]
    for f in file:
        i=0
        name, ext = os.path.splitext(f)

        track = open("listFiles.txt", 'r')
        contents = track.readlines()
        track.close()

        if ext in images:
            for x in contents:
                i+=1
                if x =='\tImage Files:\n':
                    contents.insert(i,'\t\t'+f+'\n')
                extension = '/Image Files'

        elif ext in videos:
            for x in contents:
                i+=1
                if x=='\tVideo Files:\n':
                    contents.insert(i,'\t\t'+f+'\n')
                extension = '/Video Files'

        elif ext in document:
            if name=='listFiles':
                pass
            else:
                for x in contents:
                    i+=1
                    if x=='\tDocument Files:\n':
                        contents.insert(i,'\t\t'+f+'\n')
                extension = '/Document Files'

        elif ext in compressed:
            for x in contents:
                i+=1
                if x == '\tCompressed Files:\n':
                    contents.insert(i,'\t\t'+f+'\n')
            extension = '/Compressed Files'

        elif ext in database:
            for x in contents:
                i+=1
                if x=='\tDatabase Files:\n':
                    contents.insert(i,'\t\t'+f+'\n')
            extension = '/Database Files'

        elif ext in executable:
            if name=='winFileSorter':
                pass
            else:
                for x in contents:
                    i+=1
                    if x == '\tExecutable Files:\n':
                        contents.insert(i,'\t\t'+f+'\n')
                extension = '/Executable Files'

        elif ext in program:
            for x in contents:
                i+=1
                if x=='\tProgramming Files:\n':
                   contents.insert(i,'\t\t'+f+'\n')
            extension = '/Programming Files'

        elif ext in system:
            for x in contents:
                i+=1
                if x=='\tSystem Files:\n':
                    contents.insert(i,'\t\t'+f+'\n')
            extension = '/System Files'

        else:
            for x in contents:
                i+=1
                if x=='\tOther Files:\n':
                    contents.insert(i,'\t\t'+f+'\n')
            extension = '/Other Files'

        if i>0:
            track = open("listFiles.txt", "r+")
            track.seek(0)
            contents = "".join(contents)
            track.write(contents)
            track.truncate()

            if not os.path.exists(current_path + extension):
                os.mkdir(current_path + extension)

            os.rename(current_path+'\\'+f, current_path+extension+'\\'+f)

def dynamicOne():
    class Myhandler(FileSystemEventHandler):
        def on_modified(self, event):
            staticOne()

    event = Myhandler()
    observe = Observer()
    observe.schedule(event, current_path, recursive=True)
    observe.start()

Button(win,text='Sort current files',font=("Times",10),command=staticOne,width=30,height=2,bg="Gray23",fg="White").grid(row=1,column=1,padx=0,pady=10)
Button(win,text="Sort upcoming files",font=("Times",10),command=dynamicOne,width=30,height=2,bg="Gray23",fg="White").grid(row=2,column=1,padx=0,pady=20)
Label(win,text="Note: Selecting sort upcoming files will require to leave app running",font=("Times",10),fg="Red",bg="Gray15").grid(row=3,column=1,padx=20,pady=20)
Button(win,text="Exit",font=("Times",10),command=sys.exit,width=10,bg="Gray23",fg="White").grid(row=4,column=1,padx=0,pady=30)

win.mainloop()



