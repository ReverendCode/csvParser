from flask import Flask, render_template, request
import Reports

app = Flask(__name__)

def getHeaders():
	fileIO = Reports.FileIO()
	data = fileIO.LoadCSV('file.csv')
	headerDict = Reports.HeaderDictionary(fileIO.LoadOrCreateDictionary('headerDict.txt'))
	headerDict.AddHeaders(data.pop(0))
	return headerDict

def saveHeaders(headers):
	fileIO = Reports.FileIO()
	fileIO.SaveDictionary('headerDict.txt',headers)

def getReportHeaders(reportType):
	pass

@app.route('/')
def main_page():
	return render_template('main.html', name = 'Turtle Watch')

@app.route('/update_name', methods=['POST'])
def update_name():
	key = request.form['key']
	value = request.form['value']
	kind = request.form['reportType']
	allHeaders = getHeaders()
	allHeaders.UpdateHeaders({key:value})
	saveHeaders(allHeaders.headers)
	return render_template('edit_report.html', allHeaders = allHeaders.headers, reportType=kind) 

@app.route('/edit_report/<reportType>')
def edit_report(reportType):
	headerDict = getHeaders()
	reportHeaders = getReportHeaders(reportType)
	return render_template('edit_report.html', allHeaders = headerDict.headers, reportType=reportType) 

@app.route('/get_reports/<reportType>')
def get_reports(reportType):
	pass


if __name__ == '__main__':
   app.run()