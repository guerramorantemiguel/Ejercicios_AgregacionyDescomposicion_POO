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