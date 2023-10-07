'''class shape:
    def __init__(self,x,y):
      self.x=x 
      self.y=y
    def area(self):
       return self.x*self.y
class circle(shape):
    def __init__(self,redius):
       self.redius=redius
       super().__init__(redius,redius)
    def area(self):
    # return 3.14*self.redius*self.redius
       return 3.14*super().area()


rectangle=shape(5,6)
print(rectangle.area())

c=circle(5)
print(c.area())
    

'''

# the another example  of  method  overriding
class shape:
   def __init__(self,l,w):
        self.l=l
        self.w=w
   def perimeter(self):
         return 2*(self.l+self.w)
class rectangle(shape):
      def __init__(self, l, w):
          super().__init__(l,w)
      def perimeter(self):
           return super().perimeter()
      
st1=rectangle(12,10)
# print(rectangle)
print(st1.perimeter())