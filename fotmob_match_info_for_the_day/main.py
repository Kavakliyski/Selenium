from selenium import webdriver
import unittest

# class Fotmob_info(unittest.TestCase):

driver = webdriver.Chrome(executable_path='../chromedriver/chromedriver.exe')
driver.implicitly_wait(10)
# driver.maximize_window()


driver.get('https://www.fotmob.com/')


def Premier_league_Table():
    driver.find_element_by_xpath('//*[@id="root"]/section/section/section[1]/section/div[2]/div[1]/div/a').click()
    # Team_1 = driver.find_element_by_xpath('//*[@id="root"]/section/section/section[2]/section[2]/div[1]/section/div[2]/a/span').text

    column_info = []
    columns = driver.find_elements_by_xpath("//body//div//section//section//section//section//div//section//div//span")
    for column in columns:
        column_info.append(str(column.text))

    # ['#', 'Team', 'PL', 'W', 'D', 'L', '+/-', 'GD', 'PTS', '1', 'Man City', '34', '25', '5', '4', '71-24', '47', '80',
    #  '2', 'Man United', '33', '19', '10', '4', '64-35', '29', '67', '3', 'Leicester', '34', '19', '6', '9', '61-39',
    # ...]

    for i in range(len(column_info)):
        print(column_info[i])


    print('here')
    # print(Team_1)



Premier_league_Table()


def tearDown():
    driver.close()
    driver.quit()
    print('======   Closed  ======')


tearDown()
