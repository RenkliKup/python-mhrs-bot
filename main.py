from selenium import webdriver
import time
import os
import sys
class Selenium_Mhrs_Bot:
    def __init__(self):
        if getattr(sys,"frozen",False):
            chromedriver_path=os.path.join(sys._MEIPASS,"chromedriver.exe")
            self.driver=webdriver.Chrome(chromedriver_path)
        else:
            self.driver=webdriver.Chrome()
        self.driver.get("https://mhrs.gov.tr/")
    def firs_access_alert(self):
        try:
            
            time.sleep(5)
            alert=self.driver.find_element_by_xpath('//*[@id="duyuruModalAsi"]/div/div[1]/div[1]/button')
            print(alert)
            alert.click()
        except Exception as e:
            time.sleep(5)
            print(e)
            self.firs_access_alert()
            
    def Access_Appointment(self):
        try:
            
            accces_button=self.driver.find_element_by_xpath('//*[@id="randevuLink"]/button')
            accces_button.click()
        except Exception as e:
            print("randevu al sayfa girisi")
            time.sleep(5)
            self.Access_Appointment()
    def switch_window(self,number):
        try:
            window=self.driver.window_handles[number]
            self.driver.switch_to_window(window)
        except Exception as e:
            print(e)
            pass
    def driver_close(self):
        self.driver.close()

    def entire_Tc_pass(self,mhrs_tc,mhrs_pass):
        try:
            tc_input=self.driver.find_element_by_xpath('//*[@id="LoginForm_username"]')
            tc_input.send_keys(int(mhrs_tc))
            pass_input=self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/form/div[2]/div/div/span/span/input')
            pass_input.send_keys(str(mhrs_pass))
            entire_button=self.driver.find_element_by_xpath('//*[@id="vatandasApp"]/div[2]/div[1]/div[2]/form/div[3]/div/div/span/div/div/button')
            entire_button.click()
        except :
            time.sleep(3)
            self.entire_Tc_pass(mhrs_tc,mhrs_pass)

    def appointment_button(self):
        try:
            button=self.driver.find_element_by_xpath('/html/body/div/section/main/div/div/div[4]/div')
            button.click()
            time.sleep(5)
            modal_button=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[1]/div/div/button[1]')
            modal_button.click()
        except :
            time.sleep(3)
            self.appointment_button()

    def country_box(self,country_name):
        try:
            country=self.driver.find_element_by_xpath("/html/body/div/section/main/div/div/div[2]/div/div[3]/div/div[2]/div[2]/form/div[2]/div/div/span/span")
            country.click()
            time.sleep(2)
            country_input=self.driver.find_element_by_xpath("/html/body/div/section/main/div/div/div[2]/div/div[3]/div/div[2]/div[2]/form/div[11]/div/div/div/span/span/input")
            country_input.send_keys(str(country_name))
            time.sleep(2)
            selection_country=self.driver.find_element_by_xpath("/html/body/div/section/main/div/div/div[2]/div/div[3]/div/div[2]/div[2]/form/div[11]/div/div/div/ul/li/span[2]")
            selection_country.click()
        except :
            print("country box")
            time.sleep(3)
            self.country_box()

    def district_box(self,district_text):
        try:
            
            box=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[2]/div/div[3]/div/div[2]/div[2]/form/div[3]/div/div/span/div/div/div")
            box.click()
            
            district=self.driver.find_element_by_xpath(f"/html/body/div[1]/section/main/div/div/div[2]/div/div[3]/div/div[2]/div[2]/form/div[12]/div/div/div/ul/li[contains(text(), '{str(district_text)}')]")
            district.click()
        except :
            time.sleep(3)
            self.district_box(district_text)

    def clinic_box(self,clinic_text):
        try:
            
            box=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[2]/div/div[3]/div/div[2]/div[2]/form/div[4]/div/div/span/span/span/span[1]")
            box.click()
            
            clinic=self.driver.find_element_by_xpath(f"/html/body/div/section/main/div/div/div[2]/div/div[3]/div/div[2]/div[2]/form/div[13]/div/div/div/ul/li/span[2]/span[contains(text(), '{clinic_text}')]")
            clinic.click()
        except :
            time.sleep(3)
            self.clinic_box(clinic_text)

    def search_doctor(self):
        try:
            submit=self.driver.find_element_by_xpath(f"/html/body/div/section/main/div/div/div[2]/div/div[3]/div/div[2]/div[2]/form/div[10]/div/div/span/div/div[1]/button")
            submit.click()
        except :
            time.sleep(3)
            self.search_doctor()

    def search_doctor_alert(self):
        try:
            alert=self.driver.find_element_by_xpath(f"/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
            alert.click()
        except :
            pass
    def back_history(self):
        self.driver.back()
    def list_early_time(self):
        try:
            self.doc_info=""
            e_time=self.driver.find_elements_by_css_selector("#vatandasApp > section > main > div > div > div.ant-card-body > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-tabs.ant-tabs-top.ant-tabs-line > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-list.ant-list-split.ant-list-bordered.ant-list-something-after-last-item > div.ant-spin-nested-loading > div > ul > li > div > div.ant-col.ant-col-xs-24.ant-col-sm-12.ant-col-md-8.ant-col-lg-3.ant-col-xl-3 > span > strong > span")
            time.sleep(1)
            name=self.driver.find_elements_by_css_selector("#vatandasApp > section > main > div > div > div.ant-card-body > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-tabs.ant-tabs-top.ant-tabs-line > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-list.ant-list-split.ant-list-bordered.ant-list-something-after-last-item > div.ant-spin-nested-loading > div > ul > li > div > div.ant-col.ant-col-xs-24.ant-col-sm-12.ant-col-md-8.ant-col-lg-6.ant-col-xl-6")
            doc_name=self.driver.find_elements_by_css_selector("#vatandasApp > section > main > div > div > div.ant-card-body > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-tabs.ant-tabs-top.ant-tabs-line > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-list.ant-list-split.ant-list-bordered.ant-list-something-after-last-item > div.ant-spin-nested-loading > div > ul > li:nth-child(1) > div > div > span")

            for i,j,k in zip(e_time,name,doc_name):
                 self.doc_info+=str(k.text+" "+i.text+" "+j.text)+"\n"
            if len(name)>=2:
                self.send_mail()
        except :
            time.sleep(3)
            self.list_early_time()
            
        
    def send_mail(self):
        try:
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            mail_content = f'''{self.doc_info}'''
            #The mail addresses and password
            sender_address = '<mail>'
            sender_pass = '<pass>'
            receiver_address = sender_address
            #Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Mhrs Botu'   #The subject line
            #The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))
            #Create SMTP session for sending the mail
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print('Mail Sent')
        except:
            print("Error: unable to send email")
            pass
                    
                
print("basladi")
mhrs=Selenium_Mhrs_Bot()
mhrs.firs_access_alert()
print("ilk sayfaya girdi")

mhrs.Access_Appointment()
time.sleep(15)
mhrs.switch_window(1)
mhrs.entire_Tc_pass("<tc>","<pass>")
print("giris yapildi")
time.sleep(15)
while True:
    mhrs.appointment_button()
    time.sleep(1)
    mhrs.country_box("istanbul")
    mhrs.district_box("-FARKETMEZ-")
    mhrs.clinic_box("Deri ve Zührevi Hastalıkları (Cildiye)")
    time.sleep(1)
    mhrs.search_doctor()
    time.sleep(1)
    mhrs.search_doctor_alert()
    time.sleep(1)
    mhrs.list_early_time()
    time.sleep(1)
    mhrs.back_history()
    time.sleep(1)









