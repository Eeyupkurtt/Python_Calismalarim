import tkinter as tk
from tkinter import messagebox
import requests
import pyperclip

#URL kısaltma fonksiyonu
def shortener_url():
    long_url=entry.get()
    response=requests.get(f'http://tinyurl.com/api-create.php?url={long_url}')
    short_url= response.text
    result_label.config(text=f'Kısaltılmış URL:{short_url}')
    copy_button.config(state=tk.NORMAL)#tk'dan veriyi normal şekilde kopyalamak için

#kopyalama fonksiyonu
def copy_to_clipboard():
    short_url=result_label.cget("text")[11:]#11 haneden sonrasını kopyalayacak
    pyperclip.copy(short_url)#pyprclip kütüphanesi kısaltılan url'i panoya kopyalamamızı sağlıyor
    messagebox.showinfo("Kopyalandı","Kısa URL kopyalandı")

#Tasarım
root=tk.Tk()
root.title("URL Shortener")
root.geometry("300x160")

#uzun adresin girileceği yer
label=tk.Label(root,text="Kısaltılacak URL'i giriniz:")
label.pack(pady=10)
entry=tk.Entry(root,width=40)
entry.pack()

#URL kısaltma butonu
shorten_button=tk.Button(root,text="KISALT",command=shortener_url)
shorten_button.pack()

#kısaltılan URL'in görüneceği yer
result_label=tk.Label(root,text="")
result_label.pack()

#kopyalama butonu
copy_button=tk.Button(root,text="KOPYALA",command=copy_to_clipboard,state=tk.DISABLED)
copy_button.pack()

root.mainloop()