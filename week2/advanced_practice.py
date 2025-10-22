#Sample data

expenses = [
        {"amount":200,"category":"Food","description":"Breakfast"},
        {"amount":5000,"category":"Rent","description":"Monthly house rent"},
        {"amount":150,"category":"Transport","description":"Bus fare"},
        {"amount":300,"category":"Food","description":"Lunch"},
        {"amount":1000,"category":"Transport","description":"Train"}
          ]

# Challenge 1: Use list comprehension to get all Food items
food_items = [exp for exp in expenses if exp['category'] == "Food"]
print("Food items",food_items)

# Challenge 2: Use lambda + sorted to sort by amount (highest first)
sorted_by_amount = sorted(expenses,key=lambda x:x['amount'], reverse = True)
print("Sorted:", sorted_by_amount)

# Challenge 3: Use map to get just the amounts
just_amounts = list(map(lambda x:x['amount'],expenses))
print("\nAmount", just_amounts)

# Challenge 4: Use filter to get expenses over ₹500
big_expenses = list(filter(lambda x:x ['amount']> 500,expenses))
print("Big expenses",big_expenses)
