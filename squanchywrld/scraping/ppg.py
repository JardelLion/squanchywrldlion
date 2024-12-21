from object_main import ObjecMain


class PPG(ObjecMain):
    _selectors = ['#content > div:nth-child(9) > div:nth-child(7) > div:nth-child(1) > div:nth-child(2) > table:nth-child(12)',
    '#content > div:nth-child(11) > div:nth-child(7) > div:nth-child(1) > div:nth-child(2) > table:nth-child(12)'
    
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

    
        
        


    def get_table_ppg(self):
        
        table = self._new_part[0].find_all('table')[1]


        table_row_first = table.find('tr')
        table_row_second = table.find_all("tr")[-2]

        home_ppg = table_row_first.find_all("td")[1].text
        away_ppg = table_row_first.find_all('td')[-2].text

        total_home_ppg = table_row_second.find_all("td")[1].text
        total_away_ppg = table_row_second.find_all('td')[-2].text


        try:
            home_ppg = float(home_ppg)
            away_ppg = float(away_ppg)

            total_home_ppg = float(total_home_ppg)
            total_away_ppg = float(total_away_ppg)

        except:
            print("Can't convert value into float please check the ppg table")
        
        objec_values = {
            'home_ppg': home_ppg,
            "away_ppg": away_ppg,
            "home_total_ppg": total_home_ppg,
            'away_total_ppg': total_away_ppg
        }
        
        return objec_values
    
    @property
    def get_home_ppg(self):
        home = self.get_table_ppg()


        return home['home_ppg']
    
    @property
    def get_away_ppg(self):
        away = self.get_table_ppg()

        return away['away_ppg']
    

    @property
    def get_home_total_ppg(self):
        home_total = self.get_table_ppg()

        return home_total['home_total_ppg']
    
    @property
    def get_away_total_ppg(self):
        away_total_ppg = self.get_table_ppg()

        return away_total_ppg['away_total_ppg']
    


class PPGPoints(ObjecMain):

    _selectors = [
       # '#content > div:nth-child(9) > div:nth-child(7) > div:nth-child(1) > div:nth-child(2) > table:nth-child(12) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(3)',
        '#content > div:nth-child(11) > div:nth-child(7) > div:nth-child(1) > div:nth-child(2) > table:nth-child(12) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(3)'
        
    ]
    def __init__(self, url):
        self._soup = None
        self._table_row_first = None
        self._table_row_second = None

        for selector in self._selectors:
            try:
                # Chama o método da classe pai para realizar a extração do conteúdo
                super().__init__(url, selector)
                
                # Se o conteúdo foi encontrado, tenta acessar as linhas da tabela
                if self._new_part:
                    rows = self._new_part[0].find_all("tr")
                    
                    # Verifica se o número esperado de linhas está presente
                    if len(rows) > 2:
                        self._table_row_first = rows[1]  # Linha 1
                        self._table_row_second = rows[2]  # Linha 2
                    else:
                        raise ValueError("Número insuficiente de linhas na tabela.")
                    
                    break  # Se o conteúdo foi encontrado, sai do laço de seletores
                else:
                    raise ValueError("Nenhum dado encontrado com o seletor fornecido.")
            except Exception as e:
                # Trata erros na execução da extração ou na manipulação da estrutura
                print(f"Erro ao processar seletor {selector}: {e}")
                continue

        # Se nenhum dado válido for encontrado, lança uma exceção
        if self._table_row_first is None or self._table_row_second is None:
            raise ValueError("Nenhum dado encontrado com os seletores fornecidos.")

        
    def _get_table_ppg_points(self, table_row_soup):
        """
            table_row_soup is the new part[0] table based on 
            - self._table_row_first
            - self._table_row_second
        """

        table_data_first = table_row_soup.find_all("td")

        object_values_home = {
            "home_gp": table_data_first[1].text,
            'home_win': table_data_first[2].text,
            'home_draw':table_data_first[3].text,
            'home_lose': table_data_first[4].text

        }

        object_values_away = {
            "away_gp": table_data_first[9].text,
            'away_win':table_data_first[6].text,
            'away_draw': table_data_first[7].text,
            'away_lose': table_data_first[8].text 
        }
       
        return [object_values_home, object_values_away]


    @property
    def get_home_point_gp(self):
        values = self._get_table_ppg_points(self._table_row_first)
       

        return values[0]['home_gp']
    
    @property
    def get_home_point_win(self):
        values = self._get_table_ppg_points(self._table_row_first)

        return values[0]['home_win']
    
    @property
    def get_home_point_draw(self):
        values = self._get_table_ppg_points(self._table_row_first)

        return values[0]['home_draw']
    
    @property
    def get_home_point_lose(self):
        values = self._get_table_ppg_points(self._table_row_first)

        return values[0]['home_lose']
    

    @property
    def get_away_point_gp(self):
        values = self._get_table_ppg_points(self._table_row_first)
       

        return values[-1]['away_gp']
    
    @property
    def get_away_point_win(self):
        values = self._get_table_ppg_points(self._table_row_first)

        return values[-1]['away_win']
    
    @property
    def get_away_point_draw(self):
        values = self._get_table_ppg_points(self._table_row_first)

        return values[-1]['away_draw']
    
    @property
    def get_away_point_lose(self):
        values = self._get_table_ppg_points(self._table_row_first)

        return values[-1]['away_lose']
    

    # point per game total based on gp, w, d, l, 


    @property
    def get_home_point_gp_total(self):
        values = self._get_table_ppg_points(self._table_row_second)
       

        return values[0]['home_gp']
    
    @property
    def get_home_point_win_total(self):
        values = self._get_table_ppg_points(self._table_row_second)

        return values[0]['home_win']
    
    @property
    def get_home_point_draw_total(self):
        values = self._get_table_ppg_points(self._table_row_second)

        return values[0]['home_draw']
    
    @property
    def get_home_point_lose_total(self):
        values = self._get_table_ppg_points(self._table_row_second)

        return values[0]['home_lose']
    

    @property
    def get_away_point_gp_total(self):
        values = self._get_table_ppg_points(self._table_row_second)
       

        return values[-1]['away_gp']
    
    @property
    def get_away_point_win_total(self):
        values = self._get_table_ppg_points(self._table_row_second)

        return values[-1]['away_win']
    
    @property
    def get_away_point_draw_total(self):
        values = self._get_table_ppg_points(self._table_row_second)

        return values[-1]['away_draw']
    
    @property
    def get_away_point_lose_total(self):
        values = self._get_table_ppg_points(self._table_row_second)

        return values[-1]['away_lose']
    






if __name__ == "__main__":
    url = 'file:///home/jardel-lion-studio/Documents/games/octuber/18/Alaves%20vs%20Valladolid%20H2H%20stats%20preview%20and%20analysis,%202024-2025.html'
    
    last_resutl = PPG(url)
    