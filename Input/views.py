from django.shortcuts import render, HttpResponse
import pandas as pd
from .utility import create_sample_data
import logging as log

data = {}

def Input(request):
    return render(request, 'input.html',)

def Source(request):
    if "GET" == request.method:
        return render(request,'Source.html', {})
        bFileSelected = False
    else:
        excel_File1 = request.FILES["excel_file1"]
        excel_File2 = request.FILES["excel_file2"]

        bFileSelected=True
        log.info("Reading data files")

        dfSource = pd.read_excel(excel_File1,dtype=str)
        data['dfSource'] = dfSource
        dfITM = pd.read_excel(excel_File2,dtype=str)
        data['dfITM'] = dfITM

        sampleSource = create_sample_data(dfSource)
        sampleITM = create_sample_data(dfITM)

    return render(request,'Source.html',{"excel_data1":sampleSource,"excel_data2":sampleITM,"excel_File1":excel_File1,"excel_File2":excel_File2,"bFileSelected":bFileSelected})

def column_list(request):
    try:
        dfSource = data['dfSource']
        dfITM = data['dfITM']
    except e as Exception:
        ConcatFields();
        return HttpResponse(str(e))
    column_Name= set(dfSource.columns.tolist()).intersection( set(dfITM.columns.tolist()))
    return  render(request,'SelectColumns.html',{"column_list":column_Name,"data":create_sample_data(dfITM) })


def ConcatFields(request):
    try:
        dfITM = data['dfITM']
    except:
        return HttpResponse("Error")
    FieldsToConcat = request.POST.getlist('concatFields')
    ReplaceWith = request.POST.get('fname')
    dfITM[ReplaceWith]  = ''
    for field in FieldsToConcat:
        dfITM[ReplaceWith] = dfITM[ReplaceWith]+ dfITM[field]

    # dfITM[ReplaceWith]= np.add.reduce( dfITM[FieldsToConcat])
    dfITM=dfITM.drop(columns=FieldsToConcat)
    data['dfITM'] = dfITM
    NewColumns = dfITM.columns.tolist()

    return render(request, 'SelectColumns.  html',{"data":create_sample_data(dfITM),"column_list":NewColumns} )


def PreRun(request):
    return render(request, 'PreRun.html', )

def ControlSettings(request):
    return render(request, 'ControlSettings.html', )


def ReplaceWords(request):
    if "GET" == request.method:
        return render(request,'ReplaceWords.html', {})
    else:
        replaceFile = request.FILES["ReplaceWords_file"]
        print(replaceFile)
        global dfReplaceFile

        dfReplaceFile = pd.read_excel(replaceFile, dtype=str)
        replaceData = [dfReplaceFile.columns.tolist()]

        for li in dfReplaceFile.head( ).values:
            replaceData.append(li)
        ReplaceCol_list = [dfReplaceFile.columns.tolist()]


    return render(request, 'ReplaceWords.html',{"replaceData":replaceData})

def CatFieldSelection(request):
    return render(request, 'CatFieldSelection.html',)

def ColumnList(request):
    global SelCommonCols
    SelCommonCols = request.POST.getlist('SelectCommonColumns[]')