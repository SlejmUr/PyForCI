TXT = "logging.txt" ## edit this to make new file
## Open and close, dont do much
a = open(TXT, "a",encoding="utf-8")
a.close
## Open for reading
r = open(TXT, "r",encoding="utf-8")
ev_lines = r.readlines()
r.close
## Open for writing
w = open(TXT, "w",encoding="utf-8")
w.writelines(ev_lines)
w.close

def plog(*args):
    #Print and log
    f  = "" #adding new things to can be written down
    for i in args: #getting all stuff from args
        #print(i)
        f += str(i) + " " # add " " to stuff
    print(f + "\n") #print
    w.write(f + "\n") #log
    w.close # close

