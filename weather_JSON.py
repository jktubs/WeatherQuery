import time
import requests
import xlsxwriter

#Wireshark Filter:
#(ip.src== 192.168.178.31 and ip.dst== 62.138.109.56) or( ip.src== 62.138.109.56 and ip.dst== 192.168.178.31)

try:
    #url = 'http://www.wetter.com/wetter_aktuell/rueckblickdata/?code=Q440&offset=4'
    #headers = {'Accept': 'application/json, text/plain', 'Referer': 'http://www.wetter.com/wetter_aktuell/rueckblick/?id=DE0012247011', 'X-Requested-With': 'XMLHttpRequest'}
    url = 'http://www.wetter.com/wetter_aktuell/rueckblickdata/?code=Q440&offset=4'
    headers = {'Accept': 'application/json, text/plain', 'Referer': 'http://www.wetter.com/wetter_aktuell/rueckblick/?id=DE0012247011', 'X-Requested-With': 'XMLHttpRequest'}
    
    print 1
    r = requests.get(url, headers=headers)
    print r
    data = r.json()
    print 3
    #len(data)
    
    days = 5
    daysSum = days * [0]
    daysSumThres = 40
    daysIndex = 0
    
    
    
    sumRainFall = 0.0
    maxRainFall = 0.0
    maxRainFallDay = 0
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
    for element in data:
        day = element['x']
        th = element['th']
        tl = element['tl']
        rainfall = element['pd']
        if rainfall > maxRainFall:
            maxRainFall = rainfall
            maxRainFallDay = day
        #print type(rainfall)
        if rainfall is None:
            pass
        else:
            daysSum[daysIndex] = rainfall
            daysIndex += 1
            if(daysIndex == days):
                daysIndex = 0
                
            sumOfRain = sum(daysSum)
                
            sumRainFall = sumRainFall + rainfall
            cell = time.strftime('%Y-%m-%d', time.localtime(day))
            worksheet1.write(row, 0, cell)
            if sumOfRain > daysSumThres:
                worksheet1.write_number(row, 1, rainfall, format_red)
            else:
                worksheet1.write_number(row, 1, rainfall)

        print time.strftime('\nDay: %Y-%m-%d %H:%M:%S', time.localtime(day))
        print 'Temp High: %s' %(th)
        print 'Temp Low: %s' %(tl)
        print 'Rainfall: %s liter' %(rainfall)
        print '%d day sum: %.2f' %( days, sumOfRain)
        row += 1
    
    print '\nRainfall over the last 365 Days: %.2f liter' %(sumRainFall)
    print '\nMax Rainfall over the last 365 Days: %.2f liter per Day (%s)' %(maxRainFall, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(maxRainFallDay)))
    #print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))
finally:
    f_out.close()
    workbook.close()

