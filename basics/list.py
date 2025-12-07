# Even Odd Numbers
numbers = [0,1,2,3,4,5,6,7,8]
print(f"Even numbers: {numbers[0::2]}")
print(f"Odd numbers: {numbers[1::2]}")

numbers = [0,1,2,3,4,5,6,7,8]
even_numbers = [num for num in numbers if num % 2 ==0]
odd_numbers = [num for num in numbers if num % 2 !=0]
print(f"Even numbers (by value): {even_numbers}")
print(f"Odd numbers (by value): {odd_numbers}")

# Checking the existence
print("-----Checking for existence------")

fruits = ['Apple','Banana','Grapes']
if "Banana" in fruits:
     print("Yes, Banana is in list.")
if "Orange" in fruits:
    print("No, Orange is not in list.")
if "Peach" in fruits:
    print("No, Peach is not in list.")

