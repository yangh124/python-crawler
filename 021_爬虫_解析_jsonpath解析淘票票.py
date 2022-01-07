import json
import urllib.request
import jsonpath

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'cookie': 'cna=xpiJGIzHOkECAX123xwW1liO;tracknick=%5Cu6768%5Cu7693124;hng=CN%7Czh-CN%7CCNY%7C156;thw=cn;miid=70579962686733061;sgcookie=E100b3xZBLBei0wALtaw%2BfBDHe99s7CNgCpSc2ekqxGDRtiWZv7NDJ%2Fi3w3MuMDkYVhdZc9qN%2FgytmBJrnf3Qt7KRtcEzxP4Zu3F1fNb9th12Ek%3D;_cc_=UtASsssmfA%3D%3D;enc=hxskXniHgV%2Bx9%2Fjgp19MbI0QxZJ3fLaEJLK4Kj%2BmwIlP7W4Ya%2BnWYHg64o4h0J87Xgk%2FXdCCJxwsr3Ptxigo2g%3D%3D;t=c0f16de680c1b07a60b2c2d75556762a;cookie2=1aff09c95a450cdcab486aa3502faa41;v=0;_tb_token_=e09e19b8b7e5e;xlly_s=1;_m_h5_tk=9c5d06ae1254d5b2ab02cc43e483a792_1641567367272;_m_h5_tk_enc=8842153e163971860a53dd896e24b1b1;tfstk=cMQ1BOG8MtQFD9rq71NEgKE4juLfaL0BMlOR1icRLa2Uoj1MpsmnzLtqdiDDuIdC.;l=eBT3sXQejS2YBPmWBO5Bhurza77TeQOb4nVzaNbMiInca1uf9FGDoNCpBnCvWdtjgtCbxetzTBEsnRLHRnO0hc0c0xb0hlvjfxvO.;isg=BNLSiJL957UAWhq_xiy713HII56049Z9O2WMoZwoxAVwr3KphHJbjZnJHwuT604V',
    'pragma': 'no-cache',
    'referer': 'https://www.taobao.com/',
    'sec-ch-ua': '"Not;ABrand";v="99","GoogleChrome";v="97","Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_15_7)AppleWebKit/537.36(KHTML,likeGecko)Chrome/97.0.4692.71Safari/537.36',
}

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1641560077609_63&jsoncallback=jsonp64&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

jsonObj = json.loads(content)

city_list = jsonpath.jsonpath(jsonObj, '$..regionName')

print(len(city_list))
print(city_list)
