
j = [["ID","FIO","YOSH"],[1,"Ashirbekov Sardor",19],[2,"Muratov Oybek",42],[3,"Madrimova Marg'uba",40]]
# j = [[1,"abcd",12],[2,"asbkjsdb",15],[3,"ajsndjansd",20]]

class TABLE:
    
    def __init__(self,jadval):
        self.j = jadval
    
    def showtable(self,row=0,column=0):
        b = " "
        p = "+"
        c = "|"
        m = "-"
        max_uslar=[]
        
        #CHANGE TYPE AND ADD ID
        
        for satr in range(len(self.j)):
            """"ID"""
            # idd = satr+1
            # self.j[satr].insert(0,str(idd))
            for ustun in range(len(self.j[satr])):
                self.j[satr][ustun]=str(self.j[satr][ustun])
        
        #MAXLEN
        
        for ustun in range(len(self.j[1])):
            us = []
            for satr in range(len(self.j)):
                e = len(self.j[satr][ustun])
                us.append(e)
            max_us = max(us)
            max_uslar.append(max_us)
        
        if row == 0 and column == 0:
            #1-LINE    
            
            print(p,end="")
            for ch in range(len(self.j[0])):
                bj=(max_uslar[ch]+2)*m
                print(f"{bj}",end=p)
            print("")
            
            #MAIN
            
            for satr in range(len(self.j)):   
                for ustun in range(len(self.j[satr])):
                    bj=(max_uslar[ustun]-len(self.j[satr][ustun]))*b
                    print(f"{c} {bj}{self.j[satr][ustun]} ",end="")
                print(c)
                
                # AJRATISH
                print(p,end="")
                for ch in range(len(self.j[0])):
                    bj=(max_uslar[ch]+2)*m
                    print(f"{bj}",end=p)
                print("")
        
        elif row == 1 and column == 0:
           print(p,end="")
           for ch in range(len(self.j[0])):
               bj=(max_uslar[ch]+2)*m
               print(f"{bj}",end=p)
           print("")
           
           for satr in range(1):
               for ustun in range(len(self.j[satr])):
                   bj=(max_uslar[ustun]-len(self.j[satr][ustun]))*b
                   print(f"{c} {bj}{self.j[satr][ustun]} ",end="")
               print(c)
           
           print(p,end="")
           for ch in range(len(self.j[0])):
               bj=(max_uslar[ch]+2)*m
               print(f"{bj}",end=p)
           print("")
           
           for satr in range(len(self.j)):
               if satr == 0:
                   continue
               for ustun in range(len(self.j[satr])):
                   bj=(max_uslar[ustun]-len(self.j[satr][ustun]))*b
                   print(f"{c} {bj}{self.j[satr][ustun]} ",end="")
               print(c)
               
           print(p,end="")
           for ch in range(len(self.j[0])):
               bj=(max_uslar[ch]+2)*m
               print(f"{bj}",end=p)
           print("")

        
        if row == 0 and column == 1:
            print(p,end="")
            for ch in range(len(self.j[0])):
                bj=(max_uslar[ch]+2)*m
                print(f"{bj}",end=p)
            print("")
            
            for satr in range(1):
                for ustun in range(len(self.j[satr])):
                    bj=(max_uslar[ustun]-len(self.j[satr][ustun]))*b
                    print(f"{c} {bj}{self.j[satr][ustun]} ",end="")
                print(c)
            
            
            for satr in range(len(self.j)):
                if satr == 0:
                    continue
                for ustun in range(len(self.j[satr])):
                    bj=(max_uslar[ustun]-len(self.j[satr][ustun]))*b
                    print(f"{c} {bj}{self.j[satr][ustun]} ",end="")
                print(c)
                
            print(p,end="")
            for ch in range(len(self.j[0])):
                bj=(max_uslar[ch]+2)*m
                print(f"{bj}",end=p)
            print("")
            """"DELL ID"""
            # for satr in range(len(self.j)):
            #     del self.j[satr][0]


    def sumcolumn(self,n,nom=0):
        if nom == 0:
            for satr in range(len(self.j)):
                if satr == 0:
                    continue
                else:
                    self.j[satr][n-1] = int(self.j[satr][n-1])
            s = 0
            for satr in range(len(self.j)):
                if satr == 0:
                    continue
                else:
                    s = s + self.j[satr][n-1]
            for satr in range(len(self.j)):
                if satr == 0:
                    continue
                else:
                    self.j[satr][n-1] = str(self.j[satr][n-1])
        elif nom == 1:
            for satr in range(len(self.j)):
                self.j[satr][n-1] = int(self.j[satr][n-1])
            s = 0
            for satr in range(len(self.j)):
                s = s + self.j[satr][n-1]
            for satr in range(len(self.j)):
                self.j[satr][n-1] = str(self.j[satr][n-1])
        return s


    def sumrow(self,n,nom = 0):
        if nom == 0:
            for ustun in range(len(self.j[n-1])):                
                if ustun == 0:
                    continue
                else:
                    self.j[n-1][ustun] = int(self.j[n-1][ustun])
            
            s = 0
            for ustun in range(len(self.j[n-1])):
                if ustun == 0:
                    continue
                else:
                    s = s + self.j[n-1][ustun]
            for ustun in range(len(self.j[n-1])):
                if ustun == 0:
                    continue
                else:
                    self.j[n-1][ustun] = str(self.j[n-1][ustun])
                
        elif nom == 1:
            for ustun in range(len(self.j[n-1])):
                self.j[n-1][ustun] = int(self.j[n-1][ustun])
            
            s = 0
            for ustun in range(len(self.j[n-1])):
                s = s + self.j[n-1][ustun]
            for ustun in range(len(self.j[n-1])):
                self.j[n-1][ustun] = str(self.j[n-1][ustun])
        return s

    def addcolumn(self,n):
        for satr in range(len(self.j)):
            self.j[satr].insert(n-1,"None")

    def delcolumn(self,m):
        
        for satr in range(len(self.j)):
            del self.j[satr][m-1] 
    
    def addrow(self,n):
        u = []
        for ustun in range(len(self.j[0])):
            e = input(f" {ustun+1} - ustunni kiriting: ")
            u.append(e)
        self.j.insert(n-1,u)
    
    def delrow(self,n):
        del self.j[n-1]

    def reverse(self):
        v = []
        for ustun in range(len(self.j[0])):
            s = []
            for satr in range(len(self.j)):
                s.append(self.j[satr][ustun])
            v.append(s)
        
        del self.j[:]
            
        for satr in range(len(v)):
            self.j.append(v[satr])

    def value(self,satr,ustun):
        val = input(" Ma'lumot kiriting: ")
        self.j[satr-1][ustun-1] = val

jt = TABLE(j)



jt.showtable(1,0)












