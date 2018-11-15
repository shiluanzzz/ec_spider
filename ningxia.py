import json
import os
import random
import re
import requests
import traceback

from bs4 import BeautifulSoup


def find_cn(string):
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(string)
    # print(match.group(0))
    if match:
        return match.group(0)
    else:
        return string

def get_page(url):
    with open('ip.json','r')as f:
        ip_data=json.load(f)
    USER_AGENTS = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]
    headers={'User-Agent':random.choice(USER_AGENTS)}
    down_count=0 # 设置重试次数
    while down_count<10:
        try:
            proxy_ip = random.choice(ip_data)
            r = requests.get(url=url, headers=headers, proxies=proxy_ip)

            return r.content
        except:
            pass
    return False

def down_file(url,path):
    with open('ip.json','r')as f:
        ip_data=json.load(f)
    USER_AGENTS = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]
    headers={'User-Agent':random.choice(USER_AGENTS)}
    down_count=0 # 设置重试次数
    while down_count<5:
        flag=False
        try:
            proxy_ip = random.choice(ip_data)
            r=requests.get(url=url,headers=headers,proxies=proxy_ip)
            with open(r'{}'.format(path), 'wb') as file:
                file.write(r.content)
            flag=True
        except:
            down_count+=1
            if down_count==5:
                print("下载失败！")
                traceback.print_exc()
        if flag:
            break

    # with open(r'{}{}{}'.format(path + "/", filename, href[-4:]), 'wb')as f:
    #     f.write(source.content)
    # print('正在抓取宁夏：' + href)

def ningxia_2013(year,path):
    pass
def ningxia_2014(year,path):
    pass
def ningxia_2015(year,path):
    pass

def ningxia_2016(path):
    year = '2016'
    try:
        os.mkdir(path + '/' + str(year))
    except:
        pass
    path = path + '/' + str(year)
    url_2016 = 'http://www.nxtj.gov.cn/tjsj/ndsj/2016/indexfiles/left.htm'
    re_text = get_page(url_2016)
    soup=BeautifulSoup(re_text,'lxml')
    ul=soup.find('th',align='left').find('ul')
    ul_list=ul.find_all('ul',id="foldinglist")
    for each in ul_list:
            # print(each.find_previous_sibling('li',id="foldheader").text,"\n=====",each.text[:20],"\n********************************")
        try:
            mulu=each.find_previous_sibling('li',id="foldheader").text.replace("\n",'')
        except:
            break
        try:
            os.mkdir(path+'/'+mulu)
        except:
            pass
        temp_path=path+'/'+mulu
        for a in each.find_all('a'):
            file_name=a.text[:6]+find_cn(a.text[6:])
            link = "http://www.nxtj.gov.cn/tjsj/ndsj/2016/" + a['href'][2:]
            down_file(url=link,path=path+'/'+mulu+'/'+file_name+link[-4:])
            print("正在下载 宁夏 2016 年",file_name)
def ningxia_2017(path):
    year = '2017'
    try:
        os.mkdir(path+'/'+str(year))
    except:
        pass
    path=path+'/'+str(year)
    url_2017='http://www.nxtj.gov.cn/tjsj/ndsj/2017/indexfiles/left.htm'
    re_text=get_page(url_2017)
    if re_text:
        soup=BeautifulSoup(re_text,'lxml')
        target_content=soup.find('th','style18')
        p_list=target_content.find_all('p')
        temp_path=path
        for each in p_list:
            # 标题
            if "统计图" in each.text or "统计公报" in each.text or ("第" in each.text and "篇" in each.text):
                print("=========={}======".format(each.text.replace("\n","")))
                try:
                    os.mkdir(path+'/'+each.text.replace("\n","").replace(" ","").replace("\r",""))
                except:
                    pass
                temp_path=path+'/'+each.text.replace("\n","").replace(" ","").replace("\r","")
            else:
                try:
                    print("正在下载",each.find('a').text)
                    file_name=str(each.find('a').text).replace(" ","").replace('\\',"").replace('/','').replace(':','').replace('*','')
                    file_name=find_cn(file_name).replace("表","")
                    herf="http://www.nxtj.gov.cn/tjsj/ndsj/2017/"+each.find('a')['href'][2:]
                    # print(herf)
                    down_file(url=herf,path=temp_path+'/'+file_name+herf[-4:])
                except:
                    pass
                    # traceback.print_exc()
                    #print("************{}*****".format(each.text))
    else:
        print("网络请求错误！")

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
                    with open(r'{}{}{}'.format(path+"/",filename,href[-4:]),'wb')as f:
                        f.write(source.content)
                    print('正在抓取宁夏：' + href)
                except:
                    traceback.print_exc()
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
                    with open(r'{}{}{}'.format(path+ "/", filename, href[-4:]), 'wb')as f:
                        f.write(source.content)
                    print('正在抓取宁夏：' + href)
                except:
                    traceback.print_exc()
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
    get_pic_by_request(year=year,path=path)

if __name__ == '__main__':

    # 2017
    # http: // www.nxtj.gov.cn / tjsj / ndsj / 2017 / indexfiles / left.htm
    # 2016
    # http: // www.nxtj.gov.cn / tjsj / ndsj / 2016 / indexfiles / left.htm
    # get_ningxia(2015,"F:/ec")
    # ningxia_2017("F:/ec/宁夏")
    # down_file(11,1)
    # tt="5-17表第六次全国人口普查就业人口产业构成Employment\n\tCompositionbyIndustryonPopulationCensusin2010.htm"
    # find_cn(tt)
    ningxia_2016(path="F:/ec/宁夏")