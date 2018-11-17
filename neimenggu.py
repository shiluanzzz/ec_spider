import urllib3
import json
import traceback
import os


'''
原始URL
http://www.nmgtj.gov.cn/acmrdatashownmgpub/tablequery.htm?
m=QueryData&code=OA0C&wds=[{"wdcode":"reg","valuecode":"150000"},{"wdcode":"sj","valuecode":"201804"}]&fvrt_code=
'''

#通过控制，data_name,code,time 三个参数获取内蒙古地区的数据
def get_data(data_name,code,date_list,path):

    ori_path = path+'/'+'原始数据'
    data_path = path+'/'+'解析数据'
    try:
        os.mkdir(path+'/'+'原始数据')
    except:
        pass
    try:
        os.mkdir(path + '/' + '解析数据')
    except:
        pass

    #----------------原始参数--------------------
    url='http://www.nmgtj.gov.cn/acmrdatashownmgpub/tablequery.htm'
    #data_name = '工业经济效率'
    #code = 'OA0104'
    wdcode1='reg'
    valuecode1='150000'
    wdcode2='sj'
    valuecode2='201804' #日期？
    #-----------------------------------

    data_list=[]# 储存数据流
    try:
        os.mkdir(ori_path+'/'+data_name)
    except:
    #目录存在
        pass

    for valuecode2 in date_list:
        #参数

        wds2=[{"wdcode":"{}".format(wdcode1),"valuecode":"{}".format(valuecode1)},{"wdcode":"{}".format(wdcode2),'valuecode':'{}'.format(valuecode2)}]
        url_parmas={"m":"QueryData","code":"{}".format(code),"wds":"{}".format(str(wds2).replace('\'','\"')),"fvrt_code":""}
        try:
            #http请求
            http=urllib3.PoolManager()
            r=http.request("GET",url,fields=url_parmas)
            #数据加载
            hs=json.loads(r.data)
            file_name=ori_path+'/'+data_name+'/'+str(valuecode2)+".json"
            #原始数据保存
            with open(file_name,"w") as f :
                    json.dump(hs,f,ensure_ascii=False)
                    #print(data_name,' : ',valuecode2,"原始json数据保存成功")
                    print('正在下载： 内蒙古 {}  {} 原始数据'.format(valuecode2,data_name))
            #数据解析
            b=hs['exceltable']
            ll=[] #用来记录属性值。
            data=[]
            temp={}
            for a in b : # a即为单个字典
                if(a['sort']=='row'):
                    temp={}
                if(a['sort']=='col'):
                    ll.append(a['data'])
                elif(a['sort']=='row' or a['sort']=='cell'):
                    temp["{}".format(ll[a['col']])]=a['data']
                    if(a['col']==len(ll)-1):
                        temp['time']=str(valuecode2)
                        data.append(temp)
                else:
                    print('error : ',a['sort'],a['col'])
                    print('----------------')
            data_list.append(data)
        except:
            print("内蒙古地区，原始数据 {} 出错！".format(data_name))
            #traceback.print_exc(file=open("Exc.txt","a"))
            continue
    #解析后总数据保存
    file_nn="{}.json".format(data_path+'/'+date_list[0][:4]+data_name)
    print(file_nn)
    with open(file=file_nn,mode='w') as f:
        json.dump(data_list, f,ensure_ascii=False)
        print('内蒙古 {}  {} 数据 解析成功！'.format(valuecode2, data_name))

def get_neimenggu(year,path):
    try:
        a=int(year)
    except:
        print("内蒙古地区 目标年鉴 {} 时间格式错误！".format(year))
        return 0

    if int(year)<=2016 and int(year)>=2000:
        try:
            os.mkdir(path+'/'+'内蒙古')
        except:
            pass
        path=path+'/'+'内蒙古'

        try:
            os.mkdir(path + '/' + '{}'.format(year))
        except:
            pass
        path = path + '/' + '{}'.format(year)


        list = [{'工业增加值增长速度': 'OA0101'},
                {'工业产品销售率': 'OA0102'},
                {'主要工业产品产量': 'OA0103'},
                {'工业经济效率': 'OA0104'},
                {'固定投资资产': 'OA0505'},
                {'主要行业固定投资资产': 'OA0506'},
                {'房地产开发': 'OA0507'},
                {'社会消费品零售总额': 'OA08'},
                {'对外经济': 'OA09'},
                {'财政': 'OA0A'},
                {'金融': 'OA0C'},
                {'全区及全国主要经济指标': 'OA1F'}
                ]
        t_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        time_list=[]
        for num in t_list:
            time_list.append("{}{}".format(str(year),num))
        for a in list:
            # 读取list里的字典的第一个键值对
            for key, value in a.items():
                #print("data_name: {},code : {}".format(key, value))
                get_data(key, value, time_list,path=path)
                break
    else:
        print("内蒙古地区目标年限 {} 超出可抓取范围！".format(year))

if __name__ == '__main__':
    get_neimenggu('2001',"F:/ec")
