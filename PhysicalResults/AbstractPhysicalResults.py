"""
L'objet de ce module est de définir la classe AbstractPhysicalResults, 
qui contiendra un template de base de classe PhysicalResultsBuilder 
qui sera hérité par de futures classes
"""
class AbstractPhysicalResults():
    def __init__(self,
                 code_supervisor,
                 l_user_results : list[str],
                 l_velocities : list[tuple[float]],
                 l_coordinates : list[tuple[float]],
                 l_mass : list[float]):
        self.code_supervisor = code_supervisor
        self.l_user_results = l_user_results
        self.l_velocities = l_velocities
        self.l_coordinates = l_coordinates
        self.l_mass = l_mass
        self.args = [self.l_velocities, self.l_coordinates, self.l_mass]

    @classmethod
    def name(cls):
        return "AbstractPhysicalResults"
    
class AbstractBuilder():
    def __init__(self,
                 code_supervisor,
                 l_velocities : list[tuple[float]],
                 l_coordinates : list[tuple[float]],
                 l_mass : list[float]):
        self.code_supervisor = code_supervisor
        self.l_velocities = l_velocities
        self.l_coordinates = l_coordinates
        self.l_mass = l_mass
        self.args = [self.l_velocities, self.l_coordinates, self.l_mass]

    @classmethod
    def name(cls):
        return "AbstractBuilder"