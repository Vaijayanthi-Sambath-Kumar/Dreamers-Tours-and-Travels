import csv
def package():
    print("There are the following packages: \n 1. Kyrgyzstan \n 2. Vanuatu \n 3. Tajikistan \n 4. Nauru \n 5. Ivory Coast \n 6. Andorra \n 7. Liechtenstein \n 8. Wallis and Futuna \n 9. Tuvalu \n 10. Moldova")
    y=1
    while y==1:
        x=int(input("Which package would you like to know more about? Enter the number of the package. Enter 0 to exit."))
        if x==1:
            f=open("Kyrgyzstan.txt","r")
            print(f.read())
            f.close()
        elif x==2:
            f=open("Vanuatu.txt","r")
            print(f.read())
            f.close()
        elif x==3:
            f=open("Tajikistan.txt","r")
            print(f.read())
            f.close()
        elif x==4:
            f=open("Nauru.txt","r")
            print(f.read())
            f.close()
        elif x==5:
            f=open("Ivory Coast.txt","r")
            print(f.read())
            f.close()
        elif x==6:
            f=open("Andorra.txt","r")
            print(f.read())
            f.close()
        elif x==7:
            f=open("Liechtenstein.txt","r")
            print(f.read())
            f.close()
        elif x==8:
            f=open("Wallis and Futuna.txt","r")
            print(f.read())
            f.close()
        elif x==9:
            f=open("Tuvalu.txt","r")
            print(f.read())
            f.close()
        elif x==10:
            f=open("Moldova.txt","r")
            print(f.read())
            f.close()
        elif x==0:
            y=0
        else:
            print("Invalid input")

def book():
    pas=input("Set a strong password. Enter your old password if you have already made a booking")
    print("Make sure you do your booking atleast 45 days before the date of travel.")
    x=int(input("Which country do you want to visit of the following? Enter the number.  \n 1. Kyrgyzstan \n 2. Vanuatu \n 3. Tajikistan \n 4. Nauru \n 5. Ivory Coast \n 6. Andorra \n 7. Liechtenstein \n 8. Wallis and Futuna \n 9. Tuvalu \n 10. Moldova"))
    start=input("Enter the start date in the format DD/MM/YYYY.")
    durn=int(input("Enter the number of days you want to travel"))
    f=open("booking.csv","a",newline="")
    d=int(input("Number of people travelling:"))
    rec=csv.writer(f,delimiter=",")
    rec.writerow(["Password","COUNTRY","START","DURATION"])
    if x==1:
        country='Kyrgyzstan'
    elif x==2:
        country='Vanuatu'
    elif x==3:
        country='Tajikistan'
    elif x==4:
        country='Nauru'
    elif x==5:
        country='Ivory Coast'
    elif x==6:
        country='Andorra'
    elif x==7:
        country='Liechtenstein'
    elif x==8:
        country='Wallis and Futuna'
    elif x==9:
        country='Tuvalu'
    elif x==10:
        country='Moldova'
    else:
        print("Invalid input")
    r=[pas,country,start,durn]
    c=input("Do you want to confirm your booking? Enter y for yes.")
    print("Send your itenary to dreams007@gmail.com atleast one month prior to your travel date.")
    print("Cost per person is",durn*12000, "Pay", d*(durn*12000)," through PayTM or GPay at the number 9098909899 and you will recieve the reciept on your whatsapp.")
    print("If you do not send your itenary within the given period, you will recieve a 90% refund.")
    if c in 'yY':
        rec.writerow(r)
    else:
        pass
    f.close()
def read():
    f=open("booking.csv","r",newline="")
    x=csv.reader(f)
    y=input("Enter your password to see your bookings.")
    a=[]
    for i in x:
        if i[0]==y:
            a.append(i)
        else:
            pass
    if len(a)==0:
        print("Invalid Password")
    else:
        for j in a:
            print(j)
