from Ejercicio_1 import Ejercicio_1
from Ejercicio_2 import Ejercicio_2
from Ejercicio_3 import Ejercicio_3

def main():
  while True:
    
    

yin = Yin() 
yang = Yang() 
yin.yang = yang 
print(yang is yin.yang)
del(yang)
del(yin.yang)
print(yang)