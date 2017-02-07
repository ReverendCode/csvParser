import Reports

fileIO = Reports.FileIO()
csvFile = fileIO.LoadCSV('file.csv')
headers = fileIO.LoadOrCreateDictionary('headerDict.txt')
headerList = csvFile[0]
headers = fileIO.UpdateHeaderList(headers, headerList)

fileIO.SaveDictionary('headerDict.txt',headers)

