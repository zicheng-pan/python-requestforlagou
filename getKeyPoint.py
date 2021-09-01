import os

import jieba
import pandas as pd

word_count = {}
filter_word = ['HTML', 'CSS', 'Linux', 'linux', 'jvm', 'JVM', 'Spring', 'ibatis', 'struts', 'NIO', 'nio', 'IoT', '5G',
               'io',
               'cloud', 'Boot', 'TCP', 'IP', 'Nginx', 'nginx',
               'MySQL', 'MongoDB', 'Kafka', 'hadoop', 'Spark', 'spark', 'Flink', '开源', '需求', '沟通', 'NoSQL', 'Hive',
               'Qps',
               'golang', 'rust', 'python', 'c', 'c++', '设计', '模式', '多线程', 'springboot', 'spring-boot', 'boot',
               'spring-cloud', 'cloud', 'hbase', 'clickhouse'
    , 'presto', 'azkaban', 'tomcat', 'Tomcat', 'Oracle', 'Mysql', 'MySql', 'redis', 'kafka', 'mysql', 'hive', 'DEVops',
               'J2EE', 'Docker', 'K8s', 'k8s', 'SAAS', 'SpringMVC']


def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


contentstr = ""
joblist = os.listdir('jobdetails')
for filename in joblist:
    for line in open('jobdetails/' + filename, encoding="utf-8").readlines():
        contentstr = contentstr + line

keyword_dict = {}
jieba.load_userdict('userDic.txt')
ds_list = list(jieba.cut(contentstr, cut_all=False))
key_word_count = pd.Series(ds_list).value_counts()
with open('keyworld.txt', 'w', encoding="utf-8") as file:
    for key, value in key_word_count.iteritems():
        if len(str(key)) >= 2 and len(str(key)) < 10 and int(value) < 380 and int(value) > 15 and not str(key)[
            0].isdigit() and is_Chinese(str(key)) or filter_word.__contains__(str(key)):
            file.write(str(key) + " " + str(value) + "\n")
            keyword_dict[str(key)] = int(value)

result_dict = {}
with open('userDic.txt', encoding='utf-8') as user_dict:
    liens = user_dict.readlines()
    for line in liens:
        line = line[:-1]
        if not keyword_dict.get(line, 0) == 0:
            result_dict[line] = keyword_dict.get(line, 0) * 3

from pyecharts import options as opts
from pyecharts.charts import WordCloud

# task5 用词云方式展示10个热门标签
words = [(key, value) for key, value in zip(result_dict.keys(), result_dict.values())]
wordcloud = WordCloud()
wordcloud.add("", words, word_size_range=[20, 200])
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title="技能树"))
wordcloud.render()
