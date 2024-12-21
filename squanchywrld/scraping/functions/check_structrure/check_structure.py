from bs4 import BeautifulSoup # type: ignore
import difflib
from web.get_access import access

def extract_structure_part(html, seletor):
    """
        Extract date form the site by selector
    """
    soup = BeautifulSoup(access(html), 'html.parser')

    # searching for a specific part by css selector
    specific_part = soup.select(seletor)
   
    structure = []
    
    for tag in specific_part:
        # removing the attribute 'src', 'href', 'class', etc.
        attribute = {key: value for key, value in tag.attrs.items() if key not in ['src', 'style', 'class', 'href']}
        structure.append(f"{tag.name} {sorted(attribute.items())}")
    


    return structure, specific_part

    



def compare_structures(old_structure, new_structure):
    diff = difflib.unified_diff(old_structure, new_structure)
    change = '\n'.join(diff)
    return change
