import requests
import json
import codecs

# 模拟浏览器请求
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
}

# 抓取新闻评论url
url = 'http://comment.sports.163.com/sports2_bbs/DHU2MKF20005877U.html'

# 创建获取评论url
def createUrl(url, offset, limit):
    # 网易评论加载API链接
    s1 ='http://comment.sports.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/'
    s2 ='/comments/newList?offset='
    name = url.split('/')[-1].split('.')[0]
    u = s1 + str(name) + s2 + str(offset) + '&limit=' + str(limit)
    return u


def save_to_file(list, filename):
    with codecs.open(filename, 'a', encoding='utf-8') as f:
        f.write(list + '\n')



res = requests.get(url=createUrl(url,1,40), headers=headers).content
data = json.loads(res.decode())

# 控制台输出评论信息
for key in data['comments'].keys():
    comment = data['comments'][key]['content']
    print(comment)
    save_to_file(comment, 'comments.txt')

print("写入文件成功!")
