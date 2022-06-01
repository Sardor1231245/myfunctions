

class TABLE:
    
    def __init__(self,jadval):
        self.j = jadval
    
    def showtablem(self):

        b = " "
        p = "+"
        c = "|"
        m = "-"
        max_uslar=[]
        
        for satr in range(len(self.j)):
            idd = satr+1
            self.j[satr].insert(0,str(idd))
            for ustun in range(len(self.j[satr])):
                self.j[satr][ustun]=str(self.j[satr][ustun])
        
        for ustun in range(len(self.j[1])):
            us = []
            for satr in range(len(self.j)):
                e = len(self.j[satr][ustun])
                us.append(e)
            max_us = max(us)
            max_uslar.append(max_us)
            
        print(p,end="")
        for ch in range(len(self.j[0])):
            bj=(max_uslar[ch]+2)*m
            print(f"{bj}",end=p)
        print("")
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
            
        for satr in range(len(self.j)):
            del self.j[satr][0]
      
    def showtable(self):
        b = " "
        p = "+"
        c = "|"
        m = "-"
        max_uslar=[]
        
        for satr in range(len(self.j)):
            idd = satr+1
            self.j[satr].insert(0,str(idd))
            for ustun in range(len(self.j[satr])):
                self.j[satr][ustun]=str(self.j[satr][ustun])
        
        for ustun in range(len(self.j[1])):
            us = []
            for satr in range(len(self.j)):
                e = len(self.j[satr][ustun])
                us.append(e)
            max_us = max(us)
            max_uslar.append(max_us)
            
    
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
    
        for satr in range(len(self.j)):
            del self.j[satr][0]














