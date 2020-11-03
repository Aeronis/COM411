import os
def cwd():
  path = os.getcwd()
  print(f"current working folder path: {path}") 
  print("The folder contains the following:")
  for file in os.listdir(path):
    print(file)
def run():
  print("Processing...")
  cwd()
run()