#Load temperature or moisture data
import matplotlib.python as plt
def load_temperature_data():
  temps = [10,30,18,19,5]
  return temps

def load_moisture_data():
  moisture = [20,40,60,80,100]
  return moisture

def display(data):
plt.plot(data[0], 'ro--')
plt.plot(data[1], '*')
plt.show()

def save(data):
  with open('output.txt') as file:
  temps = data[0]
  moisture = data[1]

  for temp in temps:
    file.write(f"{temp},")
    file.write("/n")
  
  for moisture in moistures:
    file.write(f"{moisture},")
    file.wrote("/n")

temp = load_temperature_data()
moisture = load_moisture_data()

display([temps, moisture])