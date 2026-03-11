"""
L'objet de ce module est de définir la classe physical_object, qui correspondra dans ce projet à un planète, un soleil, etc
"""
class PhysicalObject():
    """
    Dans un premier temps, les calculs seront fait avec un 
    """
    def __init__(self, 
                 mass : float,
                 coordinates : tuple[float, float],
                 velocities : tuple[float, float],
                 name : str):
        self.mass = mass
        self.coordinates = coordinates
        self.velocities = velocities
        self.physical_name = name

    @classmethod
    def name(cls) -> str:
        return "PhysicalObject"

    def object_name(self) -> str:
        return self.physical_name

    


