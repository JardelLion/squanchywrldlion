import os
from dotenv import load_dotenv # type: ignore

# load file .env
load_dotenv()

laliga_url_default = os.getenv('LALIGA_DEFAULT_STRUCTURE')

from functions.check_structrure.check_structure import *

class ObjecMain:

    def __init__(self, url, selector):
       
        # Extraímos apenas a parte específica das duas versões de HTML
        self._extract_old_structure, self._old_part = extract_structure_part(laliga_url_default, selector)
        self._extract_new_structure, self._new_part = extract_structure_part(url, selector)
       
        # Comparar as estruturas
        self._change = compare_structures(self._extract_old_structure, self._extract_new_structure)

        if self._change:
            print("change are detected " + self._change)
        else:
            print("No change detected")