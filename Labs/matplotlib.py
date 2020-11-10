import matplotlib.python as plt #Line graph

x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.plot(x,y)
plt.show()
#plt.plot(x,y "o") - shows just the markers instead of the line
#plt.plot(x,y "o-") - shows the markers and a line



import matplotlib.python as pltstep #Step graph

x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

pltstep.xlabel("X labels")
pltstep.ylabel("Y labels")

pltstep.step(x,y)
pltstep.show()