
# coding: utf-8

# In[4]:


#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14
a=int(input("enter radius"))
c1 = Circle(a)
print(c1.area())
print(c1.perimeter())


# In[26]:


#Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 
#1. Display - It should display all informations of the student. 
#2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.
class Student:
    age=19 
    marks=90
    def __init__(self, name, rno):
        self.name = name
        self.rno = rno 
    def display(self):
        print('Name: %s, RollNo: %s,'%(self.name, self.rno), end=' ')
        print('Marks:', self.marks)   
    def setAge(self):
        return self.age
    def setMarks(self,marks):
        self.marks=marks       
s1 = Student('abc', 1)
s1.display()
s2 = Student('efg',2)
s2.display()
s3=Student('xyz',3)
s3.display()
print("Age of 3rd student is:",s3.setAge())
print()


        


# In[14]:


#Q.3- Create a Temprature class and create two methods: 
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class Temp:
    def  convertF(self,celsius):
        return (celsius*(9/5))+32
    def convertC(self,farenhiet):
        return (farenhiet-32)*(5/9)
t=Temp()
c=int(input("enter the temp in celsius"))
print("the temp in farenheit is %s"%(t.convertF(c)))
f=int(input("enter the temp in farenheit"))
print("the temp in celsius is %s"%(t.convertC(f)))


# In[19]:


#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
#Make methods to 
#1. Display-Display the details. 
#2. Add- Add the movie details
class MovieDetails:
    def __init__(self, artistname, release,ratings):
        self.artistname = artistname
        self.release = release
        self.ratings = ratings
    
    def display(self):
        print('Movie details are :: Artist Name: {}, Year of Release: {}, Ratings: {}'.format(self.artistname, self.release,self.ratings), end=' ')

    def add(self,mname):
        self.mname=mname
        print("Name of Movie is:",self.mname)
    
n=input("enter artist name")
y=int(input("enter year of release"))
r=int(input("enter the ratings of movie"))
mname=input("enter the movie name")
m=MovieDetails(n,y,r)
m.display()
m.add(mname)
print()


# In[16]:


#Q.5- Create a class Animal as a base #class and define method animal_attribute. 
#Create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
    def animal_attribute(self,name,atri):
        print(name," has attribute to ",atri)

class Tiger(Animal):
    def show_attribute(self,name,atri):
        self.animal_attribute(name,atri)

T = Tiger()
T.show_attribute("Tiger","roar")


# In[17]:


#Q.6- What will be the output of following code. 
class A:
    def f(self):
         return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print( a.f(), b.f())
print( a.g(), b.g())

#output will be 
#A B
#A B


# In[18]:


#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area. 
#Create class rectangle and square which inherits shape and access the method Area.
class Shape:
    length=int()
    breadth=int()
    def area(self,l,b):
        self.length=l
        self.breadth=b
        return self.length*self.breadth
class Rectangle(Shape):
    def display_area(self):
        l=int(input("Enter length"))
        b=int(input("Enter breadth"))
        print("Area of rectangle: ",self.area(l,b))
class Square(Shape):
    def display_area(self):
        a=int(input("Enter side"))
        print("Area of square: ",self.area(a,a))

r= Rectangle()
r.display_area()
s= Square()
s.display_area()

