#see https://www.codementor.io/kiok46/beginner-kivy-tutorial-basic-crash-course-for-apps-in-kivy-y2ubiq0gz
from __future__ import division
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
import sys

import requests
#import xlsxwriter

from os import listdir 
kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

class QueryWeatherDataButton(Button):
    pass

class QueryWeatherYearDataButton(Button):
    pass

class YearButton(Button):
    pass

class YearPlusButton(Button):
    pass

class YearMinusButton(Button):
    pass

class Container(GridLayout):
    display = ObjectProperty()


    def increment_year(self):
        value = int(self.year_button.text)
        self.year_button.text = str(value+1)

    def decrement_year(self):
        value = int(self.year_button.text)
        self.year_button.text = str(value-1)

    def query_weather_data(self):
        print "query_weather_data"
        try:
            url = 'https://www.wetter.com/wetter_aktuell/rueckblick/deutschland/weil/weil_der_stadt/DE0012247011.html?sid=Q440&timeframe=30d'
            headers = {'Accept': 'application/json, text/plain', 'Referer': 'http://www.wetter.com/wetter_aktuell/rueckblick/?id=DE0012247011', 'X-Requested-With': 'XMLHttpRequest'}
            
            text = ''
            r = requests.get(url, headers=headers)
            print r
            #print r.text
            response = r.text

            dateString = '\"date\":\"' #"date":"2018-05-27",
            tempMinString = '\"temperatureMin\":' #"temperatureMin":13.5,
            tempMaxString = '\"temperatureMax\":' #"temperatureMax":25.9,
            precipitationString = '\"precipitation\":' #"precipitation":0.2},
            
            if self.average_days.text.isdigit():
                days = int(self.average_days.text)
            else:
                self.display.text = 'The entered days for avarage calculation is no digit!'
                return

            daysSum = days * [0]
            daysSumThres = 40
            daysIndex = 0
                
            sumprecipitation = 0.0
            maxprecipitation = 0.0
            maxprecipitationDay = 0
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
                        text += '\n  %s %s liter   ( %d days sum: %s)' %(day, str(precipitation).rjust(5,'_'), int(days), str(sumOfRain).rjust(5,'_'))
                    row += 1
            
            text += '\n\n  Precipitation over the last %d Days:\n  %.2f liter' %(row, sumprecipitation)
            #text += '\n  Average Precipitation per year:\n  %.2f liter' %(sumprecipitation/(row/365))
            text += '\n  Max precipitation over the last %d Days:\n  %.2f liter per Day (%s)' %(row, maxprecipitation, maxprecipitationDay)
            #print text
            self.display.text = text
        except:
            error = "Unexpected error:" + str(sys.exc_info()[0])
            print error
            self.display.text = error
        finally:
            print "Finished"

    def query_year_data(self):
        print "query_year_data"
        try:
            url = 'https://www.wetter.com/wetter_aktuell/rueckblick/deutschland/weil/weil_der_stadt/DE0012247011.html?sid=Q440&timeframe=10y'
            headers = {'Accept': 'application/json, text/plain', 'Referer': 'http://www.wetter.com/wetter_aktuell/rueckblick/?id=DE0012247011', 'X-Requested-With': 'XMLHttpRequest'}
            
            text = ''
            r = requests.get(url, headers=headers)
            print r
            #print r.text
            response = r.text

            dateString = '\"date\":\"' #"date":"2018-05-27",
            tempMinString = '\"temperatureMin\":' #"temperatureMin":13.5,
            tempMaxString = '\"temperatureMax\":' #"temperatureMax":25.9,
            precipitationString = '\"precipitation\":' #"precipitation":0.2},
            
            if self.average_days.text.isdigit():
                days = int(self.average_days.text)
            else:
                self.display.text = 'The entered days for avarage calculation is no digit!'
                return
                
            sum1 = 0.0 #January
            days1 = 0 #January
            sum2 = 0.0
            days2 = 0
            sum3 = 0.0
            days3 = 0
            sum4 = 0.0
            days4 = 0
            sum5 = 0.0
            days5 = 0
            sum6 = 0.0
            days6 = 0
            sum7 = 0.0
            days7 = 0
            sum8 = 0.0
            days8 = 0
            sum9 = 0.0
            days9 = 0
            sum10 = 0.0
            days10 = 0
            sum11 = 0.0
            days11 = 0
            sum12 = 0.0
            days12 = 0
            sumprecipitation = 0.0
            maxprecipitation = 0.0
            maxprecipitationDay = 0
            row = 0
            for line in response.splitlines():
                result_dateString = line.find(dateString)
                result_tempMinString = line.find(tempMinString)
                result_tempMaxString = line.find(tempMaxString)
                result_precipitationString = line.find(precipitationString)
                if(result_dateString != -1 and result_tempMinString != -1 and result_tempMaxString != -1 and result_precipitationString != -1):
                    day = line[(result_dateString+len(dateString)):(result_tempMinString-2)]
                    #Analyze for current year only
                    if(day.find(self.year_button.text)!= -1):
                        tempMin = line[(result_tempMinString+len(tempMinString)):(result_tempMaxString-1)]
                        tempMax = line[(result_tempMaxString+len(tempMaxString)):(result_precipitationString-1)]
                        precipitation = line[(result_precipitationString+len(precipitationString)):(line.find("},"))]
                        print "date: %s, tempMin: %s, tempMax: %s, precipitation: %s" %(day, tempMin, tempMax, precipitation)
                        #print "%d %d %d %d: %s" %(result_dateString, result_tempMinString, result_tempMaxString, result_precipitationString,line) 

                        precipitation = float(precipitation)
                        if precipitation > maxprecipitation:
                            maxprecipitation = precipitation
                            maxprecipitationDay = day
                        #print type(precipitation)
                        if precipitation is None:
                            pass
                        else:             
                            if(day.find('-01-')!= -1):
                                sum1 += precipitation
                                days1 += 1
                            elif(day.find('-02-')!= -1):
                                sum2 += precipitation
                                days2 += 1
                            elif(day.find('-03-')!= -1):
                                sum3 += precipitation
                                days3 += 1
                            elif(day.find('-04-')!= -1):
                                sum4 += precipitation
                                days4 += 1
                            elif(day.find('-05-')!= -1):
                                sum5 += precipitation
                                days5 += 1
                            elif(day.find('-06-')!= -1):
                                sum6 += precipitation
                                days6 += 1
                            elif(day.find('-07-')!= -1):
                                sum7 += precipitation
                                days7 += 1
                            elif(day.find('-08-')!= -1):
                                sum8 += precipitation
                                days8 += 1
                            elif(day.find('-09-')!= -1):
                                sum9 += precipitation
                                days9 += 1
                            elif(day.find('-10-')!= -1):
                                sum10 += precipitation
                                days10 += 1
                            elif(day.find('-11-')!= -1):
                                sum11 += precipitation
                                days11 += 1
                            elif(day.find('-12-')!= -1):
                                sum12 += precipitation
                                days12 += 1

                            sumprecipitation = sumprecipitation + precipitation
                            cell = day #time.strftime('%Y-%m-%d', time.localtime(day))
                            #text += '\n  %s %s liter   ( %d days sum: %s)' %(day, str(precipitation).rjust(5,'_'), int(days), str(sumOfRain).rjust(5,'_'))
                        row += 1
                    else:
                        pass
            text += '\n  %s %s    %d days' %('01:'.ljust(5, ' '), str(sum1).rjust(8,'_'), days1)
            text += '\n  %s %s    %d days' %('02:'.ljust(5, ' '), str(sum2).rjust(8,'_'), days2)
            text += '\n  %s %s    %d days' %('03:'.ljust(5, ' '), str(sum3).rjust(8,'_'), days3)
            text += '\n  %s %s    %d days' %('04:'.ljust(5, ' '), str(sum4).rjust(8,'_'), days4)
            text += '\n  %s %s    %d days' %('05:'.ljust(5, ' '), str(sum5).rjust(8,'_'), days5)
            text += '\n  %s %s    %d days' %('06:'.ljust(5, ' '), str(sum6).rjust(8,'_'), days6)
            text += '\n  %s %s    %d days' %('07:'.ljust(5, ' '), str(sum7).rjust(8,'_'), days7)
            text += '\n  %s %s    %d days' %('08:'.ljust(5, ' '), str(sum8).rjust(8,'_'), days8)
            text += '\n  %s %s    %d days' %('09:'.ljust(5, ' '), str(sum9).rjust(8,'_'), days9)
            text += '\n  %s %s    %d days' %('10:'.ljust(5, ' '), str(sum10).rjust(8,'_'), days10)
            text += '\n  %s %s    %d days' %('11:'.ljust(5, ' '), str(sum11).rjust(8,'_'), days11)
            text += '\n  %s %s    %d days' %('12:'.ljust(5, ' '), str(sum12).rjust(8,'_'), days12)
            text += '\n\n  Precipitation over the last %d Days:\n  %.2f liter' %(row, sumprecipitation)
            text += '\n  Average Precipitation per year:\n  %.2f liter' %(sumprecipitation/(row/365))
            text += '\n  Max precipitation over the last %d Days:\n  %.2f liter per Day (%s)' %(row, maxprecipitation, maxprecipitationDay)
            #print text
            self.display.text = text
        except:
            error = "Unexpected error:" + str(sys.exc_info()[0])
            print error
            self.display.text = error
            #raise
        finally:
            print "Finished"

class MainApp(App):

    def build(self):
        self.title = 'Query Weather Data Weil der Stadt'
        return Container()

if __name__ == "__main__":
    app = MainApp()
    app.run()