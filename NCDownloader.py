import sys, getopt
import subprocess
import datetime

if len(sys.argv) != 4:
    print("Usage: {} <GOES16 | GOES17> <start_date(MM/DD/YY)> <end_date(MM/DD/YY)>".format(sys.argv[0]))
    sys.exit(2)
    
bucket = sys.argv[1]
startDateStr = sys.argv[2]
endDateStr = sys.argv[3]

bucketName1 = "gcp-public-data-goes-16"
bucketName2 = "gcp-public-data-goes-17"

bucketName = bucketName1 if bucket == 'GOES16' else bucketName2

startDateObj = datetime.datetime.strptime(startDateStr, '%m/%d/%y')
startDayCount = (startDateObj - datetime.datetime(startDateObj.year, 1, 1)).days + 1

endDateObj = datetime.datetime.strptime(endDateStr, '%m/%d/%y')
endDayCount = (endDateObj - datetime.datetime(endDateObj.year, 1, 1)).days + 1

totalDays = endDayCount - startDayCount
glmDataType = "GLM-L2-LCFA"
year = str(startDateObj.year)

while totalDays >= 0:
    day = str(startDayCount).zfill(3)
    path = "gs://" + bucketName + "/" + glmDataType + "/" + year + "/" + day
    completed = subprocess.run('gsutil -m cp -r ' + path + ' .', shell=True)
    #print(path)
    totalDays -= 1
    startDayCount += 1
    if completed.returncode != 0:
        break
