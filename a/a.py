import configparser
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import threading
import requests
import datetime
import pytz
from timezonefinder import TimezoneFinder


def main():

    Tk.title("Weather App")
    Tk.geometry("800x480")
    Tk.iconbitmap(r"Images/weather_icon.ico")
    Tk.resizable(False,False)
    threading.Thread(target=gui).start()

    def gui():
        # placing the black border for search
       img=Image.open(r"Images/black_border.png")
       resizeimg=img.resize((275,35))
       finalimg=ImageTk.PhotoImage(resizeimg)
       Label(image=finalimg).place(x=20,y=20)
       
       # creating the search button
       img1=Image.open(r"Images/search_btn.png")
       resizeim1=img1.resize((29,29))
       finalimg1=ImageTk.PhotoImage(resizeim1)
       b1=Button(image=finalimg1,bg="black",command=threading)
       b1.place(x=297,y=22)
       bind("<Return>",threading)
     
       # creating the search textbox
       search=StringVar()
       search_textbox=Entry(textvariable=search,font=("Segoe UI",14,'bold'),width=24,justify="center",relief="flat")
       search_textbox.place(x=25,y=25)

       # creating the current weather label to display the city name and city time
       Label(text="Current Weather :",font='Arial 14 bold',fg="red").place(x=590,y=7)

       # location image logo
       img2=Image.open(r'Images/location.png')
       resizeimg2=img2.resize((20,20))
       finalimg2=ImageTk.PhotoImage(resizeimg2)
       Label(image=finalimg2).place(x=595,y=36)

       # location label 
       location=Label(text='',font='Calibri 15')
       location.place(x=620,y=34)

       # time label for the searched city
       timelbl=Label(text="",font=("Cambria",16))
       timelbl.place(x=590,y=60)

       # creating the label for the logo according to main
       img3=Image.open(r"Icons/main.png")
       resizeimg3=img3.resize((200,190))
       finalimg3=ImageTk.PhotoImage(resizeimg3)
       icons=Label(image=finalimg3)
       icons.place(x=70,y=110)

       # creating the label to display the temperature
       temperature=Label(text="",font=("Cambria",75,'bold'))
       temperature.place(x=270,y=140)
       degree=Label(text="",font="Cambria 40 bold")
       degree.place(x=390,y=135)

       # feels like label and sunny or fog like labels
       feel=Label(text="",font=("Nirmala UI",16,"bold"))
       feel.place(x=280,y=245)
       
       # sunrise logo
       finalimg4=ImageTk.PhotoImage(image=Image.open(r"Images/sunrise.png").resize((40,40)))
       Label(image=finalimg4).place(x=560,y=150)
       sunrise=Label(text="Sunrise : ",font=("Segoe UI",14,'bold'))
       sunrise.place(x=603,y=155)

       #sunset logo
       finalimg5=ImageTk.PhotoImage(image=Image.open(r"Images/sunset.png").resize((40,30)))
       Label(image=finalimg5).place(x=560,y=215)
       sunset=Label(text="Sunset : ",font=("Segoe UI",14,'bold'))
       sunset.place(x=603,y=210)

       # bottom bar
       finalimg6=ImageTk.PhotoImage(image=Image.open(r'Images/bottom_bar.png').resize((770,70)))
       Label(image=finalimg6,bg='#00b7ff').place(x=5,y=330)

       # placing the labels
       Label(text="Humidity",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=35,y=335)
       Label(text="Pressure",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=210,y=335)
       Label(text="Description",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=400,y=335)
       Label(text="Visibility",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=600,y=335)

       # humidity label
       humidity=Label(text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
       humidity.place(x=50,y=361)

       # pressure label
       pressure=Label(text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
       pressure.place(x=203,y=361)

       # description label
       des=Label(text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
       des.place(x=405,y=361)

       # visibility label
       vis=Label(text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
       vis.place(x=610,y=361)

       # exit and reset button
       Button(text='Exit',font=("Georgia",16,"bold"),bg='orange',fg='black',width=7,relief='groove',command=exit).place(x=680,y=420)
       Button(text='Reset',font=("Georgia",16,"bold"),bg='orange',fg='black',width=7,relief='groove',activebackground="blue",activeforeground='white',command=clear).place(x=560,y=420)
    def get_weather():
        try:
            # getting the weather information
            city=.search.get()
            config_file=configparser.ConfigParser()
            config_file.read("config.ini")
            api=config_file['Openweather']['api']
            data=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
            weather=requests.get(data).json()
            .__set_information(weather=weather)

        except requests.exceptions.ConnectionError:
            messagebox.showwarning('Connect',"Connect to The internet")
        except:
            messagebox.showerror('Error',"Some Errored Occured\nTry again Later!")
        
    def __set_information(weather):
        # print(weather)
        if weather['cod']=='404' and weather['message']=='city not found':
            messagebox.showerror("Error","Entered City Not Found")
            search.set("")
        elif weather['cod']=='400' and weather['message']=='Nothing to geocode':
            messagebox.showinfo("Warning",'Enter The city name')
            search.set('')
        else:
            # getting time according to timezone
            lon=weather['coord']['lon']  # longitutde
            lat=weather['coord']['lat']  # latitude
            tf=TimezoneFinder()
            result=tf.timezone_at(lng=lon,lat=lat)
            home=pytz.timezone(result)
            local=datetime.datetime.now(home).strftime("%d/%m/%y  %I:%M %p")
            self.timelbl['text']=local
            .des['text']=weather['weather'][0]['description']
            .feel['text']=f"Feels Like {int(weather['main']['feels_like']-273)}° | {weather['weather'][0]['main']}"
            type=weather['weather'][0]['main']
            .place_image(type)
            
            # sets the temperature and degree label
            temp=int(weather['main']['temp']-273)
            degree = degree['text']="°C"
            if temp>=100:
                degree.place(x=450,y=135)
            elif temp<=9 and temp>=0:
                degree.place(x=340,y=135)
            elif temp<=99 and temp>=10:
                degree.place(x=390,y=135)
            elif temp<0 and temp>=-9:
                degree.place(x=358,y=135)
            elif temp<=-10 and temp>=-99:
                degree.place(x=419,y=135)
            temperature = temperature['text']=int(weather['main']['temp']-273)
            humidity = humidity['text']=weather['main']['humidity'],'%'
            pressure = pressure['text']=weather['main']['pressure'],'mBar'
            location.config(text=weather['name'])
            vis['text']=int(weather['visibility']/1000),'km'
            sunrise['text']=f"Sunrise : \n{datetime.datetime.fromtimestamp(int(weather['sys']['sunrise'])).strftime('%d/%m/%y  %I:%M %p')}"
            sunset['text']=f"Sunset : \n{datetime.datetime.fromtimestamp(int(weather['sys']['sunset'])).strftime('%d/%m/%y   %I:%M %p')}"

    def place_image(type):
        if type=="Clear":
            img="clear.png"
            .set_image(img)
        elif type=="Clouds":
            img='clouds.png'
            .set_image(img)
        elif type=="Rain":
            img='rain.png'
            .set_image(img)
        elif type=='Haze':
            img='haze.png'
            .set_image(img)
        else:
            img='main.png'
            .set_image(img)
    def set_image(al,img):
       al.img3=Image.open(f"Icons/{img}")
       al.resizeimg3=al.img3.resize((190,190))
       al.finalimg3=ImageTk.PhotoImage(.resizeimg3)
       al.icons=Label(image=al.finalimg3)
       al.icons.place(x=70,y=110)
    def clear():
        .des.config(text="")
        .vis.config(text="")
        .pressure.config(text="")
        .humidity.config(text="")
        .sunset.config(text="Sunset :")
        .sunrise.config(text="Sunrise :")
        .feel.config(text="")
        .degree.config(text="")
        .temperature.config(text="")
        .timelbl.config(text="")
        .location.config(text="")
        .search.set("")
        img='main.png'
        .set_image(img)

    def exit():
        a=messagebox.askyesno('Confirmation',"Are You sure You Want To Exit !")
        if a==True:
            destroy()

    def threading(event=0):
        t1=threading.Thread(target=.get_weather)
        t1.start()

if __name__=="__main__":
    root=main()
    root.mainloop()



