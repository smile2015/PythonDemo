# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     RequestsSpiderDemo01
   Description :
   Author :       Administrator
   date：          2019/6/18 0018
-------------------------------------------------
   Change Activity:
                   2019/6/18 0018:
-------------------------------------------------
"""
__author__ = 'Administrator'

import sys
import types
import os

import requests

reload(sys)
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

'''

'''

#打印列表信息
def showList(listdata):
    list_temp=[]
    for item in listdata:
        print item[0],item[1]
        list_temp.append(item[1])
    return list_temp

'''
网页请求操作

'''
#请求并返回相应
def getHtmlByRequests(html_url):
    # 请求html
    r = requests.get(html_url)
    # # 响应头
    # print r.headers
    # print r.headers.get('content-type')  # 访问响应头部分内容的两种方式
    # print r.headers['Content-Type']

    # 获取/修改网页编码
    source_encoding = r.encoding
    # print source_encoding

    # 响应状态码
    r_status_code = r.status_code
    # print r_status_code

    if r_status_code == 200:
        # 获取响应内容
        html_data = r.content  # 以字节的方式去显示，中文显示为字符
        # print html_data
        return html_data, source_encoding
    else:
        return ''

'''
列表处理

'''
#获取列表
def getList(reg_str,html_data):
    import re
    result=re.findall(reg_str,html_data)
    print result
    return result


# #取单类小说列表、正则表达式、保存路径
def getBookList(url_str,reg_str,save_path):
    # url_str = 'http://www.quanshuwan.com/category/2_1_1.aspx'
    # reg_str = r'<a target="_blank" href="/book/(.*?).aspx" class="bookname">(.*?)</a>'
    # readlist_result_path = 'D:\\code\\PythonWebSpider\\booklist.html'

    response = getHtmlByRequests(url_str)

    bookList_result=getList(reg_str,response[0])

    #showList(bookList_result)

    writeNovel(save_path, bookList_result)

    return bookList_result

#
def getNovalCatalogList(url_str,reg_str,save_path):
    #url_str = 'http://www.quanshuwan.com/book/4812.aspx#readlist'
    #reg_str = r'<a href="/article/(.*?).aspx">(.*?)</a>'
    #save_path = 'D:\\code\\PythonWebSpider\\novalCatalogList.html'

    response = getHtmlByRequests(url_str)

    novalCatalogList_Result = getList(reg_str, response[0])

    #showList(novalCatalogList_Result)


    # for item in novalCatalogList_Result:
    #     writeNovel(save_path,item[0])

    writeNovel(save_path, novalCatalogList_Result)
    return novalCatalogList_Result

'''
小说详情处理

'''

#请求小说详情
def getNovalDetail(url_str,process_path):
    novalDetail_result = getHtmlByRequests(url_str)
    if novalDetail_result!='':
        writeNovel(process_path,url_str)
        print url_str


    return novalDetail_result


'''
文件操作

'''

#根据内容生成html
def writeNovel(save_path, html_data, encoding_str=None):

    path=os.path.split(save_path)[0]
    #创建目录
    createFolder(path)


    html_string = str(html_data)
    if type(encoding_str) is not types.NoneType:
        html_string = html_string.decode(encoding_str).encode('utf-8')

    # # python写文件方式一
    # file = open(save_path, 'wb')
    # file.write(html_string)
    # file.close()

    # python写文件方式二
    with open(save_path, 'wb') as file:
        file.write(html_string)
        file.close()

#创建目录
def createFolder(path):
    import os
    if os.path.isdir(path)==False:
        return os.makedirs(path)
    else:
        return path


if __name__ == '__main__':

    base_path='D:\\code\\PythonWebSpider\\data\\www.quanshuwu.com'
    # # ================================================================
    url_str = 'http://www.quanshuwan.com/category/2_1_1.aspx'
    reg_str = r'<a target="_blank" href="/book/(.*?).aspx" class="bookname">(.*?)</a>'
    import os
    save_path=os.path.join(base_path, 'booklist_2_1_1.html')
    book_list=getBookList(url_str,reg_str,save_path)



    #===========================
    # 取单本小说具体目录列表、正则表达式、保存路径
    url_str = 'http://www.quanshuwan.com/book/4812.aspx#readlist'
    reg_str = r'<a href="/article/(.*?).aspx">(.*?)</a>'
    #save_path = os.path.join(base_path, 'novalCatalogList.html')
    save_path=base_path+'\\4812\\novalCatalogList.html'
    print '++++++++++++++++++++++=======================+++++++++++++++++'
    print save_path
    noval_catalog_list=getNovalCatalogList(url_str,reg_str,save_path)

    #============
    process_path=base_path+'\\4812\\process_path.txt'
    print '=====start get noval content \n'
    for item in noval_catalog_list:
        #文章url
        url_str = 'http://www.quanshuwan.com/article/'+item[0]+'.aspx'
        save_path = base_path + '\\4812\\'+item[0]+'.html'
        # 请求小说详情，并根据相应内容生成HTML
        novalDetail_result = getNovalDetail(url_str,process_path)
        # 写入html
        writeNovel(save_path, novalDetail_result[0], novalDetail_result[1])
        import time
        time.sleep(5)
    print '\n=====end get noval content \n'