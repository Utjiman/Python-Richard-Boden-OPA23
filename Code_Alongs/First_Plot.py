import matplotlib.pyplot as plt

numbers = list(range(1,11))
squares = [number**2 for number in numbers]
print(numbers)
print(squares)

plt.plot(numbers, squares)
plt.title("x^2 for positiv intergers 0-9")
plt.xlabel("x")
plt.ylabel("y")
plt.show()