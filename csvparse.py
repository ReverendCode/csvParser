
"""
Turtle Watch CSV parsing script

This program will take in a complete .csv of the turtle nest program.

it will then present a list of all field headers, with the "human readable" 
name substituted whenever possible. To the right, is a list of the headers
 that will be used to generate a report, it should be possible to save a 
 collection of these as a report. E.G. "False Crawl Report, Nest Report". 
 There should also be a button to "generate existing report"

INPUTS:
	csv file (raw data)
	"human readable" headers
	Existing report types (phase 2: what if the report is missing a header
	 the report type wants?)
"""
def getHeaderDictionary(): #what if the file doesn't exist? return {}?
	try:
		rawFile = open('headerNames','rb').read()
		return eval(rawFile)
	except IOError:
		return {}


def loadHeaders(headerList, dataLists):
	numHeaders = len(headerList)
	headers = []
	hDict = getHeaderDictionary()
	for i in range(numHeaders):
		# iterate through each dataList, grab the i'th item, place into record
		data = []
		for datum in dataLists:
			data.append(datum[i])

		# title = getOrGenerateTitle(headerList[i],hDict)
		headers.append(Header(headerList[i],data,hDict))
	return headers
	



def saveHeaderDictionary(headerDict):
	with open('headerNames','a') as rawFile:
		rawFile.write(str(headerDict))

def loadRawData():
	rawData = []
	with open('file.csv', 'rb') as csvfile:
		fileReader = csv.reader(csvfile, delimiter = ';')
		for row in fileReader:
			rawData.append(row)
	return rawData

class Header:
	"""This class contains all the information about the headers
	The raw header value, the ordering, and the human readable value """
	def __init__(self, rawHeader, data, dictionary):
		self.rawHeader = rawHeader
		self.headerTitle = self.getOrGenerateTitle(rawHeader,dictionary)
		self.data = data

	def getOrGenerateTitle(self, header, dictionary):
		if not dictionary.has_key(header):
			dictionary[header] = header
		return dictionary[header]



import csv
rawData = loadRawData()
# remove the 'sep=;' line at the front of the csv.
rawData.pop(0)

# load existing headers into data structure.
headers = loadHeaders(rawData[0], rawData)


