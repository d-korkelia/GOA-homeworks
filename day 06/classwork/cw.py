name = input("enter your name : ") 
vowels = "aeiouAEIOU"

count = 0

for i in name:
    print(i)

if "d" in vowels:
    count += 1
print(count)

for i in range (2, 5):
    print(i)

for i in range (1, 18 + 1, 2):
    print (i)


weather = input("Enter the weather (sunny, rainy, cloudy, etc.): ")
if weather == "sunny":
    print("Wear a Hat")
elif weather == "rainy":
    print("Wear boots")
elif weather == "cloudy":
    print("Wear a jacket")
else:
    print("Wear a T-shirt")

# როცა გვინდა რომ რაღაც პირობა შევამოწმოთ — ვიყენებთ if-ს
# elif გამოიყენება მაშინ როცა პირველივე პირობა არ შესრულებულა
# else გამოიყენება მაშინ როცა არც ერთი ზემოთ ჩამოთვლილი პირობა არ შესრულებულა

name = input('Enter your name: ')
vowels = 'aeiouAEIOU'

count = 0

for i in name:
    if i in vowels:
        count = count + 1
print(count) 
# მომხმარებლისგან ვითხოვთ სახელის შეყვანას
# ცვლადი count გამოვიყენეთ რომ დავითვალოთ რამდენი ხმოვანი ასოა
# for ციკლით გამოვიყენებთ სახელის თითოეულ სიმბოლოს


# for loop გამოიყენება მაშინ, როცა გვსურს რამდენჯერმე გავიმეოროთ მოქმედება 

seats = 20 
while seats >=10:
    print ("sell ticket")
    seats = seats -1

