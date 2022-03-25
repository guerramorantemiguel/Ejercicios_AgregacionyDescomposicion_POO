class Empresa:
  def __del__(self):
    self.edificios = []
class Edificio:
  def __init__(self):
    self.empresa = None
edificios = [edificios() for i in range(3)]    
empresa = Empresa()
empresa.edificios = edificios

    