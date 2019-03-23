import datetime
import RPi.GPIO as pi

pi.setmode(pi.BOARD)

pi.setwarnings(False)


upperMinInput=3

upperMaxInput=5

lowerMinInput=7

lowerMaxInput=11

relay1=13 	#For the motor taking water from underground storage to storage on the roof

relay2=15 	#For the motor that fills the underground storage with water from the main supply


pins=[upperMinInput,upperMaxInput,lowerMinInput,lowerMaxInput,relay1,relay2]



for i in range(0,3):

    pi.setup(pins[i],pi.IN)

    pi.setup(pins[4],pi.OUT)

    pi.setup(pins[5],pi.OUT)



while(1):

    a=str(datetime.datetime.now())

    time=int(a[11:13])

    print(time)

    if(time>=6 | time>=18):     #For motor to be on at 6 am in the morning till 8 am to fill the under ground storage

        print("Test1")

    if(time<8 | time<20):

        print("Test2")


if((pi.input(lowerMaxInput)==0 & pi.input(lowerMinInput)==1) | (pi.input(lowerMaxInput)==0 & pi.input(lowerMinInput)==0)):

        pi.output(relay2,1)

if(pi.input(lowerMaxInput)==1):

    pi.output(relay2,0)


if((pi.input(upperMaxInput)==0 & pi.input(upperMinInput)==1) | (pi.input(upperMaxInput)==0 & pi.input(upperMinInput)==0)):

    if(lowerMinInput!=0):

        pi.output(relay1,1)

if((pi.input(upperMaxInput)==1) | (pi.input(lowerMinInput)==0)):

    pi.output(relay1,0)