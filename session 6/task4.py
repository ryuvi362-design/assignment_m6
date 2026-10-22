import matplotlib.pyplot as plt
import numpy as np

youtube = [2, 4, 3, 5, 6, 7, 4, 8, 9, 5, 6, 10, 7, 8, 11]

spotify = [1, 2, 2, 3, 4, 5, 3, 6, 7, 4, 5, 8, 6, 7, 9]

m, b = np.polyfit(youtube, spotify, 1)

plt.scatter(youtube, spotify, color='purple')

x = np.linspace(min(youtube), max(youtube), 100)

plt.plot(x, m*x + b, color='red')

plt.title('YouTube vs Spotify Hours')
plt.xlabel('YouTube Watch Hours')
plt.ylabel('Spotify Listening Hours')

print("Equation: y =", round(m, 2), "x +", round(b, 2))

plt.show()