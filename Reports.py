
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
	def GeneratePrunedReports(self, rawReports):
		prunedReports = []
		reports = []
		# remove headers from rawReports
		headers = rawReports.pop(0)
		for report in rawReports:
			reports.append(Report(headers,report))
		for report in reports:
			if report.MeetsConditions(conditions):
				prunedReports.append(report.prune(headers))
		return prunedReports

class FileIO:
	"""docstring for FileIO"""
	def LoadCSV(self, name):
		rawData = []
		with open(name,'r') as data:
			fileReader = csv.reader(data, delimiter = ';')
			for row in fileReader:
				rawData.append(row)
		# remove 'SEP=;' that is in this file
		rawData.pop(0)
		return rawData
	
	# take a list of Reports, generates a csv from the reports
	def SaveCSV(self, name, reportList):
		raise NotImplementedError

	def UpdateHeaderList(self, headerDict, rawHeaders):
		for rawHeader in rawHeaders:
			if not headerDict.has_key(rawHeader):
				headerDict[rawHeader] = rawHeader
		return headerDict

	def LoadOrCreateDictionary(self, name):
		try:
			newDict = open(name,'r').read()
			return eval(newDict)
		except IOError:
			return {}

	def SaveDictionary(self, name, data):
		with open(name, 'a') as rawFile:
			rawFile.write(str(data))

class HeaderDictionary:
	def __init__(self, headers):
		self.headers = headers

	def AddHeaders(self,rawHeaders):
		for header in rawHeaders:
			if header not in self.headers:
				self.headers[header] = header

	def UpdateHeaders(self, headers):
		for key in headers:
			self.headers[key] = headers[key]


class Report:
	"""docstring for Report
		reportData[rawHeader] = value
	"""
	def __init__(self, headersList, reportData):
		self.reportData = {}
		for i in range(len(headersList)):
			self.reportData[headersList[i]] = reportData[i] 

	def MeetsConditions(self, conditions):
		for key, value in conditions:
			if self.reportData[key] != value:
				return False
		return True
	
	def prune(self, headers):
		prunedReport = {}
		for key, value in headers.headers:
			#TODO: possibly throw missing header error here?
			prunedReport[key] = self.reportData[key]
		return prunedReport
		