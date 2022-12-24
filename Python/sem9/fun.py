import requests, json

def joke():
    api_url = 'http://rzhunemogu.ru/RandJSON.aspx?CType=1'

    response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response
    
    if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
        try:
            return json.loads(response.text, strict=False)['content']
        except:
            return 'Мой генератор анекдотов перегрелся, попробуйте позднее.'
    else:
       return 'Мой генератор анекдотов перегрелся, попробуйте позднее.'    # При другом коде ответа выводим этот код


#__________________________________________________________________________________________


def cat():
    api_url = 'https://aws.random.cat/meow'

    response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response
    
    if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
        return json.loads(response.text, strict=False)['file']
    else:
       return 'Котики спят, приходите позже'    # При другом коде ответа выводим этот код

#_______________________________________________________________________________________

def yesno():
    api_url = 'https://yesno.wtf/api'

    response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response

    if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
        return json.loads(response.text, strict=False)['image']
    else:
       return 'Это слишком серьезный выопрос, не стоит полагаться на бота'    # При другом коде ответа выводим этот код


