from tkinter import *
from tkinter.ttk import *
from newsapi import NewsApiClient
import webbrowser

newsapi = NewsApiClient(api_key='dcfc3054f85a496db49f08bb0682796b')

root = Tk()
l1 = Label(root, text = "News",font =('Verdana', 15))
l1.pack(fill = BOTH, expand= True,pady = 10)
l1.config(anchor=CENTER)

l = Label(root, text = "Click on the text to read more",font =('Verdana', 10))
l.pack(fill = BOTH, expand= True,pady = 10)
l.config(anchor=CENTER)

tx = Text(root, height="10", width="30")
tx.pack(fill=X, expand=True,pady=10)



def callback(url):
    webbrowser.open_new(url)

def retrieve_input():
    global input1,data
    input1 = tx.get("1.0",END)
    data = newsapi.get_everything(q=input1, language="en",page_size=5)
    l3.config(text=data["articles"][0]["title"])
    l3.bind("<Button-1>", lambda e: callback(data["articles"][0]["url"]))
    l4.config(text=data["articles"][1]["title"])
    l4.bind("<Button-1>", lambda e: callback(data["articles"][0]["url"]))
    l5.config(text=data["articles"][2]["title"])
    l5.bind("<Button-1>", lambda e: callback(data["articles"][0]["url"]))
    l6.config(text=data["articles"][3]["title"])
    l6.bind("<Button-1>", lambda e: callback(data["articles"][0]["url"]))
    l7.config(text=data["articles"][4]["title"])
    l7.bind("<Button-1>", lambda e: callback(data["articles"][0]["url"]))

b1 = Button(root,text="Submit")
b1.pack(fill=X, expand=True)
b1.config(command=lambda: retrieve_input())


pane = Frame(root) 
pane.pack(fill = BOTH, expand = True)

l3 = Label(pane, text = "",font =('Verdana', 10))
l4 = Label(pane, text = "",font =('Verdana', 10))
l5 = Label(pane, text = "",font =('Verdana', 10))
l6 = Label(pane, text = "",font =('Verdana', 10))
l7 = Label(pane, text = "",font =('Verdana', 10))

l8 = Label(pane, text = "1",font =('Verdana', 10,"bold italic"))
l9 = Label(pane, text = "2",font =('Verdana', 10,"bold italic"))
l10 = Label(pane, text = "3",font =('Verdana', 10,"bold italic"))
l11 = Label(pane, text = "4",font =('Verdana', 10,"bold italic"))
l12 = Label(pane, text = "5",font =('Verdana', 10,"bold italic"))
 

l8.grid(row = 0, column = 0, sticky = W)
l3.grid(row = 0, column = 1, sticky = W)

l9.grid(row = 1, column = 0, sticky = W)
l4.grid(row = 1, column = 1, sticky = W)

l10.grid(row = 2, column = 0, sticky = W)
l5.grid(row = 2, column = 1, sticky = W)

l11.grid(row = 3, column = 0, sticky = W)
l6.grid(row = 3, column = 1, sticky = W)

l12.grid(row = 4, column = 0, sticky = W)
l7.grid(row = 4, column = 1, sticky = W)

mainloop()