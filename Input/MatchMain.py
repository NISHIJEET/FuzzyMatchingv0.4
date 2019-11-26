from Input.SupportClasses import *
from Input.MatchingClasses import *
from Input.OutputRepresentation import *
from scipy.sparse.csgraph._traversal import depth_first_order


class MainController:

    def __init__(self):
        self.lst_category_columns = []
        self.dict_categories = {}
        self.dict_Final_Result = {}

    #// will control the final flow of values
    def flow_controller(self, df_itm, df_src, df_replace_words, dict_config):

        dict_weights = dict_config["weights"]

        self.identify_categories(dict_weights)

        # create edit word object to operate the word before inserting
        cls_ew = EditWords(df_replacement_meta = df_replace_words)

        for index, row in df_src.iterrows():
            s_category = self.create_category(row)
            if s_category in self.dict_categories.keys():
                row_src = RowClass(row, dict_weights, index+1, cls_ew)
                self.dict_categories[s_category].add_row_src(row_src)
            else:
                cat_curr = CategoryClass(s_category)
                row_src = RowClass(row, dict_weights, index+1, cls_ew)
                cat_curr.add_row_src(row_src)
                self.dict_categories[s_category] = cat_curr


        for index, row in df_itm.iterrows():
            s_category = self.create_category(row)
            if s_category in self.dict_categories.keys():
                row_itm = RowClass(row, dict_weights, index+1, cls_ew)
                self.dict_categories[s_category].add_row_itm(row_itm)
            else:
                cat_curr = CategoryClass(s_category)
                row_itm = RowClass(row, dict_weights, index+1, cls_ew)
                cat_curr.add_row_itm(row_itm)
                self.dict_categories[s_category] = cat_curr

            match_helper = MatchingAlgorithms(row_itm, self.dict_categories[s_category])
            match_helper.tentative_matching()
            match_helper.final_matching()
            self.dict_Final_Result[index + 1]= match_helper.dict_final_match_result

        output_views = OutputViews(self.dict_Final_Result, df_itm, df_src)
        df_output_table = output_views.create_table()

        return  df_output_table
        #df_output_table.to_csv("Output.csv", index = False)

    def identify_categories(self, dict_weights):
        for s_column, s_weight in dict_weights.items():
            if not isinstance(s_weight, numbers.Number):
                self.lst_category_columns.append(s_column)

    def create_category(self, ser_row):
        s_category = ""
        for s_col in self.lst_category_columns:
            s_category = s_category + ser_row[s_col]
        return s_category

