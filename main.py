from Ejercicio_1 import Ejercicio_1
from Ejercicio_2 import Ejercicio_2
from Ejercicio_3 import Ejercicio_3

def main():
  while True:
    Ejercicio = input("Número del ejercicio que quiera iniciar")
    if Ejercicio == Ejercicio_1:
      ciudad = input("¿Que ciudad va a destruir?")
      if ciudad == Nueva_York:
        print("Nueva York ha sido destruida, así como los edificios A y B")
      if ciudad == Los_Angeles:
        print("No ha habido cataclismo en Los Ángeles")
    if Ejercicio == Ejercicio_2:
      yin = Yin() 
      yang = Yang() 
      yin.yang = yang 
      print(yang is yin.yang)
      del(yang)
      del(yin.yang)
      print(yang)