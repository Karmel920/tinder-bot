import undetected_chromedriver as uc
# from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import randint, random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import username, password


class TinderBot:

    def __init__(self):
        option = uc.ChromeOptions()
        option.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 1})
        self.driver = uc.Chrome(version_main=108, options=option)

    def login(self):
        self.driver.get('https://tinder.com')

        agreement = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'I decline')]")))
        agreement.click()

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='c1p6lbu0 Miw(120px)']")))
        login_button.click()

        google_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button']")))
        google_button.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='identifierId']")))
        email_input.send_keys(username)

        go_on_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='identifierNext']")))
        go_on_button.click()

        password_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Passwd']")))
        password_input.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='passwordNext']")))
        login_button.click()

        self.driver.switch_to.window(base_window)

        popup_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Allow']")))
        popup_1.click()

        popup_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Not interested']")))
        popup_2.click()

    def like(self):
        # like_button = WebDriverWait(bot.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//main/div/div/div/div/div/div/div[4]/div/div[4]")))
        like_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//main/div/div/div/div/div/div/div[4]/div/div[4]")))
        like_button.click()

    def dislike(self):
        dislike_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//main/div/div/div/div/div/div/div[4]/div/div[2]")))
        dislike_button.click()

    def first_swipe(self):
        first_swipe = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//main/div/div/div/div/div/div/div[3]/div/div[4]")))
        first_swipe.click()

    def close_add_popup(self):
        popup_3 = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Not interested')]")))
        popup_3.click()

    def close_likes_popup(self):
        popup_4 = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'No Thanks')]")))
        popup_4.click()

    def close_likes_popup_2(self):
        popup_5 = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='Pos(r) Z(1)']")))
        popup_5.click()

    def close_match(self):
        match_popup = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Back to Tinder']")))
        match_popup.click()

    def auto_swipe(self):
        try:
            self.first_swipe()
        except Exception:
            pass

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
            except Exception:
                try:
                    self.close_add_popup()
                    print("popupadd!")
                except Exception:
                    try:
                        self.close_likes_popup()
                        print("popup1!")
                    except Exception:
                        try:
                            self.close_likes_popup_2()
                            print("popup2!")
                        except Exception:
                            try:
                                self.close_match()
                                print("Match!")
                            except Exception:
                                break

    def message_all(self):
        matches = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Matches'])")))
        matches.click()
        match = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='tabpanel']//div//div[3]//a")))
        while match:
            match.click()
            message = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@placeholder="Type a message"]')))
            message.send_keys('Witam cię kolezanko, jesteś bardzo piękna i ładna, powiedz mi z jakiej jesteś miejscowości')
            send_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            send_button.click()
            sleep(1)
            matches = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Matches'])")))
            matches.click()
            match = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='tabpanel']//div//div[3]//a")))


# bot = TinderBot()
# bot.login()


if __name__ == '__main__':
    bot = TinderBot()
    bot.login()
    while True:
        try:
            bot.auto_swipe()
        except Exception:
            break
