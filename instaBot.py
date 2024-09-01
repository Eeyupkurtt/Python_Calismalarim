import instaloader
import tkinter as tk
from tkinter import messagebox

def download_post():
    #kullanıcı adı alma
    username=entry_username.get()

    try:
        #nesne oluştur
        bot=instaloader.Instaloader()
        #profil nesnesi oluşturma
        profile=instaloader.Profile.from_username(bot.context,username)
        #kullanıcı gönderilerini al
        posts=profile.get_posts()
        #gönderileri indir(buralar ezber kodu hep)
        for index,post in enumerate(posts,1):#enumerate içinde iki değişkenin gezmesine olanak sağlar
            bot.download_post(post,target=f"{profile.username}_{index}")
        #başarı mesajı
        messagebox.showinfo("Başarılı","Gönderiler indirildi...")
    except Exception as e:
        messagebox.showerror("Hata",str(e))

#tkinter arayüzü oluşturma
root=tk.Tk()
root.title("İnstagram Gönderi İndirici")
root.geometry("300x200")
root.resizable(0,0)

#kullanıcı adı labeli
label=tk.Label(root,text="Kullanıcı Adı")
label.pack(pady=10)
#kullanıcı adı girişi
entry_username=tk.Entry(root)
entry_username.pack()
#indirme butonu
download_button=tk.Button(root,text="Bilgileri İndir",command=download_post)
download_button.pack(pady=10)


root.mainloop()