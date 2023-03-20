from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Inicializa o ChromeDriver automaticamente
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navega para uma página
driver.get("https://www.unoeste.br/site/AVA/default.aspx")
login =
senha  =
achados=[]
novalista=[]
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,('tbLogin')).send_keys(login)
sleep(4)
driver.find_element(By.ID,('tbSenha')).send_keys(senha)
sleep(4)
driver.find_element(By.ID,('bAutenticar')).click()
sleep(4)
driver.find_element(By.XPATH,('/html[1]/body[1]/form[1]/div[3]/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/a[1]')).click()
sleep(4)
aulas = driver.find_elements(By.CLASS_NAME,('fc-title'))
for i in aulas:
    achados.append(i.text)

sleep(2)

palavra_especifica = 'Acesse a aula ao vivo'

for frase in achados:
    if palavra_especifica in frase:
        novalista.append(frase)

print(novalista)

df=pd.DataFrame({'dias de aula':novalista})
print(df)
df.to_csv("aulas.csv")