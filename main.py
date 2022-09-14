import cfscrape
from bs4 import BeautifulSoup
import pandas as pd

cfs = cfscrape.create_scraper()
r = cfs.get('https://www.kabum.com.br/hardware/placa-de-video-vga?page_number=1&page_size=100&facet_filters=&sort=most_searched')
page = BeautifulSoup(r.text, 'html.parser')
prices = page.find_all('span', {'class': 'sc-3b515ca1-2 jTvomc priceCard'})
names = page.find_all('span', {'height': 54}, {'class': 'sc-d99ca57-0 iRparH sc-b5e5e1a1-14 bNrqTg nameCard'})

price_list = []
name_list = []

for price in prices:
    price_format = price.string.replace('\xa0', ' ')
    price_format = price_format.replace('.', '')
    price_format = price_format.replace(',', '.')
    price_format = price_format.replace('R$ ', '')
    price_format = float(price_format)
    price_list.append(price_format)

for name in names:
    name_list.append(name.string)


r = cfs.get('https://www.kabum.com.br/hardware/placa-de-video-vga?page_number=2&page_size=100&facet_filters=&sort=most_searched')
page = BeautifulSoup(r.text, 'html.parser')
prices = page.find_all('span', {'class': 'sc-3b515ca1-2 jTvomc priceCard'})
names = page.find_all('span', {'height': 54}, {'class': 'sc-d99ca57-0 iRparH sc-b5e5e1a1-14 bNrqTg nameCard'})


for price in prices:
    price_format = price.string.replace('\xa0', ' ')
    price_format = price_format.replace('.', '')
    price_format = price_format.replace(',', '.')
    price_format = price_format.replace('R$ ', '')
    price_format = float(price_format)
    price_list.append(price_format)

for name in names:
    name_list.append(name.string)


r = cfs.get('https://www.kabum.com.br/hardware/placa-de-video-vga?page_number=3&page_size=100&facet_filters=&sort=most_searched')
page = BeautifulSoup(r.text, 'html.parser')
prices = page.find_all('span', {'class': 'sc-3b515ca1-2 jTvomc priceCard'})
names = page.find_all('span', {'height': 54}, {'class': 'sc-d99ca57-0 iRparH sc-b5e5e1a1-14 bNrqTg nameCard'})

for price in prices:
    price_format = price.string.replace('\xa0', ' ')
    price_format = price_format.replace('.', '')
    price_format = price_format.replace(',', '.')
    price_format = price_format.replace('R$ ', '')
    price_format = float(price_format)
    price_list.append(price_format)

for name in names:
    name_list.append(name.string)




name_list_1660s, name_list_1660ti, name_list_1660, name_list_1650s, name_list_1650, name_list_1050ti, name_list_2060, name_list_2060s, name_list_3050, name_list_3060, name_list_3060ti, name_list_3070ti, name_list_3070, name_list_3080ti, name_list_3080, name_list_3090, name_list_3090ti, name_list_6500xt, name_list_6600, name_list_6600xt, name_list_6650xt, name_list_6700xt, name_list_6750xt, name_list_6800, name_list_6800xt, name_list_6900xt, name_list_6950xt, price_1660s, price_1660, price_1660ti, price_1650, price_1650s, price_1050ti, price_2060, price_2060s, price_3050, price_3060, price_3060ti, price_3070ti, price_3070, price_3080, price_3080ti, price_3090, price_3090ti, price_6500xt, price_6600, price_6600xt, price_6650xt, price_6700xt, price_6750xt, price_6800, price_6800xt, price_6900xt, price_6950xt = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

for name in name_list:
    if name.count('1660') != 0:
        if name.lower().count('super') != 0:
            name_list_1660s.append(name)
            price_1660s.append(price_list[name_list.index(name)])
        elif (name.lower().count(' ti ') != 0) or (name.lower().count('0ti') != 0) or (name.lower().count('ti,') != 0):
            name_list_1660ti.append(name)
            price_1660ti.append(price_list[name_list.index(name)])
        else:
            name_list_1660.append(name)
            price_1660.append(price_list[name_list.index(name)])
        
    elif name.count('1650') != 0:
        if name.lower().count('super') != 0:
            name_list_1650s.append(name)
            price_1650s.append(price_list[name_list.index(name)])
        else:
            name_list_1650.append(name)
            price_1650.append(price_list[name_list.index(name)])
    elif name.count('1050') != 0:
        name_list_1050ti.append(name)
        price_1050ti.append(price_list[name_list.index(name)])
    elif name.count('2060') != 0:
        if name.lower().count('super') != 0:
            name_list_2060s.append(name)
            price_2060s.append(price_list[name_list.index(name)])
        else:
            name_list_2060.append(name)
            price_2060.append(price_list[name_list.index(name)])
    elif name.count('3050') != 0:
        name_list_3050.append(name)
        price_3050.append(price_list[name_list.index(name)])
    elif name.count('3060') != 0:
        if (name.lower().count(' ti ') != 0) or (name.lower().count('0ti') != 0) or (name.lower().count('ti,') != 0):
            name_list_3060ti.append(name)
            price_3060ti.append(price_list[name_list.index(name)])
        else:
            name_list_3060.append(name)
            price_3060.append(price_list[name_list.index(name)])
    elif name.count('3070') != 0:
        if (name.lower().count(' ti ') != 0) or (name.lower().count('0ti') != 0) or (name.lower().count('ti,') != 0):
            name_list_3070ti.append(name)
            price_3070ti.append(price_list[name_list.index(name)])
        else:
            name_list_3070.append(name)
            price_3070.append(price_list[name_list.index(name)])
    elif name.count('3080') != 0:
        if (name.lower().count(' ti ') != 0) or (name.lower().count('0ti') != 0) or (name.lower().count('ti,') != 0):
            name_list_3080ti.append(name)
            price_3080ti.append(price_list[name_list.index(name)])
        else:
            name_list_3080.append(name)
            price_3080.append(price_list[name_list.index(name)])
    elif name.count('3090') != 0:
        if (name.lower().count(' ti ') != 0) or (name.lower().count('0ti') != 0) or (name.lower().count('ti,') != 0):
            name_list_3090ti.append(name)
            price_3090ti.append(price_list[name_list.index(name)])
        else:
            name_list_3090.append(name)
            price_3090.append(price_list[name_list.index(name)])
    elif name.count('6600') != 0:
        if name.lower().count('xt') != 0:
            name_list_6600xt.append(name)
            price_6600xt.append(price_list[name_list.index(name)])
        else:
            name_list_6600.append(name)
            price_6600.append(price_list[name_list.index(name)])
    elif name.count('6650') != 0:
        name_list_6650xt.append(name)
        price_6650xt.append(price_list[name_list.index(name)])
    elif name.count('6700') != 0:
        name_list_6700xt.append(name)
        price_6700xt.append(price_list[name_list.index(name)])
    elif name.count('6750') != 0:
        name_list_6750xt.append(name)
        price_6750xt.append(price_list[name_list.index(name)])
    elif name.count('6800') != 0:
        if name.lower().count('xt') != 0:
            name_list_6800xt.append(name)
            price_6800xt.append(price_list[name_list.index(name)])
        else:
            name_list_6800.append(name)
            price_6800.append(price_list[name_list.index(name)])
    elif name.count('6900') != 0:
        name_list_6900xt.append(name)
        price_6900xt.append(price_list[name_list.index(name)])
    elif name.count('6950') != 0:
        name_list_6950xt.append(name)
        price_6950xt.append(price_list[name_list.index(name)])


print(len(name_list))

a = len(name_list_1050ti) + len(name_list_1650) + len(name_list_1650s) + len(name_list_1660) + len(name_list_1660s) + len(name_list_1660ti) + len(name_list_2060) + len(name_list_2060s) + len(name_list_3050) + len(name_list_3060) + len(name_list_3060ti) + len(name_list_3070) + len(name_list_3070ti) + len(name_list_3080) + len(name_list_3080ti) + len(name_list_3090) + len(name_list_3090ti) + len(name_list_6500xt) + len(name_list_6600) + len(name_list_6600xt) + len(name_list_6650xt) + len(name_list_6700xt) + len(name_list_6750xt) + len(name_list_6800) + len(name_list_6800xt) + len(name_list_6900xt) + len(name_list_6950xt)

print(a) ## getting the length for debugging purposes

name_list_general = []
name_list_general = name_list_1660s + name_list_1660ti + name_list_1660 + name_list_1650s + name_list_1650 + name_list_1050ti + name_list_2060 + name_list_2060s + name_list_3050 + name_list_3060 + name_list_3060ti + name_list_3070ti + name_list_3070 + name_list_3080ti + name_list_3080 + name_list_3090 + name_list_3090ti + name_list_6500xt + name_list_6600 + name_list_6600xt + name_list_6650xt + name_list_6700xt + name_list_6750xt + name_list_6800 + name_list_6800xt + name_list_6900xt + name_list_6950xt

price_list_general = []
price_list_general = price_1660s + price_1660ti + price_1660 + price_1650s + price_1650 + price_1050ti + price_2060 + price_2060s + price_3050 + price_3060 + price_3060ti + price_3070ti + price_3070 + price_3080ti + price_3080 + price_3090 + price_3090ti + price_6500xt + price_6600 + price_6600xt + price_6650xt + price_6700xt + price_6750xt + price_6800 + price_6800xt + price_6900xt + price_6950xt

#print(name_list_general)

dict = {
    'Name': name_list_general,
    'Price (BRL)': price_list_general
}

#tabela = pd.DataFrame.from_dict(dict, orient='index')
tabela = pd.DataFrame(dict)
tabela = tabela.sort_values(by=['Price (BRL)'])
#tabela = tabela.transpose()

#tabela = pd.DataFrame.from_dict(dict, orient='index')
#aa = tabela.sort_values(by=['Preço'], ascending=True)
#print(aa)
#tabela = tabela.transpose()
tabela.to_excel('example.xlsx')