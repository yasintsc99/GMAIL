from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
def PasswordGenerator():
    charList = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvYyZzXxQq0123456789{*+.!-&%}"
    password = ""
    for i in range(10):
        rastgele = random.randint(0,len(charList)-1)
        password += charList[rastgele]
    return password
service = Service("./chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("useAutomationExtension",False)
options.add_argument("--user-data-dir=C:\\Users\\YASIN\\AppData\\Local\\Google\\Chrome\\User Data\\Profile\\Default") #YOUR CHROME PROFILE PATH, YOU CAN LEARN YOUR PATH FROM chrome://version ADRESS
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36')
url = "https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp&theme=glif"
driver = webdriver.Chrome(service=service,options=options)
driver.maximize_window()
driver.implicitly_wait(5)
file = open("NameList.txt","r",encoding="utf-8")
index = 0
for line in file:
    # IT WILL BE CHOOSE ONLY TWO SLICES LINES INTO TXT FILE LIKE (JOHN DOE)
    if len(line.split(" ")) < 3:
        driver.get(url)
        aa = random.randint(1, 12)
        # ONLY FOR FEBRUARY
        if aa == 2:
            # CREATE RANDOM DAY FOR FEBRUARY (BETWEEN 1 AND 28)
            gg = random.randint(1, 28)
        else:
            # FOR 1, 3, 5, 7, 8, 10, 12 MONTHS WITH 31 DAYS CONTROLLER
            if aa in [1, 3, 5, 7, 8, 10, 12]:
                gg = random.randint(1, 31)
            else:
                # FOR OTHER MONTHS WITH 30 DAYS CONTROLLER
                gg = random.randint(1, 30)

        # CREATE A RANDOM YEAR (FOR EXAMPLE, BETWEEN 1960 AND 2005)
        yyyy = random.randint(1960, 2005)
        # NAME-SURNAME INPUTS
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"input#firstName").send_keys(line.split(" ")[0])
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"input#lastName").send_keys(line.split(" ")[1] + Keys.ENTER)

        # BIRTHDAY & GENDER
            # DAY
        driver.find_element(By.CSS_SELECTOR,"input#day").send_keys(gg)
        time.sleep(1)
        
            # MONTH
        month_comboBox = driver.find_element(By.CSS_SELECTOR,"select#month")
        month = Select(month_comboBox)
        month.select_by_value(str(aa))
        time.sleep(1)
            # YEAR
        driver.find_element(By.CSS_SELECTOR,"input#year").send_keys(yyyy)
        time.sleep(1)
            # GENDER
        gender_ComboBox = driver.find_element(By.CSS_SELECTOR,"select#gender")
        gender = Select(gender_ComboBox)
        gender.select_by_visible_text("Belirtmemeyi tercih ediyorum")
        time.sleep(1.5)
        gender_ComboBox.send_keys(Keys.TAB+Keys.ENTER)
        # GMAIL ADRESS
        gmail = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/span/div[1]/div/div[1]/div/div[3]/div")
        driver.execute_script("arguments[0].click();", gmail)
        time.sleep(0.5)
        next_button = driver.find_element(By.CSS_SELECTOR,"div#next")
        driver.execute_script("arguments[0].click();", next_button)
        # GMAIL PASSWORD
        pw = PasswordGenerator()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"input[name = 'Passwd']").send_keys(pw)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"input[name='PasswdAgain']").send_keys(pw)
        time.sleep(3)
        pw_nextBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button/div[1]")
        driver.execute_script("arguments[0].click();", pw_nextBtn)
        driver.execute_script("window.open('about:blank', '_blank');")
        driver.switch_to.window(driver.window_handles[index+1])
        index += 1
    else:
        pass
input()