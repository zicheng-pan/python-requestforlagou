from lxml import etree
import jieba
import pandas as pd

word_count = {}
filter_word = ['.', ' ', '\n']


def printEtree(element):
    return etree.tostring(element, encoding='utf-8', pretty_print=True, method='html').decode('utf-8')


contentstr = ""
for line in open("temp.html", encoding="utf-8").readlines():
    contentstr = contentstr + line
job = etree.HTML(contentstr)
job_detail_str = printEtree(job.xpath('//dd[@class="job_bt"]/div')[0])
for item in job_detail_str.split("<br>"):
    if "职位描述" in item:
        continue
    ds_list = list(jieba.cut(item))
    key_word_count = pd.Series(ds_list)
    print(str(ds_list))
