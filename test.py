import cbsodata
import pandas as pd

woonlasten = pd.DataFrame(
                cbsodata.get_data('85949NED',
                                  filters="Woningkenmerken eq 'T001100' and Huishoudenskenmerken eq 'T001139' and Regiokenmerken eq 'NL01    ' or Regiokenmerken eq 'PV24    '",
                                  select=['Regiokenmerken', 'Perioden', 'EigenaarHuurder', 'TotaleWoonlasten_2', 'NettoWoonlasten_3', 'Woonquote_5']))
woonlasten