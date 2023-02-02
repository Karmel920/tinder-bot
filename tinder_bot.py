import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import randint, random
from config import username, password


class TinderBot:

    def __init__(self):
        option = uc.ChromeOptions()
        option.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 1})
        self.driver = uc.Chrome(options=option)

    def login(self):
        self.driver.get('https://tinder.com/pl')

        sleep(2)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="s1221153819"]/div/div[1]/div/main/div['
                                                          '1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div['
                                                          '2]')
        login_button.click()

        sleep(5)

        google_button = self.driver.find_element(By.XPATH, '//*[@id="s1442494255"]/main/div/div[1]/div/div/div['
                                                           '3]/span/div[1]')
        google_button.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_input = self.driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        email_input.send_keys(username)

        go_on_button = self.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
        go_on_button.click()

        sleep(5)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
        login_button.click()

        self.driver.switch_to.window(base_window)

        sleep(5)
        popup_1 = self.driver.find_element(By.XPATH, '//*[@id="s1442494255"]/main/div/div/div/div[3]/button[1]/div['
                                                     '2]/div[2]')
        popup_1.click()

        sleep(3)
        popup_2 = self.driver.find_element(By.XPATH, '//*[@id="s1442494255"]/main/div/div/div/div[3]/button[2]/div['
                                                     '2]/div[2]')
        popup_2.click()

        sleep(3)
        agreement = self.driver.find_element(By.XPATH, '//*[@id="s1221153819"]/div/div[2]/div/div/div[1]/div['
                                                       '2]/button/div[2]/div[2]')
        agreement.click()

    def like(self):
        like_button = self.driver.find_element(By.XPATH, '//*[@id="s1221153819"]/div/div[1]/div/main/div['
                                                         '1]/div/div/div[1]/div[1]/div/div[4]/div/div['
                                                         '4]/button/span/span')
        like_button.click()

    def dislike(self):
        dislike_button = self.driver.find_element(By.XPATH, '//*[@id="s1221153819"]/div/div[1]/div/main/div['
                                                            '1]/div/div/div[1]/div[1]/div/div[4]/div/div['
                                                            '2]/button/span/span')
        dislike_button.click()

    def first_swipe(self):
        first_swipe = self.driver.find_element(By.XPATH, '// *[ @ id = "s1221153819"] / div / div[1] / div / main / '
                                                         'div[1] / div / div / div[1] / div[1] / div / div[3] / div /'
                                                         ' div[4] / button / span / span')
        first_swipe.click()

    def close_add_popup(self):
        popup_3 = self.driver.find_element(By.XPATH, '//*[@id="s1442494255"]/main/div/div[2]/button[2]/div[2]/div[2]')
        popup_3.click()

    def close_likes_popup(self):
        popup_4 = self.driver.find_element(By.XPATH, '//*[@id="s1442494255"]/main/div/button[2]/span')
        popup_4.click()

    def close_likes_popup_2(self):
        popup_5 = self.driver.find_element(By.XPATH, '//*[@id="s1442494255"]/main/div/button[2]/div[2]/div[2]')
        popup_5.click()

    def close_match(self):
        match_popup = self.driver.find_element(By.XPATH,'// *[ @ id = "s677621626"] / main / div / div[1] / div / '
                                                        'div[4]')
        match_popup.click()

    def send_open_message(self):
        message_input = self.driver.find_element(By.XPATH, '//*[@id="s-344516134"]')
        message_input.send_keys('Wygladasz na ciekawa i otwarta dziewczyne, nieczesto takie spotykam')

        send_button = self.driver.find_element(By.XPATH, '// *[ @ id = "s677621626"] / main / div / div[1] / div / '
                                                         'div[3] / div[3] / form / button / span')
        send_button.click()

    def auto_swipe(self):
        # try:
        #     self.first_swipe()
        # except Exception:
        #     sleep(1)
        #     try:
        #         self.close_add_popup()
        #     except Exception:
        #         try:
        #             self.close_likes_popup()
        #         except Exception:
        #             try:
        #                 self.close_likes_popup_2()
        #             except Exception:
        #                 self.close_match()

        left_count, right_count = 0, 0
        while True:
            sleep(randint(1, 3))
            try:
                n = random()
                if n < .75:
                    self.like()
                    right_count += 1
                    print(f'{right_count}th right swipe')
                else:
                    self.dislike()
                    left_count += 1
                    print(f'{left_count}th left swipe')
                sleep(3)
            except Exception:
                try:
                    self.close_add_popup()
                except Exception:
                    try:
                        self.close_likes_popup()
                    except Exception:
                        try:
                            self.close_likes_popup_2()
                        except Exception:
                            self.close_match()


    def message_all(self):
        matches = self.driver.find_element(By.XPATH, '//*[@id="s-1195660753"]')
        match = self.driver.find_element(By.XPATH, '// *[ @ id = "s-46830125"] / div[1] / div[3] / a')
        while match:
            match.click()
            sleep(2)
            message = self.driver.find_element(By.XPATH, '//*[@id="s-344516134"]')
            message.send_keys('Wygladasz na ciekawa i otwarta dziewczyne, nieczesto takie spotykam')
            send_button = self.driver.find_element(By.XPATH, '//*[@id="s1221153819"]/div/div[1]/div/main/div['
                                                             '1]/div/div/div/div[1]/div/div/div[3]/form/button['
                                                             '2]/span')
            send_button.click()
            sleep(2)
            matches.click()
            sleep(2)
            match = self.driver.find_element(By.XPATH, '// *[ @ id = "s-46830125"] / div[1] / div[3] / a')


bot = TinderBot()
bot.login()


# if __name__ == '__main__':
#     pass
#     # bot = TinderBot()
#     # bot.login()
#     # bot.auto_swipe()

