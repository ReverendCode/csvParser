import Reports

fileIO = Reports.FileIO()
csvFile = fileIO.LoadCSV('file.csv')
headerDict = HeaderDictionary(fileIO.LoadOrCreateDictionary('headerDict.txt'))
headerList = csvFile.pop(0)
headerDict.UpdateHeaders(headerList)

fileIO.SaveDictionary('headerDict.txt',headerDict.headers)

"""
Now we have the existing human readable headers, along with any new headers loaded into the headerDict dictionary.

We need a display that takes a dictionary of headers, a ReportType object, and the csvFile. This display needs to show the name of the reportType, along with the list of headers the reportType contains, next to a separate list, containing the headerDict.
This display should also have a generate Csv button. When clicked, this should take the csv, and hand it to the reportType to generate a set of pruned reports
"""