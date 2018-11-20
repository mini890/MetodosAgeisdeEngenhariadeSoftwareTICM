from selenium import webdriver
browser = webdriver.Firefox()
# verificar que existe um site ativo naquele endereço
browser.get("http://localhost:8000")
# verificar que é o site dos todo's
assert 'To-Do' in browser.title, "title=" + browser.title
# Tenho um interface para escrever o ToDo
# Escrevo "Alimentar o gato"
# carrego Enter
# Aparece no ecrâ
# "1: Alimentar o gato"
# Escrevo "Comprar Leite" seguido de enter
# Aparece no ecrâ
# "1: Alimentar o gato"
# "2: Comprar Leite"
# ...
browser.quit()