import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain_price.models import Vendor
from vps.models import VPS

homepage = "https://nhanhoa.com/"
urls = "https://nhanhoa.com/may-chu/may-chu-ao-vps.html"
source = "NhanHoa"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_pack_A():
    dom = get_dom(urls)
    mark = dom.findAll(class_='col-md-4 col-sm-6')[0].contents[1]
    pack = mark.contents[1].text.strip()
    vcpu = mark.find('ul').contents[3].contents[2].contents[0].strip(' Cores')
    ssd = mark.find('ul').contents[5].contents[2].contents[0].strip('GB ')
    ram = mark.find('ul').contents[7].contents[2].contents[0].strip('GB ')
    price_3 = mark.find('h2', text='3 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_1 = str(round(float(price_3) / 3))
    price_6 = mark.find('h2', text='6 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_12 = mark.find('h2', text='12 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_B():
    dom = get_dom(urls)
    mark = dom.findAll(class_='col-md-4 col-sm-6')[1].contents[1]
    pack = mark.contents[1].text.strip()
    vcpu = mark.find('ul').contents[3].contents[2].contents[0].strip(' Cores')
    ssd = mark.find('ul').contents[5].contents[2].contents[0].strip('GB ')
    ram = mark.find('ul').contents[7].contents[2].contents[0].strip('GB ')
    price_3 = mark.find('h2', text='3 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_1 = str(round(float(price_3) / 3))
    price_6 = mark.find('h2', text='6 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_12 = mark.find('h2', text='12 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_C():
    dom = get_dom(urls)
    mark = dom.findAll(class_='col-md-4 col-sm-6')[2].contents[1]
    pack = mark.contents[1].text.strip()
    vcpu = mark.find('ul').contents[3].contents[2].contents[0].strip(' Cores')
    ssd = mark.find('ul').contents[5].contents[2].contents[0].strip('GB ')
    ram = mark.find('ul').contents[7].contents[2].contents[0].strip('GB ')
    price_3 = mark.find('h2', text='3 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_1 = str(round(float(price_3) / 3))
    price_6 = mark.find('h2', text='6 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_12 = mark.find('h2', text='12 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_D():
    dom = get_dom(urls)
    mark = dom.findAll(class_='col-md-4 col-sm-6')[3].contents[1]
    pack = mark.contents[1].text.strip()
    vcpu = mark.find('ul').ul.contents[3].contents[2].contents[0].strip(' Cores')
    ssd = mark.find('ul').ul.contents[5].contents[2].contents[0].strip('GB ')
    ram = mark.find('ul').ul.contents[7].contents[2].contents[0].strip('GB ')
    price_3 = mark.find('h2', text='3 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_1 = str(round(float(price_3) / 3))
    price_6 = mark.find('h2', text='6 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_12 = mark.find('h2', text='12 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_E():
    dom = get_dom(urls)
    mark = dom.findAll(class_='col-md-4 col-sm-6')[4].contents[1]
    pack = mark.contents[1].text.strip()
    vcpu = mark.find('ul').contents[3].contents[2].contents[0].strip(' Cores')
    ssd = mark.find('ul').contents[5].contents[2].contents[0].strip('GB ')
    ram = mark.find('ul').contents[7].contents[2].contents[0].strip('GB ')
    price_3 = mark.find('h2', text='3 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_1 = str(round(float(price_3) / 3))
    price_6 = mark.find('h2', text='6 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_12 = mark.find('h2', text='12 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_F():
    dom = get_dom(urls)
    mark = dom.findAll(class_='col-md-4 col-sm-6')[5].contents[1]
    pack = mark.contents[1].text.strip()
    vcpu = mark.find('ul').contents[3].contents[2].contents[0].strip(' Cores')
    ssd = mark.find('ul').contents[5].contents[2].contents[0].strip('GB ')
    ram = mark.find('ul').contents[7].contents[2].contents[0].strip('GB ')
    price_3 = mark.find('h2', text='3 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_1 = str(round(float(price_3) / 3))
    price_6 = mark.find('h2', text='6 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    price_12 = mark.find('h2', text='12 Tháng').parent.contents[3].contents[3].text.strip('Tổng: đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]



class Command(BaseCommand):
    help = 'Crawl PriceList'
    

    def add_arguments(self, parser):
        parser.add_argument('-A',action='store_true', help='crawl pack A')
        parser.add_argument('-B',action='store_true', help='crawl pack B')
        parser.add_argument('-C',action='store_true', help='crawl pack C')
        parser.add_argument('-D',action='store_true', help='crawl pack D')
        parser.add_argument('-E',action='store_true', help='crawl pack C')
        parser.add_argument('-F',action='store_true', help='crawl pack F')
        parser.add_argument('-a',action='store_true', help='crawl all')
    

    def handle(self, *args, **kwargs):
        def new_pack_1():
            lst = get_pack_A()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_2():
            lst = get_pack_B()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_3():
            lst = get_pack_C()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_4():
            lst = get_pack_D()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_5():
            lst = get_pack_E()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_6():
            lst = get_pack_F()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='NhanHoa'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        if kwargs['A']:
            new_pack_1()
        elif kwargs['B']:
            new_pack_2()
        elif kwargs['C']:
            new_pack_3()
        elif kwargs['D']:
            new_pack_4()
        elif kwargs['E']:
            new_pack_5()
        elif kwargs['F']:
            new_pack_6()
        elif kwargs['a']:
            new_pack_1()
            new_pack_2()
            new_pack_3()
            new_pack_4()
            new_pack_5()
            new_pack_6()
        else:
            print("Invalid options! Please type '-h' for help")