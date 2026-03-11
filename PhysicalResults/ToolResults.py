"""
L'objet de ce module est de définir les classes Builder, 
qui permettent de construire les résultats demandés par l'utilisateur
"""
import numpy as np
import itertools 

from PhysicalResults.AbstractPhysicalResults import AbstractBuilder
GRAVITATIONAL_CONSTANT = 0.01720209895 # au**3/2 / day * solar mass ** -1/2

class KineticEnergyBuilder(AbstractBuilder):
    """Classe permettant de calculer l'énergie cinétique des PhysicalObject

    Args:)
        PhysicalPropertiesContainer (PhysicalPropertiesContainer):
            Classe permettant de stocker les attributs élémentaires d'un PhysicalObject (l_coordinates, l_velocities, l_mass)
    """
    def __init__(self, code_supervisor, l_velocities, l_coordinates, l_mass):
        super().__init__(code_supervisor, l_velocities, l_coordinates, l_mass)

    @classmethod
    def name(cls) -> str:
        return "kinetic_energy" 

    def result(self) -> dict[str,float]:
        l_names = self.code_supervisor.get_names_physical_objects() 
        return {name : 0.5 * mass * np.sum(np.array(velocities)**2.)
                for name, mass, velocities in zip(l_names, self.l_mass, self.l_velocities)}

class TotalKineticEnergyBuilder(AbstractBuilder):
    def __init__(self, code_supervisor, l_velocities, l_coordinates, l_mass):
        super().__init__(code_supervisor, l_velocities, l_coordinates, l_mass)

    def result(self) -> float:
        return np.sum(list(KineticEnergyBuilder(code_supervisor=self.code_supervisor,
                                                l_velocities=self.l_velocities,
                                                l_coordinates=self.l_coordinates,
                                                l_mass=self.l_mass).result().values()))
    
    @classmethod
    def name(cls) -> str:
        return "total_kinetic_energy"

class PotentialEnergyBuilder(AbstractBuilder):
    """Classe permettant de calculer l'énergie potentielle entre les PhysicalObject

    Args:
        AbstractBuilder (AbstractBuilder):
            Classe permettant de stocker les attributs élémentaires d'un PhysicalObject (l_coordinates, l_velocities, l_mass)
    """
    def __init__(self, code_supervisor, l_velocities, l_coordinates, l_mass):
        super().__init__(code_supervisor, l_velocities, l_coordinates, l_mass)

    @classmethod
    def name(cls) -> str:
        return "potential_energy" 

    def result(self) -> dict[str,float]:
        """
        dans l'idéal, il faudrait le produit cartésien des tuples de coordonnées puis faire une liste d'énergies potentielles dessus
        """
        #arr_coor = np.transpose(np.array(self.l_coordinates)) # rassembler les coordonnées de chaque dimensions ensemble
        # il faut mtn construire les combinaisons possibles de coordonnées à soustraire deux à deux pour chaque dimension
        #coor_combinaison = np.array([list(itertools.combinations(r=2, iterable=dim_coor)) for dim_coor in arr_coor])
        #l_differences = []
        #for num_dim in range(np.shape(coor_combinaison)[0]):
        #    l_differences.append([pos1**2. - pos2**2. for pos1, pos2 in coor_combinaison[num_dim]])
        #l_denominators = np.sum(l_differences, axis=0)

        #l_numerators = [- GRAVITATIONAL_CONSTANT  * np.prod(mass_combi) 
        #                for mass_combi in itertools.combinations(iterable=self.l_mass, r=2)]

        #d = {}
        #l_names = self.code_supervisor.get_names_physical_objects()
        #for i, numerator, denomitor in enumerate(zip(l_numerators, l_denominators)):
        #    d[l_names[i]] = numerator / denomitor
        nbr_physical_objects = len(self.l_coordinates)
        arr_coordinates = np.array(self.l_coordinates)
        d_out = {
            f'{name1}_{name2}' : 0. 
            for name1, name2 in itertools.combinations(self.code_supervisor.l_name_physical_object,
                                                       r=2)
            }

        for i in range(nbr_physical_objects):
            for j in range(nbr_physical_objects):
                name1 = self.code_supervisor.l_name_physical_object[i]
                name2 = self.code_supervisor.l_name_physical_object[j]
                if i == j:
                    continue

                num = - GRAVITATIONAL_CONSTANT * self.l_mass[i] * self.l_mass[j]
                den = np.sqrt(np.abs(np.sum(arr_coordinates[i]**2. - arr_coordinates[j]**2.)))
                d_out[f'{name1}_{name2}'] =  num / den
        return d_out
    
class TotalPotentialEnergyBuilder(AbstractBuilder):
    def __init__(self, code_supervisor, l_velocities, l_coordinates, l_mass):
        super().__init__(code_supervisor, l_velocities, l_coordinates, l_mass)

    def result(self) -> float:
        d_pot = PotentialEnergyBuilder(code_supervisor=self.code_supervisor, 
                                       l_velocities=self.l_velocities, 
                                       l_coordinates=self.l_coordinates,
                                       l_mass=self.l_mass).result()
        pot_total = 0.
        for name1, name2 in itertools.combinations(self.code_supervisor.l_name_physical_object,
                                                   r=2):
            pot_total += d_pot[f'{name1}_{name2}']
        return pot_total
    
    @classmethod
    def name(cls) -> str:
        return "total_potential_energy"
    
class TotalMechanicalEnergyBuilder(AbstractBuilder):
    def __init__(self, code_supervisor, l_velocities, l_coordinates, l_mass):
        super().__init__(code_supervisor, l_velocities, l_coordinates, l_mass)

    def result(self) -> float:
        
        return TotalKineticEnergyBuilder(code_supervisor=self.code_supervisor, 
                                         l_velocities=self.l_velocities, 
                                         l_coordinates=self.l_coordinates,
                                         l_mass=self.l_mass).result() \
                + TotalPotentialEnergyBuilder(code_supervisor=self.code_supervisor, 
                                              l_velocities=self.l_velocities, 
                                              l_coordinates=self.l_coordinates,
                                              l_mass=self.l_mass).result()
    
    @classmethod
    def name(cls) -> str:
        return "total_mechanical_energy"




    
