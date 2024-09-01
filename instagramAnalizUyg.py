import instaloader
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#kullanıcı bilgilerini çekme
def get_user_info(username):
    bot=instaloader.Instaloader()
    profile=instaloader.Profile.from_username(bot.context,username)

    #sözlük oluşturma
    user_info={
        "Username":profile.username,
        "Followers":profile.followers,
        "Followees":profile.followees,
        "Post Count":profile.mediacount,
        "Last Post Date": get_last_post_info(profile)
    }
    return user_info

#son gönderi tarihi çekme
def get_last_post_info(profile):
    last_post=None

    for post in profile.get_posts():
        if not last_post or post.date_utc > last_post.date_utc:
            last_post=post
    return last_post.date_utc.strftime("%Y-%m-%d  %H:%M:%S")          

#kullanıcı bilgilerini görüntüleme
def user_show():
    username=entry_username.get()
    user_info=get_user_info(username)
    if isinstance(user_info,dict):
        for widget in tree.get_children():
            tree.delete(widget)
        #tabloya kullanıcı verilerini ekleme
        tree.insert("","end",values=(
            user_info["Username"],
            user_info["Followers"],
            user_info["Followees"],
            user_info["Post Count"],
            user_info["Last Post Date"]
        ))
    else:
        messagebox.showerror("Hata",user_info)

#Tasarım
root = tk.Tk()
root.title("Instagram Analiz")

frame = tk.Frame(root)
frame.pack(padx=20,pady=20)

#kullancı adı etiketi
label = tk.Label(frame,text="Kullanıcı Adı:")
label.grid(row=0, column=0, padx=5, pady=5)

#kulllanıcı adı giriş kutusu
entry_username = tk.Entry(frame)
entry_username.grid(row=0,column=1,padx=5,pady=5)

#bilgi görüntüleme kutusu
search_button = tk.Button(frame,text="Bilgileri Görüntüle",command=user_show)
search_button.grid(row=0,column=2,padx=5,pady=5)

#tablo oluşturma
tree = ttk.Treeview(root,columns=("Username","Followers","Followees","Post Count","Last Post Date"))
tree.heading("Username",text="Kullanıcı Adı:")
tree.heading("Followers",text="Takipçiler:")
tree.heading("Followees",text="Takip Edilenler:")
tree.heading("Post Count",text="Gönderi Sayısı:")
tree.heading("Last Post Date",text="Son Gönderi Tarihi:")
tree.pack(padx=20,pady=20)



root.mainloop()