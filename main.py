from selenium.webdriver import Firefox
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
#/html/body/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div/div[3]
#/html/body/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div/div[31]
#/html/body/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div/div[31]/div[2]/div/div[2]/div[2]/div[2]/a
#xpath de seta para cima /html/body/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div[5]
#xpath da barra de rolagem /html/body/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div[1]/div
#xath de seta para baixo /html/body/div[1]/div[2]/div/div/div[3]/div/div[4]/div/div[6]

#url = "https://artofproblemsolving.com/community/c5h404350_perfect_squares_2011_usajmo_1"
url =  "https://artofproblemsolving.com/community/c5h2308615_fav_program"
#url = "https://artofproblemsolving.com/community/c5h404347_a2b2c2lt4_2011_usamo_1_2011_usajmo_2"
#url = "https://artofproblemsolving.com/community/c6h2478239_incredible_vanilla_geometry_again"

#url = "https://artofproblemsolving.com/community/c5h2308615_fav_program"

driver = Firefox()
driver.get(url)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR  , "div.cmty-post"))
    )
    teste = driver.find_elements_by_css_selector("div.cmty-post")

    barra_rolagem = driver.find_element_by_css_selector('.cmty-topic-posts-outer-wrapper > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    seta_para_baixo = driver.find_element_by_css_selector('div.cmty-topic-jump-bottom')
    tamanho_html_atual = len(driver.page_source)
    webdriver.ActionChains(driver).drag_and_drop(barra_rolagem,seta_para_baixo).perform()
    tamanho_html_final = len(driver.page_source)
    while tamanho_html_atual < tamanho_html_final:
        tamanho_html_atual = len(driver.page_source)
        webdriver.ActionChains(driver).drag_and_drop(barra_rolagem,seta_para_baixo).perform()
        tamanho_html_final = len(driver.page_source)
    tamanho_html_atual = len(driver.page_source)
    with open(url.split('/')[-1] + '.html', 'w',  encoding="utf-8") as arquivo:
        arquivo.write(driver.page_source)
    print(f"arquivo salvo com nome {url.split('/')[-1]}.html")
    
except:
    print("página sem barra de rolagem html veio completo")
    print(f"arquivo salvo com nome {url.split('/')[-1]}.html")
    with open(url.split('/')[-1] + '.html', 'w',  encoding="utf-8") as arquivo:
        arquivo.write(driver.page_source)
finally:
    driver.quit()