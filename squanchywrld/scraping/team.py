"""
the purpose of this classes is to pic the first team and the second team
"""
from object_main import ObjecMain

class Team(ObjecMain):
    _selectors = [
        '#content > div:nth-child(9) > div:nth-child(7) > div:nth-child(1) > table:nth-child(1)',
        '#content > table:nth-child(6)'
    ]
    
    
    def __init__(self, url):
        self._soup = None

        for selector in self._selectors:
            
            super().__init__(url, selector)
            
            if self._new_part:
                self._soup = self._new_part[0]
                break

        if self._soup is None:
            raise ValueError("Nenhum dado encontrado com os seletores fornecidos.")


        self.teams_names = self._new_part[0].find("h1").text

        self._values = self.teams_names.split("vs")
        self._home = self._values[0]
        self._away = self._values[-1]
        

    def get_home(self):
        
        return str(self._home).strip()
    

    def get_away(self):

        return str(self._away).strip()
       
      
        