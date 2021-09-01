import requests
import time
from tkinter import *



def button_command():
	file =  open('links.txt', 'r') #the file must be in the same directory of the bot
	urls = file.readlines() 
	time.sleep(int(entry1.get()) *60)
	for url in urls:
		base_url = 'https://api.telegram.org/bot1980956363:AAFL6YPDp-jnMdBKdeNTb4SY1RFa_N8-pc4/sendMessage?chat_id=XXXXXXCHATID&text={}'.format(url) # insert chat id
		requests.get(base_url)
		time.sleep(int(entry2.get())) 

		
root = Tk()
root.geometry('400x200')
root.iconbitmap('pathforicon') #Insert the path of the icon (must be .ico file)
root.title('GalaxyExpress999bot')

StartingTime = Label(root, text="Minutes before sending messages: ", width=100)
StartingTime.pack()

entry1 = Entry(root, width=5)
entry1.pack()


WaitingTime = Label(root, text="Seconds of delay between messages", width=100)
WaitingTime.pack()

entry2 = Entry(root, width=5)
entry2.pack()


Sendbtn = Button(root, text="Send",command= button_command).pack()
  
root.mainloop()



