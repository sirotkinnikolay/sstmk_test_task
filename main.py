import requests
import re
import socket


class UrlPage:
    def __init__(self, url, s_pattern, host_n, phone_company_pattern):
        self.s_pattern = s_pattern
        self.host_n = host_n
        self.response = requests.get(url)
        self.phone_company_pattern = phone_company_pattern

    def page(self):
        if self.response.status_code == 200:
            return "Сайт работает"
        else:
            return f'Ошибка: код ответа: {self.response.status_code}'

    def ip_address(self):
        ip_address = socket.gethostbyname(self.host_n)
        return f'IP адрес: {ip_address}'

    def search_phone_number(self):
        phone_numbers = re.findall(self.s_pattern, self.response.text)
        if not phone_numbers:
            return 'На данной странице номеров телефона подходящих шаблону поиска не обнаружено.'
        else:
            number_list = [number for number in phone_numbers]
            return f'Найдены номера телефона, подходящие шаблону поиска: {number_list}'
    def company_phone_number(self):
        phone_company = re.findall(self.phone_company_pattern, self.response.text)[0][4:]
        return f'На странице найден телефон компании: {phone_company}'


if __name__ == '__main__':
    page_url = "http://sstmk.ru"
    search_patter = r'(\+d{1,3}\(d+\)d+-d+-d+|\(d+\)d+-d+-d+)'
    phone_company_pat = r'tel:\d+'
    host_name = "sstmk.ru"
    try:
        instance = UrlPage(page_url, search_patter, host_name, phone_company_pat)
        print(instance.page())
        print(instance.ip_address())
        print(instance.search_phone_number())
        print(instance.company_phone_number())
    except Exception as e:
        print(f'Ошибка: {type(e).__name__}')
