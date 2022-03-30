# Ejercicios_AgregacionyDescomposicion_POO
Este es el link del [repositorio]:https://github.com/guerramorantemiguel/Ejercicios_AgregacionyDescomposicion_POO.git

# Ejercicio 1:
UML: ![Ejercicio_1_AyC](https://user-images.githubusercontent.com/100090620/160115007-da23143e-d60a-4b0e-9f8f-000f30df617e.PNG)

```
class Empresa:
  def __del__(self, edificios, empleados, nombre):
    self.edificios = []
    self.empleados = []
    self.nombre = []
class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
class Edificio:
  def __init__(self):
    self.empresa = None
edificios = [edificios() for i in range(3)]    
empresa = Empresa()
empresa.edificios = edificios
for Edificio in edificios: 
    Edificio.empresa = empresa
  
class NuevaYork: 
 
    def __del__(self): 
        print("Nueva York ha sido destruida por el cataclismo, así como los edificios A y B") 
```

# Ejercicio 2:

```
class Yin: 
  pass 
class Yang: 
    def __delete__(self): 
        print("Yang destruido") 
```

# Ejercicio 3:
```
class Pared: 
  def __init__(self, orientacion):
      self.orientacion = orientacion
class Ventana:
    def __init__(self, orientacion, superficie):
      super().__init__(orientacion)
      self.superficie = superficie
class Casa:
    def __init__(self, paredes, orientacion, superficie):
        self.paredes = paredes
    def SuperficieAcristalada(self):
        return(self.paredes.superficie)
```

# Main:
```
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
```
