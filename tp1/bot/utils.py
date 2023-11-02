import unicodedata

def remove_accents(input_str):
  nfkd_form = unicodedata.normalize('NFKD', input_str)
  return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def col_to_snake_case(serie):
    return serie.apply(remove_accents)\
                .str.lower()\
                .str.replace(' ', '_')

def serie_to_str(serie):
    idxs   = serie.index
    values = serie.values

    string = str()

    for (idx, value) in zip(idxs, values):
        idx = '/' + str(idx)
        value = value[:40] + '...'
        string += f'{value:<43} {idx}\n'

    return string
