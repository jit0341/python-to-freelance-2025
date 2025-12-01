
import numpy as np

print("="*44)
print("Test 1: seed(42) twice")
print("="*44)

np.random.seed(42)
result1 = np.random.randint(1,100,5)
print("First Time:", result1)

np.random.seed(42)
result2 = np.random.randint(1,100,5)
print("Second Time:", result2)
print("Are they same:", list(result1) == list(result2))

print("\n" + "="*50)
print("TEST 2: seed(99) twice")
print("="*50)

np.random.seed(99)
result3 = np.random.randint(1, 100, 5)
print("First time:", result3)

np.random.seed(99)
result4 = np.random.randint(1, 100, 5)
print("Second time:", result4)
print("Are they same?", list(result3) == list(result4))

print("\n" + "="*50)
print("TEST 3: No seed twice")
print("="*50)

result5 = np.random.randint(1, 100, 5)
print("First time:", result5)

result6 = np.random.randint(1, 100, 5)
print("Second time:", result6)
print("Are they same?", list(result5) == list(result6))





