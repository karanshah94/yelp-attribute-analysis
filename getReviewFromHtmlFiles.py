import os
import time
from bs4 import BeautifulSoup
cuisine = input("Enter the cuisine: ")
path = "HtmlFiles/"+cuisine+"/"
fw = open('reviews_'+cuisine+'.txt', 'w')
count = 1
for filename in os.listdir(path):
    print (path+filename)
    soup = None
    for i in range(5):  # try 5 times
        try:
            soup = BeautifulSoup(open(path+filename), "html.parser")
            break  # we got the file, break the loop
        except Exception as e:  # browser.open() threw an exception, the attempt to get the response failed
            print('failed attempt', i)
            time.sleep(2)  # wait 2 secs

    if not soup: continue  # couldnt get the page, ignore

    reviews = soup.findAll('div', {'class': 'review-content'})  # get all the review divs
    for review in reviews:
        text = review.find('p',{'lang': 'en'})
        if text:
            #print (count,text.text)
            fw.write(str(count)+". "+text.text+'\n')
            count += 1


