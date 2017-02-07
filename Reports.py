
import csv
class ReportType:
	"""Contains a list of headers and conditions that make up a 
	type of report. E.G. "False Crawl"
	headers[rawHeader] = header
	conditions[rawHeader] = value
	 """
	def __init__(self, name, headers, conditions):
		self.name = name
		self.headers = headers 
		self.conditions = conditions
	# Takes a list of reports, returns a list of reports matching the conditions
	# containing only the headers listed
	def GenerateReport(self, reports):
		prunedReports = []
		for report in reports:
			if report.MeetsConditions(conditions):
				prunedReports.append(report.prune(headers))
		return prunedReports

class FileIO:
	"""docstring for FileIO"""
	def LoadCSV(self, name):
		rawData = []
		with open(name,'rb') as data:
			fileReader = csv.reader(data, delimiter = ';')
			for row in fileReader:
				rawData.append(row)
		rawData.pop(0)
		return rawData

	def UpdateHeaderList(self, headerDict, rawHeaders):
		for rawHeader in rawHeaders:
			if not headerDict.has_key(rawHeader):
				headerDict[rawHeader] = rawHeader
		return headerDict

	def LoadOrCreateDictionary(self, name):
		try:
			newDict = open(name,'rb').read()
			return eval(newDict)
		except IOError:
			return {}

	def SaveDictionary(self, name, data):
		with open(name, 'a') as rawFile:
			rawFile.write(str(data))


class Report:
	"""docstring for Report
		reportData[rawHeader] = value
	"""
	def __init__(self, reportData):
		self.reportData = reportData

	def MeetsConditions(self, conditions):
		for key, value in conditions:
			if self.reportData[key] != value:
				return False
		return True
	
	def prune(self, headers):
		prunedReport = {}
		for key, value in headers:
			#TODO: possibly throw missing header error here?
			prunedReport[key] = self.reportData[key]
		return prunedReport
		