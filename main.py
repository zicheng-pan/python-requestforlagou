import requests
from lxml import etree
import re
import time
import http.cookiejar

url = "https://www.lagou.com/wn/jobs?px=new&xl=%E6%9C%AC%E7%A7%91&yx=25k-50k&kd=Java&pn={page}&city=%E5%8C%97%E4%BA%AC"


def printEtree(element):
    return etree.tostring(element, encoding='utf-8', pretty_print=True, method='html').decode('utf-8')


for i in range(10):
    data = requests.get(url.format(page=2))

    # print(data.text)
    page = etree.HTML(data.text, parser=etree.HTMLParser(encoding='utf-8'))
    joblist = page.xpath(u'//div[@id="jobList"]//div[@class="item__10RTO"]')

    print(len(joblist))
    for i in joblist:
        str_item = printEtree(i)
        job_href = re.findall("a href=\"(.*?)\" target=\"_blank\">", str_item, re.S)[0]
        print(job_href)
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0',
            ':authority': 'www.lagou.com',
            ':method': 'GET',
            ':path': '/jobs/8868310.html',
            ':scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': ' max-age=0'
        }
        # HEADER
        headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Host': 'www.lagou.com',
                   'Origin': 'http://www.lagou.com',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Referer': 'http://www.lagou.com',
                   'Proxy-Connection': 'keep-alive',
                   'X-Anit-Forge-Code': '0',
                   'X-Anit-Forge-Token': None}

        # COOKIES
        cookies = {'JSESSIONID': '99021FFD6F8EC6B6CD209754427DEA93',
                   '_gat': '1',
                   'user_trace_token': '20210824170403-d8e0baf8-3045-4098-b425-c0a58cdc84e3',
                   'PRE_UTM': '',
                   'PRE_HOST': '',
                   'PRE_SITE': '',
                   'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F',
                   'LGUID': '20170203041008-9835b1c9-e983-11e6-8a36-525400f775ce',
                   'SEARCH_ID': 'bfed7faa3a0244cc8dc1bb361f0e8e35',
                   'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1486066203',
                   'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1486066567',
                   '_ga': 'GA1.2.2003702965.1486066203',
                   'LGSID': '20170203041008-9835b03a-e983-11e6-8a36-525400f775ce',
                   'LGRID': '20170203041612-714b1ea3-e984-11e6-8a36-525400f775ce'}

        job_detail = requests.get(job_href,headers=headers,cookies=cookies).text
        print(job_detail)
        job = etree.HTML(job_detail)
        job_detail_str = printEtree(job.xpath('//div[@id="job_detail"]/dd[2]/div')[0])

        print(job_detail_str)
        time.sleep(1)
