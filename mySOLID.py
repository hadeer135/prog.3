# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:29:25 2024

@author: hadee
"""

'''SRP'''
### vaiolates the princible
class book :
    def __init__(self,author,title,content):
        self.author=author
        self.title=title
        self.content=content
        
        
    def get_author(self):
        return self.author
    def get_title(self):
        return self.title
    def get_content(self):
        return self.content
    
    def print_book(self):
        print(f"auther:,{self.get_author()}")  
        print(f"title:,{self.get_title()}")
        print(f"content :,{self.get_content()}")
        
### doesn't vaiolate
class book :
    def __init__(self,author,title,content):
        self.author=author
        self.title=title
        self.content=content
        
        
    def get_author(self):
        return self.author
    def get_title(self):
        return self.title
    def get_content(self):
        return self.content
        
class printer:
    def print_book(self):
        print(f"auther:,{book.get_author()}")  
        print(f"title:,{book.get_title()}")
        print(f"content :,{book.get_content()}")
        
  ################################################

'''OCP'''
### before 
class Student:
    def __init__(self,name:str):
        self.name=name
    def get_name(self)-> str:
        pass
          
students =[
    Student("hadeer"),
    Student("hager")  
    ]
def student_level(students : list):
    for student in students:
        if student.name =="hadeer":
            print("level2")
        elif student.name=="hager":
            print("level4")
student_level(students)
### after 

class Student:
    def __init__(self,name:str):
        self.name=name
    def get_name(self):
        pass
    def get_level(self):
        pass

class Hadeer(Student):
    def get_level(self):
        return"level2"
        
class Hager(Student):
    def get_level(self):
        return"level4"
###############################
''' LSP'''
### BEFORE 



class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calculate_area(self):
        return self.width*self.height
    
class Circle(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    def setter(self,key,value):
        if key in ("width","height"):
            self.__dict__["width"]=value
            self.__dict__["height"]=value
        
        
### after

from abc import ABC,abstractmethod
import math
class shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass
    
class Rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calc_area(self):
        return self.width*self.height
class circle(shape):
     def __init__(self,radious):
         self.radious=radious
     def calc_area(self):
         return math.pi*self.radious**2
     
###################################################
'''ISP'''
 
### before 
class Bird:
    def fly(self):
        pass
    def swim(self):
        pass
    
class Duck(Bird):
    def fly(self):
        raise NotImplementedError
    def swim(self):
        pass
    def quack(self):
        pass
    
class beginun(Bird):
    def fly(self):
        pass
    def swim(self):
        raise NotImplementedError
        
### after 
from abc import ABC,abstractmethod
 
class Bird(ABC):
     @abstractmethod
     def make_sound(self):
         pass
     
class flying_Bird(Bird,ABC):
   @abstractmethod
   def fly(self):
        pass
    
class swimming_Bird(Bird,ABC):
   @abstractmethod
   def swim(self):
        pass
    
class Duck(swimming_Bird):
    def make_sound(self):
        return "quackk"
    
    def swim(self):
        pass
    
class beginun(flying_Bird):
    def make_sound(self):
        return "cooing"
    def fly(self):
        pass
    
    
###########################

'''DIP'''
### before

class pdfReader:
    def __init__(self,file):
        self.file=file
    def read(self):
        pass
    
class documentViewer:
    def __init__(self):
        self.reader=pdfReader(open("document.pdf","rb"))
        
    def view(self):
        self.reader.read()
        
### after 
from abc import ABC,abstractmethod

class documentReader(ABC):
    def read(self):
        pass
class pdfReader(documentReader):
    def __init__(self,file):
        self.file=file
        
    def read(self):
        pass
    
class txtReader(documentReader):
    def __init__(self,file):
        self.file=file
    def read(self):
        pass
    
class documentViewer:
    def __init__(self,reader:documentReader):
        self.reader=reader
        def view(self):
            self.reader.read()
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    