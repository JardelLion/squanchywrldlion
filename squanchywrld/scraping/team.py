"""
the purpose of this classes is to pic the first team and the second team
"""
from classes.ppg import ObjecMain

class Team(ObjecMain):
    _selector = '#content > div:nth-child(9) > div:nth-child(7) > div:nth-child(1) > table:nth-child(1)'
    def __init__(self, url):
        super().__init__(url, self._selector)

        self.teams_names = str(self._new_part[0].find_all("tr")[2].text)

        self._values = self.teams_names.split("vs")
        self._home = self._values[0]
        self._away = self._values[-1]
        

    def get_home(self):
        
        return self._home
    

    def get_away(self):

        return self._away
       
      
        