import pandas as pd
def readExcel():
    #Dataframe object
    df = pd.read_excel('rostering.xlsx', header=None)

    #How many times the loop will iterate/how many rows exist
    rows = df.shape[0]

    #How many rows exist
    cols = df.shape[1]

    listOfValues = []
    columnA = []
    columnB = []
    columnC = []
    columnD = []
    columnE = []
    columnF = []
    columnG = []
    columnH = []
    columnI = []
    columnJ = []
    for x in range(rows):        
        y = 0
        rowOfValues = df.iloc[x,y]
        listOfValues.append(rowOfValues)
        columnA.append(df.iloc[x,y])
        columnB.append(df.iloc[x,y+1])
        columnC.append(df.iloc[x,y+2])
        columnD.append(df.iloc[x,y+3])
        columnE.append(df.iloc[x,y+4])
        columnF.append(df.iloc[x,y+5])
        columnG.append(df.iloc[x,y+6])
        columnH.append(df.iloc[x,y+7])
        columnI.append(df.iloc[x,y+8])
        columnJ.append(df.iloc[x,y+9])
        
    
    valuesToUse = {
        "rows":rows,
        "columnA": columnA,
        "columnB": columnB,
        "columnC": columnC,
        "columnD": columnD,
        "columnE": columnE,
        "columnF": columnF,
        "columnG": columnG,
        "columnH": columnH,
        "columnI": columnI,
        "columnJ": columnJ,
    }
    
    
    print("Column A", valuesToUse["columnA"])
    print("Column B", valuesToUse["columnB"])
    print("Column C", valuesToUse["columnC"])
    print("Column D", valuesToUse["columnD"])
    print("Column E", valuesToUse["columnE"])
    print("Column F", valuesToUse["columnF"])
    print("Column G", valuesToUse["columnG"])
    print("Column H", valuesToUse["columnH"])
    print("Column I", valuesToUse["columnI"])
    print("Column J", valuesToUse["columnJ"])


    # # Access List in Dictionary.
    # assigned = valuesToUse["columnA"]
    # print("Assigned is " ,assigned)

    # #Loop through list
    # for i in assigned:
    #     print("i is " + i)
        
    #Get list length, a.k.a number of rows/loops
    # print("List length is ",len(assigned))
    return valuesToUse