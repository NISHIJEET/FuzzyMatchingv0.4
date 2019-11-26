from Input.SupportClasses import *
import numbers


class MatchingAlgorithms:

    def __init__(self, row_itm, cat_category):
        self.cat_current = cat_category
        self.row_itm = row_itm
        self.l_tentative_count = 3
        self.l_final_count = 3
        l_max_records = len(self.cat_current.dict_row_src)
        self.l_tentative_count = min(l_max_records,self.l_tentative_count)
        self.l_final_count = min(l_max_records, self.l_final_count)
        self.lst_row_tentative = []
        self.dict_final_match_result = {}

    def tentative_matching(self):
        l_max_records = 1000000
        lst_record_freq = [0] * (l_max_records+1)
        for s_gram in self.row_itm.lst_grams:
            for l_record in self.cat_current.dict_src_grams_records[s_gram]:
                lst_record_freq[l_record] += 1

        lst_tentative_record_num = sorted(range(1,l_max_records+1), key = lambda x: lst_record_freq[x], reverse= True)[:self.l_tentative_count]
        self.lst_row_tentative = [self.cat_current.dict_row_src[x] for x in lst_tentative_record_num]


    def final_matching(self):
        compare_helper = CompareHelper()
        for row_src in self.lst_row_tentative:
            l_field_score = 0
            for field_curr in self.row_itm.dict_field_values.values():
                if not isinstance(field_curr.s_field_weight, numbers.Number):
                    continue

                compare_helper.update_words(field_curr.s_text,row_src.dict_field_values[field_curr.s_fieldID].s_text)
                l_field_score += compare_helper.l_compare_score * (field_curr.s_field_weight/row_src.get_total_field_weight())

            self.dict_final_match_result[row_src.s_row_num] = l_field_score










