#coding=utf-8
import sys,logging
import configparser,traceback
import guangxi,guojia,neimenggu,ningxia
def get_guojia():
    config=configparser.ConfigParser()
    config.read('ec.ini')
    path=config.get('datafile','path')
    a=config.get('待抓取','国家统计局')
    b=config.get('已抓取','国家统计局')
    if a :
        if b:
            print('国家统计局已经抓取！')
        else:
            try:
                guojia.get_guojia(path)
                config['待抓取']['国家统计局']=''
                config['已抓取']['国家统计局']='1'
                with open('ec.ini','w')as f:
                    config.write(f)
            except:
                traceback.print_exc(file=open('{}guojia_error.txt'.format(path+'/'), 'w+'))
                logging.error('国家统计局抓取错误，请查看日志。')
def get_neimenggu():
    config = configparser.ConfigParser()
    config.read('ec.ini')
    path = config.get('datafile', 'path')
    a = config.get('待抓取', '内蒙古')
    b =config.get('已抓取','内蒙古')
    b_list=str(b).split(',')
    if a:
        a_list=str(a).split(',')
        for each in a_list:
            try:
                neimenggu.get_neimenggu(each,path)
                b_list.append(each)
            except:
                traceback.print_exc(file=open('{}内蒙古_error.txt'.format(path + '/'), 'w+'))
                logging.error('内蒙古抓取错误，请查看日志。')
    tt=""
    for each in b_list:
        tt=tt+each+','
    tt=tt[:-1]
    config['已抓取']['内蒙古']=tt
    with open('ec.ini', 'w')as f:
        config.write(f)
if __name__ == '__main__':
    get_guojia()
    get_neimenggu()