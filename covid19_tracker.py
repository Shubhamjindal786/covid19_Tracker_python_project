import requests
import datetime
import tkinter as tk

def getCovidData():
    url="https://disease.sh/v3/covid-19/all"
    json_data=requests.get(url).json()
    #print(json_data)
    total_cases=str(json_data['cases'])
    total_deaths=str(json_data['deaths']) 
    today_cases=str(json_data['todayCases'])
    today_deaths=str(json_data['todayDeaths'])
    today_recovered=str(json_data['todayRecovered'])
    Upadted_at=json_data['updated']
    date=datetime.datetime.fromtimestamp(Upadted_at/1e3)
    label.config(text="Total Cases : "+today_cases+"\nTotal Deaths: " +total_cases+ "\nToday Cases: "+today_cases
    + "\nToday Deaths: "+today_deaths+"\nTotal Recovered: "+today_recovered)
    label1.config(text=date)

canvas=tk.Tk()
canvas.geometry("400x500")
canvas.title("Covid19 Tracker App")

f=("poppins",15,"bold")


button=tk.Button(canvas,font=f,text="Load Information",command=getCovidData)
button.pack(pady=20)

label=tk.Label(canvas,font=f)
label.pack(pady=20)

label1=tk.Label(canvas,font=f)
label1.pack(pady=20)

getCovidData()
canvas.mainloop()