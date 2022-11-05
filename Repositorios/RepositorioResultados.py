from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultados

from bson import ObjectId

class RepositorioResultados(InterfaceRepositorio[Resultados]):
    def getListadoResultados(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
