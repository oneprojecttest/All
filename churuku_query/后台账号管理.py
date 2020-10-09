import pymysql
from datetime import datetime
import time
import sys
from sql import *

if __name__ == '__main__':
    print('========================')
    print('||欢迎来到后台账号管理||')
    print('========================')
    while(1):
        print('========================')
        print('输入0：添加账号')
        print('输入1：删除账号')
        print('输入2：修改账号密码')
        print('输入3：查看登录记录')
        print('输入4：查看账号密码')
        print('输入5：退出')
        choose = input('请输入：')
        if choose == '0':
            zhanghao = input('新账号：(输入b返回上一级)')
            if zhanghao == 'b':
                continue
            mima = input('新密码：(输入b返回上一级)')
            if zhanghao == 'b':
                continue
            yonghu_mima_add(zhanghao,mima)
            print('添加成功！')
            continue
        elif choose == '1':
            zhanghao = input('要删除的账号：(输入b返回上一级)')
            if zhanghao == 'b':
                continue
            yonghu_mima_delete(zhanghao)
            print('删除成功！')
            continue
        elif choose == '2':
            zhanghao = input('要修改的账号：(输入b返回上一级)')
            if zhanghao == 'b':
                continue
            mima = input('新密码：(输入b返回上一级)')
            if mima == 'b':
                continue
            yonghu_mima_modify(zhanghao,mima)
            print('修改成功！')
            continue
        elif choose == '3':
            data = denglu_record_query()
            print('时间                  登录账号  登录状态')
            for item in data:
                time = item[0].strftime("%Y-%m-%d %H:%M:%S")
                zhanghao = item[1]
                zhuangtai = item[2]
                print(time+'   '+zhanghao+'     '+zhuangtai)
        elif choose == '4':
            data = denglu_query()
            print('账号      密码(md5)')
            for item in data:
                print(item[0]+'     '+item[1])
        elif choose == '5':
            break
        else:
            print('输入不正确，请重新输入！')
            continue
