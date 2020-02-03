class Gsearch_python:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      count = 0
      try :
         from googlesearch import search
      except ImportError:
         print("No Module named 'google' Found")
      for i in search(query=self.name,tld='com',lang='en',stop=4,pause=2):
         count += 1
         print (count)
         print(i + '\n')
if __name__=='__main__':
   c = input()
   gs = Gsearch_python(c)
   gs.Gsearch()