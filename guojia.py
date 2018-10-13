import requests
import time
import json,os
#import glom



url="http://data.stats.gov.cn/easyquery.htm"
# 检测当前序号是否有数据，没有数据则可能有二级序号
def try_get_data(city_code,valuecode):
    # 返回True 表示这个是最底层的等级了
    k11 = int(round(time.time() * 1000))

    # 请求参数部分
    wdss = str([{"wdcode": "reg", "valuecode": "{}".format(city_code)}]).replace('\'', '\"').replace('+', '')
    dfwdss=str([{"wdcode":"zb","valuecode":"{}".format(valuecode)}]).replace('\'', '\"').replace('+', '')
    params = {'colcode': 'sj',
              'dbcode': 'fsnd',
              'dfwds': dfwdss,
              'k1': k11,
              'm': 'QueryData',
              'rowcode': '{}'.format('zb'),
              'wds': wdss
              }

    # 获取请求 未配置代理池 不需要
    r = requests.get(url=url, params=params)
    # 数据解码解析成json
    data = json.loads(r.content.decode())

    if(data['returncode'] == 200):
        return True
    else:
        return False
        # print(data)
def get_data(city_name,city_code,path):
    try:
        os.mkdir(path+'/'+'国家统计局数据')
    except:
        pass
    ll=[]
    # 记录爬取了多少数据
    all_count=0

    '''
    单个省份的字典储存格式
    {'city_name':''
     'code_mean':[{code:''},{},{},{}]
     'data':[{code:'',
              time:'',
              data:''}
              {},{},{},{}...]
    }
    '''

    Area_data={}
    Area_data.setdefault('code_mean',[])
    Area_data.setdefault('data',[])
    with open("par_list.json","r",encoding="utf-8") as file:
        value_data=json.load(file)
    for each in value_data:
        print("开始爬取国家统计局 {} {} 数据".format(city_name,each['name']))
        valuecode=each['id']
        #时间戳
        k11 = int(round(time.time() * 1000))

        #请求参数部分
        wdss = str([{"wdcode": "reg", "valuecode": "{}".format(city_code)}]).replace('\'', '\"').replace('+', '')
        dfwdss = str([{"wdcode": "zb", "valuecode": "{}".format(valuecode)}]).replace('\'', '\"').replace('+', '')
        params = {'colcode': 'sj',
                  'dbcode': 'fsnd',
                  'dfwds': dfwdss,
                  'k1': k11,
                  'm': 'QueryData',
                  'rowcode': 'zb',
                  'wds': wdss
                  }

        #获取请求 未配置代理池 不需要
        r=requests.get(url=url,params=params)
        #数据解码解析成json
        data=json.loads(r.content.decode())
        # print(data)

        #数据解析
        Area_data['city_name']=data["returndata"]["wdnodes"][1]['nodes'][0]['cname']
        Indicators=data["returndata"]["wdnodes"][0]['nodes']

        for each in Indicators:
            temp={}
            code=each['code']
            mean=each['cname']
            temp[code]=mean
            Area_data['code_mean'].append(temp)

        origin_data=data['returndata']['datanodes']
        for each in origin_data:
            temp={}
            temp['data']=each['data']['data']
            temp['code'] =each['wds'][0]['valuecode']
            temp['time'] =each['wds'][2]['valuecode']
            all_count+=1
            Area_data['data'].append(temp)

    print('国家统计局 {} 爬取完毕 总数据：'.format(Area_data['city_name']),all_count,'条')
    ll.append(Area_data)
    with open("{}.json".format(path+'/'+'国家统计局数据/'+Area_data['city_name']), "w", encoding='utf-8') as file2:
        json.dump(ll, file2,ensure_ascii=False)
    #print("{}.json".format(Area_data['city_name']),"文件保存成功！")

    return Area_data


def get_guojia(path):

    city_id={
        '北京市' : '110000' ,
        '天津市' : '120000' ,
        '河北省' : '130000' ,
        '山西省' : '140000' ,
        '内蒙古自治区' : '150000' ,
        '辽宁省' : '210000' ,
        '吉林省' : '220000' ,
        '黑龙江省' : '230000' ,
        '上海市' : '310000' ,
        '江苏省' : '320000' ,
        '浙江省' : '330000' ,
        '安徽省' : '340000' ,
        '福建省' : '350000' ,
        '江西省' : '360000' ,
        '山东省' : '370000' ,
        '河南省' : '410000' ,
        '湖北省' : '420000' ,
        '湖南省' : '430000' ,
        '广东省' : '440000' ,
        '广西壮族自治区' : '450000' ,
        '海南省' : '460000' ,
        '重庆市' : '500000' ,
        '四川省' : '510000' ,
        '贵州省' : '520000' ,
        '云南省' : '530000' ,
        '西藏自治区' : '540000' ,
        '陕西省' : '610000' ,
        '甘肃省' : '620000' ,
        '青海省' : '630000' ,
        '宁夏回族自治区' : '640000' ,
        "新疆维吾尔自治区":"650000"
    }
    for city_name,id in city_id.items():
        get_data(city_name,id,path)
if __name__=="__main__":
    get_guojia()

