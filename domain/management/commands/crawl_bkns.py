import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain.models import Domain, Vendor

homepage = "https://www.bkns.vn/"
urls = "https://www.bkns.vn/ten-mien/bang-gia-ten-mien.html"
source = "BKNS"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.findAll("u", text=".vn")[0].parent.parent.parent
    reg_origin = mark_origin.contents[5].contents[0].string.strip(' đ').replace('.', '')
    try:
        dom_sale = get_dom(homepage)
        reg_promotion = int(dom_sale.find("p", text=".vn").nextSibling.text.strip('đ/năm').replace('.', '')) + 10000
    except:
        reg_promotion = reg_origin
    renew_price = mark_origin.contents[6].string.strip(' đ').replace('.', '')
    mark_trans = dom_origin.findAll("u", text=".vn")[1].parent.parent.parent
    trans_price= mark_trans.contents[4].string.strip(' đ').replace('.', '') 
    return [reg_origin, reg_promotion, renew_price, trans_price]
    
def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.findAll("u", text=".net.vn/ .biz.vn/ .com.vn")[0].parent.parent.parent
    reg_origin = mark_origin.contents[5].contents[0].string.strip(' đ').replace('.', '')
    try:
        dom_sale = get_dom(homepage)
        reg_promotion = dom_sale.find("p", text=".com.vn").nextSibling.text.strip('đ/năm').replace('.', '')
    except:
        reg_promotion = reg_origin
    renew_price = mark_origin.contents[6].string.strip(' đ').replace('.', '')
    mark_trans = dom_origin.findAll("u", text=".net.vn/ .biz.vn/ .com.vn")[1].parent.parent.parent
    trans_price= mark_trans.contents[4].string.strip(' đ').replace('.', '')
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".com").parent
    reg_origin = int(mark_origin.contents[2].strong.string.replace('.', '')) * 110 // 100
    try:
        dom_sale = get_dom(homepage)
        mark = dom_sale.find("p", text=".com")
        mark_sibling = mark.nextSibling
        reg_promotion = int(mark_sibling.text.strip('đ/năm').replace('.', '')) * 110 // 100
    except:
        reg_promotion = reg_origin
    renew_price = int(mark_origin.contents[3].string.replace('.', '')) * 110 // 100
    trans_price = int(mark_origin.contents[4].string.replace('.', '')) * 110 // 100
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".net").parent
    reg_origin = int(mark_origin.contents[2].string.replace('.', '')) * 110 // 100
    try:
        dom_sale = get_dom(homepage)
        mark = dom_sale.find("p", text=".net")
        mark_sibling = mark.nextSibling
        reg_promotion = int(mark_sibling.text.strip('đ/năm').replace('.', '')) * 110 // 100
    except:
        reg_promotion = reg_origin
    renew_price = int(mark_origin.contents[3].string.replace('.', '')) * 110 // 100
    trans_price = int(mark_origin.contents[4].string.replace('.', '')) * 110 // 100
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".org").parent
    reg_origin = int(mark_origin.contents[2].strong.string.replace('.', '')) * 110 // 100
    try:
        dom_sale = get_dom(homepage)
        mark = dom_sale.find("p", text=".org")
        mark_sibling = mark.nextSibling
        reg_promotion = int(mark_sibling.text.strip('đ/năm').replace('.', '')) * 110 // 100
    except:
        reg_promotion = reg_origin
    renew_price = int(mark_origin.contents[3].string.replace('.', '')) * 110 // 100
    trans_price = int(mark_origin.contents[4].string.replace('.', '')) * 110 // 100
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".info").parent
    reg_origin = int(mark_origin.contents[2].strong.string.replace('.', '')) * 110 // 100
    try:
        dom_sale = get_dom(homepage)
        mark = dom_sale.find("p", text=".info")
        mark_sibling = mark.nextSibling
        reg_promotion = int(mark_sibling.text.strip('đ/năm').replace('.', '')) * 110 // 100
    except:
        reg_promotion = reg_origin
    renew_price = int(mark_origin.contents[3].string.replace('.', '')) * 110 // 100
    trans_price = int(mark_origin.contents[4].string.replace('.', '')) * 110 // 100
    return [reg_origin, reg_promotion, renew_price, trans_price]


class Command(BaseCommand):
    help = 'Crawl PriceList'

    def add_arguments(self, parser):
        parser.add_argument('-vn',action='store_true', help='crawl .vn')
        parser.add_argument('-comvn',action='store_true', help='crawl .com.vn')
        parser.add_argument('-com',action='store_true', help='crawl .com')
        parser.add_argument('-net',action='store_true', help='crawl .net')
        parser.add_argument('-org',action='store_true', help='crawl .org')
        parser.add_argument('-info',action='store_true', help='crawl .info')
        parser.add_argument('-a',action='store_true', help='crawl all')

    def handle(self, *args, **kwargs):
        def new_vn():
            lst = get_vn()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_comvn():
            lst = get_comvn()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), domain_type='comvn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_com():
            lst = get_com()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_net():
            lst = get_net()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_org():
            lst = get_org()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_info():
            lst = get_info()
            Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKNS'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        if kwargs['vn']:
            new_vn()
        elif kwargs['comvn']:
            new_comvn()
        elif kwargs['com']:
            new_com()
        elif kwargs['net']:
            new_net()
        elif kwargs['org']:
            new_org()
        elif kwargs['info']:
            new_info()
        elif kwargs['a']:
            new_vn()
            new_comvn()
            new_com()
            new_net()
            new_org()
            new_info()
        else:
            print("Invalid options! Please type '-h' for help")
