name = "Datuna"
lastname = "korkelia"

for letter in "Datuna Korkelia":
    print(letter)

#for i in name
#print(i)
# აკლია :

#for ციკლი გამოიყენება მაშინ როცა ვიცით რამდენჯერ უნდა გამეორდეს მოქმედება
#while ციკლი გამოიყენება მაშინ როცა არ ვიცით ზუსტად რამდენჯერ უნდა განმეორდეს მოქმედება

for i in range(1, 120 + 1): 
    sum = sum + i

for i in range(10):
    print(i)

name = input("enter ur name: ")

password = "paroli"
enter = input("შეიყვანეთ პაროლი")
while enter != password:
    print("პაროლი არასწორია, სცადეთ თავიდან!")
    enter = input("შეიყვანეთ პაროლი კიდევ ერთხელ: ")