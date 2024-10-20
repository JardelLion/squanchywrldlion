
from classes.ppg import ObjecMain

class TotalMatchGoalStatic(ObjecMain):
    """
    Stastic team based on the lastest 8 game
    """

    _selector = 'div.tab:nth-child(6) > table:nth-child(3)'
    def __init__(self, url):
        super().__init__(url, self._selector)

        self._soup = self._new_part[0]


    def _table_row_obj(self, class_name):
        """
            class_name is based on the website class name into html
        """

        """
        gp -> game played
        avg -> average
        bts -> both team to score
        cs -> clean sheet
        fts -> failed to score
        wtn -> won to nil
        ltn -> lose and the opponent scored
        """
        tr = self._soup.find("tr", attrs={
            'class': class_name
        })

        td = tr.find_all("td")

        obj_values = {
            "name": str(td[0].text).strip(),
            'gp':str(td[1].text).strip(),
            'avg': str(td[2].text).strip(),
            "1.5+": str(td[3].text).strip(),
            '2.5+': str(td[4].text).strip(),
            '3.5+': str(td[5].text).strip(),
            "4.5+": str(td[6].text).strip(),
            "5.5+": str(td[7].text).strip(),
            'bts': str(td[8].text).strip(),
            'cs': str(td[9].text).strip(),
            'fts': str(td[10].text).strip(),
            'wtn': str(td[11].text).strip(),
            'ltn': str(td[12].text).strip()

        }

        return obj_values


    @property
    def get_home_obj(self):
        

        return self._table_row_obj("trow7")
    
    @property
    def get_away_obj(self):

        return self._table_row_obj("trow5")

    