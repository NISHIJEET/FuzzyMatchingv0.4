from nltk.util import ngrams
import re
import Levenshtein as lev

class EditWords:

    dict_replacement_meta = {}
    bol_replace = False
    bol_alphanumeric = False

    # replacement module - indexes all words that need to be replaced(as dictionary)
    def __init__(self, df_replacement_meta, bol_replace=True, bol_alphanumeric=True):
        # dropping all duplicates since the table cannot contain duplicates
        df_replacement_meta = df_replacement_meta.drop_duplicates("Words")
        self.dict_replacement_meta = df_replacement_meta.set_index("Words")['Replacement'].to_dict()
        self.bol_alphanumeric = bol_alphanumeric
        self.bol_replace = bol_replace

    # replace the non alpha-numeric symbol with the specified replacement
    def replace_alphanumeric(self, s_statement, s_replacement=''):
        return re.sub(r'[^a-zA-Z0-9\s]', s_replacement, s_statement)

    # returns a list of tuples as n-grams of a word
    def create_grams(self, s_word, n):
        return list(ngrams(s_word, n))

class CompareHelper:

    s_word_itm = ""
    s_word_src = ""
    l_compare_score = 0
    l_distance = 0

    def update_words(self,s1,s2):
        self.s_word_itm = s1.lower().strip()
        self.s_word_src = s2.lower().strip()
        self.calculate_distance()
        self.calculate_score()

    def calculate_distance(self):
        if self.s_word_itm == self.s_word_src:
            self.l_distance = 0
            return
        self.l_distance= lev.distance(self.s_word_itm, self.s_word_src)

    def calculate_score(self):
        l_msx_len = max(len(self.s_word_itm),len(self.s_word_src))
        self.l_compare_score = (l_msx_len - self.l_distance)/l_msx_len


