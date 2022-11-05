from Modelos.Resultados import Resultados
from Modelos.Mesa import Mesa
from Modelos.Partido import Partido
from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioPartido import RepositorioPartido

class ControladorResultados():
    def __init__(self):
        self.repositorioResultados = RepositorioResultados()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioPartido = RepositorioPartido()
    def index(self):
        return self.repositorioResultados.findAll()
    """
    Asignacion Mesa y Partido
    """
    def create(self,infoResultados,id_mesa,id_partido):
        nuevoResultados = Resultados(infoResultados)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elPartido = Partido(self.repositorioPartido.findById(id_partido))
        nuevoResultados.mesa=laMesa
        nuevoResultados.partido=elPartido
        return self.repositorioResultados.save(nuevoResultados)
    def show(self,id):
        elResultados = Resultados(self.repositorioResultados.findById(id))
        return elResultados.__dict__
    """
    Modificación de Resultados (Mesa y Partido)
    """
    def update(self,id,id_mesa,id_partido):
        losResultados = Resultados(self.repositorioResultados.findById(id))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elPartido = Partido(self.repositorioPartido.findById(id_partido))
        losResultados.mesa = laMesa
        losResultados.partido = elPartido
        return self.repositorioResultados.save(losResultados)
    def delete(self, id):
        return self.repositorioResultados