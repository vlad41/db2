import requests #импортируем модуль
import csv
import py7zr
import psycopg2
from datetime import datetime

def proverka_na_chislo(x):
    if x == 'null':
        return 0
    else:
        return float(x.replace(',', '.'))

# Встановлюємо з єднання з базою даних
con = psycopg2.connect(
  database="postgres",
  user="postgres",
  password="postgres",
  host="127.0.0.1",
  port="5432"
)

# Визиваємо курсор
cur = con.cursor()

# Створюємо таблицю для зберігання даних
cur.execute('''CREATE TABLE IF NOT EXISTS zno
     (OUTID TEXT UNIQUE, BIRTH INTEGER, SEXTYPENAME TEXT, REGNAME TEXT, AREANAME TEXT, TERNAME TEXT, REGTYPENAME TEXT, TerTypeName TEXT, ClassProfileNAME TEXT,
     ClassLangName TEXT, EONAME TEXT, EOTYPENAME TEXT, EORegName TEXT, EOAreaName TEXT, EOTerName TEXT, EOParent TEXT, UkrTest TEXT, UkrTestStatus TEXT, UkrBall100 REAL,
     UkrBall12 REAL, UkrBall REAL, UkrAdaptScale TEXT, UkrPTName TEXT, UkrPTRegName TEXT, UkrPTAreaName TEXT, UkrPTTerName TEXT, histTest TEXT, HistLang TEXT, histTestStatus TEXT,
     histBall100 REAL, histBall12 REAL, histBall REAL, histPTName TEXT, histPTRegName TEXT, histPTAreaName TEXT, histPTTerName TEXT, mathTest TEXT, mathLang TEXT, mathTestStatus TEXT,
     mathBall100 REAL, mathBall12 REAL, mathBall REAL, mathPTName TEXT, mathPTRegName TEXT, mathPTAreaName TEXT, mathPTTerName TEXT, physTest TEXT, physLang TEXT, physTestStatus TEXT,
     physBall100 REAL, physBall12 REAL, physBall REAL, physPTName TEXT, physPTRegName TEXT, physPTAreaName TEXT, physPTTerName TEXT, chemTest TEXT, chemLang TEXT, chemTestStatus TEXT, chemBall100 REAL,
     chemBall12 REAL, chemBall REAL, chemPTName TEXT, chemPTRegName TEXT, chemPTAreaName TEXT, chemPTTerName TEXT, bioTest TEXT, bioLang TEXT, bioTestStatus TEXT, bioBall100 REAL, bioBall12 REAL,
     bioBall REAL,bioPTName TEXT, bioPTRegName TEXT, bioPTAreaName TEXT, bioPTTerName TEXT, geoTest TEXT, geoLang TEXT, geoTestStatus TEXT, geoBall100 REAL, geoBall12 REAL,
     geoBall REAL, geoPTName TEXT, geoPTRegName TEXT, geoPTAreaName TEXT, geoPTTerName TEXT, engTest TEXT, engTestStatus TEXT, engBall100 REAL, engBall12 REAL, engDPALevel TEXT,
     engBall REAL, engPTName TEXT, engPTRegName TEXT, engPTAreaName TEXT, engPTTerName TEXT, fraTest TEXT, fraTestStatus TEXT, fraBall100 REAL, fraBall12 REAL, fraDPALevel TEXT,
     fraBall REAL, fraPTName TEXT, fraPTRegName TEXT, fraPTAreaName TEXT, fraPTTerName TEXT, deuTest TEXT, deuTestStatus TEXT, deuBall100 REAL, deuBall12 REAL, deuDPALevel TEXT,
     deuBall REAL, deuPTName TEXT, deuPTRegName TEXT, deuPTAreaName TEXT, deuPTTerName TEXT, spaTest TEXT, spaTestStatus TEXT, spaBall100 REAL, spaBall12 REAL, spaDPALevel TEXT,
     spaBall REAL, spaPTName TEXT, spaPTRegName TEXT, spaPTAreaName TEXT, spaPTTerName TEXT, YEAR INTEGER );''')

con.commit()

# Зкачуємо з сайта інформацію в заархивованих файлах за 2 роки
f=open(r'zno\OpenDataZNO2019.7z',"wb") #открываем файл для записи, в режиме wb
file_2019 = requests.get("https://zno.testportal.com.ua/yearstat/uploads/OpenDataZNO2019.7z") #делаем запрос
f.write(file_2019.content) #записываем содержимое в файл; как видите - content запроса
f.close()

f=open(r'zno\OpenDataZNO2020.7z',"wb") #открываем файл для записи, в режиме wb
file_2020 = requests.get("https://zno.testportal.com.ua/yearstat/uploads/OpenDataZNO2020.7z") #делаем запрос
f.write(file_2020.content) #записываем содержимое в файл; как видите - content запроса
f.close()

# Разархівуємо в папку
archive = py7zr.SevenZipFile('zno\OpenDataZNO2020.7z', mode='r')
archive.extractall(path="zno")
archive.close()

archive = py7zr.SevenZipFile('zno\OpenDataZNO2019.7z', mode='r')
archive.extractall(path="zno")
archive.close()

time0 = datetime.now().microsecond
# Відкриваємо файл за 2020 рік та зберігаємо інформацію з необхідних полів у БД
files = ["zno\Odata2019File.csv", "zno\Odata2020File.csv"]
years = [2019, 2020]
num = 0
k=0
while num != 2:
    with open(files[num]) as r_file:
        file_reader = csv.reader(r_file, delimiter=';')
        try:
            for row in file_reader:
                    if k > 0:
                        OUTID = row[0]
                        Birth = row[1]
                        SEXTYPENAME = row[2]
                        REGNAME = row[3]
                        AREANAME = row[4]
                        TERNAME = row[5]
                        REGTYPENAME = row[6]
                        TerTypeName = row[7]
                        ClassProfileNAME = row[8]
                        ClassLangName= row[9]
                        EONAME = row[10]
                        EOTYPENAME = row[11]
                        EORegName = row[12]
                        EOAreaName = row[13]
                        EOTerName = row[14]
                        EOParent = row[15]
                        UkrTest= row[16]
                        UkrTestStatus = row[17]
                        UkrBall100 = proverka_na_chislo(row[18])
                        UkrBall12 = proverka_na_chislo (row[19])
                        UkrBall= proverka_na_chislo (row[20])
                        UkrAdaptScale = row[21]
                        UkrPTName = row[22]
                        UkrPTRegName= row[23]
                        UkrPTAreaName = row[24]
                        UkrPTTerName= row[25]
                        histTest= row[26]
                        HistLang = row[27]
                        histTestStatus = row[28]
                        histBall100 =  proverka_na_chislo (row[29])
                        histBall12 =  proverka_na_chislo (row[30])
                        histBall= proverka_na_chislo (row[31])
                        histPTName = row[32]
                        histPTRegName= row[33]
                        histPTAreaName = row[34]
                        histPTTerName= row[35]
                        mathTest = row[36]
                        mathLang = row[37]
                        mathTestStatus = row[38]
                        mathBall100 = proverka_na_chislo(row[39])
                        mathBall12 = proverka_na_chislo(row[40])
                        mathBall = proverka_na_chislo(row[41])
                        mathPTName = row[42]
                        mathPTRegName = row[43]
                        mathPTAreaName = row[44]
                        mathPTTerName = row[45]
                        physTest = row[46]
                        physLang = row[47]
                        physTestStatus= row[48]
                        physBall100 = proverka_na_chislo(row[49])
                        physBall12 = proverka_na_chislo(row[50])
                        physBall = proverka_na_chislo(row[51])
                        physPTName = row[52]
                        physPTRegName = row[53]
                        physPTAreaName = row[54]
                        physPTTerName = row[55]
                        chemTest = row[56]
                        chemLang = row[57]
                        chemTestStatus = row[58]
                        chemBall100 = proverka_na_chislo(row[59])
                        chemBall12 = proverka_na_chislo(row[60])
                        chemBall = proverka_na_chislo(row[61])
                        chemPTName = row[62]
                        chemPTRegName = row[63]
                        chemPTAreaName = row[64]
                        chemPTTerName = row[65]
                        bioTest= row[66]
                        bioLang= row[67]
                        bioTestStatus = row[68]
                        bioBall100 = proverka_na_chislo(row[69])
                        bioBall12 = proverka_na_chislo(row[70])
                        bioBall = proverka_na_chislo(row[71])
                        bioPTName = row[72]
                        bioPTRegName= row[73]
                        bioPTAreaName = row[74]
                        bioPTTerName= row[75]
                        geoTest= row[76]
                        geoLang = row[77]
                        geoTestStatus = row[78]
                        geoBall100 = proverka_na_chislo(row[79])
                        geoBall12 = proverka_na_chislo(row[80])
                        geoBall = proverka_na_chislo(row[81])
                        geoPTName = row[82]
                        geoPTRegName = row[83]
                        geoPTAreaName = row[84]
                        geoPTTerName= row[85]
                        engTest= row[86]
                        engTestStatus = row[87]
                        engBall100 = proverka_na_chislo(row[88])
                        engBall12 = proverka_na_chislo(row[89])
                        engDPALevel = row[90]
                        engBall= proverka_na_chislo(row[91])
                        engPTName = row[92]
                        engPTRegName = row[93]
                        engPTAreaName = row[94]
                        engPTTerName = row[95]
                        fraTest= row[96]
                        fraTestStatus = row[97]
                        fraBall100 = proverka_na_chislo(row[98])
                        fraBall12 = proverka_na_chislo(row[99])
                        fraDPALevel = row[100]
                        fraBall = proverka_na_chislo(row[101])
                        fraPTName = row[102]
                        fraPTRegName= row[103]
                        fraPTAreaName = row[104]
                        fraPTTerName = row[105]
                        deuTest = row[106]
                        deuTestStatus = row[107]
                        deuBall100 =  proverka_na_chislo(row[108])
                        deuBall12 = proverka_na_chislo(row[109])
                        deuDPALevel = row[110]
                        deuBall= proverka_na_chislo(row[111])
                        deuPTName = row[112]
                        deuPTRegName = row[113]
                        deuPTAreaName = row[114]
                        deuPTTerName= row[115]
                        spaTest= row[116]
                        spaTestStatus = row[117]
                        spaBall100 = proverka_na_chislo(row[118])
                        spaBall12 = proverka_na_chislo(row[119])
                        spaDPALevel = row[120]
                        spaBall = proverka_na_chislo(row[121])
                        spaPTName = row[122]
                        spaPTRegName= row[123]
                        spaPTAreaName = row[124]
                        spaPTTerName = row[125]
                        year = years[num]
                        cur.execute('''INSERT INTO zno(OUTID,Birth,SEXTYPENAME,REGNAME,AREANAME,TERNAME,REGTYPENAME,TerTypeName,ClassProfileNAME,ClassLangName,EONAME,EOTYPENAME,EORegName,EOAreaName,EOTerName,EOParent,UkrTest,UkrTestStatus,UkrBall100,UkrBall12,UkrBall,UkrAdaptScale,UkrPTName,UkrPTRegName,UkrPTAreaName,UkrPTTerName,histTest,HistLang,histTestStatus,histBall100,histBall12,histBall,histPTName,histPTRegName,histPTAreaName,histPTTerName,mathTest,mathLang,mathTestStatus,mathBall100,mathBall12,mathBall,mathPTName,mathPTRegName,mathPTAreaName,mathPTTerName,physTest,physLang,physTestStatus,physBall100,physBall12,physBall,physPTName,physPTRegName,physPTAreaName,physPTTerName,chemTest,chemLang,chemTestStatus,chemBall100,chemBall12,chemBall,chemPTName,chemPTRegName,chemPTAreaName,chemPTTerName,bioTest,bioLang,bioTestStatus,bioBall100,bioBall12,bioBall,bioPTName,bioPTRegName,bioPTAreaName,bioPTTerName,geoTest,geoLang,geoTestStatus,geoBall100,geoBall12,geoBall,geoPTName,geoPTRegName,geoPTAreaName,geoPTTerName,engTest,engTestStatus,engBall100,engBall12,engDPALevel,engBall,engPTName,engPTRegName,engPTAreaName,engPTTerName,fraTest,fraTestStatus,fraBall100,fraBall12,fraDPALevel,fraBall,fraPTName,fraPTRegName,fraPTAreaName,fraPTTerName,deuTest,deuTestStatus,deuBall100,deuBall12,deuDPALevel,deuBall,deuPTName,deuPTRegName,deuPTAreaName,deuPTTerName,spaTest,spaTestStatus,spaBall100,spaBall12,spaDPALevel,spaBall,spaPTName,spaPTRegName,spaPTAreaName,spaPTTerName,Year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (OUTID) DO NOTHING;''', (OUTID , Birth, SEXTYPENAME, REGNAME, AREANAME, TERNAME, REGTYPENAME, TerTypeName,ClassProfileNAME,ClassLangName,EONAME ,EOTYPENAME ,EORegName ,EOAreaName ,EOTerName ,EOParent ,UkrTest,UkrTestStatus ,UkrBall100 ,UkrBall12 ,UkrBall,UkrAdaptScale ,UkrPTName , UkrPTRegName,UkrPTAreaName ,UkrPTTerName, histTest,HistLang ,histTestStatus ,histBall100 ,histBall12 ,histBall, histPTName ,histPTRegName,histPTAreaName, histPTTerName,mathTest ,mathLang ,mathTestStatus ,mathBall100 ,mathBall12 ,mathBall ,mathPTName , mathPTRegName ,mathPTAreaName ,mathPTTerName ,physTest ,physLang ,physTestStatus,physBall100 , physBall12 ,physBall,physPTName ,physPTRegName ,physPTAreaName ,physPTTerName ,chemTest , chemLang ,chemTestStatus ,chemBall100 ,chemBall12 ,chemBall ,chemPTName , chemPTRegName , chemPTAreaName ,chemPTTerName ,bioTest,bioLang,bioTestStatus ,bioBall100 ,bioBall12 ,bioBall , bioPTName ,bioPTRegName,bioPTAreaName ,bioPTTerName, geoTest,geoLang ,geoTestStatus ,geoBall100 , geoBall12 ,geoBall , geoPTName ,geoPTRegName , geoPTAreaName, geoPTTerName, engTest,engTestStatus ,engBall100 ,engBall12, engDPALevel ,engBall,	engPTName ,engPTRegName, engPTAreaName ,engPTTerName ,fraTest, fraTestStatus ,fraBall100 ,fraBall12 ,fraDPALevel ,fraBall , fraPTName , fraPTRegName,fraPTAreaName ,fraPTTerName ,deuTest ,deuTestStatus ,deuBall100 , deuBall12 ,deuDPALevel ,deuBall, deuPTName ,deuPTRegName ,deuPTAreaName ,deuPTTerName,spaTest, spaTestStatus ,spaBall100 ,spaBall12 ,spaDPALevel ,spaBall ,spaPTName, spaPTRegName, spaPTAreaName ,spaPTTerName ,year))
                    k = k+1

        except:
            print(f'Error on the line ', k-1)
            raise
        finally:
            r_file.close()
            con.commit()
    num = num + 1
    k = 0

print('Chas zagruzki:', time0 - datetime.now().microsecond)

cur.execute('''SELECT Regname, AVG(UkrBall100) AS Year_2019 INTO TABLE1 FROM ZNO WHERE Year = 2019 GROUP BY Regname; SELECT Regname, AVG(UkrBall100) AS Year_2020 INTO TABLE2 FROM ZNO WHERE Year = 2020  GROUP BY Regname; SELECT TABLE1.Regname, TABLE1.Year_2019, TABLE2.Year_2020 FROM TABLE1, TABLE2 WHERE TABLE1.Regname = TABLE2.Regname ORDER BY TABLE1.Year_2019 DESC;''')

rows = cur.fetchall()
with open('result.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=';')
    a.writerows(rows)

print('Область', 23 * ' ', 'за 2019 р.', ' за 2020 р.')
print('________________________________________________________________________________')
for row in rows:
    x_2019 = round(row[1], 2)
    x_2020 = round(row[2], 2)
    lentghSpace1 = 30 - len(row[0])
    lentghSpace2 = 11 - len(str(x_2019))
    if len(str(x_2019)) == 4:
        print(row[0], '', lentghSpace1 * ' ' , x_2019, lentghSpace2 * ' ', x_2020)
    elif len(str(x_2019)) == 5:
        print(row[0], '', lentghSpace1 * ' ' , x_2019, lentghSpace2 * ' ', x_2020)
    else:
        print(row[0], '', lentghSpace1 * ' ' , x_2019, lentghSpace2 * ' ', x_2020)

cur.close()
con.close()
