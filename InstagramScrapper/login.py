from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


class App:

    def __init__(self, username='xawbeenregmi', password='fuckingworld', target_username='xawbeenregmi',
                 path='E:/Projects/instaPhotos'):
        self.username = username
        self.password = password
        self.target_username = target_username
        self.path = path
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.main_url = 'https://www.instagram.com'
        self.driver.get(self.main_url)
        sleep(3)
        #calling the login function
        self.log_in()
        sleep(2)
        self.close_dialoguebox()
        sleep(2)
        self.search_targetUser()
        sleep(2)

        input("stop for now")
        self.driver.close()


    def log_in(self,):
        log_in_button = self.driver.find_element_by_xpath('//p[@class="izU2O"]/a ')
        log_in_button.click()

        sleep(2)
        user_name_input = self.driver.find_element_by_name('username')
        user_name_input.send_keys(self.username)
        password_input = self.driver.find_element_by_name('password')
        password_input.send_keys(self.password)

        password_input.submit()



    def close_dialoguebox(self):
        try:
            select_notnow = self.driver.find_element_by_xpath('//html/body/div[3]/div/div/div[3]/button[2]')
            select_notnow.click()
        except Exception:
            pass


    def search_targetUser(self):
        target_user = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        target_user.send_keys(self.target_username)


if __name__ == '__main__':
    app = App()
