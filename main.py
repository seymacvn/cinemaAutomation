import sys
import copy
inputfile = sys.argv[1]
dataFile = open(inputfile).read()
komutlar = [i.split() for i in dataFile.split("\n")]
komutlar.pop()
alfabe = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
          "W", "X", "Y", "Z"]
salon_isimleri = []
salonlar = dict()
kişiler = []
output=open("out.txt","w")

def number_of_lists(x):
    f = lambda x: 0 if not isinstance(x, list) else (f(x[0]) + f(x[1:]) if len(x) else 1)
    m=f(x)-1
    return m
for i in komutlar:
    if i[0] == 'CREATEHALL':
        u = len(i)
        if u < 3:
            print("Error: Not enough parameters for creating a hall!", file=output)
            print("Error: Not enough parameters for creating a hall!")

        elif u > 3:
            print("Error: Too much parameters for creating a hall!", file=output)
            print("Error: Too much parameters for creating a hall!")

        else:
            k = i[2]
            c, a = k.split('x')
            c = int(c)  # satır
            a = int(a)  # sütun
            d = c * a
            d=str(d)
            if c>26:
                print("please enter values below 26", file=output)
                print("please enter values below 26")
            elif i[1] not in salon_isimleri:
                salon_isimleri.append(i[1])
                print("The hall", i[1], " having", d, "seats has been created", file=output)
                print("The hall", i[1], " having", d, "seats has been created")

                listeler = [""] * c
                for k in range(c):
                    listeler[k] = ["X"] * a
                salonlar.update({i[1]: listeler})

            else:
                print("Warning: Cannot create the hall for the second time. The cinema has already", i[1], file=output)
                print("Warning: Cannot create the hall for the second time. The cinema has already")


    elif i[0] == 'SELLTICKET':
        t=len(i)
        if t<=4:
            print("Error: Not enough parameters for selling a ticket!", file=output)
            print("Error: Not enough parameters for selling a ticket!")

        else:
            if i[1]  in kişiler:
                print("Sold the ticket to this name before", file=output)
                print("Sold the ticket to this name before")

            elif i[1] not in kişiler:
                kişiler.append(i[1])
                if i[3] not in salon_isimleri:
                    print("no such hall", file=output)
                    print("no such hall")

                else:
                    koltuklar = []
                    koltuklar = i[4:]
                    for u in koltuklar:
                        if '-' in u:
                         d, e = u.split('-')
                         e = int(e)
                         h = salonlar[i[3]]
                         f = int(alfabe.index(d[0]))
                         a = number_of_lists(h)
                         t=(a-f-1)
                         g = int(d[1:])
                         o=len(h[0])
                         if g>=o or e>=o:
                           print("Error: The hall",i[3],"has less column than the specified index",u, file=output)
                           print("Error: The hall", i[3], "has less column than the specified index", u)

                         elif h[t][g] == 'X':
                             for a in range(g, e):
                                 if i[2] == 'student':
                                  h[t][a] = 'S'

                                 elif i[2] == 'full':
                                  h[t][a] = 'F'

                             print("Success:", i[1], "has bought", u, "at", i[3], file=output)
                             print("Success:", i[1], "has bought", u, "at", i[3])

                         else:
                             print("Warning: The seat", u, " cannot be sold to", i[1], " since it was already sold!", file=output)
                             print("Warning: The seat", u, " cannot be sold to", i[1], " since it was already sold!")

                        else:
                          x = int(alfabe.index(u[0]))
                          k = int(u[1:])
                          w = salonlar[i[3]]
                          y = number_of_lists(w)
                          c=(y-x-1)

                          o=len(w[0])
                          if k>=o:
                           print("Error: The hall",i[3],"has less column than the specified index",i[4:], file=output)
                           print("Error: The hall", i[3], "has less column than the specified index", i[4:])

                          elif w[c][k] == 'X':
                             if i[2] == 'student':
                              w[c][k] = 'S'
                              print("Success:", i[1], "has bought", u, "at", i[3], file=output)
                              print("Success:", i[1], "has bought", u, "at", i[3])
                             elif i[2] == 'full':
                                   w[c][k] = 'F'
                                   print("Success:", i[1], "has bought", u, "at", i[3], file=output)
                                   print("Success:", i[1], "has bought", u, "at", i[3])
                          elif w[c][k] == 'S' or w[c][k] == 'F':
                           print("Warning: The seat", u , " cannot be sold to", i[1], " since it was already sold!", file=output)
                           print("Warning: The seat", u, " cannot be sold to", i[1], " since it was already sold!")
                           break
    elif i[0]=='CANCELTICKET':
        r=len(i)
        if r <3:
            print("Error: Not enough parameters for cancelling a ticket!", file=output)
            print("Error: Not enough parameters for cancelling a ticket!")
        elif i[1] not in salon_isimleri:
            print("no such hall", file=output)
            print("no such hall")
        iptal = []
        iptal = i[2:]
        for u in iptal:
            if '-' in u:
                d, e = u.split('-')
                e = int(e)
                f = int(alfabe.index(d[0]))
                g = int(d[1:])
                h = salonlar[i[1]]
                o = len(h[0])
                a = number_of_lists(h)
                n=(a-f-1)
                if g >= o or e >= o:
                    print("Error: The hall",i[1],"has less column than the specified index",u, file=output)
                    print("Error: The hall", i[1], "has less column than the specified index", u)

                elif h[n][g] == 'S' or h[n][g] == 'F':
                    for a in range(g, e):
                        h[n][g] = 'X'
                    print("Success: The seat",u ,"at",i[1] ,"has been canceled and now ready to be sold again", file=output)
                    print("Success: The seat", u, "at", i[1], "has been canceled and now ready to be sold again")

                else:
                    print("Error: The seat",u,"at",i[1],"has already been free! Nothing to cancel", file=output)
                    print("Error: The seat", u, "at", i[1], "has already been free! Nothing to cancel")
            else:
                x = int(alfabe.index(u[0]))
                k = int(u[1:])
                w = salonlar[i[1]]
                a = number_of_lists(w)
                f=(a-x-1)
                o = len(w[0])
                if k >= o:
                    print("Error: The hall", i[1], "has less column than the specified index", u, file=output)
                    print("Error: The hall", i[1], "has less column than the specified index", u)

                elif w[f][k] == 'S' or w[f][k] == 'F' :
                    w[f][k] ='X'
                    print("Success: The seat", u, "at", i[1], "has been canceled and now ready to be sold again", file=output)
                    print("Success: The seat", u, "at", i[1], "has been canceled and now ready to be sold again")
                elif w[f][k]=='X':
                    print("Error: The seat",u,"at",i[1],"has already been free! Nothing to cancel", file=output)
                    print("Error: The seat", u, "at", i[1], "has already been free! Nothing to cancel")

    elif i[0] == 'BALANCE':
        r=len(i)
        if r<2:
            print("Error: Not enough parameters for balance a ticket!", file=output)
            print("Error: Not enough parameters for balance a ticket!")
        denge=[]
        denge=i[1:]
        for u in denge:
          toplamstudent = 0
          toplamfull = 0
          a=salonlar[u]
          for k in a:
            c=k.count('S')
            d=k.count('F')
            if c!=0:
                toplamstudent+=c
            if d!=0:
                toplamfull+=d
          toplamsatış=(toplamfull)*10+(toplamstudent)*5

          print("\n Hall report of ",u,"\n","---------------"+(len(u)+1)*"-","\n","Sum of Students:",toplamstudent*5,"Sum of full fares:",toplamfull*10,",","Overall:",toplamsatış, file=output)
          print("\n Hall report of ",u,"\n","---------------"+(len(u)+1)*"-","\n","Sum of Students:",toplamstudent*5,"Sum of full fares:",toplamfull*10,",","Overall:",toplamsatış)
    elif i[0] == 'SHOWHALL':
        son = copy.deepcopy(salonlar)
        show=[]
        r=len(i)
        if r<2:
            print("Error: Not enough parameters for showing a ticket!", file=output)
            print("Error: Not enough parameters for showing a ticket!")
        else:
            print("Printing hall layout of", i[1], file=output)
            print("Printing hall layout of", i[1])
        if i[1]  in salon_isimleri:
            if i[1] not in show:
                k=son[i[1]]
                a=number_of_lists(k)
                liste=alfabe[:a]
                liste.reverse()
                r=len(liste)
                count=0
                x=len(k[1])
                y=[' ']

            for e in liste:
                if count < r:
                    k[count].insert(0, e)
                    count += 1
            for row in k:
                print('  '.join(row), file=output)
                print('  '.join(row))
            for t in range(x):
                if t==0:
                    print("  ",t,end="  ", file=output)
                    print("  ", t, end="  ")
                elif t<=9:
                    if t==(x-1):
                        print(t, end="  ""\n", file=output)
                        print(t, end="  ""\n")
                    else:
                        print(t, end="  ", file=output)
                        print(t, end="  ")
                elif t>=10:
                    if t==(x-1):
                        print(t, end=" ""\n", file=output)
                        print(t, end=" ""\n")
                    else:
                        print(t, end=" ", file=output)
                        print(t, end=" ")

