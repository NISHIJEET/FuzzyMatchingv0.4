import pandas as pd

class OutputViews:

    def __init__(self, dict_matching_details, df_itm, df_src):
        self.dict_matching_details = dict_matching_details
        self.df_itm = df_itm
        self.df_src = df_src
        self.dict_format = {}


    def create_table(self):
        self.dict_format = self.create_output_df_format()
        for l_itm_record in self.dict_matching_details.keys():
            for l_src_record in self.dict_matching_details[l_itm_record].keys():
                self.add_header_data(l_itm_record,l_src_record, \
                                     self.dict_matching_details[l_itm_record][l_src_record])

        return pd.DataFrame(self.dict_format)


    def create_output_df_format(self):
        dict_headers = {}

        dict_headers["ITM_row_number"] = []

        dict_headers["Match Percentage"] = []
        dict_headers["Match Type"] = []

        for s_col in self.df_itm.columns.tolist():
            dict_headers[s_col + "_ITM"] = []
            dict_headers[s_col + "_Src"] = []

        return dict_headers

    def add_header_data(self, l_row_itm, l_row_src, f_match_percentage):
        for s_col in self.df_itm.columns.tolist():
            self.dict_format[s_col + "_ITM"].append(self.df_itm.iloc[l_row_itm-1][s_col])
            self.dict_format[s_col + "_Src"].append(self.df_src.iloc[l_row_src-1][s_col])

        self.dict_format["ITM_row_number"].append(l_row_itm)

        self.dict_format["Match Percentage"].append(f_match_percentage * 100)
        # create logic for match type
        self.dict_format["Match Type"].append("Oh my God!!")