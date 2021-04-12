import requests
from lxml import etree

url = 'http://www.iwencai.com/unifiedwap/board/gmjj'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Referer': 'http://www.iwencai.com/unifiedwap/home/index',
    'Cookie': 'cid=0ffc231bfc3af3efb7f2ad5410a6ac901611821414; ComputerID=0ffc231bfc3af3efb7f2ad5410a6ac901611821414; WafStatus=0; guideState=1; other_uid=Ths_iwencai_Xuangu_nqgi83xl0x3xz3ibvtyyk6qop8c8s1ho; PHPSESSID=ccefcde422e5cbd695abba5aab6b2118; v=A5NfLmqj98iNFLucVpKIDtN0Ihy-SCcK4dxrPkWw77LpxL3KzRi3WvGs-4xW'
}

res = requests.get(url, headers=headers)
print(res.content.decode())
