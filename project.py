from bs4 import BeautifulSoup
import requests
url='https://www.americanexpress.com/'
s=requests.session()
login=s.get('https://www.americanexpress.com/')
login_soup=BeautifulSoup(login.content)

	

for element in login_soup.find_all('script'):
	if element.has_attr('src'):
		if 'homepage.min.js' in element['src']:
			js_url=url[:-1] + element['src']

js=s.get(js_url)

login_url=re.search('AHP.url.login.CARDS_ACTION="(.*?)";',js.text).group(1)
login_action_dest=re.search('AHP.url.login.CARDS_DEST="(.*?)";',js.text).group(1)

data={}
for tag in login_soup.find(id='ssoform').div:
	if "\n" not in tag: data[tag['name']]=tag['value']

data['DestPage']=login_action_dest
data['act']='soa'
data['Face']='en_US'
data['cardsmanage']=cards


Accept: text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US, en; q=0.5
Cache-Control: max-age=0
Connection: Keep-Alive
Content-Length: 1131
Content-Type: application/x-www-form-urlencoded
Cookie: visid_incap_1658692=m3ffqkijTwyuU+N7zmuCEXEscFsAAAAAQUIPAAAAAAC/jWAhNL9vPwThy5vc7jZj; nlbi_1658692=VnvcXRQjXDPf5fnMS1kgQAAAAACNthhwzbGL5kGAyJ6OXFB/; incap_ses_888_1658692=jwHXbYGEVyX/XvrRvc9SDHEscFsAAAAAo2QSbqIhs3B7CsOkzxL5lw==; tglr_tenant_id=b8e5d34b-24f1-4e1a-b9c4-234e8c2519fb; tglr_sess_count=2; tglr_req=https://www.americanexpress.com/; tglr_ref=; tglr_sess_id=e193f792-c9c8-4d23-a448-c2d5da29426f; tglr_anon_id=3f0c2102-6f87-412b-99b7-942f9c6de818; _uetmsclkid=_uet5b7daf9c176f16cbd377f4ec3b1e5918; _ga=GA1.2.339228806.1534078073; _gid=GA1.2.214393371.1534078073; RVID=14c2b859-cb22-4ddb-a8ce-0b845ae618f4%7C0%7C1534078073%7Ccard.americanexpress.com; fs_uid=www.fullstory.com`Y87Y`5350168224595968:5629499534213120`f3882613-37c4-4f71-b61e-4e6f1bde9638`; AMCV_5C36123F5245AF470A490D45%40AdobeOrg=793872103%7CMCIDTS%7C17756%7CMCMID%7C17317323792541311231340074475439899795%7CMCAAMLH-1534682881%7C7%7CMCAAMB-1534682881%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1534078021.923%7CNONE%7CMCSYNCSOP%7C411-17763%7CMCAID%7C2DB8163A8507D730-4000011A0000DE8D%7CvVersion%7C2.1.0; AMCVS_5C36123F5245AF470A490D45%40AdobeOrg=1; gctracus=gctvid=2018-08-12/12:47:55-5ff3ac45-07fb-47cf-ddf8-cb969ddcb4db&affid=&psku=&pse=bing&skw=73172534&lts=2018-08-12/08:47:50:237&veid=&crtv=&affid_ir=&affname=&sid=&refsite=www.bing.com&eep=28009&lan=1; s_vi=[CS]v1|2DB8163A8507D730-4000011A0000DE8D[CE]; TS0114bdae=018378d52a88abeffd3eea6f0c88955be0320d38731a5cced3326b7784df63676122204a47f2eff0f8b1efc427afd702ce65081a3c; s_pers=%20s_campStack%3D%255B%255B%2527extlink%25253DCH%25253Dps-CU%25253Dus-BU%25253Dccsg-SE%25253Dbing-SKW%25253DRV_CreditCard%2527%252C%25271534078076235%2527%255D%255D%7C1691844476235%3B%20s_visit%3D1%7C1534079888110%3B%20s_vnum%3D1%7C1691758088142%3B%20gpv_v41%3DUS%257CAMEX%257CHome%257CUSHomepage%7C1534079951148%3B%20s_uvid%3D1534078088137776%7C1691758151186%3B%20s_invisit%3Dtrue%7C1534079951188%3B; s_sess=%20s_dedupeCM%3Dextlink%253DCH%253Dps-CU%253Dus-BU%253Dccsg-SE%253Dbing-SKW%253DRV_CreditCardUS%253ALegacy%2520Paid%2520Searchbing.comp%257CKeyword%2520Unavailablen%252Fa%3B%20s_cpc%3D0%3B%20s_cc%3Dtrue%3B%20tp%3D914%3B%20s_ppv%3DUS%25257CAMEX%25257CHome%25257CUSHomepage%252C72%252C72%252C659%3B; mmapi.p.pd=%22-643324107%7CAQAAAApVAwD%2F5M36kRByOgABEQABQhHCW7oBAMNC3tNRANZIw0Le01EA1kgAAAAA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8ABkRpcmVjdAGREAEAAAAAAAAAAAD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8AAAAAAAAAAUU%3D%22; mmapi.p.srv=%22lvsvwcgus07%22; mmapi.p.uat=%7B%22GenerationPage%22%3A%22%2F%22%7D; axplocale=en-US; mm_pc=%7B%22affluentIndex%22%3A%22%22%7D; aampros=SBO%3D1; aam_rv=AAM%3D388075%2C6903341; amex_cms=Amex%3D1%3B2; aam_id=17476258922753098831355706304761266203; LPVID=E3Y2Y3YWMxYzE1NTAzNzJk; LPSID-14106077=wrmdbEC6QyGMMwi_T_tj_g
Host: online.americanexpress.com
Referer: https://www.americanexpress.com/
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134





Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US, en; q=0.5
Connection: Keep-Alive
Host: global.americanexpress.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134

