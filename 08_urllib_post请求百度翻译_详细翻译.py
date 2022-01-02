import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    # 'Accept': ' */*',
    # 'Accept-Encoding': ' gzip, deflate, br',
    # 'Accept-Language': ' zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cache-Control': ' no-cache',
    # 'Connection': ' keep-alive',
    # 'Content-Length': '117',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=43474593C145572B067ABC8ECC30639D; PSTM=1610787521; BAIDUID=29FFECE3408253A17D848D03D00DE54C:FG=1; H_WISE_SIDS=107316_110085_127969_131423_144966_154213_156927_165135_165936_166147_166181_167300_168030_168540_168762_168768_169066_169308_169648_169770_170151_170155_170346_170355_170449_170473_170548_170579_170580_170583_170589_170658_170798_170817_170919_170955_171004_171158_171216_171381_171523_171573_171581_171816_171916_171989_171992; __yjs_duid=1_15b69a0b0717f6e94ff92a36a118a0ae1619225545254; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-179%3A; BDSFRCVID_BFESS=H_COJexroG04WdoHl3vw--cvEeKKvV3TDYLEOwXPsp3LGJLVgaSTEG0Pt8lgCZu-2ZlgogKKKgOTHICF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=JJkO_D_atKvDqTrP-trf5DCShUFsBpRmB2Q-XPoO3KtMSnbvy-k55RbDqfbq04QiW5cpoMbgylRp8P3y0bb2DUA1y4vpK-ogQgTxoUJ2fnRJEUcGqj5Ah--ebPRiB-b9QgbA5hQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0HPonHj_Wj5cB3j; H_PS_PSSID=35414_35104_34584_35491_35585_35644_35316_26350_35624_35561; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=29FFECE3408253A17D848D03D00DE54C:FG=1; delPer=0; PSINO=5; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1641040603; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1641040603; APPGUIDE_10_0_2=1; __yjs_st=2_Y2UyMGU5MTI4NzRhMzA4NDY1NzQxMzYyNWE0YzBlYTgyY2UxNDFmYTQ1ZmNiYjg3OGMyZjVjMDY2NDgwYTU2Zjg3NTgwNDg2NGY4MTFlZWJiMzE2Yjk0YzBlZWY0YmJiYzg1Zjc1N2NjYjQ0YTc4YjRjYmY1OGVmMDJhZmI0NGM5YWIwZjFlNmFkNWYyNzVmNWZhZjgzNjFjMDNiMzA4OTQyMmRlOTY5M2QyOTY0MDFkOWVlZjMzYTE3M2UyNTRmNjU4M2UyZjFkYjcyZTdmYTg4ZWIzODk4MzEwNDNlNjRiYWVjYThjMGE0ZDJkNWM0ZjI4OTA5ODY0ZDMxOGUxNmNjZjgxMzVmMDljNmU0ZTdhZTFmMzRjOTY5M2ZkMzI1XzdfOTdkYzUxY2E=; ab_sr=1.0.1_MDFjMWEyYjQxZTg5NzA0NWI3Y2RkMDA1OTI1NTI5NGVjMzkyNTM3MTE2NDRjMDM5YjA0ZTYxZjMwN2M3NzhiMDU2ZWRhZDgxMTMyMTM0ZjU5Yzk3ZmY3MjZkYTg4MzgwOGYxZTAyZTcyZWRkOTQzYThmMDMyOTQ1OTlmYTAyNzE0ZmIwNWZiMDNiZDJmYjJiNjUxZDU0NjNhOTNhYzkwMQ==',
    # 'Host': 'fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Pragma': 'no-cache',
    # 'Referer': 'https://fanyi.baidu.com/',
    # 'sec-ch-ua': '"Chromium";v="100", "Google Chrome";v="100", ";Not A Brand";v="99"',
    # 'sec-ch-ua-mobile': ' ?0',
    # 'sec-ch-ua-platform': ' "macOS"',
    # 'Sec-Fetch-Dest': ' empty',
    # 'Sec-Fetch-Mode': ' cors',
    # 'Sec-Fetch-Site': ' same-origin',
    # 'User-Agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4692.71 Safari/537.36',
    # 'X-Requested-With': ' XMLHttpRequest'
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': 'a3d21e72279fbc0344aeaee905662feb',
    'domain': 'common'
}

# post请求必须要encode参数，必须调用encode方法
data = urllib.parse.urlencode(data).encode('UTF-8')

request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

res = json.loads(content)

print(res)
