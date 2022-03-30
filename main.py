from Ejercicio_1 import 
from Ejercicio_2 import 
from Ejercicio_3 import 

def main():
  while True:
    

yin = Yin() 
yang = Yang() 
yin.yang = yang 
print(yang is yin.yang)
del(yang)
del(yin.yang)
print(yang)