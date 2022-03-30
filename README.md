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
