"""
L'objet de ce module est de définir la classe PhysicalResultsBuilder, 
qui interprétera les demandes résultats utilisateur
"""
from typing import Union, Any

import inspect
import sys

from PhysicalResults.AbstractPhysicalResults import AbstractPhysicalResults
from PhysicalResults.PhysicalResultsVerificator import PhysicalResultsVerificator
from PhysicalResults import ToolResults

class PhysicalResultsBuilder(AbstractPhysicalResults):
    def __init__(self, code_supervisor, l_user_results, l_velocities, l_coordinates, l_mass):
        super().__init__(code_supervisor=code_supervisor,
                         l_user_results=l_user_results,
                         l_velocities=l_velocities,
                         l_coordinates=l_coordinates,
                         l_mass=l_mass)
        PhysicalResultsVerificator(l_user_results=self.l_user_results).verif()

    @classmethod
    def name(cls):
        return "PhysicalResultsBuilder"
    
    def get_results(self) -> dict[str, Any]:
        return {
            cls_obj.name() : cls_obj(code_supervisor=self.code_supervisor,
                                     l_velocities=self.l_velocities,
                                     l_coordinates=self.l_coordinates,
                                     l_mass=self.l_mass).result() 
                             for cls_name, cls_obj in inspect.getmembers(sys.modules['PhysicalResults.ToolResults'])
                             if inspect.isclass(cls_obj) 
                             and "__" not in cls_name 
                             and not all(letter.isupper() for letter in cls_name)
                             and not any(letter.isupper() for letter in cls_obj.name())
                             and cls_obj.name() in self.l_user_results
        }

    






