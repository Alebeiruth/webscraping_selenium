from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 1 - site > https://www.chavesnamao.com.br/ X
# link2 - imóveis para alugar > //*[@id="rent-realestate"] X
# 3 - casa & sobrados > //*[@id="ti-4"] X
# 4 - avançar > //*[@id="home-filter-onboarding"]/div[2]/div[2]/button X
# 5 - Procurar por nome > //*[@id="city"] X
# 5.1 Curitba > //*[@id="cityList"]/li[1] X
# 6 Cristo Rei > //*[@id="nbList"]/li[31] X
# 7 Hauer > //*[@id="nbList"]/li[38] X
# 8 Jardim Botanico > //*[@id="nbList"]/li[40] X
# 9 Jardim das Americas > //*[@id="nbList"]/li[41] X
# 10 Prado Velho > //*[@id="nbList"]/li[54] X
# 11 Rebouças > //*[@id="nbList"]/li[55] X
# 12 Guabirotuba > //*[@id="nbList"]/li[36] X
# 13 ver resultados > //*[@id="home-filter-onboarding"]/div[2]/div[2]/div/button
# 14 Dois quartos > //*[@id="quartos2"] X
# 15 Ordernar > //*[@id="orderDesktop"]/div/span X
# link16 Menor Valor > //*[@id="orderDesktop"]/div/div/ul/li[2]

# Set up the Chrome driver
navegador = webdriver.Chrome()

# Open the Chaves na mão homepage
navegador.get("https://www.chavesnamao.com.br/")

# Wait until the first button is clickable and click it
try:
    link2 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="rent-realestate"]'))
    )
    ActionChains(navegador).move_to_element(link2).click().perform()
    
    link3 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ti-4"]'))
    )
    ActionChains(navegador).move_to_element(link3).click().perform()
    
    link4 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="home-filter-onboarding"]/div[2]/div[2]/button'))
    )
    ActionChains(navegador).move_to_element(link4).click().perform()
    
    link5 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="city"]'))
    )
    link5.send_keys("Curitiba")

    link6 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cityList"]/li[1]'))
    )
    ActionChains(navegador).move_to_element(link6).click().perform()

    link7 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nbList"]/li[31]'))
    )
    ActionChains(navegador).move_to_element(link7).click().perform()

    link8 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nbList"]/li[38]'))
    )
    ActionChains(navegador).move_to_element(link8).click().perform()

    link9 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nbList"]/li[40]'))
    )
    ActionChains(navegador).move_to_element(link9).click().perform()

    link10 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nbList"]/li[41]'))
    )
    ActionChains(navegador).move_to_element(link10).click().perform()

    link11 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nbList"]/li[54]'))
    )
    ActionChains(navegador).move_to_element(link11).click().perform()

    link12 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nbList"]/li[55]'))
    )
    ActionChains(navegador).move_to_element(link12).click().perform()

    link13 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nbList"]/li[36]'))
    )
    ActionChains(navegador).move_to_element(link13).click().perform()

    link14 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="home-filter-onboarding"]/div[2]/div[2]/div/button'))
    )
    ActionChains(navegador).move_to_element(link14).click().perform()

    link15 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="quartos2"]'))
    )
    ActionChains(navegador).move_to_element(link15).click().perform()

    link16 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="orderDesktop"]/div/span'))
    )
    ActionChains(navegador).move_to_element(link16).click().perform()

    link17 = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="orderDesktop"]/div/div/ul/li[2]'))
    )
    ActionChains(navegador).move_to_element(link17).click().perform()

    # Save the last URL to a file
    with open('url_site_chaves_na_mao.txt', 'w') as file:
        file.write(navegador.current_url)

    # Keep the browser open for a while to see the results
    time.sleep(90)  # Keep the browser open for 90 seconds

finally:
    # Close the browser after the operation
    navegador.quit()
