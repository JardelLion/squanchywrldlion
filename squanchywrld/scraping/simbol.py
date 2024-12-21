from team import Team


class Simbol:


    def __init__(self, site):
        self.site = site
        self.team = Team(site)

        self.soup = site.find("div", attrs={
            'id': 'content'
        })

        self.table = self.soup.find("table", attrs={
            'cellspacing': '0',
            'cellpadding': '1',
            'width': "100%"
        })


        self.rows = self.table.find_all("tr", attrs={
        
        })[0]


        self.row_values = self.rows.find_all('b')


        self.team_names = {
            self.team.get_home: self.row_values[0].get_text().lower(),
            self.team.get_away: self.row_values[-1].get_text().lower()
        }

    @property
    def get_first_team_simbol(self):
        return self.team_names[self.team.get_home]

    @property
    def get_second_team_simbol(self):
        return self.team_names[self.team.get_away]
