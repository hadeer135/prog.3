class ComplexGenetics(object):
   def __init__(self):
      pass
   
   def genes(self, gene_code):
      return 'ComplexPatter[%s]TooHugeinSize' % (gene_code)
class Families(object):
   family = {}
   
   def __new__(cls, name, family_id):
      try:
         id = cls.family[family_id]
      except KeyError:
         id = object.__new__(cls)
         cls.family[family_id] = id
      return id
   
   def set_genetic_info(self, genetic_info):
      cg = ComplexGenetics()
      self.genetic_info = cg.genes(genetic_info)
   
   def get_genetic_info(self):
      return (self.genetic_info)

def test():
   data = (('a', 1, 'ATAG'), ('a', 2, 'AAGT'), ('b', 1, 'ATAG'))
   family_objects = []
   for i in data:
      obj = Families(i[0], i[1])
      obj.set_genetic_info(i[2])
      family_objects.append(obj)
   
   for i in family_objects:
      print ("id = " + str(id(i)))
      print (i.get_genetic_info())
   print ("similar id's says that they are same objects ")

if __name__ == '__main__':
   test()

##########################################################################
class first_trucks(object): 
    #class for trucks
    def __init__(self): 
        pass
    def trucks(self, trucks_name): 
        return "Flyweightpattern[% s]" % (trucks_name) 
class trucksKingdom(object): 
    trucks_family = {}     #This stores ids of trucks
    def __new__(cls,name, trucks_family_ident): 
        try: 
            id = cls.trucks_family[trucks_family_ident] 
        except KeyError: 
            id = object.__new__(cls) 
            cls.trucks_family[trucks_family_ident] = id
        return id
    def set_trucks_info(self, trucks_info):
        #feed the  trucks info
        bc = first_trucks() 
        self.trucks_info=bc.trucks(trucks_info)
    def get_trucks_info(self): 
        #return the available trucks info
        return (self.trucks_info) 
if __name__ == '__main__': 
    trucks_data = (('a', 1, 'Red'), ('a', 2, 'Yellow'), ('b', 2, 'Blur')) 
    trucks_family_objects = [] 
    for i in trucks_data: 
        item = trucksKingdom(i[0], i[1]) 
        item.set_trucks_info(i[2]) 
        trucks_family_objects.append(item)  
#If id same than they are having same objects
    for i in trucks_family_objects: 
        print(" id = " + str(id(i))) 
        print(i.get_trucks_info())