from __future__ import print_function
from bs4 import BeautifulSoup
import requests,re,getpass,io,pandas
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def retrieve_amex():

    url='https://www.americanexpress.com/'
    s=requests.session()
    login=s.get('https://www.americanexpress.com/')
    login_soup=BeautifulSoup(login.content,features="html.parser")

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

    login_response_soup = BeautifulSoup(login_response.content,features="html.parser")

    statements_url=login_response_soup.find_all('a',string=re.compile('Statements &.*'))[0]['href']

    statements_response=s.get(statements_url)

    statements_soup=BeautifulSoup(statements_response.content,features="html.parser")


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

    return df


def update_spreadsheet(df):

    # If modifying these scopes, delete the file token.json.
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1soSZzOu2C0aC928C2FZwIqc5IwDHmSh33kPnN2SDT2w'
    

    amex_total=df[df[7]>0][7].sum()

    transaction_count = df[0].count()


    RANGE_NAME = 'Sheet2!A1:C' + str(transaction_count)

    value_range_body = { 'range': RANGE_NAME,
    'values':df[[0,2,7]].values.tolist()}

    request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME,body=value_range_body,valueInputOption='RAW')
    response = request.execute()

    print(response)

    RANGE_NAME = 'Sheet1!D34'

    value_range_body = { 'range':RANGE_NAME,
    'values':[[amex_total]]}

    request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME,body=value_range_body,valueInputOption='RAW')
    response = request.execute()

    print(response)

    # for index,row in df.iterrows():
    #     print(row[0],row[2],row[7])


if __name__ == '__main__':

    df = retrieve_amex()
    update_spreadsheet(df)


