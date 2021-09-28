from selenium import webdriver
import time

class instagram_bot():

    def __init__(self, driver: webdriver, post_link: str) -> None:
        
        self.driver = driver
        self.post_link = post_link

    def login(self, user: str, pass_word: str) -> None:

        username= self.driver.find_element_by_css_selector("input[name='username']")
        password= self.driver.find_element_by_css_selector("input[name='password']")

        username.clear()
        password.clear()
        username.send_keys(user)
        password.send_keys(pass_word)
        login = self.driver.find_element_by_css_selector("button[type='submit']").click()

    def pass_notif(self)-> None:

        time.sleep(10)
        notnow = self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
        #turn on notif
        time.sleep(10)
        notnow2 = self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
        
        self.driver.get(self.post_link)

    
    def load_more_comment(self, count: int) -> None:
        
        i = 0
        load_more = self.driver.find_element_by_class_name("dCJp8.afkep")
        
        if(load_more):

            try:
                while load_more.is_displayed() and i < count:

                    load_more.click()
                    time.sleep(3)
                    load_more = self.driver.find_element_by_class_name("dCJp8.afkep")
                    i += 1
            except Exception as e:
                print(e)
                pass
        else:
            pass

               
    def get_comments(self) -> list:

        comments = []
        conteiner = self.driver.find_elements_by_xpath("//div[@class='C4VMK']/span")

        conteiner.pop(0)

        for element in conteiner:
            comments.append(element.text)
        
        return comments

    def get_users(self) -> list:

        users = []
        conteiner = self.driver.find_elements_by_xpath("//div[@class='C4VMK']/h3")

        for element in conteiner:
            users.append(element.text)
        
        return users

    def close(self) -> None:

        self.driver.quit()
