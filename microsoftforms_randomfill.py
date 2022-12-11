import time
from time import sleep
from splinter import Browser  # based on selenium for auto testing
                              # beautifulsoup  is mainly scraping
                              #you need to install webdrivers
                              # scrapy module can be checked
from random import randint


t1=['blabla',' blala2','blabla3',' blala23','blabla4',' blala24','blabla5',' bl5555ala2']
t2=['blabla',' blala2','blabla3',' blala23','blabla4',' blala24','blabla5',' bl5555ala2']
t3=['blabla',' blala2','blabla3',' blala23','blabla4',' blala24','blabla5',' bl5555ala2']

def fillsuvey():# Fill in the url
    browser2.visit('https://forms.office.com/r/MFv5VKKtck')
    # Find the username form and fill it with the defined username
    b=browser2.find_by_tag('input')
    print('I have ',len(b),' input boxes')
    x=randint(0,4)
    print('this is x for level',x)
   
    b[randint(0,2)].click()
    b[randint(3,5)].click()
    
    
    
    a=browser2.find_by_tag('textarea')
    print('textareas: ',len(a))
    a[0].fill(t1[randint(0,7)])
    a[1].fill(t2[randint(0,7)])
    b[6].fill(t3[randint(0,7)])
   
   #name=browser2.find_by_xpath('//*[@id="SelectId_0"]/div[2]/div[2]')

  #  name.click()
    
    
    a=browser2.find_by_tag('button').last
    
    a.click()
    sleep(3)
    
x=0 
for i in range(2000):
    sleep(2)
    browser2 = Browser()

    fillsuvey()
    x=x+1
    print(x)  
    sleep(2)
    browser2.quit()
    
