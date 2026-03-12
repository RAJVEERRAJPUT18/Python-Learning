import time
timestamp = time.strftime('%H: %M:%S')
print("Current time is:-",timestamp)
timestamp = time.strftime('%H')
print("hour:-",timestamp)
timestamp = time.strftime('%M')
print("min :-",timestamp)
timestamp = time.strftime('%S')
print("sec:-",timestamp)
hour= int(time.strftime('%H'))
print(hour)
if(hour>=0 and hour < 12):
    print("Good Morning Sir")
if(hour>=12and hour < 15):
    print("Good Afternoon Sir")
if(hour>=15and hour < 20):
    print("Good Evening Sir ")
if(hour>=20 and hour < 24 ):
    print("Good Night Sir")







 