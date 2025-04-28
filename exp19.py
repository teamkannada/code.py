import matplotlib.pyplot as plt
#sample data for the charts
x=[1,2,3,4,5] #x-axis value
y=[10,20,15,25,30]

plt.plot(x,y, color='blue', marker='o')
plt.title("simple line chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

plt.bar(x,y,color='green')
plt.title('simple bar chart')
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()