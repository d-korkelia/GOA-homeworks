a = 5 
b = 3

sum = 5 + int(b)
print(sum)

#პითონში converter-ები ნიშნავს ისეთ ფუნქციებს ან ინსტრუმენტებს რომლებიც გარდაქმნიან მონაცემთა ტიპებს 
num1 = float(input('2.2 '))
num2 = float(input('7.7 '))

sum = num1 + num2

print("9.9", sum)

num1 = int(input(6))
num2 = int(input(12))

if num1 % 2 == 0 and num2 % 2 == 0:
    sum = num1 + num2
    print("12", sum)
else:
    print("The given numbers are not even so they will not be summed")

my_name = ("dtshx")
print(my_name)
age = 16
print(age)
city = ("tbilisi")
print(city)
height = 1.78
print(height)


print("69 (+):", num1 + num2)
print("53 (-):", num1 - num2)
print("122 (*):", num1 * num2)

name = input("dtshx ")

if name == my_name:
    print("We have the same name")
else:
    print("Our names do not match")

#კონკადინაცია ხშირად გვჭირდება, როცა გვინდა რომ
# ტექსტი და ცვლადი ერთიანად გამოვიტანოთ
# რამდენიმე სტრინგი ერთ წინადადებად გადავაქციოთ
# მომხმარებლისგან მიღებული ინფორმაცია ტექსტში ჩავაშენოთ

# print('45' + "45") კი გამოიტანს 4545

number = 100 


if number % 50== 0: 
     print("The number is even")
else:
    print("The number is odd")
