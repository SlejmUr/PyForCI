print("\n[READ] App Started\n")
w = open("everything.txt", "r")
lines = w.readlines()

for line in lines:
  print(line)
print("[READ] END")