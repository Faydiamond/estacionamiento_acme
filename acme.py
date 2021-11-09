# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 23:43:30 2021

@author: FabiDiamanti
"""

import tkinter as tk
import _tkinter
import  tkcalendar as  tc
import datetime 

ventana = tk.Tk()
ventana.geometry('410x400')
ventana.title('Estacionamiento Acme')

#CALENDARIO #1
calendar = tc.Calendar(ventana, selectmode='day', year = 2021 , month=11 )
calendar.place(x = 75,y=50)
######################################

hour_in = tk.Label(text="Hora Entrada ")
hour_in.place(x=7, y=250, width=200)

hour1 = tk.Spinbox(from_=0, to=23, increment=1)
hour1.place(x=20, y=285, width=40)

sep_min = tk.Label(text=":")
sep_min.place(x=60, y=281, width=20)

min1 = tk.Spinbox(from_=0, to=59, increment=1)
min1.place(x=80, y=285, width=40)

sepsec = tk.Label(text=":")
sepsec.place(x=120, y=281, width=20)

sec1 = tk.Spinbox(from_=0, to=59, increment=1)
sec1.place(x=135, y=285, width=40)

hour_in.config(width=2,font=("Verdana",12))

#####################################################################

hour_exit = tk.Label(text="Hora Salida ")
hour_exit.place(x=200, y=250, width=200)
hour_exit.config(width=2,font=("Verdana",12))


hour2 = tk.Spinbox(from_=0, to=23, increment=1)
hour2.place(x=220, y=285, width=40)

sep_min2 = tk.Label(text=":")
sep_min2.place(x=262, y=281, width=20)

min2 = tk.Spinbox(from_=0, to=59, increment=1)
min2.place(x=285, y=285, width=40)

sepsec = tk.Label(text=":")
sepsec.place(x=330, y=281, width=20)

sec2 = tk.Spinbox(from_=0, to=59, increment=1)
sec2.place(x=350, y=285, width=40)

def prices_parking(mounth, hou,minn,sec):
    #print( mounth,hou,minn,sec )= 
    res = 0
    price_parking  = 0
    if(mounth ==12 ):
        if (minn > 0):
            hou+= 1
        i = 1
        res = 0
        while ( i <= hou):
             #print(i)
             if (i<=2):
                 price_parking = 2500
             if(i > 2 ):
                 price_parking = 800
             res = res+price_parking
             i+=1
        return res
            
    else: 
        price_parking = 1000 
        if (minn > 0):
            hou+= 1
        i = 1
        res = 0
        while ( i <= hou):
             if (i<=1):
                 price_parking = 1000
             if(i > 1 ):
                 price_parking = 500
             res = res+price_parking
             i+=1
        return res
    
def calculate():
    
    date1 = calendar.get_date();
    date1 = datetime.datetime.strptime(date1, '%m/%d/%y').month
    hour_1= int(hour1.get())
    min_1 = int(min1.get())
    sec_1 = int(sec1.get())
    hour_2= int(hour2.get())
    min_2 = int(min2.get())
    sec_2 = int(sec2.get())
    time_1 = datetime.timedelta(hours= hour_1 , minutes=min_1, seconds=sec_1)
    time_2 =  datetime.timedelta(hours= hour_2 , minutes=min_2, seconds=sec_2)
    dif_hour = str(time_2 - time_1)
    x = dif_hour.split(":")
    nu= [int(j) for j in x]
    hours   = nu[0]
    minutes = nu [1]
    seconds = nu [2]
    total =  prices_parking(date1, hours, minutes, seconds)
    #print(total)
    total_lbl.config(text= prices_parking(date1, hours, minutes, seconds)  )


calculate_btn = tk.Button(ventana ,text='Calcular Precio', command = calculate)
calculate_btn.place(x = 145, y= 325)
total_lbl = tk.Label(text='',fg='#3D59E3' )
total_lbl.place(x=145, y=360, width=60)

ventana.mainloop()