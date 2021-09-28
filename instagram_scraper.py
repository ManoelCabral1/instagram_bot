from selenium import webdriver
import time
import pandas as pd
import sys
from pathlib import Path
from insta_bot import instagram_bot

post_link = sys.argv[1]

data_name = sys.argv[2]

count = int(sys.argv[3])

fname = str(Path.cwd() / 'Dados'/ data_name) + '.csv'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(r"C:\Users\EBMquintto\Documents\chromedriver\chromedriver.exe", options=options)

driver.get("https://www.instagram.com/")

#login
time.sleep(5)
bot = instagram_bot(driver, post_link)

bot.login('manoel.cabral1989@gmail.com', 'tobias123')

#save your login info?
time.sleep(5)
bot.pass_notif()
time.sleep(5)
 
bot.load_more_comment(count)
comments = bot.get_comments()
users = bot.get_users()

data = pd.DataFrame(columns=['usuário', 'comentário'])

data['usuário'] = users
data['comentário'] = comments

data.to_csv(fname, sep=';', index=False)

print(f'Total extraido: {len(comments)}')

bot.close()
