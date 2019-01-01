#import time
from __future__ import division
import requests
import xlsxwriter

#Wireshark Filter:
#(ip.src== 192.168.178.31 and ip.dst== 62.138.109.56) or( ip.src== 62.138.109.56 and ip.dst== 192.168.178.31)

try:
    url = 'https://www.wetter.com/wetter_aktuell/rueckblick/deutschland/weil/weil_der_stadt/DE0012247011.html?sid=Q440&timeframe=1y'
    #url = 'https://www.wetter.com/wetter_aktuell/rueckblick/deutschland/weil/weil_der_stadt/DE0012247011.html?sid=Q440&timeframe=10y'
    headers = {'Accept': 'application/json, text/plain', 'Referer': 'http://www.wetter.com/wetter_aktuell/rueckblick/?id=DE0012247011', 'X-Requested-With': 'XMLHttpRequest'}
    
    print(1)
    r = requests.get(url, headers=headers)
    print(r)
    #print r.text
    response = r.text

    dateString = '\"date\":\"' #"date":"2018-05-27",
    tempMinString = '\"temperatureMin\":' #"temperatureMin":13.5,
    tempMaxString = '\"temperatureMax\":' #"temperatureMax":25.9,
    precipitationString = '\"precipitation\":' #"precipitation":0.2},
    
    days = 5
    daysSum = days * [0]
    daysSumThres = 40
    daysIndex = 0
        
    sumprecipitation = 0.0
    maxprecipitation = 0.0
    maxprecipitationDay = 0
    excelOutfile = 'out.xlsx'
    f_out = open(excelOutfile, 'w')
    workbook   = xlsxwriter.Workbook(excelOutfile)
    format_green = workbook.add_format()
    format_green.set_bg_color('green')
    format_yellow = workbook.add_format()
    format_yellow.set_bg_color('yellow')
    format_orange = workbook.add_format()
    format_orange.set_bg_color('orange')
    format_red = workbook.add_format()
    format_red.set_bg_color('red')
    worksheet1 = workbook.add_worksheet()
    row = 0
    for line in response.splitlines():
        result_dateString = line.find(dateString)
        result_tempMinString = line.find(tempMinString)
        result_tempMaxString = line.find(tempMaxString)
        result_precipitationString = line.find(precipitationString)
        if(result_dateString != -1 and result_tempMinString != -1 and result_tempMaxString != -1 and result_precipitationString != -1):
            day = line[(result_dateString+len(dateString)):(result_tempMinString-2)]
            tempMin = line[(result_tempMinString+len(tempMinString)):(result_tempMaxString-1)]
            tempMax = line[(result_tempMaxString+len(tempMaxString)):(result_precipitationString-1)]
            precipitation = line[(result_precipitationString+len(precipitationString)):(line.find("},"))]
            #print "date: %s, tempMin: %s, tempMax: %s, precipitation: %s" %(day, tempMin, tempMax, precipitation)
            #print "%d %d %d %d: %s" %(result_dateString, result_tempMinString, result_tempMaxString, result_precipitationString,line) 

            th = float(tempMin)
            tl = float(tempMax)
            precipitation = float(precipitation)
            if precipitation > maxprecipitation:
                maxprecipitation = precipitation
                maxprecipitationDay = day
            #print type(precipitation)
            if precipitation is None:
                pass
            else:
                daysSum[daysIndex] = precipitation
                daysIndex += 1
                if(daysIndex == days):
                    daysIndex = 0
                    
                sumOfRain = sum(daysSum)
                    
                sumprecipitation = sumprecipitation + precipitation
                cell = day #time.strftime('%Y-%m-%d', time.localtime(day))
                worksheet1.write(row, 0, cell)
                if sumOfRain > daysSumThres:
                    worksheet1.write_number(row, 1, precipitation, format_red)
                else:
                    worksheet1.write_number(row, 1, precipitation)

            #print '\nDay: %s' %day #time.strftime('\nDay: %Y-%m-%d %H:%M:%S', time.localtime(day))
            #print 'Temp High: %s C' %(th)
            #print 'Temp Low: %s C' %(tl)
            #print 'Precipitation: %s liter' %(precipitation)
            #print '%d day sum: %.2f liter' %( days, sumOfRain)
            row += 1
    
    print '\nPrecipitation over the last %d Days: %.2f liter' %(row, sumprecipitation)
    print '\nAverage Precipitation per year: %.2f liter' %(sumprecipitation/(row/365))
    print '\nMax precipitation over the last %d Days: %.2f liter per Day (%s)' %(row, maxprecipitation, maxprecipitationDay)
    #print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))
finally:
    f_out.close()
    workbook.close()
    print("Finished")