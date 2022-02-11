from tkinter import *

root = Tk()
root.geometry('600x300')
root.resizable(0,0)
root.title("Python Website Blocker")
Label(root, text="Python Website Blocker", font="verdana 20 bold").pack()
host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'
Label(root, text ='Enter Website :' , font ='verdana 13 bold').place(x=5 ,y=60)
Websites = Text(root,font = 'arial 10',height='1', width = '40', wrap = WORD, padx=5, pady=5)
Websites.place(x= 160,y = 60)
def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text = 'Already Blocked' , font = 'verdana 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'verdana 12 bold').place(x=230,y =200)
block = Button(root, text = 'Block',font = 'verdana 12 bold',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'sky blue')

block.place(x = 230, y = 150)
root.mainloop()