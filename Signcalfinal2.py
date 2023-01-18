import time
import requests
import dbm
import xlsxwriter
import codecs
import math
import pandas
import openpyxl
import csv
import degree
import pandas as pd
import datetime
import pytz
from datetime import datetime, timezone
import requests
from datetime import datetime, timedelta
import pytz
import os
import sys

sys.path.append('/Users/rohitsharma/opt/anaconda3/lib/python3.9/site-packages')


# Get command-line arguments
latitude = sys.argv[1]
longitude = sys.argv[2]
event = sys.argv[3]

def gpp(latitude, longitude, manifest):
    current_time = datetime.now(pytz.timezone("UTC"))
    current_time = current_time - timedelta(seconds=10)  # Subtract 10 seconds from current time
    current_date = current_time.date()
    current_time = current_time.time()
    tz_offset = datetime.now(pytz.timezone("UTC")).strftime("%z")
    day = current_date.day
    month = current_date.month
    year = current_date.year
    hour = current_time.hour
    min = current_time.minute
    global output; output = manifest
    return "Input received and script ran successfully"
    url = 'https://json.astrologyapi.com/v1/planets'
    payload = {'day': day, 'month': month, 'year': year, 'hour': hour, 'min': min, 'lat': latitude, 'lon': longitude, 'tzone': tz_offset}
    response = requests.get(url, params=payload)
    print(response.status_code)
    if response.status_code == 200:
        planetary_positions = response.json()
        return planetary_positions
    else:
        return None

gpp(lat,lon,event)
    
DC = [8,9,16]

d1deg = {'sun':(157,13), 
'moon':(173,6),
'mercury':(181,4),
'venus':(165,56),
'mars':(147,8),
'jupiter':(4,1),
'saturn':(201,53),
'uranus':(239,15),
'neptune':(251,33),
'pluto':(194,42),
'rahu':(338,40),
'ketu':(158,40),
'pranapada':(355,22)}                    #Dictionary with planetary positions in D1, values are in angles / degrees out of 360. 



lida = list(d1deg.values())              #lida is a list containing angular degree values of all planets from dictionary d1deg.
list_d1deg_deci = []
lidd = list_d1deg_deci                   #lidd is a list containing decimal values of degrees of all planets in the dictionary d1deg.              


for planet, (degree, minute) in d1deg.items():
    decimal_value = round(degree + (minute/60), 6)
    lidd.append(decimal_value)

print(lidd)

signit = ('aries','taurus','gemini','cancer','leo','virgo','libra','scorpio','saggitarius','capricorn','aquarius','pisces','justasign ')
planets = ('sun','moon','mercury','venus','mars','jupiter','saturn','uranus','neptune','pluto','rahu','ketu','pranapada')

d1deci_dict = dict(zip(planets,lidd))              #Dictionary like d1deg but all planets with their degrees in decimal values.       
d1dd = d1deci_dict

listofdegs = []
lsd = []
lsn = []

for value in lidd:
    x = value/30
    pending = x % 1
    sd1 = pending * 30
    lsd.append(sd1)
    if x < 1:
        sn = signit[0]

    elif 1 < x < 2:
        sn = signit[1]
                

    elif 2 < x < 3: 
        sn = signit[2]
                

    elif 3 < x < 4:
        sn = signit[3]
           

    elif 4 < x < 5:
        sn = signit[4]


    elif 5 < x < 6:
        sn = signit[5]
                

    elif 6 < x < 7: 
        sn = signit[6]
                

    elif 7 < x < 8:
        sn = signit[7]
                

    elif 8 < x < 9:
        sn = signit[8]
                

    elif 9 < x < 10:
        sn = signit[9]
                

    elif 10 < x < 11:
        sn = signit[10]
                


    elif 11 < x < 12: 
        sn = signit[11]
    
    lsn.append(sn)
                

dict_pl_deg = dict(zip(planets,lsd))            #dictionary showing planets with their degrees out of 30 in d1 chart. 



dict_pl_sn = dict(zip(planets,lsn))             #dictionary showing planets with their signs in d1 chart. 

d8dl = []
d9dl = []
d16dl = []
d8sl = []
d9sl = []
d16sl = []
    

    
def divisionalcharts(pl, deg, div):                #pl is for planet name, deg is for degrees in D1 out of 360, and div is for Divisional chart number.
    if deg > 360:
        print('Degrees cannot be more than 360')
        return None
    if deg < 0:
        print('Degrees cannot be less than Zero in this Program') 
        return None 
    if deg == 0: 
        print('Beginning of Zodiac at 0 means cuspal energy beyond cosmos, Please enter floating decimal degrees')
        return None
    com = 'The sign of' 
    com2 = 'in D'                                    #Gaurdiancode
    signs = 12
    d1_deg_ps = 30
    total_degrees = signs * d1_deg_ps                #total degrees in a zodiac circle
    td = total_degrees                               
    time_total_min = 24*60                           #total time minutes in full zodiac cycle of D1
    ttm = time_total_min
    divisional = div                                 #Which Divisional chart we wanna see
    sps_ddx = d1_deg_ps/div                          #Size of a Sign in Divisional Chart.
    
    total_deg_dc = sps_ddx * 12                      #total degrees in divisional chart.
    tdd = total_deg_dc
    
    degrees_in_d1 = deg
    signs_passed = deg/sps_ddx                       #Number of signs passed in the div chart                    
    
    sp = signs_passed
    
    charts_finished = sp / 12                        #Number of D charts of that Division that have finished a full sequence.
    cf = charts_finished
 
    dsd = cf % 1                                     #how much of this current cycle/sequence is finished out of whole in decimal percentage.                                   
    
    degofplindiv = dsd * tdd                         #how much of this current cycle/sequence is finished out of whole in angular degrees .             
    dpd = degofplindiv                               
    
    sign_of_div_passed = dpd / sps_ddx               #sings that have passed in this cycle/sequence. 
    sdp = sign_of_div_passed
    
    integerofsdp = sdp // 1
    intsdp = integerofsdp
    
    decimalversionofsdp = sdp % 1 
    dspd = decimalversionofsdp                       #degrees in decimal version before in the divisional chart sign. e.g 0.16 
    
    degrees_of_planet_in_divchart = dspd * d1_deg_ps
    degree_in_deci = degrees_of_planet_in_divchart   #THIS is the ACTUAL DEGREE in the sign of Div Chart. e.g 4.95
    
    int_deg = degree_in_deci // 1                    #integer part of above degree.
    
    ddd = degree_in_deci % 1                         #decimal part of above degree.                                     

    divdeg_out = int_deg + ddd
    
    minutes = ddd * 60                               #minutes version
    
    if minutes <=59:
        minutes = round(minutes)    
    else:
        int_deg = int_deg + 1
        int_deg = int(int_deg)
        minutes = 0

    if divisional == 8:
        d8dl.append(divdeg_out)
    elif divisional == 9:
        d9dl.append(divdeg_out)
    elif divisional == 16:
        d16dl.append(divdeg_out)
    else:
        print('D chart not in main program')
            
    if sdp < 1:
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[0]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchartnb = div
        divsign = signit[0]
        divdeg = int_deg + ddd
        dict_dg = {pname:divdeg}
        dict_sn = {pname:divsign}
       
        
    elif 1 < sdp < 2:
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[1]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchartnb = div
        divsign = signit[1]
        divdeg = int_deg + ddd
        dict_dg = {pname:divdeg}
        dict_sn = {pname:divsign}
        

    elif 2 < sdp < 3:
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[2]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchartnb = div
        divsign = signit[2]
        divdeg = int_deg + ddd        
        dict_dg = {pname:divdeg}
        dict_sn = {pname:divsign}
        

    elif 3 < sdp < 4:
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[3]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchartnb = div
        divsign = signit[3]
        divdeg = int_deg + ddd
        dict_dg = {pname:divdeg}
        dict_sn = {pname:divsign}
        
    elif 4 < sdp < 5:
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[4]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchartnb = div
        divsign = signit[4]
        divdeg = int_deg + ddd
        dict_dg = {pname:divdeg}
        dict_sn = {pname:divsign}
        
    elif 5 < sdp < 6:
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[5]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchartnb = div
        divsign = signit[5]
        divdeg = int_deg + ddd
        dict_dg = {pname:divdeg}
        dict_sn = {pname:divsign}
        
    elif 6 < sdp < 7:
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[6]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchartnb = div
        divsign = signit[6]
        divdeg = int_deg + ddd
        dict_dg = {pname:divdeg}
        dict_sn = {pname:divsign}
        
    elif 7 < sdp < 8:
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[7]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchartnb = div
        divsign = signit[7]
        divdeg = int_deg + ddd
    
    elif 8 < sdp < 9:
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[8]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchartnb = div
        divsign = signit[8]
        divdeg = int_deg + ddd
        dict_dg = {pname:divdeg}
        dict_sn = {pname:divsign}
        
    elif 9 < sdp < 10:
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[9]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchartnb = div
        divsign = signit[9]
        divdeg = int_deg + ddd
        dict_dg = {pname:divdeg}
        dict_sn = {pname:divsign}
       
    elif 10 < sdp < 11:
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[10]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchartnb = div
        divsign = signit[10]
        divdeg = int_deg + ddd
        dict_dg = {pname:divdeg}
        dict_sn = {pname:divsign}
       
    elif 11 < sdp < 12: 
        #print(str(com) + ' ' + str(pl) + ' ' + str(com2) + str(div) + ' ' + 'is' + ' ' + str(signit[11]) + ' ' + 'at' + ' ' + str(int_deg) + ' ' + 'degrees and' + ' ' + str(minutes) + ' ' + 'minutes')
        
        pname = pl
        dchart_nb = div
        divsign = signit[11]
        divdeg = int_deg + ddd
        dict_dg = {pname:divdeg}
        dict_sn = {pname:divsign}
        
    else: 
        print('Cuspal degrees, Please enter exact value with Decimal.') 
    
    if divisional == 8:
        d8sl.append(divsign)
    elif divisional == 9:
        d9sl.append(divsign)
    elif divisional == 16:
        d16sl.append(divsign)
    else:
        print('D Chart not in main program')
        
        
     
def dcrunner(k,v):
    dc = 0
    p = k
    deg = v
    while dc < len(DC):
        for dc in DC:
            divisionalcharts(p,deg,dc)
            
   
def valuesender():
    for key, value in d1dd.items():
        k = key
        v = value
        dcrunner(k,v)
                   
valuesender()

data = {
    'Planet': planets,
    'D1 degrees': lsd,
    'D1 signs': lsn,
    'D8 signs':d8sl,
    'D8 degrees':d8dl,
    'D9 signs':d9sl,
    'D9 degrees':d9dl,
    'D16 signs':d16sl,
    'D16 degrees':d16dl,
    'Result':output
        
}



print(data)

f = open('Alldcharts_wr_new.csv', 'w')
df.to_csv(f, index=False)
f.close()

exit()




        