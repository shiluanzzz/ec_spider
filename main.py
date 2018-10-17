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
    error_path=config.get('datafile','error_path')
    a=config.get('Todo','guojiatongjiju')
    b=config.get('worked','guojiatongjiju')
    if a :
        if b:
            print('国家统计局 已经抓取！')
            config['Todo']['guojiatongjiju'] = ''
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
                logging.error('国家统计局 抓取错误，请查看日志。')
def get_neimenggu():
    config = configparser.ConfigParser()
    config.read('ec.ini')
    path = config.get('datafile', 'path')


    a = config.get('Todo', 'neimenggu')
    b =config.get('worked','neimenggu')
    b_list=str(b).split(',')
    a_list=str(a).split(',')
    if a:
        for each in a_list:
            if each not in b_list:
                try:
                    neimenggu.get_neimenggu(each,path)
                    b_list.append(each)
                    a_list.remove(each)
                except:
                    fileee = path + '/' + '内蒙古_error.txt'
                    traceback.print_exc(file=open(fileee, 'w+'))
                    #traceback.print_exc(file=open('{}内蒙古_error.txt'.format(path + '/'), 'w+'))
                    logging.error('内蒙古 抓取错误，请查看日志。')
            else:
                a_list.remove(each)
    tt=""
    for each in b_list:
        if each!='':
            tt=tt+each+','
    tt=tt[:-1]
    tt2 = ""
    for each in a_list:
        if each != '':
            tt2 = tt2 + each + ','
    tt2 = tt2[:-1]
    config['worked']['neimenggu']=tt
    config['Todo']['neimenggu']=tt2
    with open('ec.ini', 'w')as f:
        config.write(f)
def get_guangxi():
    config = configparser.ConfigParser()
    config.read('ec.ini')
    path = config.get('datafile', 'path')

    a = config.get('Todo', 'guangxi')
    b = config.get('worked', 'guangxi')
    b_list = str(b).split(',')
    a_list = str(a).split(',')
    if a:
        for each in a_list:
            if each not in b_list:
                try:
                    guangxi.get_pic_by_request(each, path)
                    # neimenggu.get_neimenggu(each, path)
                    b_list.append(each)
                    a_list.remove(each)
                except:
                    fileee = path + '/' + '广西_error.txt'
                    traceback.print_exc(file=open(fileee, 'w+'))
                    # traceback.print_exc(file=open('{}内蒙古_error.txt'.format(path + '/'), 'w+'))
                    logging.error('广西 抓取错误，请查看日志。')
            else:
                a_list.remove(each)
    tt = ""
    for each in b_list:
        if each != '':
            tt = tt + each + ','
    tt = tt[:-1]
    tt2 = ""
    for each in a_list:
        if each != '':
            tt2 = tt2 + each + ','
    tt2 = tt2[:-1]
    config['worked']['guangxi'] = tt
    config['Todo']['guangxi'] = tt2
    with open('ec.ini', 'w')as f:
        config.write(f)





def get_ningxia():
    config = configparser.ConfigParser()
    config.read('ec.ini')
    path = config.get('datafile', 'path')

    a = config.get('Todo', 'ningxia')
    b = config.get('worked', 'ningxia')
    b_list = str(b).split(',')
    a_list = str(a).split(',')
    if a:
        for each in a_list:
            if each not in b_list:
                try:
                    guangxi.get_pic_by_request(each, path)
                    # neimenggu.get_neimenggu(each, path)
                    b_list.append(each)
                    a_list.remove(each)
                except:
                    fileee = path + '/' + '宁夏_error.txt'
                    traceback.print_exc(file=open(fileee, 'w+'))
                    # traceback.print_exc(file=open('{}内蒙古_error.txt'.format(path + '/'), 'w+'))
                    logging.error('宁夏 抓取错误，请查看日志。')
            else:
                a_list.remove(each)
    tt = ""
    for each in b_list:
        if each != '':
            tt = tt + each + ','
    tt = tt[:-1]
    tt2 = ""
    for each in a_list:
        if each != '':
            tt2 = tt2 + each + ','
    tt2 = tt2[:-1]
    config['worked']['ningxia'] = tt
    config['Todo']['ningxia'] = tt2
    with open('ec.ini', 'w')as f:
        config.write(f)


def get_area_data(name):
    config = configparser.ConfigParser()
    config.read('ec.ini')
    path = config.get('datafile', 'path')

    a = config.get('Todo', '{}'.format(name))
    b = config.get('worked', '{}'.format(name))
    b_list = str(b).split(',')
    a_list = str(a).split(',')
    if a:
        for each in a_list:
            if each not in b_list:
                try:
                    if name=='guangxi':
                        guangxi.get_pic_by_request(each, path)
                    elif name=='ningxia':
                        ningxia.get_ningxia(each,path)
                    elif name=='neimenggu':
                        neimenggu.get_neimenggu(each, path)
                    b_list.append(each)
                    a_list.remove(each)
                except:
                    fileee = path + '/' + '{}_error.txt'.format(name)
                    traceback.print_exc(file=open(fileee, 'w+'))
                    # traceback.print_exc(file=open('{}内蒙古_error.txt'.format(path + '/'), 'w+'))
            else:
                a_list.remove(each)
    tt = ""
    for each in b_list:
        if each != '':
            tt = tt + each + ','
    tt = tt[:-1]
    tt2 = ""
    for each in a_list:
        if each != '':
            tt2 = tt2 + each + ','
    tt2 = tt2[:-1]
    config['worked']['{}'.format(name)] = tt
    config['Todo']['{}'.format(name)] = tt2
    with open('ec.ini', 'w')as f:
        config.write(f)
if __name__ == '__main__':
    get_area_data('ningxia')
    # get_area_data('guangxi')
    # get_area_data('neimenggu')
    # get_guojia()