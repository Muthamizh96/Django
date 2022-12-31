from django.shortcuts import render
from django.shortcuts import redirect
import pymysql
import mysql.connector as pymysql
from tkinter import messagebox

def bikehome(request):
    return render(request,"Bikes.html")
def bikebook(request):
    Bike_No=''
    Rider_Name=''
    Mobile_No=''
    Email_Id=''
    current_city=''
    profession=''
    Licence_No=''
    country=''
    if (request.method=="POST"):
        bike=pymysql.connect(host="localhost",user="root",password="Muthamizh@5609",database="bikes",port="3307")
        cursor=bike.cursor();
        e=request.POST
        for key,value in e.items():
            if key=="ubike":
                Bike_No=value
            if key=="uname":
                Rider_Name=value
            if key=="unumber":
                Mobile_No=value
            if key=="umail":
                Email_Id=value
            if key=="ucity":
                current_city=value
            if key=="uprofession":
                profession=value
            if key=="ulicence":
                Licence_No=value
            if key=="ucountry":
                country=value
        c="insert into bikebook values('"+Bike_No+"','"+Rider_Name+"','"+Mobile_No+"','"+Email_Id+"','"+current_city+"','"+profession+"','"+Licence_No+"','"+country+"')";
        cursor.execute(c);
        bike.commit();
        bike.close();
        messagebox.showinfo("successfull","Welcome Your Bike is Booked Successfully...!")
        return redirect(bikehome)
    return render(request,"Book.html")
