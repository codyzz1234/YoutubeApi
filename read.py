import pandas as pd
import numpy as np
def readExcel():
    #Dataframe object
    df = pd.read_excel('rostering.xlsx', header=None)
    
    #How many times the loop will iterate/how many rows exist
    rows = df.shape[0]
    #How many rows exist
    cols = df.shape[1]
    
    colA = []
    colB = []
    colC = []
    colD = []
    colE = []
    colF = []
    colG = []
    colH = []
    colI = []
    colJ = []
    
    colA = df.values.T[0].tolist()
    colB = df.values.T[1].tolist()
    colC = df.values.T[2].tolist()
    colD = df.values.T[3].tolist()
    colE = df.values.T[4].tolist()
    colF = df.values.T[5].tolist()
    colG = df.values.T[6].tolist()
    colH = df.values.T[7].tolist()
    colI = df.values.T[8].tolist()
    colJ = df.values.T[9].tolist()
    
    titles = np.column_stack((colA,colB,colC,colD,colE)) #stacks the list into one array
    descriptions = np.column_stack((colF,colG,colH)) #stacks the list into one array
    dates = colI
    
    
    valuesToUse = {
        "rows":rows,
        "titles": titles,
        "descriptions": descriptions,
        "dates": dates,
    }
    
    
    # for x in range(rows):        
    #     y = 0
    #     rowOfValues = df.iloc[x,y]
    #     listOfValues.append(rowOfValues)
    #     colA.append(df.iloc[x,y])
    #     colB.append(df.iloc[x,y+1])
    #     colC.append(df.iloc[x,y+2])
    #     colD.append(df.iloc[x,y+3])
    #     colE.append(df.iloc[x,y+4])
    #     colF.append(df.iloc[x,y+5])
    #     colG.append(df.iloc[x,y+6])
    #     colH.append(df.iloc[x,y+7])
    #     colI.append(df.iloc[x,y+8])
    #     colJ.append(df.iloc[x,y+9])
    
    
    
        
    
    # valuesToUse = {
    #     "rows":rows,
    #     "colA": colA,
    #     "colB": colB,
    #     "colC": colC,
    #     "colD": colD,
    #     "colE": colE,
    #     "colF": colF,
    #     "colG": colG,
    #     "colH": colH,
    #     "colI": colI,
    #     "colJ": colJ,
    # }
    
    
    # print("Column A", valuesToUse["colA"])
    # print("Column B", valuesToUse["colB"])
    # print("Column C", valuesToUse["colC"])
    # print("Column D", valuesToUse["colD"])
    # print("Column E", valuesToUse["colE"])
    # print("Column F", valuesToUse["colF"])
    # print("Column G", valuesToUse["colG"])
    # print("Column H", valuesToUse["colH"])
    # print("Column I", valuesToUse["colI"])
    # print("Column J", valuesToUse["colJ"])


    # # Access List in Dictionary.
    # assigned = valuesToUse["colA"]
    # print("Assigned is " ,assigned)

    # #Loop through list
    # for i in assigned:
    #     print("i is " + i)
        
    #Get list length, a.k.a number of rows/loops
    # print("List length is ",len(assigned))
    return valuesToUse