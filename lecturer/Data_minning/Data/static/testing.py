# import random

# # letter = ('A','B','C','D','E','F','G','H','I','J')
# # for i in range(1):

# #     x = str(random.randint(1,1000)) + random.choice(letter)
# #     print(x)


# def card():
#     letter = ('A','B','C','D','E','F','G','H','I','J')
#     for i in range(1):
#         x = str(random.randint(1,1000)) + random.choice(letter)
#         return(x)
#         # print(x)
    


# card=card()
# print(card)


# def nonsense(add,p):

#     me = p

#     c = me + add
#     return c


# s = nonsense(2,4)
# print(s)

import mechanize
import random
from bs4 import BeautifulSoup
import lxml
import requests


mysite = requests.get("http://127.0.0.1:8000/Data/Userlogin")

soup = BeautifulSoup(mysite.text,'lxml')
with open('index.txt','wb+') as f:
    f.write(soup)

print(soup)




# learning = mechanize.Browser()

# learning.open("http://127.0.0.1:8000/Data/Userlogin")
# learning.select_form(nr=0)
# learning['username']="Holland"
# learning['password']="Afvjsdfj"

# response = learning.submit()



#cookies hijacking
# session = requests.Session()

# parameters = {
#     'username':'Holland',
#     'password':'#####',

# }

# learning = session.post("http://127.0.0.1:8000/Data/Userlogin",data=parameters)

# print(f'leaning tutorial cokie is : {learning.cookies.get_dict()}')
# print(learning.text)
