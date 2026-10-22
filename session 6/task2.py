import matplotlib.pyplot as plt

friends = ['A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L']

orders = [2, 4, 5, 3, 7, 8, 6, 9, 10, 4, 5, 7]

amount = [300, 600, 750, 450, 1000, 1200,
          900, 1400, 1500, 650, 800, 1100]

plt.scatter(orders, amount, color='red')

for i in range(len(friends)):
    plt.annotate(friends[i], (orders[i], amount[i]))

plt.title('Zomato Orders vs Amount Spent')
plt.xlabel('Number of Orders')
plt.ylabel('Amount Spent (Rs)')

plt.show()