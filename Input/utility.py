from .MatchMain import MainController

def create_sample_data(df):
    '''

    :param df:
    :return:
    '''

    sample_li = [df.columns.tolist()]
    sample_df = df.head()
    for li in sample_df.values:
        sample_li.append(li)

    # print(sample_li)
    return sample_li
#
def test(details):
    val1 = details["dfITM"]
    # print(val1)
    val2 =  details["ctrlNOM"]
    # print(val2)

    return val1

def TriggerFunction(all_parameters):
    main_controller = MainController()
    df_output =  main_controller.flow_controller(all_parameters["dfITM"], all_parameters["dfSource"], \
                                    all_parameters["replacewords"], all_parameters)
    return df_output