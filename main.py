import requests
from lxml import etree
import re
import time
import http.cookiejar

url = "https://www.lagou.com/wn/jobs?px=new&xl=%E6%9C%AC%E7%A7%91&yx=25k-50k&kd=Java&pn={page}&city=%E5%8C%97%E4%BA%AC"
search_id = "c20f0701d9aa459eae69bfbcf9ee6dfd"


def printEtree(element):
    return etree.tostring(element, encoding='utf-8', pretty_print=True, method='html').decode('utf-8')


for i in range(10):
    data = requests.get(url.format(page=2))
    get_cookie = requests.utils.dict_from_cookiejar(data.cookies)
    print(get_cookie)
    # print(data.text)
    page = etree.HTML(data.text, parser=etree.HTMLParser(encoding='utf-8'))
    joblist = page.xpath(u'//div[@id="jobList"]//div[@class="item__10RTO"]')

    print(len(joblist))
    for i in joblist:
        str_item = printEtree(i)
        job_href = re.findall("a href=\"(.*?)\" target=\"_blank\">", str_item, re.S)[0]
        job_href = job_href + "?show=" + str(search_id)
        print(job_href)

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

        # COOKIES
        cookies = {"HMACCOUNT_BFESS": "0188598B78001829",
                   "SEARCH_ID": "c20f0701d9aa459eae69bfbcf9ee6dfd",
                   "HMACCOUNT": "0188598B78001829",
                   "H_BDCLCKID_SF_BFESS": "tR4t_DLKtCP3fP36q4vHbP40qxby26nKyg69aJ5nJD_-ExnDKTJ1jj09hM7D-Po4KK-HVljFQpP-HJ72WtnHbJoLKMbmtlRqaD54Kl0MLp7tbb0xyn_VXxPh0xnMBMPj5mOnanvn3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-XDTQbDHOP",
                   "H_BDCLCKID_SF": "tR4t_DLKtCP3fP36q4vHbP40qxby26nKyg69aJ5nJD_-ExnDKTJ1jj09hM7D-Po4KK-HVljFQpP-HJ72WtnHbJoLKMbmtlRqaD54Kl0MLp7tbb0xyn_VXxPh0xnMBMPj5mOnanvn3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-XDTQbDHOP",
                   "BDSFRCVID": "aXAOJeC626BXFs7H54SlhqtaEch29AJTH6aoTYoaeq1pcC5_vniEEG0POf8g0Ku-NKzRogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0f5",
                   "BCLID": "9474617045612028743",
                   "BAIDUID_BFESS": "37F87A1F249F10FA483E35147E244D48:FG=1",
                   "PSINO": "3",
                   "delPer": "0",
                   "BDORZ": "FFFB88E999055A3F8A630C64834BD6D0",
                   "__yjs_duid": "1_77ba2b8809356bcae7d91e9db03cd6271619340000526",
                   "t": "1629620457758",
                   "IPLOC": "CN3100",
                   "SUV": "1619659931400czlzjr",
                   "Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1629903544",
                   "ticketGrantingTicketId": "_CAS_TGT_TGT-2f89c37fd3e9465fac9023d0592b7772-20210825225847-_CAS_TGT_",
                   "_putrc": "A3BD2F79AFBC1940",
                   "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221612589%22%2C%22first_id%22%3A%2217b7d632979aa0-0237501336b243-70687866-2073600-17b7d63297ac94%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2292.0.4515.159%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217b7d632979aa0-0237501336b243-70687866-2073600-17b7d63297ac94%22%7D",
                   "BDSFRCVID_BFESS": "aXAOJeC626BXFs7H54SlhqtaEch29AJTH6aoTYoaeq1pcC5_vniEEG0POf8g0Ku-NKzRogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0f5",
                   "BAIDUID": "37F87A1F249F10FA483E35147E244D48:FG=1",
                   "LGRID": "20210825225902-717e8459-5d69-4638-88dd-106868e771ee",
                   "X_HTTP_TOKEN": "82b1d6c4f81cba8024530992614f78f0f5999e8d8b",
                   "_gat": "1",
                   "hasDeliver": "4",
                   "showExpriedMyPublish": "1",
                   "WEBTJ-ID": "20210825221235-17b7da7d15e171-0b256ccd9c02c3-70687866-2073600-17b7da7d15f5f4",
                   "H_PS_PSSID": "31660_26350",
                   "BDUSS": "nU2NEQ0LTVtcXVuZk4xRmlQRmk1UmZWWndMU2hCUDBaU0hwOGhMVlpCZ1V4TzVnSVFBQUFBJCQAAAAAAAAAAAEAAAAwI3Q5MTA5NDI3UGFuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQ3x2AUN8dgQ",
                   "RECOMMEND_TIP": "true",
                   "__SAFETY_CLOSE_TIME__1612589": "1",
                   "showExpriedCompanyHome": "1",
                   "privacyPolicyPopup": "false",
                   "ab_sr": "1.0.1_YmNmNWM5NzY4MzNlYmMwODhmMWIzNDhlZWJmNWVjNjJkMDQ3YmExMmU0NDI2NWM2NWE1OWRjMDBkOThjMzQ1ODY3ZmIyZTM4NWY2MzQ5YTY3ZWQzNjgxZTY3YTdlNjAwYmFmYmYzODg5NGQyYjYwNmFjMGE0YTBlNzY5MjM3ZmNiMDg1NzZiYzliMWFkZjNlZWE1NjQzODllZjE5ZTM3NQ==",
                   "BCLID_BFESS": "9474617045612028743",
                   "_ga": "GA1.2.1572780078.1629896256",
                   "unick": "%E6%BD%98%E5%AD%90%E6%88%90",
                   "LGSID": "20210825215900-107b09a6-493b-4d3f-83b7-203bae06ddff",
                   "JSESSIONID": "ABAAAECABIEACCAAAC634431C69F8777367F8A5CD23EA62",
                   "user_trace_token": "20210825205735-ebfcea12-4407-4a61-8a98-dc1a6bb597b4",
                   "TG-TRACK-CODE": "index_navigation",
                   "LG_LOGIN_USER_ID": "8f36d01700d753aceb1f128f18135babbe66b8c3aa061c6a",
                   "BIDUPSID": "37F87A1F249F10FA9E833CE9D1AC0954",
                   "gidinf": "x099980109ee1341ad0ee3c6e0006ec657bb06abb598",
                   "index_location_city": "%E5%85%A8%E5%9B%BD",
                   "sensorsdata2015session": "%7B%7D",
                   "gate_login_token": "eba1df6d0cb099999339dc20b1ce1db75b200942887ff15b",
                   "BDUSS_BFESS": "nU2NEQ0LTVtcXVuZk4xRmlQRmk1UmZWWndMU2hCUDBaU0hwOGhMVlpCZ1V4TzVnSVFBQUFBJCQAAAAAAAAAAAEAAAAwI3Q5MTA5NDI3UGFuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQ3x2AUN8dgQ",
                   "showExpriedIndex": "1",
                   "JSESSIONID": "ABAAABAABGJABAJD2EB00FAD32CE604FDB74292060BD6F2",
                   "Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6": "1629896256,1629899940",
                   "_ga": "GA1.3.1572780078.1629896256",
                   "_gid": "GA1.2.1510584531.1629896256",
                   "sajssdk_2015_cross_new_user": "1",
                   "login": "true",
                   "LGUID": "20210825205735-b136f5c2-ea60-4c0e-88c9-1a893c031d35",
                   "PSTM": "1619191137",
                   "LG_HAS_LOGIN": "1",
                   "__lg_stoken__": "4e28d9e49e55147e44c9adad1708d76fc8c980fe6ddc68de3d232bae52340ebba3dc2134cd7e662a493e645415fd0f19025ad7cca2374226e9065edcc8302a15eab023f23f3c"}
        job_detail = requests.get(job_href, headers=headers, cookies=cookies).text
        print(job_detail)
        job = etree.HTML(job_detail)
        job_detail_str = printEtree(job.xpath('//div[@id="job_detail"]/dd[2]/div')[0])

        print(job_detail_str)
        time.sleep(1)
