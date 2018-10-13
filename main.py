#coding=utf-8
import os
import sys,logging
import configparser,traceback
import guangxi,guojia,neimenggu,ningxia
import test
def get_guojia():
    config=configparser.ConfigParser()
    config.read('ec.ini')
    path=config.get('datafile','path')
    a=config.get('Todo','guojiatongjiju')
    b=config.get('worked','guojiatongjiju')
    if a :
        if b:
            print('guojiatongjiju 已经抓取！')
        else:
            try:
                guojia.get_guojia(path)
                config['Todo']['guojiatongjiju']=''
                config['worked']['guojiatongjiju']='1'
                with open('ec.ini','w')as f:
                    config.write(f)
            except:
                fileee=path+'/'+'guojia_error.txt'
                traceback.print_exc(file=open(fileee, 'w+'))
                logging.error('guojiatongjiju 抓取错误，请查看日志。')
def get_neimenggu():
    config = configparser.ConfigParser()
    config.read('ec.ini')
    path = config.get('datafile', 'path')
    #print(path)
    #path=os.getcwd()
    #print(path)
    a = config.get('Todo', 'neimenggu')
    b =config.get('worked','neimenggu')
    b_list=str(b).split(',')
    if a:
        a_list=str(a).split(',')
        for each in a_list:
            try:
                neimenggu.get_neimenggu(each,path)
                b_list.append(each)
            except:
                fileee = path + '/' + '内蒙古_error.txt'
                traceback.print_exc(file=open(fileee, 'w+'))
                #traceback.print_exc(file=open('{}内蒙古_error.txt'.format(path + '/'), 'w+'))
                logging.error('内蒙古抓取错误，请查看日志。')
    tt=""
    for each in b_list:
        tt=tt+each+','
    tt=tt[:-1]
    config['worked']['neimenggu']=tt
    with open('ec.ini', 'w')as f:
        config.write(f)


if __name__ == '__main__':
    get_guojia()
    #test1()
    get_neimenggu()