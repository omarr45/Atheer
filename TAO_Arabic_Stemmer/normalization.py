from . import config
from .script import *


class Arabic_normalization:

    norm_table = {ALEF_MADDA: ALEF,
                  ALEF_HAMZA_ABOVE: ALEF,
                  ALEF_HAMZA_BELOW: ALEF,

                  TEH_MARBUTA: HEH,
                  ALEF_MAKSURA: YEH,

                  TATWEEL: u'',

                  # Ligatures
                  LAM_ALEF: LAM+ALEF,
                  LAM_ALEF_HAMZA_ABOVE: LAM+ALEF,
                  LAM_ALEF_HAMZA_BELOW: LAM+ALEF,
                  LAM_ALEF_MADDA_ABOVE: LAM+ALEF,

                  # Diacritics
                  FATHATAN: u'',            DAMMATAN: u'',
                  KASRATAN: u'',            FATHA: u'',
                  DAMMA: u'',               KASRA: u'',
                  SHADDA: u'',              SUKUN: u'',

                  # Numbers
                  ZERO: ar_ZERO,
                  ONE: ar_ONE,
                  TWO: ar_TWO,
                  THREE: ar_THREE,
                  FOUR: ar_FOUR,
                  FIVE: ar_FIVE,
                  SIX: ar_SIX,
                  SEVEN: ar_SEVEN,
                  EIGHT: ar_EIGHT,
                  NINE: ar_NINE,
                  }

    @staticmethod
    def normalize_token(token):

        for ch in PUNCTUATIONS:
            token = token.replace(ch, '')

        term = list()
        for char in token:
            if char == ALEF_HAMZA_ABOVE and not config.replace_ALEF_HAMZA_ABOVE:
                term.append(char)
            elif char == ALEF_HAMZA_BELOW and not config.replace_ALEF_HAMZA_BELOW:
                term.append(char)
            elif char == ALEF_MADDA and not config.replace_ALEF_MADDA:
                term.append(char)
            elif char == ALEF_MAKSURA and not config.replace_ALEF_MAKSURA:
                term.append(char)
            elif char == TEH_MARBUTA and not config.replace_TEH_MARBUTA:
                term.append(char)
            elif char == TATWEEL and not config.remove_KASHIDA:
                term.append(char)
            elif char in TASHKEEL and not config.remove_diacritics:
                term.append(char)
            else:
                term.append(Arabic_normalization.norm_table.get(char, char))

        return ''.join(term)


if __name__ == '__main__':
    pass
