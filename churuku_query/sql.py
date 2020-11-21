import pymysql
from datetime import datetime
import time
import hashlib

hostip = '127.0.0.1'
key = '12345'
##hostip = '192.168.0.5'
##key = 'Zhtk_897919'




##仅做测试用
def test_print():
    print('here i am!')


##添加材料信息
def cailiao_add(cl_id, cl_name, cl_guige, cl_danwei):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_add = "INSERT IGNORE INTO cailiao VALUES('"+str(cl_id)+"','"+str(cl_name)+"','"+str(cl_guige)+"','"+str(cl_danwei)+"');"
    cursor.execute(sql_cl_add)
    ##库存增加此材料，数量设为0
    sql_kc_add = "INSERT IGNORE INTO kucun VALUES('"+str(cl_id)+"',0);"
    cursor.execute(sql_kc_add)
    db.commit()
    db.close()
    
####删除材料信息
##def cailiao_remove(cl_id):
##    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
##    cursor = db.cursor()
##    sql_cl_remove = "DELETE FROM cailiao WHERE id = '"+str(cl_id)+"';"
##    cursor.execute(sql_cl_remove)
##    db.commit()
##    db.close()


##修改材料信息(By id)
def cailiao_modify(cl_id,cl_name,cl_guige,cl_danwei):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_modify = "UPDATE cailiao SET name='"+str(cl_name)+"', guige='"+str(cl_guige)+"', danwei='"+str(cl_danwei)\
                    +"' WHERE id='"+str(cl_id)+"';"
    cursor.execute(sql_cl_modify)
    db.commit()
    db.close()

##查询材料信息(By id)
##输出结果元组:('zhtk0100100001', '树脂', 'guigeA', '斤')
def cailiao_query_byid(cl_id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_querybyid = "SELECT * FROM cailiao WHERE id='"+str(cl_id)+"';"
    cursor.execute(sql_cl_querybyid)
    data = cursor.fetchone()
    db.commit()
    db.close()
    return data

##查询材料信息(全部)
##输出结果元组:(('zhtk0100100001', '树脂', 'guigeA', '斤'), ('zhtk0100100002', '玻璃', 'guigeB', '个'))
def cailiao_query():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT * FROM cailiao;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##查询库存信息(全部)
##输出结果元组:(('zhtk0100100001',0), ('zhtk0100100002',0))
def kucun_query():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_kc_query = "SELECT * FROM kucun;"
    cursor.execute(sql_kc_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##添加供货单位信息
def gonghuodanwei_add(ghdw_id,ghdw_name,ghdw_lianxiren,ghdw_dianhua,ghdw_dizhi,ghdw_isoid,ghdw_hege):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ghdw_add = "INSERT IGNORE INTO gonghuodanwei VALUES ('"+str(ghdw_id)+"','"+str(ghdw_name)+"','"+str(ghdw_lianxiren)\
                   +"','"+str(ghdw_dianhua)+"','"+str(ghdw_dizhi)+"','"+str(ghdw_isoid)+"','"+str(ghdw_hege)+"');"
    cursor.execute(sql_ghdw_add)
    ##未付增加此供货单位，金额设为0，已付设为0，未付设为0
    sql_wf_add = "INSERT IGNORE INTO weifu VALUES('"+str(ghdw_id)+"',0,0,0);"
    cursor.execute(sql_wf_add)
    db.commit()
    db.close()

####删除供货单位信息
##def gonghuodanwei_remove(ghdw_id):
##    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
##    cursor = db.cursor()
##    sql_ghdw_remove = "DELETE FROM gonghuodanwei WHERE id = '"+str(ghdw_id)+"';"
##    cursor.execute(sql_ghdw_remove)
##    db.commit()
##    db.close()
    
##修改供货单位信息(By id)
def gonghuodanwei_modify(ghdw_id,ghdw_name,ghdw_lianxiren,ghdw_dianhua,ghdw_dizhi,ghdw_isoid,ghdw_hege):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ghdw_modify = "UPDATE gonghuodanwei SET name='"+str(ghdw_name)+"', lianxiren='"+str(ghdw_lianxiren)+"', dianhua='"\
                    +str(ghdw_dianhua)+"', dizhi='"+str(ghdw_dizhi)+"', isoid='"+str(ghdw_isoid)+"', hege='"+str(ghdw_hege)\
                    +"'  WHERE id='"+str(ghdw_id)+"';"
    cursor.execute(sql_ghdw_modify)
    db.commit()
    db.close()

##查询供货单位信息(By id)
##输出结果元组:('zhtk0200100001', '白天集团有限公司', '李四', '18915307888', '江苏省宜兴市和桥镇开福区2号', 'ISO9002', '否')
def gonghuodanwei_query_byid(ghdw_id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ghdw_querybyid = "SELECT * FROM gonghuodanwei WHERE id='"+str(ghdw_id)+"';"
    cursor.execute(sql_ghdw_querybyid)
    data = cursor.fetchone()
    db.commit()
    db.close()
    return data

##查询供货单位信息(全部)
##输出结果元组:(('zhtk0200100001', '白天集团有限公司', '李四', '18915307888', '江苏省宜兴市和桥镇开福区2号', 'ISO9002', '否'),
##              ('zhtk0200100002', '水火集团有限公司', '王五', '18915301222', '江苏省宜兴市和桥镇开福区563号', 'ISO9003', '是'))
def gonghuodanwei_query():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ghdw_query = "SELECT * FROM gonghuodanwei;"
    cursor.execute(sql_ghdw_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data


##添加负责人信息
def fuzeren_add(fzr_name,fzr_dianhua):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fzr_add = "INSERT IGNORE INTO fuzeren VALUES('"+str(fzr_name)+"','"+str(fzr_dianhua)+"');"
    cursor.execute(sql_fzr_add)
    db.commit()
    db.close()
    
##删除负责人信息
def fuzeren_remove(fzr_name):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fzr_remove = "DELETE FROM fuzeren WHERE id = '"+str(fzr_name)+"';"
    cursor.execute(sql_fzr_remove)
    db.commit()
    db.close()

####修改负责人信息(By name)
##def fuzeren_modify(fzr_name,fzr_dianhua):
##    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
##    cursor = db.cursor()
##    sql_fzr_modify = "UPDATE fuzeren SET dianhua='"+str(fzr_dianhua)+"' WHERE name='"+str(fzr_name)+"';"
##    cursor.execute(sql_fzr_modify)
##    db.commit()
##    db.close()

##查询负责人信息(By name)
##输出结果元组:('杨狗旭', '18015306999')
def fuzeren_query_byname(fzr_name):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fzr_querybyname = "SELECT * FROM fuzeren WHERE name='"+str(fzr_name)+"';"
    cursor.execute(sql_fzr_querybyname)
    data = cursor.fetchone()
    db.commit()
    db.close()
    return data

##查询负责人信息(全部)
##输出结果元组:(('杨狗旭', '18015306999'), ('白林枭', '18915306999'))
def fuzeren_query():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fzr_query = "SELECT * FROM fuzeren;"
    cursor.execute(sql_fzr_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##未付表更新(根据金额和已付)
def weifu_update():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_wf_update = 'UPDATE weifu SET weifu = jine - yifu';
    cursor.execute(sql_wf_update)
    db.commit()
    db.close()


##添加入库信息(rk_time='2020-2-17')
def ruku_add(rk_id,rk_time,cl_id,rk_shuliang,rk_danjia,fzr_name,ghdw_id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_add = "INSERT INTO ruku VALUES('"+str(rk_id)+"','"+str(rk_time)+"','"+str(cl_id)+"',"+str(rk_shuliang)\
                 +","+str(rk_danjia)+","+str(float(rk_shuliang)*float(rk_danjia))+",'"+str(fzr_name)+"','"+\
                 str(ghdw_id)+"');"
    cursor.execute(sql_rk_add)
    ##库存增加
    sql_kc_add = "UPDATE kucun SET shuliang = shuliang + "+str(rk_shuliang)+" WHERE cailiao_id = '"+str(cl_id)+"';"
    cursor.execute(sql_kc_add)
    ##未付增加
    sql_wf_add = "UPDATE weifu SET jine = jine + "+str(float(rk_shuliang)*float(rk_danjia))+" WHERE gonghuodanwei_id = '"+str(ghdw_id)+"';"
    cursor.execute(sql_wf_add)
    db.commit()
    db.close()
    weifu_update()
    
####删除入库信息
##def ruku_remove(rk_id):
##    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
##    cursor = db.cursor()
##    sql_rk_remove = "DELETE FROM ruku WHERE id = '"+str(rk_id)+"';"
##    cursor.execute(sql_rk_remove)
##    db.commit()
##    db.close()

##修改入库信息(By id)
def ruku_modify(rk_id,rk_time,cl_id,rk_shuliang,rk_danjia,fzr_name,ghdw_id):
    pre_shuliang = ruku_query_byid(rk_id)[3]
    pre_cl_id = ruku_query_byid(rk_id)[2]
    pre_jine = float(ruku_query_byid(rk_id)[3])*float(ruku_query_byid(rk_id)[4])
    pre_ghdw_id = ruku_query_byid(rk_id)[7]
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_modify = "UPDATE ruku SET time='"+str(rk_time)+"',cailiao_id='"+str(cl_id)+"',shuliang="+str(rk_shuliang)\
                 +",danjia="+str(rk_danjia)+",jine="+str(float(rk_shuliang)*float(rk_danjia))+\
                 ",fuzeren_name='"+str(fzr_name)+"',gonghuodanwei_id='"+str(ghdw_id)+"' WHERE id='"+str(rk_id)+"';"
    cursor.execute(sql_rk_modify)
    ##库存修改
    if pre_cl_id == cl_id:
        sql_kc_mod = "UPDATE kucun SET shuliang = shuliang + "+str(rk_shuliang-pre_shuliang)+" WHERE cailiao_id = '"+str(cl_id)+"';"
        cursor.execute(sql_kc_mod)
    else:
        sql_kc_mod = "UPDATE kucun SET shuliang = shuliang - "+str(pre_shuliang)+" WHERE cailiao_id = '"+str(pre_cl_id)+"';"
        cursor.execute(sql_kc_mod)
        sql_kc_mod = "UPDATE kucun SET shuliang = shuliang + "+str(rk_shuliang)+" WHERE cailiao_id = '"+str(cl_id)+"';"
        cursor.execute(sql_kc_mod)
    ##未付修改
    if pre_ghdw_id == ghdw_id:
        sql_wf_mod = "UPDATE weifu SET jine = jine + "+str(float(rk_shuliang)*float(rk_danjia)-pre_jine)+" WHERE gonghuodanwei_id = '"+str(ghdw_id)+"';"
        cursor.execute(sql_wf_mod)
    else:
        sql_wf_mod = "UPDATE weifu SET jine = jine - "+str(pre_jine)+" WHERE gonghuodanwei_id = '"+str(pre_ghdw_id)+"';"
        cursor.execute(sql_wf_mod)
        sql_wf_mod = "UPDATE weifu SET jine = jine + "+str(float(rk_shuliang)*float(rk_danjia))+" WHERE gonghuodanwei_id = '"+str(ghdw_id)+"';"
        cursor.execute(sql_wf_mod)
    db.commit()
    db.close()
    weifu_update()

##查询入库信息(By id)
##输出结果元组:('zhtk0300100001', datetime.datetime(2020, 2, 17, 0, 0), 'zhtk0100100001', 20, 10000, 200000, 50000, '白林枭', 'zhtk0200100002')
def ruku_query_byid(rk_id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_querybyid = "SELECT * FROM ruku WHERE id='"+str(rk_id)+"';"
    cursor.execute(sql_rk_querybyid)
    data = cursor.fetchone()
    db.commit()
    db.close()
    return data

##查询入库信息(全部)
##输出结果元组:(('zhtk0300100001', datetime.datetime(2020, 2, 17, 0, 0), 'zhtk0100100001', 20, 10000, 200000, 50000, '白林枭', 'zhtk0200100002'),
##           ('zhtk0300100002', datetime.datetime(2020, 2, 18, 0, 0), 'zhtk0100100002', 10, 5000, 50000, 20000, '杨狗旭', 'zhtk0200100002'))
def ruku_query():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

###############################################################
######################chuku_add已修改##########################
###############################################################

##添加出库信息(ck_time='2020-2-17')
def chuku_add(ck_id,ck_time,cl_id,ck_shuliang,fzr_name,ck_yongtu):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_add = "INSERT INTO chuku VALUES('"+str(ck_id)+"','"+str(ck_time)+"','"+str(cl_id)+"',"+str(ck_shuliang)\
                 +",'"+str(fzr_name)+"','"+str(ck_yongtu)+"');"
    cursor.execute(sql_ck_add)
    ##库存减少
    sql_kc_minus = "UPDATE kucun SET shuliang = shuliang - "+str(ck_shuliang)+" WHERE cailiao_id = '"+str(cl_id)+"';"
    cursor.execute(sql_kc_minus)
    db.commit()
    db.close()
    
####删除出库信息
##def chuku_remove(ck_id):
##    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
##    cursor = db.cursor()
##    sql_ck_remove = "DELETE FROM chuku WHERE id = '"+str(ck_id)+"';"
##    cursor.execute(sql_ck_remove)
##    db.commit()
##    db.close()

##################################################################
######################chuku_nodify已修改##########################
##################################################################
##修改出库信息(By id)
def chuku_modify(ck_id,ck_time,cl_id,ck_shuliang,fzr_name,ck_yongtu):
    pre_shuliang = chuku_query_byid(ck_id)[3]
    pre_cl_id = chuku_query_byid(ck_id)[2]
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_modify = "UPDATE chuku SET time='"+str(ck_time)+"',cailiao_id='"+str(cl_id)+"',shuliang="+str(ck_shuliang)\
                 +",fuzeren_name='"+str(fzr_name)+"',yongtu='"+str(ck_yongtu)+"' WHERE id='"+str(ck_id)+"';"
    cursor.execute(sql_ck_modify)
    if pre_cl_id == cl_id:
        sql_kc_mod = "UPDATE kucun SET shuliang = shuliang - "+str(ck_shuliang-pre_shuliang)+" WHERE cailiao_id = '"+str(cl_id)+"';"
        cursor.execute(sql_kc_mod)
    else:
        sql_kc_mod = "UPDATE kucun SET shuliang = shuliang + "+str(pre_shuliang)+" WHERE cailiao_id = '"+str(pre_cl_id)+"';"
        cursor.execute(sql_kc_mod)
        sql_kc_mod = "UPDATE kucun SET shuliang = shuliang - "+str(ck_shuliang)+" WHERE cailiao_id = '"+str(cl_id)+"';"
        cursor.execute(sql_kc_mod)
    db.commit()
    db.close()

##查询出库信息(By id)
##输出结果元组:('zhtk0400100002', datetime.datetime(2020, 2, 15, 0, 0), 'zhtk0300100002', 12, '杨狗旭')
def chuku_query_byid(ck_id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_querybyid = "SELECT * FROM chuku WHERE id='"+str(ck_id)+"';"
    cursor.execute(sql_ck_querybyid)
    data = cursor.fetchone()
    db.commit()
    db.close()
    return data

##查询出库信息(全部)
##输出结果元组:(('zhtk0400100001', datetime.datetime(2020, 2, 17, 0, 0), 'zhtk0300100001', 15, '白林枭'),
##              ('zhtk0400100002', datetime.datetime(2020, 2, 15, 0, 0), 'zhtk0300100002', 12, '杨狗旭'))
def chuku_query():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data


##################################################################
######################fuzhang_add已修改###########################
##################################################################

##添加付账信息(fz_time='2020-2-17')
def fuzhang_add(fz_id,fz_time,ghdw_id,fz_fuzhang,fz_fangshi):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fz_add = "INSERT INTO fuzhang VALUES('"+str(fz_id)+"','"+str(fz_time)+"','"+str(ghdw_id)+"',"+str(fz_fuzhang)+",'"+str(fz_fangshi)+"');"
    cursor.execute(sql_fz_add)
    ##未付已付金额增加
    sql_wf_add = "UPDATE weifu SET yifu = yifu + "+str(fz_fuzhang)+" WHERE gonghuodanwei_id = '"+str(ghdw_id)+"';"
    cursor.execute(sql_wf_add)
    db.commit()
    db.close()
    weifu_update()
    
####删除付账信息
##def fuzhang_remove(fz_id):
##    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
##    cursor = db.cursor()
##    sql_fz_remove = "DELETE FROM fuzhang WHERE id = '"+str(fz_id)+"';"
##    cursor.execute(sql_fz_remove)
##    db.commit()
##    db.close()

####################################################################
######################fuzhang_modify已修改##########################
####################################################################
##修改付账信息(By id)
def fuzhang_modify(fz_id,fz_time,ghdw_id,fz_fuzhang,fz_fangshi):
    pre_fz_fuzhang = fuzhang_query_byid(fz_id)[3]
    pre_ghdw_id = fuzhang_query_byid(fz_id)[2]
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fz_modify = "UPDATE fuzhang SET time='"+str(fz_time)+"',gonghuodanwei_id='"+str(ghdw_id)+"',fuzhang="+str(fz_fuzhang)\
                    +",fangshi='"+str(fz_fangshi)+"' WHERE id='"+str(fz_id)+"';"
    cursor.execute(sql_fz_modify)
    ##未付修改
    if pre_ghdw_id == ghdw_id:
        sql_wf_mod = "UPDATE weifu SET yifu = yifu + "+str(fz_fuzhang-pre_fz_fuzhang)+" WHERE gonghuodanwei_id = '"+str(ghdw_id)+"';"
        cursor.execute(sql_wf_mod)
    else:
        sql_wf_mod = "UPDATE weifu SET yifu = yifu - "+str(pre_fz_fuzhang)+" WHERE gonghuodanwei_id = '"+str(pre_ghdw_id)+"';"
        cursor.execute(sql_wf_mod)
        sql_wf_mod = "UPDATE weifu SET yifu = yifu + "+str(fz_fuzhang)+" WHERE gonghuodanwei_id = '"+str(ghdw_id)+"';"
        cursor.execute(sql_wf_mod)
    db.commit()
    db.close()
    weifu_update()

####################################################################
#                  以上是我所有改动
####################################################################


##查询付账信息(By id)
def fuzhang_query_byid(fz_id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fz_querybyid = "SELECT * FROM fuzhang WHERE id='"+str(fz_id)+"';"
    cursor.execute(sql_fz_querybyid)
    data = cursor.fetchone()
    db.commit()
    db.close()
    return data

##查询付账信息(全部)
def fuzhang_query():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fz_query = "SELECT * FROM fuzhang;"
    cursor.execute(sql_fz_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data


##入库时间查询(rk_time_from='2020-2-17',rk_time_to='2020-2-18',前后均包括)
def ruku_query_bytime(rk_time_from,rk_time_to):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_querybytime = "SELECT * FROM ruku WHERE time>='"+str(rk_time_from)+"' and time<='"+str(rk_time_to)+"';"
    cursor.execute(sql_rk_querybytime)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##出库时间查询(ck_time_from='2020-2-17',ck_time_to='2020-2-18',前后均包括)
def chuku_query_bytime(ck_time_from,ck_time_to):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_querybytime = "SELECT * FROM chuku WHERE time>='"+str(ck_time_from)+"' and time<='"+str(ck_time_to)+"';"
    cursor.execute(sql_ck_querybytime)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##付账时间查询(fz_time_from='2020-2-17',fz_time_to='2020-2-18',前后均包括)
def fuzhang_query_bytime(fz_time_from,fz_time_to):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fz_querybytime = "SELECT * FROM fuzhang WHERE time>='"+str(fz_time_from)+"' and time<='"+str(fz_time_to)+"';"
    cursor.execute(sql_fz_querybytime)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data


##入库材料编号查询
def ruku_query_bycailiao_id(cl_id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_querybycailiao_id = "SELECT * FROM ruku WHERE cailiao_id='"+str(cl_id)+"';"
    cursor.execute(sql_rk_querybycailiao_id)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##出库材料编号查询
def chuku_query_bycailiao_id(cl_id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_querybycailiao_id = "SELECT * FROM chuku WHERE cailiao_id='"+str(cl_id)+"';"
    cursor.execute(sql_ck_querybycailiao_id)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##入库负责人查询
def ruku_query_byfuzeren(fzr_name):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_querybyfuzeren = "SELECT * FROM ruku WHERE fuzeren_name='"+str(fzr_name)+"';"
    cursor.execute(sql_rk_querybyfuzeren)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##出库负责人查询
def chuku_query_byfuzeren(fzr_name):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_querybyfuzeren = "SELECT * FROM chuku WHERE fuzeren_name='"+str(fzr_name)+"';"
    cursor.execute(sql_ck_querybyfuzeren)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##入库供货单位查询
def ruku_query_bygonghuodanwei(ghdw_id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_querybygonghuodanwei = "SELECT * FROM ruku WHERE gonghuodanwei_id='"+str(ghdw_id)+"';"
    cursor.execute(sql_rk_querybygonghuodanwei)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##付账供货单位查询
def fuzhang_query_bygonghuodanwei(ghdw_id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fz_querybygonghuodanwei_id = "SELECT * FROM fuzhang WHERE gonghuodanwei_id='"+str(ghdw_id)+"';"
    cursor.execute(sql_fz_querybygonghuodanwei_id)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data


def cailiao_query_allid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT id FROM cailiao;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def cailiao_query_allname():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT name FROM cailiao;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def cailiao_query_allguige():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT guige FROM cailiao;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def cailiao_query_alldanwei():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT danwei FROM cailiao;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_allid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT id FROM gonghuodanwei;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_allname():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT name FROM gonghuodanwei;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_alllianxiren():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT lianxiren FROM gonghuodanwei;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_alldianhua():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT dianhua FROM gonghuodanwei;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_alldizhi():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT dizhi FROM gonghuodanwei;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_allisoid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT isoid FROM gonghuodanwei;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_allhege():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT hege FROM gonghuodanwei;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_allid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT id FROM ruku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_alltime():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT time FROM ruku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_allcailiao_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT cailiao_id FROM ruku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_allshuliang():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT shuliang FROM ruku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_alldanjia():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT danjia FROM ruku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_allfuzeren_name():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT fuzeren_name FROM ruku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_allgonghuodanwei_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT gonghuodanwei_id FROM ruku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_allid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT id FROM chuku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_alltime():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT time FROM chuku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_allcailiao_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT cailiao_id FROM chuku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_allshuliang():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT shuliang FROM chuku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_allfuzeren_name():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT fuzeren_name FROM chuku;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def fuzhang_query_allid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT id FROM fuzhang;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def fuzhang_query_alltime():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT time FROM fuzhang;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def fuzhang_query_allruku_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT ruku_id FROM fuzhang;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def fuzhang_query_allfuzhang():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT fuzhang FROM fuzhang;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def fuzeren_query_allname():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT name FROM fuzeren;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

#####有些项目需要自动显示，所以写以下函数
def cailiao_query_id_by_name(cailiao_name):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT id FROM cailiao where name = '"+str(cailiao_name)+"';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def cailiao_query_danwei_by_name(cailiao_name):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT danwei FROM cailiao where name = '"+str(cailiao_name)+"';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def fuzeren_query_dianhua_by_name(fuzeren_name):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT dianhua FROM fuzeren where name = '" + str(fuzeren_name) + "';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_id_by_name(name):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT id FROM gonghuodanwei where name = '" + str(name) + "';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_lianxiren_by_name(name):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT lianxiren FROM gonghuodanwei where name = '" + str(name) + "';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_dianhua_by_name(name):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT dianhua FROM gonghuodanwei where name = '" + str(name) + "';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data


def gonghuodanwei_query_name_by_id(id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT name FROM gonghuodanwei where id = '" + str(id) + "';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_dizhi_by_name(name):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT dizhi FROM gonghuodanwei where name = '" + str(name) + "';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_gonghuodanwei_id_by_id(id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT gonghuodanwei_id FROM ruku where name = '" + str(id) + "';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_gonghuodanwei_id_by_id(id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT gonghuodanwei_id FROM ruku where id = '" + str(id) + "';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_gonghuodanwei_name_by_id(id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT gonghuodanwei_id FROM ruku where id = '" + str(id) + "';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    #继续查找 先从入库表里找到供货单位ID，再拿这个到供货单位里面去找供货单位名称
    data1 = str(data[0][0])
    cursor1 = db.cursor()
    sql_cl_query1 = "SELECT name FROM gonghuodanwei where id = '" + str(data1) + "';"
    cursor1.execute(sql_cl_query1)
    data2 = cursor1.fetchall()
    db.commit()
    db.close()
    return data2

def ruku_query_lianxiren_by_id(id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT gonghuodanwei_id FROM ruku where id = '" + str(id) + "';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    #继续查找 先从入库表里找到供货单位ID，再拿这个到供货单位里面去找供货单位名称
    data1 = str(data[0][0])
    cursor1 = db.cursor()
    sql_cl_query1 = "SELECT lianxiren FROM gonghuodanwei where id = '" + str(data1) + "';"
    cursor1.execute(sql_cl_query1)
    data2 = cursor1.fetchall()
    db.commit()
    db.close()
    return data2

def ruku_query_dianhua_by_id(id):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT gonghuodanwei_id FROM ruku where id = '" + str(id) + "';"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    #继续查找 先从入库表里找到供货单位ID，再拿这个到供货单位里面去找供货单位名称
    data1 = str(data[0][0])
    cursor1 = db.cursor()
    sql_cl_query1 = "SELECT dianhua FROM gonghuodanwei where id = '" + str(data1) + "';"
    cursor1.execute(sql_cl_query1)
    data2 = cursor1.fetchall()
    db.commit()
    db.close()
    return data2


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
            pass
    return False



##ruku带序查询
def ruku_query_orderbyid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY id;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbytime():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY time;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbycailiao_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY cailiao_id;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbyshuliang():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY shuliang;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbydanjia():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY danjia;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbyjine():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY jine;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbyyifu():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY yifu;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbyfuzeren_name():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY fuzeren_name;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbygonghuodanwei_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY gonghuodanwei_id;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data


##chuku带序查询
def chuku_query_orderbyid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku ORDER BY id;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_orderbytime():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku ORDER BY time;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_orderbycailiao_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku ORDER BY cailiao_id;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_orderbyshuliang():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku ORDER BY shuliang;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_orderbyfuzeren_name():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku ORDER BY fuzeren_name;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##ruku带序查询
def ruku_query_orderbyid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY id;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbytime():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY time;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbycailiao_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY cailiao_id;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbyshuliang():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY shuliang;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbydanjia():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY danjia;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbyjine():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY jine;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##def ruku_query_orderbyyifu():
##    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
##    cursor = db.cursor()
##    sql_rk_query = "SELECT * FROM ruku ORDER BY yifu;"
##    cursor.execute(sql_rk_query)
##    data = cursor.fetchall()
##    db.commit()
##    db.close()
##    return data

def ruku_query_orderbyfuzeren_name():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY fuzeren_name;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbygonghuodanwei_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY gonghuodanwei_id;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def ruku_query_orderbyweifu():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_rk_query = "SELECT * FROM ruku ORDER BY yifu-jine;"
    cursor.execute(sql_rk_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data


##chuku带序查询
def chuku_query_orderbyid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku ORDER BY id;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_orderbytime():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku ORDER BY time;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_orderbycailiao_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku ORDER BY cailiao_id;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_orderbyshuliang():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku ORDER BY shuliang;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_orderbyfuzeren_name():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku ORDER BY fuzeren_name;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def chuku_query_orderbyyongtu():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_query = "SELECT * FROM chuku ORDER BY yongtu;"
    cursor.execute(sql_ck_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##fuzhang带序查询
def fuzhang_query_orderbyid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fz_query = "SELECT * FROM fuzhang ORDER BY id;"
    cursor.execute(sql_fz_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def fuzhang_query_orderbytime():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fz_query = "SELECT * FROM fuzhang ORDER BY time;"
    cursor.execute(sql_fz_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def fuzhang_query_orderbygonghuodanwei_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fz_query = "SELECT * FROM fuzhang ORDER BY gonghuodanwei_id;"
    cursor.execute(sql_fz_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def fuzhang_query_orderbyfuzhang():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fz_query = "SELECT * FROM fuzhang ORDER BY fuzhang;"
    cursor.execute(sql_fz_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def fuzhang_query_orderbyfangshi():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fz_query = "SELECT * FROM fuzhang ORDER BY fangshi;"
    cursor.execute(sql_fz_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##kucun带序查询
def kucun_query_orderbycailiao_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_kc_query = "SELECT * FROM kucun ORDER BY cailiao_id;"
    cursor.execute(sql_kc_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def kucun_query_orderbyshuliang():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_kc_query = "SELECT * FROM kucun ORDER BY shuliang;"
    cursor.execute(sql_kc_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##gonghuodanwei带序查询
def gonghuodanwei_query_orderbyid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ghdw_query = "SELECT * FROM gonghuodanwei ORDER BY id;"
    cursor.execute(sql_ghdw_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_orderbyname():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ghdw_query = "SELECT * FROM gonghuodanwei ORDER BY name;"
    cursor.execute(sql_ghdw_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_orderbylianxiren():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ghdw_query = "SELECT * FROM gonghuodanwei ORDER BY lianxiren;"
    cursor.execute(sql_ghdw_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_orderbydianhua():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ghdw_query = "SELECT * FROM gonghuodanwei ORDER BY dianhua;"
    cursor.execute(sql_ghdw_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_orderbydizhi():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ghdw_query = "SELECT * FROM gonghuodanwei ORDER BY dizhi;"
    cursor.execute(sql_ghdw_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_orderbyisoid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ghdw_query = "SELECT * FROM gonghuodanwei ORDER BY isoid;"
    cursor.execute(sql_ghdw_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def gonghuodanwei_query_orderbyhege():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ghdw_query = "SELECT * FROM gonghuodanwei ORDER BY hege;"
    cursor.execute(sql_ghdw_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##cailiao带序查询
def cailiao_query_orderbyid():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT * FROM cailiao ORDER BY id;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def cailiao_query_orderbyname():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT * FROM cailiao ORDER BY name;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def cailiao_query_orderbyguige():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT * FROM cailiao ORDER BY guige;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def cailiao_query_orderbydanwei():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_cl_query = "SELECT * FROM cailiao ORDER BY danwei;"
    cursor.execute(sql_cl_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##fuzeren带序查询
def fuzeren_query_orderbyname():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fzr_query = "SELECT * FROM fuzeren ORDER BY name;"
    cursor.execute(sql_fzr_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def fuzeren_query_orderbydianhua():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_fzr_query = "SELECT * FROM fuzeren ORDER BY dianhua;"
    cursor.execute(sql_fzr_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data


##weifu带序查询
def weifu_query():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_wf_query = "SELECT * FROM weifu;"
    cursor.execute(sql_wf_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def weifu_query_orderbygonghuodanwei_id():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_wf_query = "SELECT * FROM weifu ORDER BY gonghuodanwei_id;"
    cursor.execute(sql_wf_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def weifu_query_orderbyjine():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_wf_query = "SELECT * FROM weifu ORDER BY jine DESC;"
    cursor.execute(sql_wf_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def weifu_query_orderbyyifu():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_wf_query = "SELECT * FROM weifu ORDER BY yifu DESC;"
    cursor.execute(sql_wf_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def weifu_query_orderbyweifu():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_wf_query = "SELECT * FROM weifu ORDER BY weifu DESC;"
    cursor.execute(sql_wf_query)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##找与用户名匹配的密码，返回密文密码
def denglu_query_mima_by_yonghuming(yonghuming):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_querybyid = "SELECT mima FROM denglu WHERE yonghuming='"+str(yonghuming)+"';"
    cursor.execute(sql_ck_querybyid)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data


##添加登录记录
def denglu_record_add(denglu_time, denglu_yonghuming, denglu_statu):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_add = "INSERT INTO denglu_record VALUES('"+str(denglu_time)+"','"+str(denglu_yonghuming)+"','"+str(denglu_statu)+"');"
    cursor.execute(sql_ck_add)
    db.commit()
    db.close()

##查询所用用户
def denglu_query_allyonghuming():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_querybyid = "SELECT yonghuming FROM denglu"
    cursor.execute(sql_ck_querybyid)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def get_md5(s):
    md5_obj = hashlib.md5()
    md5_obj.update(s.encode('utf-8'))
    ret = md5_obj.hexdigest()
    return ret

##这个函数用来手动添加一个账户
def yonghu_mima_add(yonghu,mima):
    mima = get_md5(mima)
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_add = "INSERT INTO denglu VALUES('" + str(yonghu) + "','" + str(mima) + "');"
    cursor.execute(sql_ck_add)
    db.commit()
    db.close()

##这个函数用来手动删除一个账户
def yonghu_mima_delete(yonghu):
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_add = "DELETE FROM denglu WHERE yonghuming = '" + str(yonghu) + "';"
    cursor.execute(sql_ck_add)
    db.commit()
    db.close()

##这个函数用来手动修改一个账户
def yonghu_mima_modify(yonghu,mima):
    mima = get_md5(mima)
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_add = "UPDATE denglu SET mima = '" + str(mima) + "' WHERE yonghuming = '" + str(yonghu) + "';"
    cursor.execute(sql_ck_add)
    db.commit()
    db.close()

def denglu_record_query():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_add = "SELECT * FROM denglu_record;"
    cursor.execute(sql_ck_add)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

def denglu_query():
    db = pymysql.connect(host=hostip, port=3306, user='root', passwd=key, db='churuku', charset='utf8')
    cursor = db.cursor()
    sql_ck_add = "SELECT * FROM denglu;"
    cursor.execute(sql_ck_add)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

##if __name__ == '__main__':
##    yonghu_mima_add('zhtk001', 'zhtk001')
##    yonghu_mima_add('zhtk002', 'zhtk002')
##    yonghu_mima_add('zhtk003', 'zhtk003')
##    yonghu_mima_add('zhtk004', 'zhtk004')
##    yonghu_mima_add('zhtk005', 'zhtk005')
##    yonghu_mima_add('zhtk006', 'zhtk006')
##    yonghu_mima_add('zhtk007', 'zhtk007')
##    yonghu_mima_add('zhtk008', 'zhtk008')
##    yonghu_mima_add('zhtk009', 'zhtk009')
##    yonghu_mima_add('zhtk010', 'zhtk0010')


###ruku_modify('rk0002','2020-2-25','zhtk0100100001',5,50,'白林枭','zhtk0200100001')
###fuzhang_add('fz0001','2020-2-25','rk0002',2500)
###ruku_modify('rk001','2020-2-25','zhtk0100100002',-10,500,'白林枭','zhtk0200100001')
###fuzhang_modify('fz001','2020-2-25','zhtk0300100003',-2500)
###gonghuodanwei_add('g005','11234','bai','12313131','###','123dafaf','否')


    

