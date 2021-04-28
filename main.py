from selenium import webdriver

driver=webdriver.Chrome("chromedriver.exe")
driver.get("http://www.du.ac.in/index.php?page=colleges-at-du")

#selecting A
driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/a[1]")
driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/a[2]")

#selecting B
driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/a[1]")
colleges_name=[]
their_websites=[]
for i in range(1,27):
    for t in range(1,23):
        try:
            college=driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div/div[1]/div[1]/div["+str(i)+"]/div/a["+str(t)+"]").text
            colleges_name.append(college)
            link=driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div/div[1]/div[1]/div["+str(i)+"]/div/a["+str(t)+"]").get_attribute("href")
            their_websites.append(link)
        except Exception:
            break


# print(colleges_name)
# print(their_websites)
# print("this is the length of college name :",len(colleges_name))
# print("this is the length of websites :",len(their_websites))
#
#
# import pandas as pd
#
# percentile_list = pd.DataFrame({'College Names': colleges_name,
#      'Websites': their_websites
#     }).to_excel("Details_ip.xlsx",index=False)