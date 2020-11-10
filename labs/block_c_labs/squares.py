import matplotlib.pyplot as plt


def small(): #Creates a small red dotted line square
  x = [3,4,4,3,3]
  y = [3,3,4,4,3]
  plt.plot(x,y, 'ro:')

def medium(): #Creates a medium red dashed line square
  x = [2,5,5,2,2]
  y = [2,2,5,5,2]
  plt.plot(x,y, 'gs--')

def large(): #Creates a large blue solid line square
  x = [1,1,6,6,1]
  y = [1,6,6,1,1]
  plt.plot(x,y, 'bp-')

def run(): #Calls and shows the graph
  small()
  medium()
  large()
  plt.show()

run()
