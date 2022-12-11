import pandas as pd
def readExcel():
    #Dataframe object
    df = pd.read_excel('rostering.xlsx', header=None)
    for col in df.columns:
        print("Column is " , col)
    #df.items()

    #How many times the loop will iterate/how many rows exist
    rows = df.shape[0]
    print("No of rows: " + str(rows))

    #How many rows exist
    cols = df.shape[1]
    print("No of colsumns: " + str(cols))
    print("################" + "\n")

    listOfValues = []
    columnA = []
    columnB = []
    columnC = []
    columnD = []
    columnE = []
    columnF = []
    columnG = []
    columnH = []
    # columnI = []
    count = 0
    for x in range(rows):	
        if x == rows:
            break
        for y in range(cols):
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
            # columnI.append(df.iloc[x,y+8])
            print("Row of values is ", rowOfValues)
            break;
        count = count + 1
        #print(str(listOfValues) + "\n")
        #print("################" + "\n")
    
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
        # "columnI": columnI
    }
    
    print("Count is ",count)
    #for i in range(len(listOfValues)):
        #print(listOfValues)

    print(str(listOfValues) + "\n")

    for pos, value in enumerate(listOfValues):
        print(pos,value)

    for pos, value in enumerate(listOfValues):
        if pos == 40:
            print(value + " XXX")
    

    #while i < (str(rows)):
        #print(str(listOfValues[8:15]) + "\n")
        #i += 1
    print("Column A", valuesToUse["columnA"])
    print("Column B", valuesToUse["columnB"])
    print("Column C", valuesToUse["columnC"])
    print("Column D", valuesToUse["columnD"])
    print("Column E", valuesToUse["columnE"])
    print("Column F", valuesToUse["columnF"])
    print("Column G", valuesToUse["columnG"])
    print("Column H", valuesToUse["columnH"])
    # print("Column I", valuesToUse["columnI"])

    # Access List in Dictionary.
    assigned = valuesToUse["columnA"]
    print("Assigned is " ,assigned)

    #Loop through list
    for i in assigned:
        print("i is " + i)
        
    #Get list length, a.k.a number of rows/loops
    print("List length is ",len(assigned))
    return valuesToUse