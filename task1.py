#encoding: utf-8
import pandas as pd

pd.set_option('display.width', 300)
pd.set_option('display.max_columns', 300)
pd.set_option('display.max_colwidth', 300)

rating = pd.read_csv("rating.csv", header=None, names=['userid', 'bookid', 'score'], dtype={'bookid': 'int'}).copy()

# task1.输出rating.csv中所有书本各自的平均得分
print("average score for each book:\n")
print(rating.groupby('bookid')['score'].mean())

to_read = pd.read_csv("to_read.csv").copy()
to_read_top_50 = to_read.groupby('book_id', as_index=False)['book_id'].agg({'to_read_count': 'count'}).sort_values(
    by='to_read_count', ascending=False)[:50]
# print(to_read_top_50)

tags = pd.read_csv("tags.csv").copy()
book_tags = pd.read_csv("book_tags.csv").copy()
books = pd.read_csv("books.csv").copy()
books = books[books['book_id'].isin(to_read_top_50.book_id)]
# task2 找出最多人想读的50本书
books.to_csv('hot_50_books.csv')

book_tags = book_tags[book_tags['_goodreads_book_id_'].isin(books['goodreads_book_id'])]
book_tag=book_tags.groupby('tag_id',as_index=False)['count'].sum().sort_values(by="count", ascending=False)[:10]

tag_name = tags[tags['tag_id'].isin(book_tag['tag_id'])]

tag_result = pd.merge(book_tag,tag_name)
# 找出这50本书对应最热门的10个标签，以csv格式存储
tag_result.to_csv("hot_10_tag.csv")

from pyecharts import options as opts
from pyecharts.charts import WordCloud



#task5 用词云方式展示10个热门标签
words = [(key,value) for key,value in zip(tag_result['tag_name'].tolist(),tag_result['count'].tolist())]
wordcloud = WordCloud()
wordcloud.add("",words,word_size_range=[20,100])
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title="Tags"))
wordcloud.render()



