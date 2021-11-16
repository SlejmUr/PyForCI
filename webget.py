import urllib.request
from bs4 import BeautifulSoup
import stuff 

URL = "http://www.ci-interiordecor.com"
blacklist = ["/produtos/4/Acessorios","/produtos/13/Flores-e-plantas","/produtos/11/Fragrancias","/produtos/3/Iluminaçao","/produtos/8/Infantil","/produtos/6/Moveis","/produtos/9/Natal","/produtos/12/Papel-de-parede","/produtos/5/Quadros,-Espelhos-e-Relogios","/produtos/1/Texteis"]

print("You want to merge it?\n[1] Split \t [0] Merge")
yes_no = input()
tmp = -1

for c_list, listnumb in enumerate(blacklist):
  print(listnumb,c_list)
  if c_list <= 2:
    input()
  #if c_list < 8:
   # continue
  ## MAIN PAGE
  qu = urllib.parse.quote(listnumb)
  content_main = urllib.request.urlopen(URL + qu)
  read_content_main = content_main.read()
  main_soup = BeautifulSoup(read_content_main,'html.parser')
  main_soup.encode("utf8")


  allA = main_soup.find_all('a')
  #print(allA)
  for count, value in enumerate(allA):
    prodatr = allA[count].attrs
    #print(prodatr)
    if prodatr is None:
      print()
    atr = allA[count].attrs
    #print(atr)
    for key, value in atr.items():
      #print(value)
      if value.__contains__("produto"):
        if value not in blacklist:
          #print(value)
          stuff.GetAllStuff(value,c_list,yes_no)
  for count, value in enumerate(allA):
    prodatr = allA[count].attrs
    #print(prodatr)
    if prodatr is None:
      print()
    atr = allA[count].attrs
    #print(atr)
    for key, value in atr.items():
      #print(value)
      if value.__contains__("produto"):
        if value not in blacklist:
          #print(value)
          stuff.ReadToAllStuff(c_list,yes_no)
  if str(c_list) != str(tmp):
    print("c_list,tmp: " + str(c_list),str(tmp))
    stuff.ReadEnd(c_list,yes_no)
  print("tmp before c_list: " + str(tmp))
  tmp += c_list
  print("tmp: " + str(tmp))
    #print(count, value,prodatr)
