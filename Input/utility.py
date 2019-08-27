def create_sample_data(df):
    '''

    :param df:
    :return:
    '''

    sample_li = [df.columns.tolist()]
    sample_df = df.head()
    for li in sample_df.values:
        sample_li.append(li)

    return sample_li