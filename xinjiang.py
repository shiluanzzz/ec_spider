import traceback

import requests,os

from bs4 import BeautifulSoup
def get_xinjiang(year,path):
    try:
        os.mkdir(path+'/新疆')
    except:
        pass
    path=path+'/新疆'
    try:
        os.mkdir(path+'/'+year)
    except:
        pass
    path+='/'+year

    if str(year)=='2016':
        url="http://www.xjtj.gov.cn/sjcx/tjnj_3415/"
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'lxml')
        tar=soup.find('div','xzdwLeftsidebar').find_all('li')
        for each in tar:
            data_url=each.find('a')['totarget']
            tt=requests.get(data_url)
            soup2=BeautifulSoup(tt.content,'lxml')
            for a in soup2.find_all('li'):
                target=a.find('a')
                herf=target['href'][27:-3]
                filename=target['title']
                try:
                    source=requests.get(herf)
                    with open(r'{}{}{}'.format(path+'/',filename,".html"),'wb')as f:
                        f.write(source.content)
                    print('正在下载新疆地区数据 {} '.format(filename))
                except:
                    traceback.print_exc()
                    print('下载错误！ {} : {}'.format(filename, herf))
if __name__ == '__main__':
    get_xinjiang('2016','F:/ec')
