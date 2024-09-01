from tkinter import Label, Tk
import time
import requests

# Tasarım kısmı
app_window = Tk()  # Grafik pencere oluştur
app_window.title("Digital Clock")  # Pencerenin başlığını ayarla
app_window.geometry("400x230")  # Pencerenin başlangıç boyutunu ayarla
app_window.resizable(0, 0)  # Pencerenin boyutunu değiştirilemez yap
app_window.config(bg="black")  # Arka plan rengini siyah yap

text_font = ("Boulder", 36, 'bold')  # Metin fontunu ayarla
background = "black"  # Arka plan rengini siyah yap
foreground = "green"  # Metin rengini yeşil yap

# Saat etiketi oluşturma
clock_label = Label(app_window, font=text_font, bg=background, fg=foreground)
clock_label.grid(row=0, column=1, padx=45, pady=20)  # padx sağ ve soldan pady yukarı ve aşağıdan hizalama

# Tarih etiketi oluşturma
date_label = Label(app_window, font=("Boulder", 18), bg=background, fg="white")
date_label.grid(row=1, column=1, padx=45, pady=5) 

# Hava durumu etiketi oluşturma
weather_label = Label(app_window, font=("Boulder", 18), bg=background, fg="lightblue")
weather_label.grid(row=2, column=1, padx=45, pady=5) 

bilgi_label=Label(app_window, font=("Boulder", 10), bg=background, fg="red")
bilgi_label.grid(row=3,column=1,padx=45, pady=5)

#hava durumu fonskiyonu oluşturma
def get_weather():
    try:
        
        api_key = ""#APİ Key'iniz
        city = "Kutahya"
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        
        response = requests.get(url)
        response.raise_for_status()  # HTTP hatalarını kontrol eder 
        weather_data = response.json()

        # Türkçe çeviri sözlüğü
        translation_dict = {
            "clear": "Açık hava",
            "few clouds": "Az bulutlu",
            "scattered clouds": "Dağınık bulutlar",
            "broken clouds": "Kısmi bulutlu",
            "shower rain": "Sağanak yağış",
            "rain": "Yağmur",
            "thunderstorm": "Gökgürültülü fırtına",
            "snow": "Kar",
            "mist": "Sis"
        }

        if "error" not in weather_data:

            temp = round(weather_data['current']['temp_c'])  # Sıcaklık bilgisi round ile tam sayıya yuvarladık
            weather_desc = weather_data['current']['condition']['text']  # Hava durumu açıklaması

            weather_desc_capitalized = weather_desc.lower().capitalize()#sözlükteki kelimlerin baş harflerinin büyük olması için 
            weather_desc_translated = translation_dict.get(weather_desc_capitalized.lower(), weather_desc)

            weather_info = f"Kütahya: {temp}°C, {weather_desc_translated}"#hava durumu bilgisini yazdırma
        else:
            weather_info = "Hava durumu bilgisi mevcut değil"
    except requests.RequestException as e:
        weather_info = f"Hata: {e}"
        
    return weather_info

#hava durumu güncelleme
def update_weather():
    weather_info = get_weather()
    weather_label.config(text=weather_info)
    
    #4saatte bir güncellenir
    app_window.after(14400000, update_weather)
    bilgi_label.config(text="Hava durumu her 4 saatte bir güncellenir...")
    

# Dijital saat ve hava durumu güncelleme fonksiyonu
def digital_clock():
    # Saati yazdır
    time_live = time.strftime("%H:%M:%S")
    clock_label.config(text=time_live)
    # Saati sürekli güncellemek için tekrar çağır
    clock_label.after(200, digital_clock)#200mili saniyede bir yenilenir

    # Tarihi yazdır
    date_info = time.strftime("%d %B %Y")
    date_label.config(text=date_info)

# Dijital saati ve hava durumunu güncellemeye başla
digital_clock()
update_weather()

# Pencerenin ana döngüsünü başlat
app_window.mainloop()
