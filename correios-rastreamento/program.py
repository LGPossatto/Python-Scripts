#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from notify import notification

tracking_code = 'your code'
url = 'https://www2.correios.com.br/sistemas/rastreamento/default.cfm'

#make browser invisible
options = Options()
options.add_argument('--headless')

#open firefox in the selected url
driver = webdriver.Firefox(options=options)
driver.get(url)

#add the tracking code to the form box and then click the submit button
driver.find_element_by_id('objetos').send_keys(tracking_code)
driver.find_element_by_id('btnPesq').click()

#now in the new page select the wanted element
element_text = driver.find_element_by_id('UltimoEvento').text

#organize the text to print with notify
txt_status = ''
txt_date = ''
for i in element_text:
    if i == ' ':
        txt_status += ' '
    elif i.isalpha():
        txt_status += i
    else:
        txt_date += i

notification(f'Estado: {txt_status}\nData da atualização: {txt_date[1:]}', title='Estado da encomenda')

#close
driver.quit()