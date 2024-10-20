from classes.ppg import ObjecMain

class TeamScoringStast(ObjecMain):
    
    _selector = '#content > div:nth-child(9) > div:nth-child(7) > div:nth-child(2)'

    def __init__(self, url,):
        super().__init__(url, self._selector)


        self._soup = self._new_part[0].find_all("table")


    def _get_data_scoring(self, position):
        
        table = self._soup[position].find_all('tr')[-1]

        td = table.find_all('td')

        team_data = str(td[0].text).strip()
        average_league = str(td[-1].text).strip()

        return {"team": team_data, "average_league": average_league}


    @property
    def get_home_scored_average_obj(self):
        """
            get home score average per match
        """
        values = self._get_data_scoring(2)

        return {"home": values['team'], 'average_league': values['average_league']}
    


    @property
    def get_away_scored_average_obj(self):
        """
            get home score average per match
        """
        values = self._get_data_scoring(5)

        return {"away": values['team'], 'average_league': values['average_league']}
    

    @property
    def get_total_scored_average_obj(self):
        """
            get home score average per match
        """
        values = self._get_data_scoring(8)

        return {"total_scoring": values['team'], 'average_league': values['average_league']}
        

    @property
    def get_home_scoring_rate_obj(self):
        """
            get home score average per match
        """
        values = self._get_data_scoring(11)

        return {"home_scoring": values['team'], 'average_league': values['average_league']}
        

    @property
    def get_away_scoring_rate_obj(self):
        """
            get home score average per match
        """
        values = self._get_data_scoring(14)

        return {"away_scoring": values['team'], 'average_league': values['average_league']}
            

            
    @property
    def get_total_over_1_5_goals_obj(self):
        """
            get home score average per match
        """
        values = self._get_data_scoring(17)

        return {"total_over_1_5": values['team'], 'average_league': values['average_league']}
            

             
    @property
    def get_total_over_2_5_goals_obj(self):
        """
            get home score average per match
        """
        values = self._get_data_scoring(20)

        return {"total_over_2_5": values['team'], 'average_league': values['average_league']}
            
    @property
    def get_total_over_3_5_goals_obj(self):
        """
            get home score average per match
        """
        values = self._get_data_scoring(23)

        return {"total_over_3_5": values['team'], 'average_league': values['average_league']}
            

    @property
    def get_bts_obj(self):
        """
            get home score average per match
        """
        values = self._get_data_scoring(26)

        return {"bts": values['team'], 'average_league': values['average_league']}
            


        


        

