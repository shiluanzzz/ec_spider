import time,os,requests,urllib
from bs4 import BeautifulSoup

def get_pic_by_request(year,path):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }

    #re=requests.get("http://www.nxtj.gov.cn/tjsj/ndsj/{}/indexfiles/left.htm".format(year))
    if int(year)>2015:
        re=requests.get("http://www.nxtj.gov.cn/tjsj/ndsj/{}/indexfiles/left.htm".format(year),headers=header)
        soup = BeautifulSoup(re.content, "lxml")
        #print(re.content)
        li_list = soup.find_all('ul', id='foldinglist')
        for each in li_list:
            dir_name=each.text[:4].replace('\n','').replace('-','')
            try:
                os.mkdir(path+'/'+dir_name)
            except:
                pass
            path=path+'/'+dir_name
            for a in each.find_all('a'):
                filename=a.text
                href = "http://www.nxtj.gov.cn/tjsj/ndsj/{}/indexfiles/".format(year)+a['href']

                try:
                    source=requests.get(href)
                    with open(r'{}{}{}'.format(path+'/'+dir_name+"/",filename,href[-4:]),'wb')as f:
                        f.write(source.content)
                    print('正在抓取宁夏：' + href)
                except:
                    print('宁夏，错误：' + href)
                    pass

    else:
        #re=requests.get("http://www.nxtj.gov.cn/tjsj/ndsj/{}/indexch.htm".format(year))
        re = requests.get("http://www.nxtj.gov.cn/tjsj/ndsj/{}/lefte.htm".format(year), headers=header)
        soup = BeautifulSoup(re.content, "lxml")
        # print(re.content)
        li_list = soup.find_all('ul', id='foldinglist')
        for each in li_list:
            dir_name = each.text[:4].replace('\n', '').replace('-', '')
            try:
                os.mkdir(path + '/' + dir_name)
            except:
                pass
            path = path + '/' + dir_name
            for a in each.find_all('a'):
                filename = a.text
                href = "http://www.nxtj.gov.cn/tjsj/ndsj/{}/indexfiles/".format(year) + a['href']
                try:
                    source = requests.get(href)
                    with open(r'{}{}{}'.format(path + '/' + dir_name + "/", filename, href[-4:]), 'wb')as f:
                        f.write(source.content)
                    print('正在抓取宁夏：' + href)
                except:
                    print('宁夏，错误：' +href)
                    pass


def get_ningxia(year,path):
    try:
        os.mkdir(path+'/{}'.format('宁夏'))
    except:
        pass
    path = path + '/' + '宁夏'
    year=str(year)
    try:
        os.mkdir(path+'/{}'.format(year))
    except:
        pass
    path = path + '/' + year
    get_pic_by_request(year=year,path=path+'/'+"{}".format(year))

if __name__ == '__main__':
    get_ningxia(2016,os.getcwd())
