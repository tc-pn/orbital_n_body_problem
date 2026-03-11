"""
L'objet de ce module est de définir la classe Etude,
qui correspondra dans ce projet à un ensemble de planètes, de soleils etc
"""
from typing import Any

from PhysicalObject import PhysicalObject
from PhysicalResults.PhysicalResultsBuilder import PhysicalResultsBuilder

# est qu'au final je ferai pas une initialisation en passant par un dictionnaire d'enrée du format {nom object : {grandeur : valeur}} ? 
# je peux garder le retraitement pour faire des listes mais d'un pov utilisateur je pense que c'est plus simple
class Etude():
    def __init__(self,
                 l_name_physical_object : list[str],
                 l_masses : list[float],
                 l_coordinates : list[tuple[float, float]],
                 l_velocities : list[tuple[float, float]]):
        self.nbr_physical_objects = len(l_name_physical_object)
        self.l_name_physical_object = l_name_physical_object
        self.l_masses = l_masses
        self.l_coordinates = l_coordinates
        self.l_velocities = l_velocities

        for li in [self.l_velocities, self.l_coordinates, self.l_masses]:
            if len(li) != self.nbr_physical_objects:
                raise ValueError(f"{len(li)} != {self.nbr_physical_objects}")

        self.d_physical_objects = self._construct_physical_objects()

    def _construct_physical_objects(self) -> dict[str,PhysicalObject]:
        """
        Instancie les objets physiques de l'étude
        
        :param self: Description
        :return: Description
        :rtype: list[PhysicalObject]
        """
        return {self.l_name_physical_object[i] : PhysicalObject(mass=self.l_masses[i],
                                                                coordinates=self.l_coordinates[i],
                                                                velocities=self.l_velocities[i],
                                                                name=self.l_name_physical_object[i]) 
                for i in range(len(self.l_name_physical_object))}
    
    def get_names_physical_objects(self) -> list[str]:
        return list(self.d_physical_objects)
    
    def get_physical_results(self,
                             l_user_results : list[str]) -> dict[str, Any]:
        """
        Appelle la classe PhysicalResultsBuilder permettant de construire 
        les résultats physiques demandés par l'utilisateur 
        
        :param self: Description
        :return: Description
        :rtype: dict[str, Any]
        """
        return PhysicalResultsBuilder(code_supervisor=self,
                                      l_user_results=l_user_results,
                                      l_velocities=self.l_velocities,
                                      l_coordinates=self.l_coordinates,
                                      l_mass=self.l_masses).get_results()

    
