from bs4 import BeautifulSoup
import requests,re,getpass,io,pandas
url='https://www.americanexpress.com/'
s=requests.session()
login=s.get('https://www.americanexpress.com/')
login_soup=BeautifulSoup(login.content)

js_url=url[:-1] + login_soup.find('script',attrs={'src':re.compile('.*homepage.min.js.*')})['src']

js=s.get(js_url)

login_url=re.search('AHP.url.login.CARDS_ACTION="(.*?)";',js.text).group(1)
login_action_dest=re.search('AHP.url.login.CARDS_DEST="(.*?)";',js.text).group(1)

data={}
for tag in login_soup.find(id='ssoform').div:
	if "\n" not in tag: data[tag['name']]=tag['value']

data['DestPage']=login_action_dest
data['act']='soa'
data['Face']='en_US'
data['cardsmanage']='cards'
data['UserID']='abigails171'
data['Password']=getpass.getpass()

login_response = s.post(login_url,data=data)

login_response_soup = BeautifulSoup(login_response.content)

statements_url=login_response_soup.find_all('a',string=re.compile('Statements &.*'))[0]['href']

statements_response=s.get(statements_url)

statements_soup=BeautifulSoup(statements_response.content)


data={


'sorted_index': '0',
'BPIndex': '0',
'suppIndex': '',
'liteEnabled': 'false',
'mycaLite': 'false',
'startDate': '07202018',
'endDate': '08192018',
'sortBy': 'undefined',
'sortOrder': 'undefined',
'sortClicked': 'false',
'request_type': 'authreg_Statement',
'Face': 'en_US',
'refSeNumbers': '',
'downloadType': 'C',
'downloadView': 'C',
'numberOfPages': '1',
'totalTrans': '70',
'totalTransCount': '70',
'pageNumber': '1',
'downloadIndicator': 'false',
'downloadWithETDTool': 'false',
'viewType': 'L',
'reportType': '1'
}

download_response=s.post('https://online.americanexpress.com/myca/estmt/us/downloadTxn.do',data=data)

stream = io.StringIO()

for string in download_response.content.decode("utf-8").split("\n"):
	stream.write(string+"\n")

stream.seek(0)

df=pandas.read_csv(stream,header=None)

amex_total=df[7].sum()



"""

Request URL: https://online.americanexpress.com/myca/estmt/us/downloadTxn.do
Request Method: POST
Status Code: 200 OK
Remote Address: 23.34.75.184:443
Referrer Policy: no-referrer-when-downgrade
Cache-Control: max-age=86400
Connection: keep-alive
Content-Disposition: attachment;filename=Transactions.csv
Content-Language: en-US
Content-Length: 7925
Content-Type: application/x-csv
Date: Mon, 13 Aug 2018 23:23:30 GMT
Expires: Tue, 14 Aug 2018 23:23:30 GMT
LastModified: Mon, 13 Aug 2018 23:23:30 GMT
Pragma: max-age=86400
Strict-Transport-Security: max-age=15552000; includeSubDomains
X-Content-Type-Options: nosniff
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 381
Content-Type: application/x-www-form-urlencoded
Cookie: BIGipServere3-myca-us-s-estat-us=3659928074.20625.0000; amex_cms=Amex%3D1%3B2; aam_id=34286886827372218532052149597940573213; _cc=AZxMDzVNqEeliZH7GgA4VhDk; s_vi=[CS]v1|2DB9036F8507D906-6000011B00006CC8[CE]; mmapi.p.srv=%22lvsvwcgus09%22; axplocale=en-US; mm_pc=%7B%22affluentIndex%22%3A%22%22%7D; gctracus=gctvid=2018-08-13/22:32:05-c31a826a-8a89-5617-6ca8-206f8e9af8f5; aam_rv=AAM%3D1408671%2C2837948%2C3832389%2C388075%2C6903341%2C4937781; fltk=segID%3D2837948; amex_cms=Amex%3D1%3B2; aam_id=34286886827372218532052149597940573213; LPVID=Q2ZGUyYjU0N2VhMjQ3Yzc1; LPSID-14106077=yu86PUeeSbSKaJ8PoMMRYA; SaneID=24.35.118.63-1534199555581528; ddp=D_L_TN; blueboxpublic=01cfd75fc176dd6b7eecbcd10ed365c6; AMCVS_5C36123F5245AF470A490D45%40AdobeOrg=1; __gads=ID=217ea71a1a09b9f4:T=1534199828:S=ALNI_MatK8tiwh9jG-fuONiE-0TUJmyvSg; mmapi.p.ids=%7B%222%22%3A%2201cfd75fc176dd6b7eecbcd10ed365c6%22%7D; BIGipServerme3-w-gl-s-svcgprmtns=4015198218.59301.0000; BIGipServerme3-w-us-s-fincls=3324449290.6572.0000; _dx=1; AMCV_5C36123F5245AF470A490D45%40AdobeOrg=793872103%7CMCIDTS%7C17757%7CMCMID%7C34491054491560848212031750423635894421%7CMCAAMLH-1534806657%7C7%7CMCAAMB-1534806657%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCAID%7C2DB9036F8507D906-6000011B00006CC8%7CMCOPTOUT-1534201797.276%7CNONE%7CvVersion%7C2.1.0; ausCk=1; quantcast=1; targus=1; dateoflastlogon=2018-08-13T23:16:43Z; am_km=PMV67QhXKXGhHbp999uMToyN50oblFN%2FvTD31Dr7diEc4SZi%2BbWRC95qERlumNWPjTSbAmkkiWq2JiMNfmPWtx12hE8A%3D%3D; gatekeeper=4AB84B48BD9CDA9CA76E7B1335A890FCDAC5A4E4AB50A069CE9EC25C5025469297F3913ACB30AE6EC53EC7B40D80041E570C16B4B3203962D3C513C82472E2EF54A5DB540B366CAB2DDF7A06EBA95ED794FE10BF3C44F0ADD5F81190D578B9DA802210B479118C52BCA252A45A32AE89BA0161DEFB68D0A9EB9C7E437524C9447D64E40EEE05D53C2A8DB7AD2891B2708B0B3B5EC6AB380E; blueboxvalues=ce72eff9-b4c0b519-357dcdf1-c67d468e; amexsessioncookie=easc=F36FD582F6281083F614ADA16F362D7FAF05A79471B0FDB7A3109C3969B1F6A4D88F00B43C52CE7D28BFA67476EAA10FBC1022B568FB92D8B8858FEB422D8ECDB9830F0137FB8697F5443C14FEC274E165E06C1177BAA6C5C7B2CA6DCE82B2E3361429A4CF38B1D63185CC224258D8211A70AD7932E674E01085F955F64CEC3FEA6E351EE894BCCF58EE4CCB65ADDDFFA23A041ACB775FFBACC7BB7F7204942EA725E87DFA22E41D9021FA857AD19DB83CCD4B2C6444F05DE7FA7F8BABB6495EE3E98448146B227B8C1E8BC107335789D6070CF8975BE065934D6230AE91F37026|uts=1534202482384|chv=CEF3B9479ED54CACBC2909CCE6B95843262776E4DA12BFC00F0D790DD98EA602|; MATFSI=MSV::true~BBV::ce72eff9-b4c0b519-357dcdf1-c67d468e~FSI::true~; JSESSIONID=0000xFpwg-6OsAESeK1sK4lVbh5:1aokg12rt; mmapi.p.uat=%7B%22GenerationPage%22%3A%22%2Fmyca%2Festmt%2Fus%2Flist.do%22%7D; mmapi.p.pd=%221301141978%7CCQAAAApVAwBOVEE5khDYWSAwMWNmZDc1ZmMxNzZkZDZiN2VlY2JjZDEwZWQzNjVjNgERAAFCjPeuxAEAkUHifHMB1kj8CF6VbAHWSAAAAAD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwAGRGlyZWN0AZIQAQAAAAAAAAAAAP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwAAAAAAAAABRQ%3D%3D%22; am_dlt=-5; BIGipServerme3-w-us-s-offsvc=446606228.47873.0000; fsr.s={"v2":-2,"v1":1,"rid":"d44bc84-86580966-f166-2bac-0a079","ru":"https://www.americanexpress.com/","r":"www.americanexpress.com","st":"","cp":{"BlueBox_Value":"01cfd75fc176dd6b7eecbcd10ed365c6","iNavVersion":"undefined","PageSize":"res_Large","PageWidth":"res_1850","Maxymiser":"Var undefined#Var undefined#N#N","MarketIdentifier":"US","LoggedIn":"Yes","egift_1":"N","egift_2":"N","auth":"N"},"c":"https://online.americanexpress.com/myca/estmt/us/list.do","pv":8,"lc":{"d6":{"v":6,"s":true}},"cd":6,"sd":6,"fo":1}; s_sess=%20omn_omnlogin%3Dus_homepage_myca%3B%20s_sq%3D%3B%20tp%3D5275%3B%20s_cc%3Dtrue%3B%20s_ppv%3DUS%25257CAMEX%25257CSer%25257CeStatement%25257CMainPage%252C17%252C17%252C888%3B%20omn_inav%3Dmyca_statements%3B; s_pers=%20s_vnum%3D1%7C1691879527405%3B%20s_uvid%3D1534199527402309%7C1691879976752%3B%20gpv_v41%3DUS%257CAMEX%257CSer%257CeStatement%257CMainPage%7C1534204415325%3B
Host: online.americanexpress.com
Origin: https://online.americanexpress.com
Referer: https://online.americanexpress.com/myca/estmt/us/list.do?BPIndex=0&request_type=authreg_Statement&inav=myca_statements&Face=en_US&sorted_index=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36

data:

sorted_index: 0
BPIndex: 0
suppIndex: 
liteEnabled: false
mycaLite: false
startDate: 07202018
endDate: 08192018
sortBy: undefined
sortOrder: undefined
sortClicked: false
request_type: authreg_Statement
Face: en_US
refSeNumbers: 
downloadType: C
downloadView: C
numberOfPages: 1
totalTrans: 70
totalTransCount: 70
pageNumber: 1
downloadIndicator: false
downloadWithETDTool: false
viewType: L
reportType: 1
"""