import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import Label

"""
Sesli olarak oluşturmak istediğimiz PDF'i bilgisayarımıza kaydediyoruz
Projeyi çalıştırıp gerekli işlemleri yapıyoruz.
"""

#PDF import and reading function
def pdf_txt_up(pdf_path):
    txt=""
    pdf_reader=PyPDF2.PdfReader(open(pdf_path,'rb'))

    for page_num in range(len(pdf_reader.pages)):
        txt += pdf_reader.pages[page_num].extract_text()
    return txt

#make text spoken function
def text_to_voice(txt,output_file):
    voice_translate=gTTS(text=txt,lang='tr')
    voice_translate.save(output_file)

#file selection function
def file_select():
    file_path=filedialog.askopenfilename(filetypes=[("PDF Dosyaları","*.pdf")])
    if file_path:
        pdf_txt=pdf_txt_up(file_path)
        text_to_voice(pdf_txt,"kaydet.mp3")
        os.system("start kaydet.mp3")
        information_label.config(text="Dosya çıktı olarak alındı...")

#design creation function(tkinter)
app=tk.Tk()
app.title("Audio Book App")
app.geometry("200x200")

text_font = ("Boulder", 36, 'bold') 

foreground = "green"

selection_button=tk.Button(app, text="PDF Seç",command=file_select, padx=20,pady=20)
selection_button.pack(pady=20)

information_label=Label(app, font=("Boulder", 10) ,fg="red")
information_label.pack(padx=45, pady=5)


app.mainloop()