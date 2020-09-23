from selenium import webdriver
import time


def msg(recipient_Name, msg, time_In_Secs):
    try:
        # chrome browser
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\SANTHOSH\\Desktop\\Python\\driver-selenium\\chromedriver.exe")
        # opening webWhatsApp on chrome browser
        driver.get("https://web.whatsapp.com/")

        time.sleep(2)
        # keep me signed in
        try:
            Check_box = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div[3]/label/input')
            if not (Check_box.is_selected()):
                Check_box.click()
        except:
            pass

        driver.maximize_window()
        time.sleep(5)

        # scan the QRcode
        # print("Scan the QRcode as soon as possible")

        # wait for some time to load the page
        time.sleep(5)

        Search_Bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')

        # searching for the recipient name
        Search_Bar.send_keys(recipient_Name + "\n")

        # it sends the required msg after the given seconds
        time.sleep(time_In_Secs)

        msg_textBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        msg_textBox.send_keys(msg + "\n")
        time.sleep(5)

        # logging Off
        driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div').click()
        LogOut_but = driver.find_element_by_xpath(
            '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[7]/div').click()

        time.sleep(5)

        driver.close()
    except Exception as ex:
        print("ERROR!\n", ex)
        try:
            driver.close()
        except:
            pass