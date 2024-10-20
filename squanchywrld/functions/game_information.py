from scraping.object_main import ObjecMain

class GameInformation(ObjecMain):
    _selector = '#content > div:nth-child(2)'
   
    def __init__(self,url):
        super().__init__(url, self._selector)
        self._soup = self._new_part[0]


    def get_name_league(self):
        """
        get the name league
        """
        
        return str(self._soup.find_all("div")[1].text).strip()






    def get_year(self):
        """
        get the year of the game
        """
        button = self._soup.find_all("div")[2].find("button")

        text = str(button.text)[0:-1]
        
        return text

