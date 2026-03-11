"""
L'objet de ce module est de définir la classe PhysicalResultsVerificator, 
qui permet de vérifier la disponibilité du résultat demandé par l'utilisateur
"""
import inspect
import sys 

class PhysicalResultsVerificator():
    def __init__(self,
                 l_user_results : list[str]):
        self.l_user_results = l_user_results

    @classmethod
    def name(cls):
        return "PhysicalResultsVerificator"

    def verif(self):
        classes_names = [cls_obj.name()
                         for cls_name, cls_obj 
                         in inspect.getmembers(sys.modules['PhysicalResults.ToolResults']) 
                         if inspect.isclass(cls_obj) 
                         and "__" not in cls_name 
                         and not all(letter.isupper() for letter in cls_name)
                         and not any(letter.isupper() for letter in cls_obj.name())]
        if any(user_results not in classes_names for user_results in self.l_user_results):
            raise ValueError(f"Au moins un des résultats demandés par l'utilisateur n'est pas présent parmis la liste des résultats possibles {classes_names}")
