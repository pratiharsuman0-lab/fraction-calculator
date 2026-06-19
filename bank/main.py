class fraction:
    def __init__ (self,x,y):
        self.num=x
        self.dnum=y

    def __str__ (self):
        return '{}/{}'.format (self.num,self.dnum)
        

    def __add__ (self,other):
        new_num=self.num*other.dnum+self.dnum*other.num
        new_dnum=self.dnum*other.dnum   
        return '{}/{}'.format(new_num,new_dnum)
    
    def __sub__(self, other):
        new_num=self.num*other.dnum-self.dnum*other.num
        new_dnum=self.dnum*other.dnum
        return'{}/{}'.format(new_num,new_dnum)
    
    def __mul__(self, other):
        new_num=self.num*other.num
        new_dnum=self.dnum*other.dnum
        return'{}/{}'.format(new_num,new_dnum)
    
    def __truediv__(self, other):
        new_num=self.num*other.dnum
        new_dnum=self.dnum*other.num
        return'{}/{}'.format(new_num,new_dnum)
    

suman=fraction(1,2)
suman1=fraction(2,3)
print((suman+suman1)+suman)