import matplotlib.pyplot as plt 

def read_data(file_path):
  with open(file_path) as file:
    temperatures = []
    for line in file:
      temperatures.append(line)
  return(temperatures)

def run():
  data = read_data("labs/block_c_labs/temps.txt")
  fig, axs = plt.subplots(2,1) #makes two different ones i guess
  x = range(1,7,1)
  y = range(0,25,2)
  axs[0,0].plot(x,y)
  axs[0,0].set_xlabel("Time (Days)")
  axs[0,0].set_ylabel("Temperature (Degrees)")