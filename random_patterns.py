import random

start = input("This program generates a random symmetrical pattern each time it runs. Press enter to start.\n")

again = "again"

while (again != "exit"):
  char1 = random.choice([" ", "/", "\\", "|", "_"])
  char2 = random.choice([" ", "/", "\\", "|", "_"])
  char3 = random.choice([" ", "/", "\\", "|", "_"])
  char4 = random.choice([" ", "/", "\\", "|", "_"])
  char5 = random.choice([" ", "/", "\\", "|", "_"])

  print(char1 + char2 + char3 + char4 + char5 + char5 + char4 + char3 + char2 + char1)
  print(char2 + char3 + char4 + char5 + char1 + char1 + char5 + char4 + char3 + char2)
  print(char3 + char4 + char5 + char1 + char2 + char2 + char1 + char5 + char4 + char3)
  print(char2 + char3 + char4 + char5 + char1 + char1 + char5 + char4 + char3 + char2)
  print(char1 + char2 + char3 + char4 + char5 + char5 +   char4 + char3 + char2 + char1)
  again = "exit"
  again = input("\n\nPress enter to run the program again.\n")