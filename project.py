import csv
def package():
    print("""These are the packages we offer:
1. Kyrgyzstan
2. Vanuatu
3. Tajikistan
4. Nauru
5. Ivory Coast
6. Andorra
7. Liechtenstein
8. Wallis and Futuna
9. Tuvalu
10. Moldova""")
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
    x=int(input("""Which country do you want to visit of the following? Enter the number.
1. Kyrgyzstan
2. Vanuatu
3. Tajikistan
4. Nauru
5. Ivory Coast
6. Andorra
7. Liechtenstein
8. Wallis and Futuna
9. Tuvalu
10. Moldova"""))
    start=input("Enter the start date in the format DD-MM-YYYY.")
    durn=int(input("Enter the number of days you want to travel"))
    f=open("booking.csv","a",newline="")
    d=int(input("Number of people travelling:"))
    rec=csv.writer(f,delimiter=",")
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
    r=[pas,country,start,durn,d]
    print("Here are the details of your booking in the order password, country, start date, duration and number of people travelling:",r)
    c=input("Do you want to confirm your booking? Enter y for yes and n for no.")
    print("Send your itinerary to dreams007@gmail.com atleast one month prior to your travel date.")
    print("""Cost per person is",durn*12000, "Pay", d*(durn*12000)," through PayTM or GPay at the number 9098909899.
You will recieve the reciept on your whatsapp.""")
    print("If you do not send your itinerary within the given period, your booking will be cancelled and you will recieve a 90% refund.")
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
        print("Your booking(s) is(are) in the order password, country, start date, duration and number of people travelling")
        for j in a:
            print(j)
def feedback():
    print("Please give your feedback:")
    x=input()
    f=open("feedback.txt","a")
    f.write('\n')
    f.write(x)
    f.write('\n')
    print("Thank you for your valuable feedback!")
    f.close()
def readfeed():
    f=open("feedback.txt","r")
    print(f.read())
    f.close()
    
print("Welcome to Dreamers Tours & Travels!  You have come to the right place if you want to have your dream vacation come true!")
print("We here help you to travel to the least visited countries in the world, that too on your own terms.")
print("""You can make your own itinerary and we will help you to achieve it at just INR 12000/- per day no matter what package you choose.
This cost includes all the travel, accomodation and VISA charges.""")
print("So let this wonderful journey begin!")
while True:
    x=int(input("""How would you like to explore our service?
1. Offline: in person at our office
2. Online: at the comfort of your home"""))
    if x==1:
        print("""Our offices are present in these four cities:
1. Delhi
2.Mumbai
3.Chennai
4.Kolkata""")
        x=int(input("Which office would you like to visit? Press 5 to exit."))
        if x==1:
            print("""Our office is located at Connaught Place.
Address: Dreamers Tours & Travels, N-17, Rajeev Chowk-110001""")
            print("You can visit our office anytime between 09:00 and 17:00 on weekdays. Thank you!")
        elif x==2:
            print(""""Our office is located at Altamount Road.
Address: 1A, Altamountroad, Tardeo-400026""")
            print("You can visit our office anytime between 09:00 and 17:00 on weekends. Thank you!")
        elif x==3:
            print("""Our office is located at T. Nagar
Address: No.7, Nageswara Rao Road, T.Nagar-600017""")
            print("You can visit our office anytime between 09:00 and 17:00 on any day. Thank you!")
        elif x==4:
            print("""Our office is located at Rosedale Plaza Complex
Address: Rosedale Plaza Complex, New Town Road, Action Area III, Newtown-700160""")
            print("You can visit our office anytime between 09:00 and 17:00 on weekdays. Thank you!")
        else:
            feedback()
            print("Thank you for visiting our website. If you have any query, mail us at dreamersT&T@gmail.com. Hope to see you again!")
            break
            break
    else:
        print("""What do you want to do:
1.View the Packages we offer.
2. Make a booking.
3. View your booking.
4. Read reviews of our esteemed customers
5. Exit""")
        x=int(input("Enter the number."))
        if x==1:
             package()
        elif x==2:
            book()
        elif x==3:
              read()
        elif x==4:
            readfeed()
        else:
            feedback()
            print("Thank you for visiting our website. If you have any query, mail us at dreamersT&T@gmail.com. Hope to see you again!")
            break
    
