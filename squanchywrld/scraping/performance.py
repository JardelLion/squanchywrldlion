from scraping.object_main import ObjecMain

class Performance(ObjecMain):

    """
    Home vs Away distribution
    """
    _selectors = [
        '#content > div:nth-child(9) > div:nth-child(7) > div:nth-child(2) > table:nth-child(96)'
    ]
    # model performance
    
    def __init__(self, url):
        
        self._soup = None
        for selector in self._selectors:

            super().__init__(url, selector)
            if self._new_part:
                self._soup = self._new_part[0]
                break

        if self._soup is None:
            raise ValueError("Nenhum dado encontrado com os seletores fornecidos.")



    
    @property
    def get_home_points(self):
        tr = self._soup.find_all('tr')[0]

        td = str(tr.find('td').text).strip()

        return td[:-1]
    
    @property
    def get_home_scored(self):
        tr = self._soup.find_all('tr')[1]

        td = str(tr.find('td').text).strip()

        return td[:-1]
    
    @property
    def get_home_conceded(self):
        tr = self._soup.find_all('tr')[2]

        td = str(tr.find('td').text).strip()

        return td[-1]

     
    @property
    def get_away_points(self):
        tr = self._soup.find_all('tr')[0]

        td = str(tr.find_all('td')[-1].text).strip()

        return td[:-1]
    
    @property
    def get_away_scored(self):
        tr = self._soup.find_all('tr')[1]

        td = str(tr.find_all('td')[-1].text).strip()

        return td[:-1]
    
    @property
    def get_away_conceded(self):
        tr = self._soup.find_all('tr')[2]

        td = str(tr.find_all('td')[-1].text).strip()

        return td[:-1]
  

        