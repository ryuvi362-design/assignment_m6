import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 2, 5, 6, 3, 4, 7]
posts = [5, 8, 12, 15, 10, 20, 25, 14, 18, 30]

plt.scatter(hours, posts, color='blue')

plt.title('Instagram Usage vs Posts')
plt.xlabel('Hours Spent Per Day')
plt.ylabel('Posts Uploaded Per Month')

plt.show()