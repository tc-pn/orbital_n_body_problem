from Etude import Etude

import numpy as np

l_name_physical_object = ["Sun", "Earth", "Uranus", "Venus"]
l_masses = [1., 3.00274e-6, 4.36430044e-5, 2.447e-6] # solar mases
l_coordinates = [(0.,0.), (1.,0.), (19.194, 0.0), (0.728, 0.0)] # A.U., here the aaverage distances are used for simplicity
l_velocities = [(0.,0.), (0., 2. * np.pi), (0., 1.435), (0., 7.389)]

etude = Etude(l_name_physical_object=l_name_physical_object,
              l_masses=l_masses,
              l_coordinates=l_coordinates,
              l_velocities=l_velocities)

out = etude.get_physical_results(l_user_results=["kinetic_energy", 
                                                 "total_kinetic_energy", 
                                                 "potential_energy",
                                                 "total_potential_energy",
                                                 "total_mechanical_energy"])