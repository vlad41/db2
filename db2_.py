import requests #импортируем модуль
import csv
import py7zr
import psycopg2
from datetime import datetime


# import bd1

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

# s = 0
# cur.execute('''SELECT COUNT(*) FROM ZNO;''')
# rows = cur.fetchall()
# for row in rows:
#     if row[0] > 500000:
#         s = 1


# s = 0
# cur.execute('''SELECT COUNT(*) FROM zno_people1;''')
# rows = cur.fetchall()
# for row in rows:
#     print(row[0])
#
# if s == 0:
#     create1()

# Порівняти середній бал з Української мови та літератури у кожному регіоні у 2020
# та 2019 роках серед тих кому було зараховано тест
cur.execute('''DROP Table IF EXISTS table1; DROP Table IF EXISTS table2;''')
cur.execute('''SELECT UkrPTRegName, AVG(UkrBall100) AS Year_2019 INTO TABLE1 FROM zno_ukr WHERE (Year = 2019 and UkrBall100 > 0) GROUP BY UkrPTRegName; 
	SELECT UkrPTRegName, AVG(UkrBall100) AS Year_2020 INTO TABLE2 FROM ZNO WHERE (Year = 2020 and UkrBall100 > 0) 
	GROUP BY UkrPTRegName; SELECT TABLE1.UkrPTRegName, TABLE1.Year_2019, TABLE2.Year_2020 FROM TABLE1, TABLE2 WHERE TABLE1.UkrPTRegName = TABLE2.UkrPTRegName ORDER BY TABLE1.Year_2019 DESC;''')

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

con.commit()
cur.close()
con.close()
