# Importar classe para inicializar o browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver= webdriver.Chrome(r'C:\Users\casa\chromedriver\chromedriver.exe')

driver.get("https://www.mambo.com.br/arroz-polido-longo-fino-tipo-1-camil-5kg/p/140610")


# Instanciar a classe que irá esperar até 5 segundos
wait = WebDriverWait(driver, 10)

# Aguardar até que o elemento "id_elemento" esteja visível
elemento = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'price-por')))
elemento= elemento.text
elemento= elemento[3:]
preco = float(elemento.replace(',','.'))

print(elemento)
#driver.quit()
