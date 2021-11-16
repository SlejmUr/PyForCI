print("\nApp Started\n")

print("Start script?\n[1] IDK \t [0] WebGet")
scriptinp = input()

if scriptinp=="1":
  import idk
  idk()
  input()
elif scriptinp=="0":
  import webget
  webget()
  input()
else:
  print("F")
input()
f = open("names.txt","r",encoding='utf-8')
w = open("out.txt", "w",encoding='utf-8')
lines = f.readlines()
#names = []
prev = ""

for line in lines:
    #line = line.replace("\n","")
    if line is None:
      continue
    if line.startswith("/"):
      continue
      #print("Line has : " + line)
    else:
      line = line.rstrip(line[-1])
      #line = line.strip()
      if line == "":
        continue
      if str(line) != str(prev):
        print("[" + line + "]")
      if str(prev).endswith(","):
        prev += str(line) + "\n"
        #w.write(prev + line)
      else:
        prev += str(line) + ","
    
w.write(prev) 
#w.writelines(names)
w.close()
f.close()
print("END")
