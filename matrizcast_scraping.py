# Importar as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from parsel import Selector
import csv

# Perguntar ao usuário qual o sobre qual tema ele quer encontrar convidados para o MatrizCast
busca = input("Qual é o tema que você quer encontrar pessoas no LinkedIn para convidar para o MatrizCast? \n")

# Criar o arquivo csv "lista_matrizcast"
writer = csv.writer(open('lista_matrizcast.csv', 'w', encoding='utf-8'))
writer.writerow(['Nome', 'Headline', 'URL'])

# Chrome diver
driver = webdriver.Chrome('./chromedriver')

# Acessar o LinkedIn para fazer Log in
driver.get('https://www.linkedin.com/')
sleep(1)
driver.find_element(By.XPATH,"//*[@class='nav__button-secondary btn-md btn-secondary-emphasis']").click()
sleep(1)


# Fazer o Log In para acessar a conta
usuario_input = driver.find_element(By.ID, "username")
senha_input = driver.find_element(By.ID, 'password')

# Você deve substituar "email" e "senha" pelo seu email e senha da conta no LinkedIn
usuario_input.send_keys('fabinhomori@hotmail.com')
senha_input.send_keys('FabioMori03111989')
sleep(1)
driver.find_element(By.XPATH,"//*[@class='btn__primary--large from__button--floating']").click()

# Os comandos "sleep" são colocados ao longo do código para "humanizar" o processo e diminuir o risco de ser bloqueado
# pelo site que estamos acessando pelo algotimo
sleep(1)

# Acessar o Google para fazer a pesquisa
driver.get('https://google.com')
sleep(1)

# Selecionar campo de busca
busca_input = driver.find_element(By.NAME, 'q')

# Fazer busca no google a partir do que foi definido inicialmente pelo usuário na pergunta
busca_input.send_keys("site:linkedin.com/in/ AND "+ busca)
busca_input.send_keys(Keys.RETURN)
sleep(2)

# Extrair lista dos perfis encontrados na pesquisa
lista_perfil = driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]/a')
sleep(2)
lista_perfil = [perfil.get_attribute('href') for perfil in lista_perfil]

# Extrair informacoes individuais acessando cada perfil no LinkedIn
for perfil in lista_perfil:
    driver.get(perfil)
    sleep(2)

    response = Selector(text=driver.page_source)

    # Extrair nome, descrição e url para armazenar no arquivo csv
    nome = response.xpath('//title/text()').extract_first().split(" | ")[0]
    headline = response.xpath('//div[@class="text-body-medium break-words"]//text()').extract_first()
    url_perfil = driver.current_url

    # Escrever no arquivo csv "lista_matrizcast" as informações obtidas
    writer.writerow([nome, headline, url_perfil])

# Sair do driver
driver.quit()