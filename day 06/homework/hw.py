TARGET_PASSWORD = "secret123"

attempts = 0
MAX_ATTEMPTS = 3

while attempts < MAX_ATTEMPTS:
    user_input = input("შეიყვანეთ password: ")
    attempts += 1

    if user_input == TARGET_PASSWORD:
        print("Password correct. Access granted.")
        break
    else:
        if attempts == MAX_ATTEMPTS:
            print("You have reached the maximum number of attempts")
        else:
            print(f"Wrong password. You have {MAX_ATTEMPTS - attempts} attempts left.")
            

#(True and False and 5 > 9 and 90 * 30 > 1089 or False and 'Nino' != '' or False or True and 56 * 2 > 90)
#გამოიტანს trues

# მასივი  არის კონტეინერი სადაც შეგვიძლია ერთზე მეტი მნიშვნელობის შენახვა.
# მაგალითად რიცხვები ტექსტები True/False და სხვა.

family = ["დედა", "მამა", "და", "ძმა"]

for member in family:
    print(member)

save = ["1", "2", "3", "4"]

for thing in save:
    print(thing)
 
#Indexing ნიშნავს ელემენტებზე წვდომას მათი პოზიციის მიხედვით.
#ყველა ელემენტს აქვს თავისი ნომერი ამას ეწოდება index. და კი შეგვიძლია გამოყენება String-ებზეც

#იღებ კონკრეტულ მონაცემს სწრაფად ასევე კოდი გამარტივებულია და უფრო მეტად გასაგებია

nums = [10, 20, 30, 40, 50]
print(nums[0])   

fruit = ["apple", "pineapple", "grapes", "blueberries"]

for enumerate in fruit :
    print(enumerate)


students = [("Garen", 18), ("Darius", 20)]
for name, age in students:
    print(name, age)
    
for i in range(1, 10, 2):
    print(i)