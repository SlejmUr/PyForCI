import linecache
from print_out import plog

print("[IDK] Started")

URL = "http://www.ci-interiordecor.com"
everythinglist = ["everything0","everything1","everything2","everything3","everything4","everything5","everything6","everything7","everything8","everything9"]


#print("You want to merge it?\n[1] Split \t [0] Merge")
#yes_no = input()
out_number = False
is_html = False
  # Change this to false if you dont
  # want to make tmp_o
out_number = bool(int(input("Read to URL and write to tmp_o?\n1 to True, 0 to False : ")))
is_html = bool(int(input("You want to save html too?\n1 to True,0 to False : ")))

for count_elist, listvalue in enumerate(everythinglist):
  str_count_elist = str(count_elist)
  r = open("everything/" + listvalue+".txt", "r",encoding='utf-8')
  lines = r.readlines()
  w = open("everything/" +listvalue+"_URL"+ str_count_elist +".txt", "w",encoding='utf-8')
  tmpw = open("picture_number/picnumb_" + str_count_elist + ".txt","w",encoding='utf-8')
  if is_html is True:
    html = open("productpicturehtml/product" + str_count_elist + ".html","w",encoding='utf-8')
  x = 1
  lin = ""
  prev = ""
  prev_col = ""
  y = 1
  ###

  for i, line in enumerate(lines):
    if line == "":
      continue
    if out_number is True:
      cline = linecache.getline("picture_number/picnumb_" + str_count_elist + ".txt", i+1)
      fline = line[:1]
      plog(cline,i,fline)
      tmpw.write( fline+ "," + cline)
    else:
      line = line.rstrip(line[-1])
      #print(x,x-1,line)
      if line == " ":
        continue
      if line.startswith("/") is False:
        continue
      if line.__contains__("/produto/"):
        x = 1
        lin = str(line)
        if is_html is True:
          html.write("<br>\n")
        #print(line)
      if line.__contains__("produtos"):
        #/img/produtos/1029003.jpg
        plog("[" + str(x),URL+line + "]")
        x += 1
        #lin = line
        w.write(line + "\n")
        if is_html is True:
          #trimline = line.rstrip(line[-1])
          html.write('<img height="100px" weight="100px" src="' + URL + line + '">\n')
      
      if (str(x-1) + " " + lin) != str(prev):
        if (x-1) == 0:
          if str(prev) != " ":
            plog("write_out: " + str(prev))
            w.write(str(prev) + "\n")
            if lin == "/produto/":
              tmpw.write(str(prev_col) + "\n")
              plog("Normal Produto found, skipped")
            elif not str(prev).startswith("/"):
              tmpw.write(str(prev_col) + "\n")
              plog("tmp_" + str_count_elist + ": " +  str(x-1) + "," + lin)
          elif str(prev) != "":
            plog("Elif")
          else:
            plog(" EMTPY [" + str(prev) + "] [" + str(x,y,i) +   "]")
        else:
          plog("x,prev: " + str(x),str(prev))
        #print("[" + str(x-1),lin + "]" )
      else:
        plog("[ELSE] " + str(prev) + " == " + str(x-1),lin)
      #print("[DEBUG] " + str(prev) + " != " + str(x-1),lin)
      prev = str(x-1) + " " + lin
      prev_col = str(x-1) + "," + lin
      
      
print("[IDK] END")
