import requests
from lxml import etree
import re
import time
import random

url = "https://www.lagou.com/wn/jobs?px=new&xl=%E6%9C%AC%E7%A7%91&yx=25k-50k&kd=Java&pn={page}&city={city}"

# search_id = "c20f0701d9aa459eae69bfbcf9ee6dfd"
response_cookies = {}


def printEtree(element):
    return etree.tostring(element, encoding='utf-8', pretty_print=True, method='html').decode('utf-8')


for i in range(2, 10):
    data = requests.get(url.format(page=i,city="广州"))
    get_cookie = requests.utils.dict_from_cookiejar(data.cookies)
    print(get_cookie)
    # print(data.text)
    page = etree.HTML(data.text, parser=etree.HTMLParser(encoding='utf-8'))
    joblist = page.xpath(u'//div[@id="jobList"]//div[@class="item__10RTO"]')

    print(len(joblist))
    for i in joblist:
        str_item = printEtree(i)
        job_href = re.findall("a href=\"(.*?)\" target=\"_blank\">", str_item, re.S)[0]
        job_id = job_href[str(job_href).rindex("/"):]
        job_href = job_href
        print(job_href)

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

        # COOKIES
        cookies = {
            "_gid": "GA1.2.841918748.1629956487",
            "gate_login_token": "eba1df6d0cb099999339dc20b1ce1db75b200942887ff15b",
            "LGUID": "20210824133641-2491be5d-5d18-46a0-9849-f9abef39f507",
            "_ga": "GA1.2.496549005.1629783402",
            "user_trace_token": "20210824133636-0a9e9cbf-f454-4418-9ae5-a9de8a25722d",
            "X_MIDDLE_TOKEN": "ea18914f7f1bead5ecf871227d29e9c2",
            "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2217b76a5df55143-0cc32367a31c51-e726559-2304000-17b76a5df56457%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Safari%22%2C%22%24browser_version%22%3A%2210.0%22%7D%2C%22%24device_id%22%3A%2217b76a5df55143-0cc32367a31c51-e726559-2304000-17b76a5df56457%22%7D",
            "__lg_stoken__": "25f0065d50fab3972b50c243e56dde77826a244c66309d4454d0cfd8a537abf22c3c6d85cefd932c19009c2decc83b8e214e47ecea93ae9872b1064ae02fc7628ac197bb602a",
            "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1629783402,1629956486",
            "sensorsdata2015session": "%7B%7D",
            "X_HTTP_TOKEN": "2c0d7f0b347fea5d3340799261189728ea53a7dc60",
            "PRE_SITE": "",
            "LGSID": "20210826173354-9c19a76b-fff6-4044-a628-73e4db74e35d",
            "PRE_UTM": "",
            "PRE_HOST": "",
            "PRE_LAND": "https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fmsg%3Dvalidation%26uStatus%3D2%26clientIp%3D124.64.19.31%26u%3D2",
            "LG_HAS_LOGIN": "1",
            "privacyPolicyPopup": "false",
            "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1629971161",
            "unick": "%E6%BD%98%E5%AD%90%E6%88%90",
            "LGRID": "20210826174600-8009c5bf-1d38-45fc-892e-de184b663f85",
            "LG_LOGIN_USER_ID": "d9c9883bcd72da1a7cd2149ac3594f4a0a18c8932080a6bf",
            "_putrc": "A3BD2F79AFBC1940",
            "login": "true"
        }
        cookies.update(response_cookies)
        job_detail = requests.get(job_href, headers=headers, cookies=cookies)

        response_cookies = job_detail.cookies.get_dict()
        print(response_cookies)
        job_detail = job_detail.text
        print(job_detail)

        try:
            job = etree.HTML(job_detail)
            job_detail_str = printEtree(job.xpath('//dd[@class="job_bt"]/div')[0])
            with open('jobdetails/' + job_id + ".txt", mode="w", encoding="utf-8") as file:
                file.write(job_detail_str)

            time.sleep(random.randint(10, 20))
        except Exception as e:
            with open('jobdetails/' + job_id + ".txt", mode="w", encoding="utf-8") as file:
                file.write(job_detail)

            time.sleep(random.randint(30, 50))

    print("finished")