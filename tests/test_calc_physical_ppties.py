from Etude import Etude

import numpy as np
# The tested quantities are for the moment expressed in Solar masses * AU**2 / years**2
# kinetic energy
EARTH_KINETIC = 5.927171183865412e-05
# potential energy
EARTH_SUN_POTENTIAL = -5.1653430601123e-08
# total potential energy
POTENTIAL = -9.076740046361878e-08
# total mechanical enregy
TOTAL_MECHANICAL_ENERGY = 0.0001041163273059855

def test_calc_physical_ppties():
    l_name_physical_object = ["Sun", "Earth", "Uranus"]
    l_masses = [1., 3.00274e-6, 4.36430044e-5] # solar mases
    l_coordinates = [(0.,0.), (1.,0.), (19.194, 0.0)] # A.U., here the average distances are used for simplicity
    l_velocities = [(0.,0.), (0., 2. * np.pi), (0., 1.435)]

    etude = Etude(l_name_physical_object=l_name_physical_object,
                l_masses=l_masses,
                l_coordinates=l_coordinates,
                l_velocities=l_velocities)

    out = etude.get_physical_results(l_user_results=["kinetic_energy", 
                                                    "total_kinetic_energy", 
                                                    "potential_energy",
                                                    "total_potential_energy",
                                                    "total_mechanical_energy"])
    assert out["kinetic_energy"]["Earth"] == EARTH_KINETIC
    assert out["potential_energy"]['Earth_Sun'] == EARTH_SUN_POTENTIAL
    assert out["total_potential_energy"] == POTENTIAL
    assert out["total_mechanical_energy"] == TOTAL_MECHANICAL_ENERGY
    
    
