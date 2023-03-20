import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path="C:\Development\chromedriver.exe"
driver=webdriver.Chrome(chrome_driver_path)


try:
    driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
    
#--------------------------------Get elements -----------------------------------# 
    cookie=driver.find_element(by=By.ID,value="cookie")
    money=driver.find_element(By.ID,"money").text
    features=driver.find_elements(by=By.CSS_SELECTOR,value="#store div b")
    cps=driver.find_element(By.ID,"cps")
    
                   
                    
   
    prices=[]
    for feature in features[:8]:
        price=feature.text.split("\n")[0].split("-")[1].replace(",","")
        prices.append(float(price))

        
    
    timeout=time.time()+5
    fivemin = time.time() + 60*5   # 5 minutes from now
    
    

    
    
    while True:
        if time.time()>timeout:
            money=driver.find_element(By.ID,"money").text.replace(",","")
            #search for the affordable features 
            affordable_features=[price for price in prices if price <money ]
            feature_to_buy_index=len(affordable_features)
            #choose the most expensive one
            feature_to_buy=driver.find_element(by=By.CSS_SELECTOR,value="#store :nth-child({feature_to_buy_index}+1)")
            #buy the most expensive one
            feature_to_buy.click()
            
            
            
            timeout=5+time.time()
            
        cookie.click()
        if time.time() > fivemin:
            print(cps.text)
        
    
except   :
    print("error")
finally:
    driver.close()


