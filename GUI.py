import tkinter
from tkinter import scrolledtext
from monitor import *

root = tkinter.Tk() #instantiate window (not displayed)
root.geometry("720x480") #widthxheight
root.title("Data Monitoring Tool")

icon = tkinter.PhotoImage(file='logo.png') #icon of window
root.iconphoto(True,icon)
root.config(background="gray20")

cpuMonitor = CPU_Monitor("cpuMonitor", 5)
diskMonitor = disk_Monitor("diskMonitor", 5)
ramMonitor = RAM_Monitor("RAMmonitor", 5)
netMonitor = network_Monitor("NetworkMonitor1", 5)
pingMonitor = ping_Monitor("pingMonitor", 5)

def cpuButtonLive(): # work in progress(WIP), needs threading
    if(cpuMonitor.getStatus() == "Inactive"):
        generator = cpuMonitor.start()
        for cpu_string in generator:
            outputArea.insert(tkinter.INSERT,
                      cpu_string + "\n")
    else:
        cpuMonitor.stop()

def buttonManual(monitor):
    outputArea.insert(tkinter.INSERT,
                      monitor.getInstant() + "\n")

Headinglabel = tkinter.Label(root,
                      text="PC Monitoring Tool",
                      font=('Robotic',30,'bold'),
                      fg='white',
                      bg='gray20',
                      bd=12,
                      relief='ridge',
                      highlightbackground="black",
                      highlightthickness=1)
Headinglabel.pack()


gridContainer = tkinter.Frame(root, bg='gray20') #grid container for everything besides heading
gridContainer.pack(expand=True, fill='both',padx=10,pady=10)


monitorFrame = tkinter.LabelFrame(gridContainer,
                           text='Monitor',
                           font=('Robotic',20,'bold'),
                           bg='gray20',
                           fg='white',
                           bd=6,
                           relief='ridge',
                           pady=11)
monitorFrame.grid(row=0,column=0)

widgetNames = ["CPU Percentage",
               "Disk Usage",
               "Memory Usage(RAM)",
               "Ping",
               "Network Speed"]

buttonFunctions = [cpuMonitor,
                   diskMonitor,
                   ramMonitor,
                   pingMonitor,
                   netMonitor]

# names all PC monitoring options put in widget
for i, names in enumerate(widgetNames):
    label = tkinter.Label(monitorFrame,
                          text=names,
                          font=('Robotic',10,'bold'),
                          fg='white',
                          bg='gray20',
                          bd=6,
                          relief='ridge',
                          #highlightbackground="black",
                          #highlightthickness=1,
                          pady=11)
    label.grid(row=i,column=0, pady=0, sticky="ew")


def click():
    outputArea.insert(tkinter.INSERT,
                      "hello \n")

for i in range(len(widgetNames)):
    button = tkinter.Button(monitorFrame,
                        text="      ",
                        command=lambda i=i: buttonManual(buttonFunctions[i]),
                        font=("Arial",15),
                        fg="#FFFFFF",
                        bg="gray20",
                        activeforeground="#FFFFFF",
                        activebackground="gray20",
                        state='active',
                        bd=8,
                        relief="raised",
                        #image=icon,
                        compound="top")
    button.grid(row=i,column=1)


outputArea = scrolledtext.ScrolledText(gridContainer, 
                                       wrap = tkinter.WORD,
                                       width = 40,
                                       height = 10,
                                       font = ("Arial", 
                                               15),
                                        highlightbackground="black",
                                        highlightthickness=1)
outputArea.grid(row=0, column=3)
 

root.mainloop() #display window

