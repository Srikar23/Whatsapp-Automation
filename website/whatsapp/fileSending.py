from selenium import webdriver
import time

def file(recipient_Name, path, time_In_Secs):
    try:
        # chrome browser
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\SANTHOSH\\Desktop\\Python\\driver-selenium\\chromedriver.exe")
        # opening webWhatsApp on chrome browser
        driver.get("https://web.whatsapp.com/")
        time.sleep(2)
        try:
            # keep me logged in
            Check_box = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div[3]/label/input')
            if not (Check_box.is_selected()):
                Check_box.click()
        except:
            pass

        driver.maximize_window()

        time.sleep(5)

        # scan the QRcode
        print("Scan the QRcode as soon as possible")

        # wait for some time to load the page
        time.sleep(5)
        Search_Bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')

        # searching for the recipient name
        Search_Bar.send_keys(recipient_Name + "\n")

        # it sends the required msg after the given seconds
        time.sleep(time_In_Secs)

        # attaching the file
        driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button/input').send_keys(path)
        time.sleep(2)
        # clicking the send Button
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div').click()

        time.sleep(300)
        # C:/Users/SANTHOSH/Pictures/IMG_20200129_132726880.jpg
        # logging off
        driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div').click()
        LogOut_butn = driver.find_element_by_xpath(
            '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[7]/div')
        LogOut_butn.click()

        time.sleep(5)
        driver.close()

    except Exception as ex:
        print('"ERROR!"\n', ex)
        driver.close()