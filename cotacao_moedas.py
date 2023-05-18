from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
moedas = ["Dólar", "Euro", "Peso Argentino", "Kwanza", "Dólar Australiano"]


for moeda in moedas:
    driver.get(f"https://google.com/search?q={moeda}&hoje")
    valor = driver.find_element(By.CLASS_NAME, "SwHCTb")
    print(f"1 {moeda} equivale a {valor.text} reais brasileiros", file=log_file)

driver.quit()
