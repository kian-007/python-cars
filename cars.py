import requests
from bs4 import BeautifulSoup
import re
import psycopg2
from psycopg2 import Error

temp = list(range(1, 51))
pages2 = []
for i in temp:
    pages2.append(str(i))
count = 0
for j in pages2:
    res = requests.get('https://bama.ir/car/all-brands/all-models/all-trims?page=%s' %(j))
    #res = requests.get('https://bama.ir/car/all-brands/all-models/all-trims?page=3')
    print(res, count)
    count += 1 
    soup = BeautifulSoup(res.text, 'html.parser')
    cars_title = soup.find_all('a', attrs={'class': 'cartitle-desktop'})
    prices = soup.find_all('p', attrs={'class': 'cost'})
    km = soup.find_all('p', attrs={'class': 'price hidden-xs'})
    year = soup.find_all('span', attrs={'class': 'year-label visible-xs'})
    #print(cars_title[1].text)
    '''
        mylist = []
        for i in cars_title:
            mylist.append(re.sub(r'\s+', '', i.text))
        print(mylist[2])
    '''
    '''
        for i in mylist:
            print(i)
    '''
    '''
    for x,y,z,k in zip(year, cars_title, km, prices):
        print(re.sub(r'\s+', '', x.text).strip() +"\n"+ re.sub(r'\s+', '', y.text).strip() +"\n"+ re.sub(r'\s+', '', z.text).strip() +"\n"+ re.sub(r'\s+', '', k.text).strip() + "\n")
    '''
    #bara hazf karkard!
    #re.sub(r'(\s+)(کارکرد)', '', z.text
    
    idlist = list(range(1, 1000))
    list1 = []
    year2 = []
    for l in year:
        list1.append(re.sub(r'\s+', '', l.text).strip())
    #print(list1)
    for n in list1:
        year2.append(re.sub(r'،', '', n))
    #print(list2)
    

    list3 = []
    mainlist = []
    prices2 = []
    for u in prices:
        list3.append(re.sub(r'\s+', '', u.text).strip())
    #print(list3)
    for m in list3:
        mainlist.append(re.sub(r',', '', m))
    #print(mainlist)
    for p in mainlist:
        prices2.append(re.sub(r'تومان', '', p))
    #print(prices2)


    list5 = []
    titles2 = []
    for l in cars_title:
        list5.append(re.sub(r'\s+', '', l.text).strip())
    #print(list1)
    for n in list5:
        titles2.append(re.sub(r'،', ' ', n))
    #print(titles2)
    
    for i,x,y,z,k in zip(idlist, year2, titles2, km, prices2):
        try:
            connection = psycopg2.connect(user="python",
                                          password="king.kian007",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="dbpython")

            cursor = connection.cursor()
            # SQL query
            query = "insert into cars(year, title, km, price)values('%s', '%s', '%s', '%i');" %(x, y, re.sub(r'\s+', '', z.text).strip(), int(k))
            
            # Execute a command
            cursor.execute(query)
            
            print("sql query Executed successfully in PostgreSQL ")
            connection.commit()
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed", "\n")

    
    
