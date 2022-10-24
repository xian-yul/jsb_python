import json
import socket

import requests


def ipQuery(ip):
    # 淘宝api接口
    url = "http://ip.taobao.com/outGetIpInfo?ip={}&accessKey=alibaba-inc".format(ip)
    req = requests.get(url).text
    json1 = json.loads(req)
    print(json1)
    country = json1["data"]["country"]  # 国
    province = json1["data"]["region"]  # 省
    city = json1["data"]["city"]  # 市
    return "{}-{}-{}".format(country, province, city)

    # ip-api接口
    # url = "http://ip-api.com/json/111.121.64.21?lang=zh-CN"
    # country = json1["country"]  # 国
    # province = json1["regionName"]  # 省
    # city = json1["city"]  # 市
    # print("{}-{}-{}".format(country, province, city))

    # 太平洋api接口
    # url = "http://whois.pconline.com.cn/ipJson.jsp?ip=111.121.64.21&json=true"
    # province = json1["pro"]  # 省
    # city = json1["city"]  # 市
    # print("{}-{}".format(province, city))


# 获取本机（计算机）名
hostname = socket.gethostname()

# 获取本机（计算机）ip
ip = socket.gethostbyname(hostname)
print(hostname, ip)

ip = socket.gethostbyname_ex(hostname)
print(hostname, ip)
ipQuery(ip)
