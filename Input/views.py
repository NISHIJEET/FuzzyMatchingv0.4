from django.shortcuts import render, HttpResponse
import pandas as pd
from .utility import create_sample_data, test, TriggerFunction
import logging as log
import os
from django.conf import  settings
from pandas import ExcelWriter
from io import StringIO,BytesIO
from django.http import StreamingHttpResponse,HttpResponse
import csv


data = {'modal':"", 'file_selected':False}
#from Home.views import  data
config = {}

def Input(request):
    data.clear()
    return render(request, 'input.html',)

# function called on page of input files
def Source(request):
    if "GET" == request.method:
        return render(request, 'Source.html',{})
    else:
        excel_File1 = request.FILES["excel_file1"]
        excel_File2 = request.FILES["excel_file2"]

        bFileSelected=True
        log.info("Reading data files")

        dfSource = pd.read_excel(excel_File1,dtype=str)
        data['dfSource'] = dfSource
        dfITM = pd.read_excel(excel_File2,dtype=str)
        data['dfITM'] = dfITM
        data['file_selected'] = True
        data['excel_file1'] = excel_File1
        data['excel_file2'] = excel_File2
        data.pop("new_common_fields",None)

        TotalSource = len(dfSource)
        TotalITM =len(dfITM)
        sampleSource = create_sample_data(dfSource)
        sampleITM = create_sample_data(dfITM)

        column_Name = set(dfSource.columns.tolist()).intersection(set(dfITM.columns.tolist()))

        #c = set(column_Name)
        if len(list(column_Name)) > 0:
            contains_Column = True
        else:
            contains_Column = False

        data['contains_Column'] = contains_Column

    data_details = {"excel_data1":dfSource,
                    "excel_data2":dfITM,
                    "excel_File1":excel_File1,
                    "excel_File2":excel_File2,
                    "bFileSelected":bFileSelected,
                    "contains_Column":contains_Column,
                    "TotalITM":TotalITM,
                    "TotalSource":TotalSource
                    }

    return render(request,'Source.html',data_details)

def column_list(request):
    try:
        dfSource = data['dfSource']
        dfITM = data['dfITM']
    except Exception:
        return HttpResponse(str(Exception))

    column_Name= list(set(dfSource.columns.tolist()).intersection( set(dfITM.columns.tolist())))
    data['new_common_fields'] = column_Name

    SelectColumnDetails = {"column_list":column_Name,
                           "data":dfITM,
                           "dataSource":dfSource}

    return  render(request,'SelectColumns.html',SelectColumnDetails)

def CommonField(request):
    try:
        dfITM = data['dfITM']
        dfSource = data['dfSource']
    except:
        return HttpResponse("Error")

    new_common_fields = dfITM.columns.tolist()
    SelectedCommonFields = request.POST.getlist('SelectCommonColumns')
    print(SelectedCommonFields)
    dfITM = dfITM[SelectedCommonFields]
    dfSource = dfSource[SelectedCommonFields]

    new_selections = {
        'source_data':dfSource,
        'data':dfITM,
        'column_list':new_common_fields,
        'colSelections':SelectedCommonFields,
    }

    # if request.method=="POST":
    #     # data['Sourcetemp'] = dfSource
    #     # data['ITMtemp'] = dfSource
        # data['dfITM'] = dfITM
        # data['dfSource']=dfSource

    data['new_common_fields']=SelectedCommonFields
    print(data['new_common_fields'])

    return render(request,'CommonField.html',new_selections)

def ColumnList(request):
    global SelCommonCols
    SelCommonCols = request.POST.getlist('SelectCommonColumns[]')

def ConcatCommonFields(request):

    try:
        dfITM = data['dfITM']
        dfSource = data['dfSource']
    except:
        return HttpResponse("Error")


    data['dfITM'] = dfITM[data['new_common_fields']]
    data['dfSource']=dfSource[data['new_common_fields']]
    if request.method =="POST":

        if 'new_common_fields' in data:
            data['dfITM']= data['dfITM'][data['new_common_fields']]
            data['dfSource']= data['dfSource'][data['new_common_fields']]
    dfITM=data['dfITM']
    dfSource=data['dfSource']
    new_common_fields = dfITM.columns.tolist()
    concatFields = {"data": dfITM,
                    "data_source":dfSource,
                    "column_list": new_common_fields}

    return render(request,'ConcatCommonField.html',concatFields)

def ConcatFields(request):
    try:
        dfITM = data['dfITM']
        dfSource = data['dfSource']
    except:
        return HttpResponse("Error")

    FieldsToConcat = request.POST.getlist('concatFields')
    ReplaceWith = request.POST.get('fname')
    ReplaceWith = str(ReplaceWith).upper()
    dfITM[ReplaceWith]  = ''
    dfSource[ReplaceWith]= ''

    for field in FieldsToConcat:
        dfITM[ReplaceWith] = dfITM[ReplaceWith]+ dfITM[field]
        dfSource[ReplaceWith] = dfSource[ReplaceWith] + dfSource[field]

        # dfITM[ReplaceWith] = dfITM[ReplaceWith] + '-' + dfITM[field]
        # dfSource[ReplaceWith] = dfSource[ReplaceWith] + '-' + dfSource[field]

    dfITM=dfITM.drop(columns=FieldsToConcat)
    dfSource = dfSource.drop(columns=FieldsToConcat)
    data['dfITM'] = dfITM
    data['dfSource']=dfSource
    NewColumns = dfITM.columns.tolist()

    concatenatedFields = {"data_source":dfSource,
                          "data":dfITM,
                          "column_list":NewColumns,
                          "FieldsToConcat":FieldsToConcat}

    return render(request, 'ConcatFields.html',concatenatedFields )

def CatFieldSelection(request):
    try:
        dfITM=data['dfITM']
        dfSource =data['dfSource']
        new_common_fields = dfITM.columns.tolist()
    except:
        return HttpResponse("Error")

    config['categoricalFileds']=[]
    config['weights']={}

    # for field in new_common_fields:
    #     if field not in config['categoricalFileds']:
    #         config['weights'][field]=0

    AllFields = {"data_source":dfSource,
                 "data":dfITM,
                 "column_list":new_common_fields,
                 "config":config}

    return render(request, 'CatFieldSelection.html',AllFields)

def SavedWeights(request):

    try:
        dfITM = data['dfITM']
        dfSource = data['dfSource']
        new_common_fields = dfITM.columns.tolist()

    except:
        return HttpResponse("Error")
    if request.method == "POST":
        categoricalField = request.POST.getlist('SelectCatColumns')
        config['categoricalFileds'] = categoricalField
        WeighFields = list(set(new_common_fields) - set(categoricalField))

        config['weights'].clear()
        for weight in WeighFields:
            config['weights'][weight] = request.POST.get(weight)

    AllFields = {"data_source": dfSource,
                 "data": dfITM,
                 "column_list": new_common_fields,
                 "categoricalField":config['categoricalFileds'],
                 "weights": config['weights']}

    return render(request,'SavedWeights.html',AllFields)

def PreRun(request):
    return render(request, 'PreRun.html', )

def ReplaceWords(request):

    try:
        dfITM = data['dfITM']
        dfSource = data['dfSource']
        new_common_fields = dfITM.columns.tolist()
    except:
        return HttpResponse("Error")
    ColumnLength = True

    if request.method == 'POST':
        file_to_replace = request.FILES["ReplaceWords_file"]
        replacewords_file_upload =  pd.read_excel(file_to_replace,dtype=str)
        cols = replacewords_file_upload.columns.tolist()
        print(cols[0])
        print(cols[1])
        collength = len(replacewords_file_upload.columns)
        if (collength != 2) or (cols[0]!="Words" and cols[1]!="Replacement"):
            replacewords_file = pd.read_excel(os.path.join(settings.MEDIA_ROOT, 'Replace Words.xlsx'), dtype=str)
            ColumnLength = False
        else:
            # if :
            prelist = pd.read_excel(os.path.join(settings.MEDIA_ROOT,'Replace Words.xlsx'),dtype=str)
            replacewords_file = prelist.append(replacewords_file_upload)
            replacewords_file = replacewords_file.drop_duplicates()

    elif ("replacewith" in data):
        replacewords_file = data['replacewith']
    else:
        replacewords_file = pd.read_excel(os.path.join(settings.MEDIA_ROOT,'Replace Words.xlsx'),dtype=str)

    data['replacewith'] = replacewords_file

    return render(request,'ReplaceWords.html', {"replaceData":replacewords_file,"ColumnLength":ColumnLength})

def ReplaceWordsResults(request):

    try:
        dfITM = data['dfITM']
        dfSource = data['dfSource']

    except:
        return HttpResponse("Error")

    # replacewords_file = pd.read_csv(os.path.join(settings.MEDIA_ROOT,'replace_words.csv'),dtype=str,index_col='Words').to_dict()['Replacements']
    replacewords_file = pd.read_excel(os.path.join(settings.MEDIA_ROOT, 'Replace Words.xlsx'), dtype=str, index_col='Words').to_dict()['Replacement']

    # dfITM.replace(to_replace=replacewords_file,inplace=True)
    # dfSource.replace(to_replace=replacewords_file,inplace=True)


    return render(request, 'ControlSettings.html' )

def ControlSettings(request):
    try:
        dfITM = data['dfITM']
        dfSource = data['dfSource']
        catFields = config['categoricalFileds']
        weights = config['weights']
        for scols in catFields:
            weights[scols] = "C"
        replacewords = data['replacewith']
        ctrlNOM = request.POST.get('matches')
        ctrlMAMQ= request.POST.get('mimMQ')
        ctrlAMQR= request.POST.get('drop')
        ctrlGQM= request.POST.get('goodmatch')
        ctrlMQM = request.POST.get('moderatematch')

        AllParaters = {
            "dfITM":dfITM,
            "dfSource": dfSource,
            "catFields":catFields,
            "weights": weights,
            "replacewords":replacewords,
            "ctrlNOM":ctrlNOM,
            "ctrlMAMQ":ctrlMAMQ,
            "ctrlAMQR":ctrlAMQR,
            "ctrlGQM":ctrlGQM,
            "ctrlMQM":ctrlMQM,
        }
    except:
        return HttpResponse("Error")

    global df

    df= test(AllParaters)

    config['AllParaters'] = AllParaters

    return render(request, 'ControlSettings.html',)

def Output(request):
    if request.method == "POST":
        data['output'] = TriggerFunction(config['AllParaters'])

    return render(request, 'Output.html',{"df":data['output']})

def Download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="MatchResults.csv"'

    writer = csv.writer(response)
    writer = df_to_writer(df, writer)
    print(df.values)

    # df.to_csv(index=False)
    # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response

def df_to_writer(df,writer):
    writer.writerow(df.columns.tolist())
    for row in df.values:
        writer.writerow(row)
    return writer

