from Input.SupportFunctions import *
import numbers

class WordClass:

    def __init__(self, s_word, cls_ew):

        self.s_val = ''
        self.lst_ngrams = []

        # clean the word before moving (if defined true) - removing everything except alphanumeric
        if cls_ew.bol_alphanumeric:
            s_word = cls_ew.replace_alphanumeric(s_word).lower().strip()

        # replace words that mean the same (if defined true) - replace what is not required
        if cls_ew.bol_replace:
            try:
                self.s_val = s_word.replace(s_word, cls_ew.dict_replacement_meta[s_word]).lower()
            except KeyError as e:
                self.s_val = s_word.lower()

        # create n-grams of the word and store them in the word - also need to index them on the go as well
        self.lst_ngrams = self.lst_ngrams + list(cls_ew.create_grams(self.s_val, 3))


# Contains all field info including the words in that field
class FieldForRowClass:

    def __init__(self, s_field_name, s_field_weight, bol_is_categorical=False):
        self.s_fieldID = s_field_name
        self.s_field_weight = s_field_weight
        self.bol_isCategorical = bol_is_categorical
        self.lst_cls_words = []
        self.s_text = ''


# Contains all row info. Will be the pivot point between categories and table info
class RowClass:

    def __init__(self, ser_row, dict_weights, s_row_num, cls_ew):
        # create row id by concatenating all the values in that row
        #self.s_row_ID = ''.join(map(str,list(ser_row.values())))
        self.s_row_num = s_row_num
        self.lst_words = []
        self.lst_grams = []
        self.l_total_field_weights = 0
        self.dict_field_values = {}

        # add field items to the row and word items to field. The constructor of Word function automatically creates the 3 grams
        for s_column in ser_row.keys():
            cls_field = FieldForRowClass(s_column, dict_weights.get(s_column,1))
            s_curr_text = str(ser_row[s_column]).lower().strip()
            for s_word in s_curr_text.split(" "):
                wrd_curr = WordClass(s_word, cls_ew)
                self.lst_words.append(wrd_curr)
                cls_field.lst_cls_words.append(wrd_curr)
                self.lst_grams = self.lst_grams + wrd_curr.lst_ngrams

            cls_field.s_text = s_curr_text
            self.dict_field_values[cls_field.s_fieldID] = cls_field
            #ls_field.update_ngram_count() //NJ// removing this because field-wise takes time


    def get_total_field_weight(self):
        l_weight_sum = 0
        for field_val in self.dict_field_values.values():
            if not isinstance(field_val.s_field_weight, numbers.Number):
                continue
            l_weight_sum += field_val.s_field_weight

        return l_weight_sum

class CategoryClass:

    def __init__(self, s_category):
        self.s_category_id = s_category
        self.dict_row_itm = {}
        self.dict_row_src = {}
        self.dict_src_grams_records = {}

    def add_row_itm(self, cls_row):
        self.dict_row_itm[cls_row.s_row_num] = cls_row

    def add_row_src(self, cls_row):
        self.dict_row_src[cls_row.s_row_num] = cls_row
        # save the words to records data
        self.update_record_word_mapping(cls_row)

    def update_record_word_mapping(self, cls_row):
        for s_gram in cls_row.lst_grams:
            if s_gram in self.dict_src_grams_records.keys():
                self.dict_src_grams_records[s_gram].append(cls_row.s_row_num)
            else:
                self.dict_src_grams_records[s_gram] = [cls_row.s_row_num]