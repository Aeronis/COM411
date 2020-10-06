print("I need to paint this!! But im not sure which direction to stroke.")

while True:
  print("Should i paint up, down, left or right?")
  paint = input()

  if paint == "up" or paint == "Up":
    print("Ok, Painting upwards!")
    break
  elif paint == "down" or paint == "Down":
    print("Ok, Painting down!")
    break
  elif paint == "left" or paint == "Left":
    print("Ok, Painting left!")
    break
  elif paint == "right" or paint == "Right":
    print("Ok, Painting right!")
  else:
    print("I don't know what that is, your options where up, down, left and right!")