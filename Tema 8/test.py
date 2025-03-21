import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]

ax.bar(fruits, counts, color='blue')

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')

plt.show()