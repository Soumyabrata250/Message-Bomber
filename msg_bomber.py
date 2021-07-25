#import the important libraries
from selenium import webdriver
import time

browser=webdriver.Chrome(r"C:\Users\HP\Desktop\chromedriver.exe")

browser.get('https://www.flipkart.com/account/login?ret=/')


#phone_number=input("Enter your phone Number:")
phone_number='9874191801'

#times=input("Enter number of times you want to send the message:")
times=5

#finding the input number element
phone=browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
phone.send_keys(phone_number)

reqOTP=browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[5]/button')
reqOTP.click()
time.sleep(3)

times=int(times)
n=times-1
for i in range(n):
	# click on resend otp
	r=browser.find_element_by_xpath("//*[contains(text(), 'Resend code')]")
	r.click()
	time.sleep(2)

browser.quit()
