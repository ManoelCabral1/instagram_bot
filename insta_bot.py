from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class instagram_bot():
    """ A classe recebe como argumentos iniciais:
     - webdriver selenium já conectado na página inicial do instagram web
     - o link do post de onde os comentários serão extraídos
     """
    def __init__(self, driver: webdriver, post_link: str) -> None:
        
        self.driver = driver
        self.post_link = post_link

    def login(self, user: str, pass_word: str) -> None:
        """ O método recebe como argumentos:
         - login: email ou username de uma conta ativa do instagram
         - senha: senha da conta
        """
        username= self.driver.find_element_by_css_selector("input[name='username']")
        password= self.driver.find_element_by_css_selector("input[name='password']")

        username.clear()
        password.clear()
        username.send_keys(user)
        password.send_keys(pass_word)
        login = self.driver.find_element_by_css_selector("button[type='submit']").click()

    def pass_notif(self)-> None:
        """ Método para fechar as caixas de pop-up de notificações"""
        
        time.sleep(10)
        notnow = self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
        #turn on notif
        time.sleep(10)
        notnow2 = self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
        
        self.driver.get(self.post_link)

    
    def load_more_comment(self, count: int) -> None:
        """ Método para clickar no botão mais comentários, 
        recebe como argumentos um limite para o número de clicks, 
        muito importante para evitar looping infinito"""
        
        i = 0
        try:
              load_more = self.driver.find_element_by_class_name("dCJp8.afkep")
        
              while load_more.is_displayed() and i < count:

                    load_more.click()
                    time.sleep(3)
                    load_more = self.driver.find_element_by_class_name("dCJp8.afkep")
                    i += 1
        except NoSuchElementException as e:
              print(e)
              pass

               
    def get_comments(self) -> list:
         """ Método para extrair comentários"""
            
        comments = []
        conteiner = self.driver.find_elements_by_xpath("//div[@class='C4VMK']/span")

        conteiner.pop(0)

        for element in conteiner:
            comments.append(element.text)
        
        return comments

    def get_users(self) -> list:
         """ Método para extrair usuário que fez o comentário"""
            
        users = []
        conteiner = self.driver.find_elements_by_xpath("//div[@class='C4VMK']/h3")

        for element in conteiner:
            users.append(element.text)
        
        return users

    def close(self) -> None:
        """ Método para fechar o driver do navegador"""
        self.driver.quit()
