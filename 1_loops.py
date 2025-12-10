
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))
# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)



# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
for subject in subjects:
    if subject == "History":
        break
        print(subject)
# skip over "science" and print the rest
for subject in subjects:
    if subject == "science":
        continue
        print(subject)

list1000 = list(range(1, 1001))
for number in list1000:
    if number >599:
        break
        print(number)

list500 = list(range(1, 501))
for number in list500:
    if number >599
    break
    print(number)

for number in list1000
if 300 <= number <= 500:
    continue
    print(number)



applicants_for_credit= ["Alice", "Bob", "Charlie", "David", "Eve"]
credit_scores = [720, 680, 590, 610, 750]
for applicant, score in zip(applicants_for_credit, credit_scores):
    if score < 600:
        continue
    print(applicant +" approved for credit with score:" + str(score))

print(len(subject))
for index in range (len(subjects)):
    print("subject" + str(index) + ":"+ subjects[index])


# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.
total = 0
for number in numbers:
    total += numbers 
print("total:", total)


new_number = list(range(1, 261))
total = 0
for number in new_numbers:
    total += numbers
    print("Total sum from 1 to 260: ", total)
