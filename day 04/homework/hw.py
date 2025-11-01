#Python-ში ლოგიკური ოპერატორები გამოიყენება პირობითი გამონათქვამების 
# შესაკავშირებლად და ლოგიკური შედარებების შესასრულებლად,
#  საბოლოო შედეგად კი ბრუნდება True ან False. 

name = "john"
age = 25
if name == "John" and "age" == 25:
    print("True")
else:
    print("False")

#სამი მთელი რიცხვის შემოტანა
a = int(input("choose first number: "))
b = int(input("choose second number: "))
c = int(input("choose third number: "))
sum = a + b + c
average = sum / 3
print("The arithmetic mean of three numbers is:", average)

# Sequencing 
# ეს ნიშნავს, რომ პროგრამა კითხულობს და ასრულებს კოდს ზუსტად იმ მიმდევრობით, როგორც დაწერილია — ზემოდან ქვემოთ.
# მაგალითად:
print("პირველი სტრიქონი შესრულდა")
print("მეორე სტრიქონი შესრულდა")  
print("მესამე სტრიქონი შესრულდა")  



# Selection 
# Selection ნიშნავს, რომ პროგრამა არჩევანს აკეთებს სხვადასხვა გზებს შორის, გარკვეული პირობის მიხედვით.
age = 18
if age >= 18:
    print("შენ სრულწლოვანი ხარ")  
else:
    print("შენ არასრულწლოვანი ხარ") 


# Iteration
# Iteration ნიშნავს, რომ პროგრამა განმეორებით ასრულებს კოდს მანამ, სანამ პირობა დაკმაყოფილებულია.
for i in range(5):
    print("number:", i)

#for loop  არის პროგრამირების კონცეფცია, რომელიც საშუალებას აძლევს კოდის ბლოკის განმეორებით შესრულებას.

#for loop როცა წინასწარ ვიცით რამდენჯერ უნდა შესრულდეს ციკლი
#while loop როცა არ ვიცით ზუსტად რამდენჯერ უნდა შესრულდეს
score = int(input("choose: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

a = int(input("choose first number: "))
b = int(input("choose second number: "))
c = int(input("choose third number: "))
