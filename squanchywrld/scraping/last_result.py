from scraping.object_main import ObjecMain

class LastResult(ObjecMain):

    _selectors = [
        '#content > div:nth-child(9) > div:nth-child(7) > div:nth-child(1) > div:nth-child(2) > table:nth-child(9)'
        ,'#content > div:nth-child(11) > div:nth-child(7) > div:nth-child(1) > div:nth-child(2) > table:nth-child(9)'
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

    
        tr = self._soup.find_all('tr') # table row

        self._home_data_object = []
        self._away_data_object = []

        for index in range(0, len(tr)):

            data_home = str(tr[index].find_all('td')[0].text).strip() # table data
            game_home = str(tr[index].find_all('td')[1].text).strip() # table data
            results_home = tr[index].find_all('td')[2].find_all("font") # table data

            main_result_home = results_home[0].text


            data_away = str(tr[index].find_all('td')[6].text).strip() # table data
            game_away = str(tr[index].find_all('td')[5].text).strip() # table data
            results_away = tr[index].find_all('td')[4].find_all("font") # table data

            main_result_away = results_away[0].text


            self._home_data_object.append({
                'data': data_home,
                'game': game_home,
                'result': main_result_home,
                'moments': [

                ]
                
            })

            self._away_data_object.append({
                'data': data_away,
                'game': game_away,
                'result': main_result_away,
                'moments': [

                ]
            })

            # home
            self._get_data_lastestREsult(results_home, data_object=self._home_data_object[index])
            # away
            self._get_data_lastestREsult(results_away, data_object=self._away_data_object[index])




    def _get_data_lastestREsult(self, results, data_object):
        
        if len(results) > 1:
            for font in results:
                try:
                    index_by_char = font.find("font").text.find("(")
                    data_object['moments'].append(
                        {"time":str(font.find("font").text[index_by_char + 1:-1]).strip(),
                         "goal": str(font.find("b").text).strip(),
                         "who_scored":str(font.find("font").text[0:index_by_char]).strip()
                        }
                    )
                except :
                    pass
        

    @property
    def get_home(self):
        return self._home_data_object
    

    @property
    def get_away(self):
        return self._away_data_object

