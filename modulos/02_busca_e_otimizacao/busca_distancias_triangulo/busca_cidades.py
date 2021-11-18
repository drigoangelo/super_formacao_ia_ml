from numpy import matrix
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
import traceback
import configparser
import pandas as pd
import numpy as np




def main():

    config = load_config()
    browser = create_browser(config)
    
    try:
        d = buscar_distancias(config, browser)
        np.savetxt("distancias.csv", d, fmt = "%.2f")
    except:
        traceback.print_exc()
    finally:
        browser.quit()

def buscar_distancias(config, browser):
    cidades = pd.read_csv("cidades.csv")["cidade"]
    urls = config['urls']
    url = urls["distancia_cidades"]
    timeout = config['webdriver'].getfloat('timeout')
    
    n =  len(cidades)
    d = np.zeros((n,n))

    for i in range(n):
        for j in range(i+1,n):
            de = cidades[i]
            para = cidades[j]
            distancia = buscar_distancia(browser, url.format(de, para), timeout)
            d[i][j] = d[j][i] = float(distancia)
    return(d)
    
    
def buscar_distancia(browser, url, timeout):
    d = -1
    try:
        browser.get(url)
        id_elemento = "kmsruta"
        WebDriverWait(browser, timeout) \
            .until(EC.visibility_of_element_located((By.XPATH, "//*[@id='{0}']".format(id_elemento))))

        d = browser.find_element_by_id(id_elemento).text \
            .replace(" km", "") \
            .replace(",", "")
    except:
        traceback.print_exc()
    return(d)
    


def load_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config

def create_browser(config):
    option = webdriver.ChromeOptions()
    option.add_argument(" — incognito")

    browser = webdriver.Chrome(executable_path=config['webdriver']['chrome_path'], options=option)
    return browser



main()