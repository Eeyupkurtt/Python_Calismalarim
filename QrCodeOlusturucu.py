import tkinter as tk
from tkinter import filedialog
import pyqrcode
from pyqrcode import QRCode

#fonksiyon
def qr_kod_olustur():
    url=url_girdi.get()

    if url:
        qr_url=pyqrcode.create(url)
        dosya_yolu=filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG Dosyaları","*.svg")])

        if dosya_yolu:
            qr_url.svg(dosya_yolu, scale=8)
            durum_etiketi.config(text="QR Kodu oluşturuldu ve kaydedildi...")


#Tasarım
uygulama_penceresi=tk.Tk()
uygulama_penceresi.title("Qr Kod Oluşturucu")

etiket=tk.Label(uygulama_penceresi,text=("URL'yi Giriniz: "))
url_girdi=tk.Entry(uygulama_penceresi,width=40)
olustur_butonu=tk.Button(uygulama_penceresi,text="Qr kodu oluştur",command=qr_kod_olustur)
durum_etiketi=tk.Label(uygulama_penceresi,text="")

# etiket.pack()#etiketi grafik arayüzüne eklemek için. ama genelde bu kullanılmaz
# url_girdi.pack()
# olustur_butonu.pack()
# durum_etiketi.pack()

etiket.grid(row=0,column=0,padx=10,pady=10)
url_girdi.grid(row=0,column=1,padx=10,pady=10)
olustur_butonu.grid(row=1,column=0,columnspan=2,padx=10,pady=10) #columnspan kolonun kapladığı alan 2 birim olsun demek
durum_etiketi.grid(row=2,column=0,columnspan=2,padx=10,pady=10)


uygulama_penceresi.mainloop()

