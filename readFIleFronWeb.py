from urllib import request

file_url = 'http://www.sample-videos.com/csv/Sample-Spreadsheet-100-rows.csv'

def downloadCSVFIle(csv_url):
    response = request.urlopen(csv_url)
    csvData = response.read()
    csvStrData = str(csvData)
    lines = csvStrData.split('\\n')
    dest_url = r'csvDatafromNet.csv'
    fw = open(dest_url, 'w')

    for line in lines:
        fw.write(line + "\n")
    fw.close()

downloadCSVFIle(file_url)