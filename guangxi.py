#from selenium import webdriver
import time,os,requests,urllib
from bs4 import BeautifulSoup

def get_pic_by_request(year,path):
    try:
        os.mkdir(path + '/' + '广西')
    except:
        pass
    path = path + '/' + '广西'
    try:
        os.mkdir(path+'/'+'{}'.format(year))

    except:
        pass
    path = path = '/' + '{}'.format(year)
    url='http://www.gxtj.gov.cn/tjsj/tjnj/2015/zk/left.htm'
    re=requests.get("http://www.gxtj.gov.cn/tjsj/tjnj/{}/zk/left.htm".format(year))
    #file=open('test.txt','w',encoding='utf-8')
    #file.write(re.content)
    #file.close()
    soup=BeautifulSoup(re.content,"lxml")
    tag_list=soup.find_all('li',id='foldheader')
    ul_list=soup.find_all('ul',id='foldinglist')
    if(len(tag_list)==len(ul_list)):
        for num in range(len(tag_list)):
            try:
                os.mkdir(path+'/'+tag_list[num].text)
            except:
                pass
            dir=path+'/'+tag_list[num].text
            print('===={}===='.format(tag_list[num].text))
            for each in ul_list[num].find_all('li'):
                herf="http://www.gxtj.gov.cn/tjsj/tjnj/{}/zk/".format(year)+each.find('a')['href']
                filename=each.find('a').text
                try:
                    source=requests.get(herf)
                    with open(r'{}{}{}'.format(dir+'/',filename,herf[-4:]),'wb')as f:
                        f.write(source.content)
                    print('正在下载 {} : {}'.format(filename,herf))

                except:
                    print('下载错误！ {} : {}'.format(filename, herf))



if __name__ == '__main__':
    #get_pic('2017')
    #get_driver()
    path=os.getcwd()
    os.mkdir('{}'.format(2015))
    get_pic_by_request(year=2015,path=path+'/'+"{}".format(2015))