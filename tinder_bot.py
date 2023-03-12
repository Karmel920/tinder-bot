from time import sleep
from random import randint, random
import requests
import shutil
from PIL import Image
import tensorflow as tf
import os
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import numpy as np
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import gmail, password


class TinderBot:

    def __init__(self):
        option = uc.ChromeOptions()
        option.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 1})
        self.driver = uc.Chrome(version_main=110, options=option)

    def login(self):
        self.driver.get('https://tinder.com')

        agreement = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'I decline')]")))
        agreement.click()

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='c1p6lbu0 Miw(120px)']")))
        login_button.click()

        google_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button']")))
        google_button.click()

        # name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@itemprop='name']")))
        # photo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Profile slider']")))

        sleep(2)
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='identifierId']")))
        email_input.send_keys(gmail)

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
        like_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//main/div/div/div/div/div/div/div[4]/div/div[4]")))
        like_button.click()

    def dislike(self):
        dislike_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//main/div/div/div/div/div/div/div[4]/div/div[2]")))
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
        is_match = False
        left_count, right_count = 0, 0

        try:
            self.first_swipe()
            right_count += 1
            print(f'{right_count}th right swipe')
        except Exception:
            pass

        while True:
            sleep(randint(1, 3))
            try:
                info_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                                    (By.XPATH, "(//main/div/div/div/div/div/div/div[2]/div[3]/button)"))
                              )
                info_button.click()
                sleep(1)
                photo_url = self.get_photo()
                self.photo_save_eval(photo_url)
                predict_class = self.photo_predict()
                back_to_likes = WebDriverWait(bot.driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, "(//main/div/div/div/div/div/div/div/span/a)"))
                )
                back_to_likes.click()
                sleep(1)
                if predict_class > 0.5:
                    if is_match:
                        self.first_swipe()
                        is_match = 0
                    else:
                        self.like()
                    right_count += 1
                    print(f'{predict_class} - {right_count}th right swipe')
                else:
                    self.dislike()
                    left_count += 1
                    print(f'{predict_class} - {left_count}th left swipe')
                # n = random()
                # if n < .75:
                #     if is_match:
                #         self.first_swipe()
                #         is_match = 0
                #     else:
                #         self.like()
                #     right_count += 1
                #     print(f'{right_count}th right swipe')
                # else:
                #     self.dislike()
                #     left_count += 1
                #     print(f'{left_count}th left swipe')
            except Exception:
                try:
                    self.close_add_popup()
                    # print("popupadd!")
                    sleep(0.5)
                    continue
                except Exception:
                    pass
                try:
                    self.close_likes_popup()
                    # print("popup1!")
                    sleep(0.5)
                    continue
                except Exception:
                    pass
                try:
                    self.close_match()
                    is_match = True
                    print("Match!")
                    sleep(0.5)
                    continue
                except Exception:
                    pass
                try:
                    self.close_likes_popup_2()
                    # print("popup2!")
                    sleep(0.5)
                    continue
                except Exception:
                    print('End of swiping!')
                    return

    def message_all(self):
        try:
            matches = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Matches'])[1]")))
            matches.click()
            match = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul//li[3]")))
            # match = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='tabpanel']//div//div[3]//a")))
            while match:
                match.click()
                self.send_message(mess=open_message)
                sleep(1)
                matches = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Matches'])[1]")))
                matches.click()
                match = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul//li[3]")))
        except Exception:
            return

    def send_message(self, mess=''):
        try:
            if not mess:
                mess = input('Type message: ')
            message = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@placeholder="Type a message"]')))
            message.send_keys(mess)
            send_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            send_button.click()
        except Exception:
            return

    def photo_predict(self):
        img = cv2.imread('eval_photo.jpg')
        resize_img = tf.image.resize(img, (256, 256))
        predict_class = new_model.predict(np.expand_dims(resize_img / 255, 0))
        return predict_class

    def photo_save_eval(self, photo_url):
        img_data = requests.get(photo_url).content
        with open('eval_photo.jpg', 'wb') as handler:
            handler.write(img_data)
        im = Image.open('eval_photo.jpg').convert("RGB")
        im.save('eval_photo.jpg', "jpeg")

    # Collect data for learn a neural network
    def photo_save(self, photo_url, liked):
        file_name = 'data'

        if liked:
            file_name += '/likes/'
        else:
            file_name += '/dislikes/'

        file_name += photo_url.split('/')[4]
        file_name += '.jpg'

        res = requests.get(photo_url, stream=True)

        if res.status_code == 200:
            with open(file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ', file_name)
        else:
            print('Image Couldn\'t be retrieved')

    def get_photo(self):
        photo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='profileCard__slider__img Z(-1)']")))
        photo_url = photo.value_of_css_property('background-image')[5:-2]
        return photo_url

    def photo_stuff(self):
        photo_url = self.get_photo()

        input_string = input('Write 1 to like, Write 2 to dislike').lower()

        if input_string == '1':
            self.photo_save(photo_url, True)
        elif input_string == '2':
            self.photo_save(photo_url, False)


new_model = load_model('models/imageclassifier_1051hqphotos.h5')
open_message = 'Witam cię kolezanko, jesteś bardzo piękna i ładna, powiedz mi z jakiej jesteś miejscowości'
bot = TinderBot()
bot.login()


# if __name__ == '__main__':
#     bot = TinderBot()
#     bot.login()
#     bot.auto_swipe()
