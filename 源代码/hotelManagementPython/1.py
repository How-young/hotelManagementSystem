from flask import Flask, request, jsonify
import pymysql
from time import strftime, localtime

app = Flask(__name__)


#数据库操作
def ConnectMysql(sql):
    connect = pymysql.connect("localhost", "root", "1234", "hotel")
    cur = connect.cursor()
    try:
        cur.execute(sql)
        if "select" in sql:
            if "administratorinformation" in sql:
                res = cur.fetchone()
            else:
                res = cur.fetchall()
        connect.commit()
        return res
    except:
        connect.rollback()
    cur.close()
    connect.close()


#管理员登录
@app.route("/Login", methods = ["post"])
def AdministratorLogin():
    adminnum = request.args.get("adminnum")
    adminpassword = request.args.get("adminpassword")

    if adminnum and adminpassword:
        sql = "select * from administratorinformation where adminnum='%s'"%adminnum
        res = ConnectMysql(sql)
        if res[1] == adminpassword:
            return jsonify({"adminnum": adminnum,
                            "adminpassword": adminpassword,
                            "status": True
            })
        else:
            return Error()

    else:
        return Error()


#获得所有房间类型
@app.route("/RoomType/Get")
def GetRoomType():
    sql = "select * from roomtypeinformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "roomtypenum": type[0], "roomtype": type[1],
                     "roomprice": type[2], "roomquantity": type[3], "roomdescribe": type[4]})
        list.append(item)
    return jsonify({
        "RoomType": list,
        "status": True
    })


#增加房间类型
@app.route("/RoomType/Add")
def AddRoomType():
    roomtypenum = request.args.get("roomtypenum")
    roomtype = request.args.get("roomtype")
    roomprice = request.args.get("roomprice")
    roomquantity = request.args.get("roomquantity")
    roomdescribe = request.args.get("roomdescribe")

    if roomtypenum:
        sql = """insert into
                 roomtypeinformation(roomtypenum, roomtype, roomprice, roomquantity,roomdescribe)
                 values('%s', '%s', '%s', '%s', '%s')
              """%(roomtypenum, roomtype, roomprice, roomquantity, roomdescribe)
        ConnectMysql(sql)
        return jsonify({
                    "roomtypenum": roomtypenum,
                    "roomtype": roomtype,
                    "roomprice": roomprice,
                    "roomquantity": roomquantity,
                    "roomdescribe": roomdescribe,
                    "status": True
        })
    else:
        return Error()


#修改指定roomtypenum的房间类型
@app.route("/RoomType/Modify")
def ModifyRommType():
    roomtypenum = request.args.get("roomtypenum")
    roomtype = request.args.get("roomtype")
    roomprice = request.args.get("roomprice")
    roomquantity = request.args.get("roomquantity")
    roomdescribe = request.args.get("roomdescribe")

    if roomtypenum:
        sql = """update roomtypeinformation
                 set roomtype='%s',roomprice='%s',roomquantity='%s',roomdescribe='%s'
                 where roomtypenum='%s'
              """%(roomtype, roomprice, roomquantity, roomdescribe, roomtypenum)
        ConnectMysql(sql)
        return jsonify({
            "roomtypenum": roomtypenum,
            "roomtype": roomtype,
            "roomprice": roomprice,
            "roomquantity": roomquantity,
            "roomdescribe": roomdescribe,
            "status": True
        })
    else:
        return Error()


#删除指定的roomtypenum的房间类型
@app.route("/RoomType/Delete")
def DeleteRoomType():
    roomtypenum = request.args.get("roomtypenum")

    if roomtypenum:
        sql1 ="delete from roominformation where roomtypenum='%s'"%roomtypenum
        ConnectMysql(sql1)
        sql2 = "delete from roomtypeinformation where roomtypenum='%s'" %roomtypenum
        ConnectMysql(sql2)
        return jsonify({
            "roomtypenum": roomtypenum,
            "status": True
        })
    else:
        return Error()

#楼层信息相关操作
@app.route("/Floor/Add")
def AddFloor():
    floornum = request.args.get("floornum")
    floordescribe = request.args.get("floordescribe")
    #remainnum = request.args.get("remainnum")

    if floornum:
        sql = """insert into
                 floorinformation(floornum, floordescribe)
                 values('%s', '%s')
              """%(floornum, floordescribe)
        ConnectMysql(sql)
        return jsonify({
            "floornum": floornum,
            "floordescribe": floordescribe,
            "status": True
        })
    else:
        return Error()

@app.route("/Floor/Modify")
def ModifyFloor():
    floornum = request.args.get("floornum")
    floordescribe = request.args.get("floordescribe")
    #remainnum = request.args.get("remainnum")

    if floornum:
        sql = """update floorinformation
                         set floordescribe='%s'
                         where floornum='%s'
                      """ % (floordescribe, floornum)
        ConnectMysql(sql)
        return jsonify({
            "floornum": floornum,
            "floordescribe": floordescribe,
            "status": True
        })
    else:
        return Error()

@app.route("/Floor/Delete")
def DeleteFloor():
    floornum = request.args.get("floornum")

    if floornum:
        sql = "delete from floorinformation where floornum='%s'" % floornum
        ConnectMysql(sql)
        return jsonify({
            "floornum": floornum,
            "status": True
        })
    else:
        return Error()

@app.route("/Floor/Get")
def GetFloor():
    sql = "select * from floorinformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "floornum": type[0], "floordescribe": type[1]})
        list.append(item)
    return jsonify({
        "Floor": list,
        "status": True
    })

#商品信息相关操作
@app.route("/Goods/Add")
def AddGoods():
    goodsnum = request.args.get("goodsnum")
    goodsnanme = request.args.get("goodsnanme")
    goodstypenum = request.args.get("goodstypenum")
    goodsprice = request.args.get("goodsprice")
    goodsquantify = request.args.get("goodsquantify")

    if goodsnum:
        sql = """insert into
                 goodsinformation(goodsnum, goodsnanme, goodstypenum, goodsprice, goodsquantify)
                 values('%s', '%s', '%s', '%s', '%s')
              """%(goodsnum, goodsnanme, goodstypenum, goodsprice, goodsquantify)
        ConnectMysql(sql)
        return jsonify({
            "goodsnum": goodsnum,
            "goodsnanme": goodsnanme,
            "goodstypenum": goodstypenum,
            "goodsprice": goodsprice,
            "goodsquantify": goodsquantify,
            "status": True
        })
    else:
        return Error()

@app.route("/Goods/Modify")
def ModifyGoods():
    goodsnum = request.args.get("goodsnum")
    goodsnanme = request.args.get("goodsnanme")
    goodstypenum = request.args.get("goodstypenum")
    goodsprice = request.args.get("goodsprice")
    goodsquantify = request.args.get("goodsquantify")

    if goodsnum:
        sql = """update goodsinformation
                         set goodsnanme='%s',goodstypenum='%s',goodsprice='%s',goodsquantify='%s'
                         where goodsnum='%s'
              """ % (goodsnanme, goodstypenum, goodsprice, goodsquantify, goodsnum)
        ConnectMysql(sql)
        return jsonify({
            "goodsnum": goodsnanme,
            "goodsnanme": goodstypenum,
            "goodstypenum": goodsprice,
            "goodsprice": goodsquantify,
            "goodsquantify": goodsnum,
            "status": True
        })
    else:
        return Error()

@app.route("/Goods/Delete")
def DelteGoods():
    goodsnum = request.args.get("goodsnum")

    if goodsnum:
        sql = "delete from goodsinformation where goodsnum='%s'" % goodsnum
        ConnectMysql(sql)
        return jsonify({
            "goodsnum": goodsnum,
            "status": True
        })
    else:
        return Error()

@app.route("/Goods/Get")
def GetGoods():
    sql = "select * from goodsinformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "goodsnum": type[0], "goodsnanme": type[1],
                     "goodstypenum": type[2], "goodsprice": type[3], "goodsquantify": type[4]})
        list.append(item)
    return jsonify({
        "Goods": list,
        "status": True
    })

#商品类别相关操作
@app.route("/GoodsType/Add")
def AddGoodsType():
    goodstypenum = request.args.get("goodstypenum")
    goodstype = request.args.get("goodstype")
    typedescribe = request.args.get("typedescribe")

    if goodstypenum:
        sql = """insert into
                 goodstypeinformation(goodstypenum, goodstype, typedescribe)
                 values('%s', '%s', '%s')
              """%(goodstypenum, goodstype, typedescribe)
        ConnectMysql(sql)
        return jsonify({
            "goodstypenum": goodstypenum,
            "goodstype": goodstype,
            "typedescribe": typedescribe,
            "status": True
        })
    else:
        return Error()

@app.route("/GoodsType/Modify")
def ModifyGoodsType():
    goodstypenum = request.args.get("goodstypenum")
    goodstype = request.args.get("goodstype")
    typedescribe = request.args.get("typedescribe")

    if goodstypenum:
        sql = """update goodstypeinformation
                         set goodstype='%s',typedescribe='%s'
                         where goodstypenum='%s'
              """ % (goodstype, typedescribe, goodstypenum)
        ConnectMysql(sql)
        return jsonify({
            "goodstypenum": goodstypenum,
            "goodstype": goodstype,
            "typedescribe": typedescribe,
            "status": True
        })
    else:
        return Error()

@app.route("/GoodsType/Delete")
def DeleteGoodsType():
    goodstypenum = request.args.get("goodstypenum")

    if goodstypenum:
        sql = "delete from goodstypeinformation where goodstypenum='%s'" % goodstypenum
        ConnectMysql(sql)
        return jsonify({
            "goodstypenum": goodstypenum,
            "status": True
        })
    else:
        return Error()

@app.route("/GoodsType/Get")
def GetGoodsType():
    sql = "select * from goodstypeinformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "goodstypenum": type[0], "goodstype": type[1],
                     "typedescribe": type[2]})
        list.append(item)
    return jsonify({
        "GoodsType": list,
        "status": True
    })

#会员信息相关操作
@app.route("/Vip/Add")
def AddVip():
    vipnum = request.args.get("vipnum")
    idcard = request.args.get("idcard")
    vipname = request.args.get("vipname")
    vipsex = request.args.get("vipsex")

    if vipnum:
        sql = """insert into
                 vipinformation(vipnum, idcard, vipname, vipsex)
                 values('%s', '%s', '%s', '%s')
              """%(vipnum, idcard, vipname, vipsex)
        ConnectMysql(sql)
        return jsonify({
            "vipnum": vipnum,
            "idcard": idcard,
            "vipname": vipname,
            "vipsex": vipsex,
            "status": True
        })
    else:
        return Error()

@app.route("/Vip/Modify")
def ModifyVip():
    vipnum = request.args.get("vipnum")
    idcard = request.args.get("idcard")
    vipname = request.args.get("vipname")
    vipsex = request.args.get("vipsex")

    if vipnum:
        sql = """update vipinformation
                         set idcard='%s',vipname='%s',vipsex='%s'
                         where vipnum='%s'
              """ % (idcard, vipname, vipsex, vipnum)
        ConnectMysql(sql)
        return jsonify({
            "vipnum": vipnum,
            "idcard": idcard,
            "vipname": vipname,
            "vipsex": vipsex,
            "status": True
        })
    else:
        return Error()

@app.route("/Vip/Delete")
def DelteVip():
    vipnum = request.args.get("vipnum")

    if vipnum:
        sql = "delete from vipinformation where vipnum='%s'" % vipnum
        ConnectMysql(sql)
        return jsonify({
            "vipnum": vipnum,
            "status": True
        })
    else:
        return Error()

@app.route("/Vip/Get")
def GetVip():
    sql = "select * from vipinformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "vipnum": type[0], "idcard": type[1],
                     "vipname": type[2], "vipsex": type[3]})
        list.append(item)
    return jsonify({
        "Vip": list,
        "status": True
    })

#员工信息相关操作
@app.route("/Employee/Add")
def AddEmployee():
    employeenum = request.args.get("employeenum")
    employeemail = request.args.get("employeemail")
    employeepassword = request.args.get("employeepassword")
    employeename = request.args.get("employeename")
    employeesex = request.args.get("employeesex")

    if employeenum:
        sql = """insert into
                 employeeinfromation(employeenum, employeemail, employeepassword, employeename, employeesex)
                 values('%s', '%s', '%s', '%s', '%s')
              """%(employeenum, employeemail, employeepassword, employeename, employeesex)
        ConnectMysql(sql)
        return jsonify({
            "employeenum": employeenum,
            "employeemail": employeemail,
            "employeepassword": employeepassword,
            "employeename": employeename,
            "employeesex": employeesex,
            "status": True
        })
    else:
        return Error()

@app.route("/Employee/Modify")
def ModifyEmployee():
    employeenum = request.args.get("employeenum")
    employeemail = request.args.get("employeemail")
    employeepassword = request.args.get("employeepassword")
    employeename = request.args.get("employeename")
    employeesex = request.args.get("employeesex")

    if employeenum:
        sql = """update employeeinfromation
                         set employeemail='%s',employeepassword='%s',employeename='%s',employeesex='%s'
                         where employeenum='%s'
              """ % (employeemail, employeepassword, employeename, employeesex, employeenum)
        ConnectMysql(sql)
        return jsonify({
            "employeenum": employeenum,
            "employeemail": employeemail,
            "employeepassword": employeepassword,
            "employeename": employeename,
            "employeesex": employeesex,
            "status": True
        })
    else:
        return Error()

@app.route("/Employee/Delete")
def DelteEmployee():
    employeenum = request.args.get("employeenum")

    if employeenum:
        sql = "delete from employeeinfromation where employeenum='%s'" % employeenum
        ConnectMysql(sql)
        return jsonify({
            "employeenum": employeenum,
            "status": True
        })
    else:
        return Error()

@app.route("/Employee/Get")
def GetEmployee():
    sql = "select * from employeeinfromation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "employeenum": type[0], "employeemail": type[1],
                     "employeepassword": type[2], "employeename": type[3], "employeesex": type[4]})
        list.append(item)
    return jsonify({
        "Employee": list,
        "status": True
    })


#客房信息相关操作
@app.route("/Room/Add")
def AddRoom():
    roomnum = request.args.get("roomnum")
    roomtypenum = request.args.get("roomtypenum")
    isempty = request.args.get("isempty")
    roomfloor = request.args.get("roomfloor")

    if roomnum:
        sql = """insert into
                 roominformation(roomnum, roomtypenum, isempty, roomfloor)
                 values('%s', '%s', '%s', '%s')
              """%(roomnum, roomtypenum, isempty, roomfloor)
        ConnectMysql(sql)
        return jsonify({
            "roomnum": roomnum,
            "roomtypenum": roomtypenum,
            "isempty": isempty,
            "roomfloor": roomfloor,
            "status": True
        })
    else:
        return Error()

@app.route("/Room/Modify")
def ModifyRoom():
    roomnum = request.args.get("roomnum")
    roomtypenum = request.args.get("roomtypenum")
    isempty = request.args.get("isempty")
    roomfloor = request.args.get("roomfloor")

    if roomnum:
        sql = """update roominformation
                         set roomtypenum='%s',isempty='%s',roomfloor='%s'
                         where roomnum='%s'
              """ % (roomtypenum, isempty, roomfloor, roomnum)
        ConnectMysql(sql)
        return jsonify({
            "roomnum": roomnum,
            "roomtypenum": roomtypenum,
            "isempty": isempty,
            "roomfloor": roomfloor,
            "status": True
        })
    else:
        return Error()

@app.route("/Room/Delete")
def DelteRoom():
    roomnum = request.args.get("roomnum")

    if roomnum:
        sql = "delete from roominformation where roomnum='%s'" % roomnum
        ConnectMysql(sql)
        return jsonify({
            "roomnum": roomnum,
            "status": True
        })
    else:
        return Error()

@app.route("/Room/Get")
def GetRoom():
    sql = "select * from roominformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "roomnum": type[0], "roomtypenum": type[1],
                     "isempty": type[2], "roomfloor": type[3]})
        list.append(item)
    return jsonify({
        "Room": list,
        "status": True
    })

#消费信息相关操作
@app.route("/Bill/Add")
def AddBill():
    goodsnum = request.args.get("goodsnum")
    idcard = request.args.get("idcard")
    quantity = request.args.get("quantity")

    sql1 = "select goodsquantity,goodsprice from goodsinformation where goodsnum='%s'"%goodsnum
    res = ConnectMysql(sql1)
    if res.__len__() == 0:
        return Error()
    elif goodsnum:
        total = res[1] * quantity
        today = strftime("%Y-%m-%d", localtime())
        sql2 = """insert into
                 billinformation(goodsnum, idcard, quantity)
                 values('%s', '%s', '%s')
              """%(goodsnum, idcard, quantity)
        sql3 = "update goodsinformation set goodsquantity='%s' where goodsnum='%s'"%(res[0]-quantity,goodsnum)
        sql4 = """insert into payinformation(idcard, paytime, total)
                          value('%s', '%s', '%s')
                """%(idcard, today, total)
        ConnectMysql(sql2)
        ConnectMysql(sql3)
        ConnectMysql(sql4)
        return jsonify({
            "goodsnum": goodsnum,
            "idcard": idcard,
            "quantity": quantity,
            "status": True
        })
    else:
        return Error()

@app.route("/Bill/Modify")
def ModifyBill():
    goodsnum = request.args.get("goodsnum")
    idcard = request.args.get("idcard")
    quantity = request.args.get("quantity")

    if goodsnum:
        sql = """update billinformation
                         set idcard='%s',quantity='%s'
                         where goodsnum='%s'
              """ % (idcard, quantity, goodsnum)
        ConnectMysql(sql)
        return jsonify({
            "goodsnum": goodsnum,
            "idcard": idcard,
            "quantity": quantity,
            "status": True
        })
    else:
        return Error()

@app.route("/Bill/Delete")
def Deltebill():
    goodsnum = request.args.get("goodsnum")

    if goodsnum:
        sql = "delete from billinformation where goodsnum='%s'" % goodsnum
        ConnectMysql(sql)
        return jsonify({
            "goodsnum": goodsnum,
            "status": True
        })
    else:
        return Error()

@app.route("/Bill/Get")
def Getbill():
    sql = "select * from billinformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "goodsnum": type[0], "idcard": type[1],
                     "quantity": type[2]})
        list.append(item)
    return jsonify({
        "Room": list,
        "status": True
    })


#获得所有可预定的房间
@app.route("/Tenant/Get")
def GetTenant():
    sql = """select roomnum, roomtype, roomprice, roomquantity, roomdescribe, roomfloor
             from roominformation, roomtypeinformation
             where roomquantity>0 and roomtypeinformation.roomtypenum=roominformation.roomtypenum
             and isempty=1
          """
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "roomnum": type[0], "roomtype": type[1], "roomprice": type[2],
                     "roomquantity": type[3], "roomdescribe": type[4], "roomfloor": type[5]})
        list.append(item)
    return jsonify({
        "CanBookRoom": list,
        "status": True
    })


#预定房间
@app.route("/Tenant/Book")
def BookTenant():
    idcard = request.args.get("idcard")
    stayroom = request.args.get("stayroom")
    tenantname = request.args.get("tenantname")
    tenantsex = request.args.get("tenantsex")
    checkin = request.args.get("checkin")
    checkout = request.args.get("checkout")

    if idcard and stayroom:
        # 一张idcard只能订一个房间
        sql0 = "select stayroom from tenantinformation where idcard='%s'"%idcard
        res0 = ConnectMysql(sql0)
        if res0.__len__() != 0:
            return Error()
        else:
            sql1 = "select isempty from roominformation where roomnum='%s'" % stayroom
            res = ConnectMysql(sql1)
            if res.__len__() == 0:
                return Error()
            elif res[0][0] == '1':
                sql2 = """insert into
                         tenantinformation(idcard, stayroom, tenantname, tenantsex, checkin, checkout)
                         values('%s', '%s', '%s', '%s', '%s', '%s')
                      """ % (idcard, stayroom, tenantname, tenantsex, checkin, checkout)
                ConnectMysql(sql2)
                sql3 = """update roominformation, roomtypeinformation 
                          set isempty='0',roomquantity=roomquantity-1
                          where roominformation.roomtypenum=roomtypeinformation.roomtypenum
                          and roomnum='%s'
                       """ % stayroom
                ConnectMysql(sql3)
                return jsonify({
                    "idcard": idcard,
                    "stayroom": stayroom,
                    "tenantname": tenantname,
                    "tenantsex": tenantsex,
                    "checkin": checkin,
                    "checkout": checkout,
                    "status": True
                })
            else:
                return Error()
    else:
        return Error()


#获得所有已预定的房间
@app.route("/Tenant/GetBook")
def GetBookTenant():
    nowtime = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sql = """select idcard, stayroom, tenantname, tenantsex, checkin, checkout
             from tenantinformation
             where datediff(checkin, '%s')>0
          """%nowtime
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "idcard": type[0], "stayroom": type[1], "tenantname": type[2],
                     "tenantname": type[3], "checkin": type[4], "checkout": type[5]})
        list.append(item)
    return jsonify({
        "BookRoom": list,
        "status": True
    })


#住的房间和idcard是改不了的 房间在另外一个部分转出
#修改住房信息
@app.route("/Tenant/Modify")
def ModifyTenant():
    idcard = request.args.get("idcard")
    tenantname = request.args.get("tenantname")
    tenantsex = request.args.get("tenantsex")
    checkin = request.args.get("checkin")
    checkout = request.args.get("checkout")
    if idcard:
        sql = """update tenantinformation
                 set tenantname='%s',tenantsex='%s',checkin='%s',checkout='%s'
                 where idcard='%s'
              """%(tenantname, tenantsex, checkin, checkout, idcard)
        ConnectMysql(sql)
        return jsonify({
                "idcard": idcard,
                "tenantname": tenantname,
                "tenantsex": tenantsex,
                "checkin": checkin,
                "checkout": checkout,
                "status": True
            })
    else:
        Error()


#一张idcard只能订一个房间
#删除预定信息
@app.route("/Tenant/Delete")
def DeleteTenant():
    idcard = request.args.get("idcard")
    if idcard:
        sql1 = "select stayroom from tenantinformation where idcard='%s'"%idcard
        res = ConnectMysql(sql1)
        if res.__len__() == 0:
            return Error()
        else:
            roomnum = res[0][0]
            sql2 = """update roominformation, roomtypeinformation 
                      set isempty='1',roomquantity=roomquantity+1
                      where roominformation.roomtypenum=roomtypeinformation.roomtypenum
                      and roomnum='%s'
                   """%roomnum
            ConnectMysql(sql2)
            sql3 = "delete from tenantinformation where idcard='%s'"%idcard
            ConnectMysql(sql3)
            return jsonify({
                "idcard": idcard,
                "status": True
            })
    else:
        return Error()


#今天登记入住
@app.route("/Tenant/Checkin")
def CheckinTenanet():
    idcard = request.args.get("idcard")
    stayroom = request.args.get("stayroom")
    tenantname = request.args.get("tenantname")
    tenantsex = request.args.get("tenantsex")
    checkin = strftime("%Y-%m-%d %H:%M:%S", localtime())
    checkout = request.args.get("checkout")
    print(checkin)

    if idcard and stayroom:
        # 一张idcard只能订一个房间
        sql0 = "select stayroom from tenantinformation where idcard='%s'"%idcard
        res0 = ConnectMysql(sql0)
        if res0.__len__() != 0:
            return Error()
        else:
            sql1 = "select isempty from roominformation where roomnum='%s'" % stayroom
            res = ConnectMysql(sql1)
            if res.__len__() == 0:
                return Error()
            elif res[0][0] == '1':
                sql2 = """insert into
                         tenantinformation(idcard, stayroom, tenantname, tenantsex, checkin, checkout)
                         values('%s', '%s', '%s', '%s', '%s', '%s')
                      """ % (idcard, stayroom, tenantname, tenantsex, checkin, checkout)
                ConnectMysql(sql2)
                sql3 = """update roominformation, roomtypeinformation 
                          set isempty='0',roomquantity=roomquantity-1
                          where roominformation.roomtypenum=roomtypeinformation.roomtypenum
                          and roomnum='%s'
                       """ % stayroom
                ConnectMysql(sql3)
                return jsonify({
                    "idcard": idcard,
                    "stayroom": stayroom,
                    "tenantname": tenantname,
                    "tenantsex": tenantsex,
                    "checkin": checkin,
                    "checkout": checkout,
                    "status": True
                })
            else:
                return Error()
    else:
        return Error()


#入住预定的单子可以从前面的预定信息的返回里得到


#获取所有的住客信息
@app.route("/Tenant/GetAll")
def GetAllTenant():
    sql = "select * from tenantinformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "idcard": type[0], "stayroom": type[1], "tenantname": type[2],
                     "tenantname": type[3], "checkin": type[4], "checkout": type[5]})
        list.append(item)
    return jsonify({
        "AllTenant": list,
        "status": True
    })


#换房间
@app.route("/Tenant/ChangeRoom")
def ChangeRoomTenant():
    idcard = request.args.get("idcard")
    changeroom = request.args.get("changeroom")
    if idcard and changeroom:
        sql1 = "select stayroom from tenantinformation where idcard='%s'"%idcard
        res1 = ConnectMysql(sql1)
        if res1.__len__() == 1:
            stayroom = res1[0][0]
            sql2 = "select isempty from roominformation where roomnum='%s'"%changeroom
            res2 = ConnectMysql(sql2)
            if res2.__len__() == 0:
                return Error()
            elif res2[0][0] == "1":
                sql3 = "update tenantinformation set stayroom='%s' where idcard='%s'"\
                       %(changeroom, idcard)
                ConnectMysql(sql3)
                sql4 = """update roominformation, roomtypeinformation
                          set isempty=1, roomquantity=roomquantity+1
                          where roominformation.roomtypenum=roomtypeinformation.roomtypenum
                          and roomnum='%s'
                       """%stayroom
                ConnectMysql(sql4)
                sql5 ="""update roominformation, roomtypeinformation
                         set isempty=0, roomquantity=roomquantity-1
                         where roominformation.roomtypenum=roomtypeinformation.roomtypenum
                         and roomnum='%s'
                      """%changeroom
                ConnectMysql(sql5)
                return jsonify({
                    "idcard": idcard,
                    "oldroom": stayroom,
                    "newroom": changeroom,
                    "status": True
                })
            else:
                return Error()
        else:
            return Error()
    else:
        return Error()


@app.route("/Tenant/Pay")
def PayTenant():
    idcard = request.args.get("idcard")
    if idcard:
        sql1 = "select datediff(checkout, checkin)+1 from tenantinformation where idcard='%s'"%idcard
        res1 = ConnectMysql(sql1)
        if res1.__len__() == 0:
            return Error()
        elif res1[0][0] > 0:
            day = res1[0][0]
            sql2 = """select roomprice from tenantinformation, roominformation, roomtypeinformation
                      where idcard = '%s' and roomnum = stayroom
                      and roominformation.roomtypenum = roomtypeinformation.roomtypenum
                   """%idcard
            res2 = ConnectMysql(sql2)
            if res2.__len__() == 0:
                return Error()
            elif res2[0][0] > 0:
                money = res2[0][0]
                total = day * money
                today = strftime("%Y-%m-%d", localtime())
                sql3 = """insert into payinformation(idcard, paytime, total)
                          value('%s', '%s', '%s')
                       """%(idcard, today, total)
                ConnectMysql(sql3)
                return jsonify({
                    "idcard": idcard,
                    "day": day,
                    "money": money,
                    "total": total,
                    "status": True
                })
            else:
                return Error()
        else:
            return Error()
    else:
        return Error()


#一段时间的入住等报表
@app.route("/Report/LongTime")
def LongTimeReport():
    beginday = request.args.get("beginday")
    endday = request.args.get("endday")
    if beginday and endday:
        sql = """select * from tenantinformation where datediff(checkin, '%s')+1>0
                 and datediff('%s', checkout)+1>0
              """ % (beginday, endday)
        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "idcard": type[0], "stayroom": type[1], "tenantname": type[2],
                         "tenantname": type[3], "checkin": type[4], "checkout": type[5]})
            list.append(item)
        return jsonify({
            "BookRoom": list,
            "status": True
        })
    else:
        return Error()


#当日入住和离开
@app.route("/Report/Day")
def DayReport():
    totay = strftime("%Y-%m-%d", localtime())
    sql1 = "select * from tenantinformation where checkin like '%%%s%%'"%totay
    res1 = ConnectMysql(sql1)
    if res1.__len__() > 0:
        list1 = []
        for num, type in enumerate(res1):
            item = dict({"index": num, "idcard": type[0], "stayroom": type[1], "tenantname": type[2],
                         "tenantname": type[3], "checkin": type[4], "checkout": type[5]})
            list1.append(item)
    else:
        return Error()

    sql2 = "select * from tenantinformation where checkout like '%%%s%%'"%totay
    res2 = ConnectMysql(sql2)
    if res2.__len__() > 0:
        list2 = []
        for num, type in enumerate(res2):
            item = dict({"index": num, "idcard": type[0], "stayroom": type[1], "tenantname": type[2],
                         "tenantname": type[3], "checkin": type[4], "checkout": type[5]})
            list2.append(item)
    else:
        return Error()

    return jsonify({
        "checkin": list1,
        "checkout": list2,
        "status": True
    })


#统一错误类型 后面可以改
def Error():
    return jsonify({"status": False})


if __name__ == '__main__':
    app.run()
