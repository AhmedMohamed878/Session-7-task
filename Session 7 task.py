import matplotlib.pyplot as plt

x = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
y = [30, 25, 16, 20, 22, 35, 25]

plt.plot(x, y, marker = 'o', linestyle = '-', color = "red" )
plt.title("Temperature in Celsius.")

plt.xlabel("Days")
plt.xticks(rotation = 45)
plt.ylabel("Temp")
plt.show()