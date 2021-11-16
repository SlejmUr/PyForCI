import urllib.request
from bs4 import BeautifulSoup


URL = "http://www.ci-interiordecor.com"


def GetAllStuff(value,count,merge):
  print(value,count)
  TXT = ""
  if merge == "1":
    #Yes, split!
    print("[GetAll] Splitting!")
    TXT = "everything" + str(count) + ".txt"
  else:
    print("[GetAll] Merge!")
    TXT = "everything.txt"
    
  a = open(TXT, "a",encoding="utf-8")
  a.close()

  r = open(TXT, "r",encoding="utf-8")
  ev_lines = r.readlines()
  r.close()
  w = open(TXT, "w",encoding="utf-8")
  w.writelines(ev_lines)
  w.write("\n" + value + "\n")
  qu = urllib.parse.quote(value) 
  content = urllib.request.urlopen(URL + qu)
  read_content = content.read()
  soup = BeautifulSoup(read_content,'html.parser')


  ##PRODDESC
  prodDesc = soup.find_all("div", {"class": "prodDesc"})
  #print(prodDesc[0])
  all_proddesc = []
  for x in prodDesc[0]:
      all_proddesc.append(str(x))

  ci_numb = all_proddesc[2]
  ci_numb = ci_numb.strip()
  #print(ci_numb.upper())
  w.write(ci_numb.upper() + "\n")

  ##picture
  ss = soup.find_all("div", {"class": "prodP2mini"})
  x = 0
  len_ss = len(ss)
  #print(len(ss))
  while x < len_ss:
    #print(x,len_ss)
    atr = ss[x].attrs
    #print(atr)
    for key, value in atr.items():
      if key == "onclick":
        value= value.replace("preVisualizar('","")
        value= value.replace("')","")
        #print(value)
        w.write(value + "\n")
    x += 1


  ##PRODname
  prodn = soup.find_all("div", {"class": "prodP1"})
  #print(prodn)
  prodname = []
  for x in prodn:
      prodname.append(str(x.contents))

  prod_n = prodname[0]
  prod_n = prod_n.strip()
  prod_n = prod_n.replace("['","")
  prod_n = prod_n.replace("']","")
  #print(prod_n)
  w.write(prod_n + "\n")
  
  w.close


def ReadEnd(count,merge):
  if merge == "1":
    #Yes, split!
    print("[ReadEnd] Splitting!")
    TXT = "everything" + str(count) + ".txt"
  else:
    print("[ReadEnd] Merge!")
    TXT = "everything.txt"


  r = open(TXT, "r",encoding="utf-8")
  ev_lines = r.readlines()
  r.close()
  w = open(TXT, "w",encoding="utf-8")
  w.writelines(ev_lines)
  w.write("\n/produto/\n")
  w.close
  print("PRODUTO")

##
## 2. round
##
def ReadToAllStuff(count,merge):
  TXT = ""
  out = ""
  if merge == "1":
    #Yes, split!
    print("[ReadToALL] Splitting!")
    TXT = "everything" + str(count) + ".txt"
    out = "out" + str(count) + ".txt"
  else:
    print("[ReadToALL] Merge!")
    TXT = "everything.txt"
    out = "out.txt"
  wf = open(TXT,"r",encoding='utf-8')
  wo = open(out, "w",encoding='utf-8')
  lines2 = wf.readlines()
  #names = []
  prev = ""
  for line in lines2:
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
          d = ""
          #print(" != [" + line + "]")
        if str(prev).endswith(","):
          prev += str(line) + "\n"
          #w.write(prev + line)
        else:
          prev += str(line) + ","
  wo.write(prev) 
  #w.writelines(names)
  wo.close()
