from flask import Flask, request, jsonify
import pymysql
from time import strftime, localtime

app = Flask(__name__)


# 数据库操作
def ConnectMysql(sql):
    connect = pymysql.connect("localhost", "root", "123456", "hotel")
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


# 管理员登录
@app.route("/Login", methods=["post"])
def AdministratorLogin():
    adminnum = request.args.get("adminnum")
    adminpassword = request.args.get("adminpassword")

    if adminnum and adminpassword:
        sql = "select * from administratorinformation where adminnum='%s'" % adminnum
        res = ConnectMysql(sql)
        if res[1] == adminpassword:
            td = strftime("%Y-%m-%d %H:%M:%S", localtime())
            sss = "管理员登录"
            sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
            ConnectMysql(sqlr)
            return jsonify({"adminnum": adminnum,
                            "adminpassword": adminpassword,
                            "status": True
                            })
        else:
            return Error()

    else:
        return Error()


# 获得所有房间类型
@app.route("/RoomType/Get")
def GetRoomType():
    sql = "select * from roomtypeinformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "roomtypenum": type[0], "roomtype": type[1],
                     "roomprice": type[2], "roomquantity": type[3], "roomdescribe": type[4]})
        list.append(item)
    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sss = "所有房间类型获取"
    sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
    ConnectMysql(sqlr)
    return jsonify({
        "RoomType": list,
        "status": True
    })


# 增加房间类型
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
              """ % (roomtypenum, roomtype, roomprice, roomquantity, roomdescribe)
        ConnectMysql(sql)
        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "房间类型增加"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)
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


# 修改指定roomtypenum的房间类型
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
              """ % (roomtype, roomprice, roomquantity, roomdescribe, roomtypenum)
        ConnectMysql(sql)
        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "房间类型被修改"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)
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


# 删除指定的roomtypenum的房间类型
@app.route("/RoomType/Delete")
def DeleteRoomType():
    roomtypenum = request.args.get("roomtypenum")

    if roomtypenum:
        sql1 = "delete from roominformation where roomtypenum='%s'" % roomtypenum
        ConnectMysql(sql1)
        sql2 = "delete from roomtypeinformation where roomtypenum='%s'" % roomtypenum
        ConnectMysql(sql2)
        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "房间类型被删除"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)
        return jsonify({
            "roomtypenum": roomtypenum,
            "status": True
        })
    else:
        return Error()


# 关键词查询房间类型
@app.route("/RoomType/KeyGet")
def KeyGetRoomType():
    keyword = request.args.get("keyword")

    if keyword:
        sql = """select * from roomtypeinformation
                 where roomtypenum='%s' or roomtype='%s' or roomdescribe='%s'
              """ % (keyword, keyword, keyword)

        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "roomtypenum": type[0], "roomtype": type[1],
                         "roomprice": type[2], "roomquantity": type[3], "roomdescribe": type[4]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "房间类别关键词获取"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "RoomType": list,
            "status": True
        })
    else:
        sql = "select * from roomtypeinformation"
        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "roomtypenum": type[0], "roomtype": type[1],
                         "roomprice": type[2], "roomquantity": type[3], "roomdescribe": type[4]})
            list.append(item)
        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "所有房间类型获取"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)
        return jsonify({
            "RoomType": list,
            "status": True
        })


# 楼层信息相关操作
@app.route("/Floor/Add")
def AddFloor():
    floornum = request.args.get("floornum")
    floordescribe = request.args.get("floordescribe")
    # remainnum = request.args.get("remainnum")

    if floornum:
        sql = """insert into
                 floorinformation(floornum, floordescribe)
                 values('%s', '%s')
              """ % (floornum, floordescribe)
        ConnectMysql(sql)
        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "楼层信息添加"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)
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
    # remainnum = request.args.get("remainnum")

    if floornum:
        sql = """update floorinformation
                         set floordescribe='%s'
                         where floornum='%s'
                      """ % (floordescribe, floornum)
        ConnectMysql(sql)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "楼层信息修改"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "楼层信息被删除"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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

    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sss = "所有楼层信息获取"
    sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
    ConnectMysql(sqlr)

    return jsonify({
        "Floor": list,
        "status": True
    })


# 楼层信息关键词查询
@app.route("/Floor/KeyGet")
def KeyGetFloor():
    keyword = request.args.get("keyword")

    if keyword:
        sql = """select * from floorinformation
                 where floornum='%s' or floordescribe='%s'
              """ % (keyword, keyword)

        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "floornum": type[0], "floordescribe": type[1]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "楼层信息关键词获取"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "Floor": list,
            "status": True
        })
    else:
        sql = "select * from floorinformation"
        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "floornum": type[0], "floordescribe": type[1]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "所有楼层信息获取"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "Floor": list,
            "status": True
        })


# 商品信息相关操作
@app.route("/Goods/Add")
def AddGoods():
    goodsnum = request.args.get("goodsnum")
    goodsname = request.args.get("goodsname")
    goodstypenum = request.args.get("goodstypenum")
    goodsprice = request.args.get("goodsprice")
    goodsquantity = request.args.get("goodsquantity")

    if goodsnum:
        sql = """insert into
                 goodsinformation(goodsnum, goodsname, goodstypenum, goodsprice, goodsquantity)
                 values('%s', '%s', '%s', '%s', '%s')
              """ % (goodsnum, goodsname, goodstypenum, goodsprice, goodsquantity)
        ConnectMysql(sql)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "商品信息添加"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "goodsnum": goodsnum,
            "goodsname": goodsname,
            "goodstypenum": goodstypenum,
            "goodsprice": goodsprice,
            "goodsquantity": goodsquantity,
            "status": True
        })
    else:
        return Error()


@app.route("/Goods/Modify")
def ModifyGoods():
    goodsnum = request.args.get("goodsnum")
    goodsname = request.args.get("goodsname")
    goodstypenum = request.args.get("goodstypenum")
    goodsprice = request.args.get("goodsprice")
    goodsquantity = request.args.get("goodsquantity")

    if goodsnum:
        sql = """update goodsinformation
                         set goodsname='%s',goodstypenum='%s',goodsprice='%s',goodsquantity='%s'
                         where goodsnum='%s'
              """ % (goodsname, goodstypenum, goodsprice, goodsquantity, goodsnum)
        ConnectMysql(sql)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "商品信息修改"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "goodsnum": goodsname,
            "goodsname": goodstypenum,
            "goodstypenum": goodsprice,
            "goodsprice": goodsquantity,
            "goodsquantity": goodsnum,
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

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "商品信息删除"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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
        item = dict({"index": num, "goodsnum": type[0], "goodsname": type[1],
                     "goodstypenum": type[2], "goodsprice": type[3], "goodsquantity": type[4]})
        list.append(item)

    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sss = "所有商品信息获取"
    sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
    ConnectMysql(sqlr)

    return jsonify({
        "Goods": list,
        "status": True
    })


# 关键词查询商品信息
@app.route("/Goods/KeyGet")
def KeyGetGoods():
    keyword = request.args.get("keyword")

    if keyword:
        #        sql = """SELECT goodsnum,goodsname,goodsinformation.goodstypenum,goodsprice,goodsquantity
        #                 FROM goodsinformation,goodstypeinformation
        #                 WHERE goodsinformation.goodstypenum=goodstypeinformation.goodstypenum
        #                 AND (goodstype='%s' or goodsnum='%s' or goodsname='%s' or goodsinformation.goodstypenum='%s')
        #              """%(keyword, keyword, keyword, keyword)
        sql1 = "select * from goodsinformation where goodsnum='%s' or goodsname='%s' or goodstypenum='%s'" % (
        keyword, keyword, keyword)
        res = ConnectMysql(sql1)
        print(res)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "goodsnum": type[0], "goodsname": type[1],
                         "goodstypenum": type[2], "goodsprice": type[3], "goodsquantity": type[4]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "关键词查询商品信息"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "Goods": list,
            "status": True
        })
    else:
        sql = "select * from goodsinformation"
        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "goodsnum": type[0], "goodsname": type[1],
                         "goodstypenum": type[2], "goodsprice": type[3], "goodsquantity": type[4]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "所有商品信息获取"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "Goods": list,
            "status": True
        })


# 商品类别相关操作
@app.route("/GoodsType/Add")
def AddGoodsType():
    goodstypenum = request.args.get("goodstypenum")
    goodstype = request.args.get("goodstype")
    typedescribe = request.args.get("typedescribe")

    if goodstypenum:
        sql = """insert into
                 goodstypeinformation(goodstypenum, goodstype, typedescribe)
                 values('%s', '%s', '%s')
              """ % (goodstypenum, goodstype, typedescribe)
        ConnectMysql(sql)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "商品类别信息添加"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "商品类别信息修改"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "商品类别信息删除"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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

    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sss = "所有商品类别获取"
    sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
    ConnectMysql(sqlr)

    return jsonify({
        "GoodsType": list,
        "status": True
    })


# 商品类型信息的关键词查询
@app.route("/GoodsType/KeyGet")
def KeyGetGoodsType():
    keyword = request.args.get("keyword")

    if keyword:
        sql = """select * from goodstypeinformation
                 where goodstypenum='%s' or goodstype='%s' or typedescribe='%s'
              """ % (keyword, keyword, keyword)
        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "goodstypenum": type[0], "goodstype": type[1],
                         "typedescribe": type[2]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "关键词查询商品类型信息"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "GoodsType": list,
            "status": True
        })
    else:
        sql = "select * from goodstypeinformation"
        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "goodstypenum": type[0], "goodstype": type[1],
                         "typedescribe": type[2]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "所有商品类别获取"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "GoodsType": list,
            "status": True
        })


# 会员信息相关操作
@app.route("/Vip/Add")
def AddVip():
    vipnum = request.args.get("vipnum")
    idcard = request.args.get("idcard")
    vipname = request.args.get("vipname")
    vipsex = request.args.get("vipsex")
    vipemail = request.args.get("vipemail")
    vipphone = request.args.get("vipphone")

    if vipnum:
        registertime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sql = """insert into
                 vipinformation(vipnum, idcard, vipname, vipsex,vipemail,registertime,vipphone)
                 values('%s', '%s', '%s', '%s', '%s', '%s', '%s')
              """ % (vipnum, idcard, vipname, vipsex, vipemail, registertime, vipphone)
        ConnectMysql(sql)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "vip用户添加"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "vipnum": vipnum,
            "idcard": idcard,
            "vipname": vipname,
            "vipsex": vipsex,
            "vipemail": vipemail,
            "registertime": registertime,
            "vipphone": vipphone,
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
    vipemail = request.args.get("vipemail")
    registertime = strftime("%Y-%m-%d %H:%M:%S", localtime())
    vipphone = request.args.get("vipphone")

    if vipnum:
        sql = """update vipinformation
                         set idcard='%s',vipname='%s',vipsex='%s',vipemail='%s',registertime='%s',vipphone='%s'
                         where vipnum='%s'
              """ % (idcard, vipname, vipsex, vipemail, registertime, vipphone, vipnum)
        ConnectMysql(sql)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "vip用户信息修改"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "vipnum": vipnum,
            "idcard": idcard,
            "vipname": vipname,
            "vipsex": vipsex,
            "vipemail": vipemail,
            "registertime": registertime,
            "vipphone": vipphone,
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

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "vip用户信息删除"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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
                     "vipname": type[2], "vipsex": type[3], "vipemail": type[4],
                     "registertime": type[5], "vipphone": type[6]})
        list.append(item)

    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sss = "vip用户所有信息获取"
    sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
    ConnectMysql(sqlr)

    return jsonify({
        "Vip": list,
        "status": True
    })


# 根据会员号查找会员信息
@app.route("/Vip/NumGet")
def NumGetVip():
    vipnum = request.args.get("vipnum")

    if vipnum:
        sql = "select * from vipinformation where vipnum='%s'" % vipnum
        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "vipnum": type[0], "idcard": type[1],
                         "vipname": type[2], "vipsex": type[3], "vipemail": type[4],
                         "registertime": type[5], "vipphone": type[6]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "会员号查询会员信息"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "Vip": list,
            "status": True
        })
    else:
        return Error()


# 员工信息相关操作
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
              """ % (employeenum, employeemail, employeepassword, employeename, employeesex)
        ConnectMysql(sql)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "员工信息添加"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "员工信息修改"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "员工信息删除"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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

    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sss = "所有员工信息获取"
    sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
    ConnectMysql(sqlr)

    return jsonify({
        "Employee": list,
        "status": True
    })


# 根据员工编号或姓名查找员工信息
@app.route("/Employee/NumGet")
def NumGetEmployee():
    employeenumOrname = request.args.get("employeenumOrname")

    if employeenumOrname:
        sql1 = "select * from employeeinfromation where employeenum='%s'" % employeenumOrname
        sql2 = "select * from employeeinfromation where employeename='%s'" % employeenumOrname
        res1 = ConnectMysql(sql1)
        res2 = ConnectMysql(sql2)
        if res1:
            res = res1
        else:
            res = res2
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "employeenum": type[0], "employeemail": type[1],
                         "employeepassword": type[2], "employeename": type[3], "employeesex": type[4]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "员工编号或姓名查找员工信息"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "Employee": list,
            "status": True
        })
    else:
        return Error()


# 客房信息相关操作
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
              """ % (roomnum, roomtypenum, isempty, roomfloor)
        ConnectMysql(sql)
        sql1 = """update roomtypeinformation
                  set roomquantity=roomquantity+1
                  where roomtypenum='%s'
               """%roomtypenum
        ConnectMysql(sql1)
        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "客房信息添加"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "客房信息修改"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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
        sql0 = "select roomtypenum from roominformation where roomnum='%s'"%roomnum
        res = ConnectMysql(sql0)
        if res.__len__() == 0:
            return Error()
        elif res.__len__() == 1:
            roomtypenum = res[0][0]
            sql1 = """update roomtypeinformation
                      set roomquantity=roomquantity-1
                      where roomtypenum='%s'
                   """ % roomtypenum
            ConnectMysql(sql1)
        else:
            return Error()

        sql1 = "delete from roominformation where roomnum='%s'"%roomnum
        ConnectMysql(sql1)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "客房信息删除"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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

    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sss = "所有客房信息获取"
    sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
    ConnectMysql(sqlr)

    return jsonify({
        "Room": list,
        "status": True
    })


# 关键词查询房间信息
@app.route("/Room/KeyGet")
def KeyGetRoom():
    keyword = request.args.get("keyword")

    if keyword:
        print("hello")
        #        sql = """SELECT roomnum,roominformation.roomtypenum,isempty,roomfloor
        #                 from roomtypeinformation,roominformation
        #                 where roomtypeinformation.roomtypenum=roominformation.roomtypenum
        #                 and (roomtype='%s' or roomnum='%s' or roominformation.roomtypenum='%s' or isempty='%s' or roomfloor='%s')
        #                  """ % (keyword, keyword, keyword,keyword,keyword)
        sql1 = """select * from roominformation 
                  where roomnum='%s' or roomtypenum='%s' or isempty='%s' or roomfloor='%s'
               """ % (keyword, keyword, keyword, keyword)
        res = ConnectMysql(sql1)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "roomnum": type[0], "roomtypenum": type[1],
                         "isempty": type[2], "roomfloor": type[3]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "客房信息关键词获取"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "Room": list,
            "status": True
        })
    else:
        sql = "select * from roominformation"
        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "roomnum": type[0], "roomtypenum": type[1],
                         "isempty": type[2], "roomfloor": type[3]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "所有客房信息获取"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "Room": list,
            "status": True
        })


# 消费信息相关操作
@app.route("/Bill/Add")
def AddBill():
    goodsnum = request.args.get("goodsnum")
    idcard = request.args.get("idcard")
    quantitystr = request.args.get("quantity")
    quantity = float(quantitystr)

    if goodsnum and idcard:
        sql1 = "select goodsquantity,goodsprice from goodsinformation where goodsnum='%s'" % goodsnum
        res = ConnectMysql(sql1)
        if res.__len__() == 0:
            return Error()

        sql5 = "select * from payinformation where idcard='%s'" % idcard
        res5 = ConnectMysql(sql5)
        if res5.__len__() == 0:
            sql6 = "insert into payinformation(idcard) value ('%s')" % idcard
            ConnectMysql(sql6)

        summoney = res[0][1] * float(quantity)
        today = strftime("%Y-%m-%d %H:%M:%S", localtime())

        sql9 = "select quantity,summoney from billinformation where goodsnum='%s' and idcard='%s'" % (goodsnum, idcard)
        res9 = ConnectMysql(sql9)
        if res9:
            sql10 = ("update billinformation set quantity='%s',summoney='%s' where goodsnum='%s' and idcard='%s'"
                     % (res9[0][0] + quantity, res9[0][1] + summoney, goodsnum, idcard))
            ConnectMysql(sql10)
        else:
            sql2 = """insert into
                     billinformation(goodsnum, idcard, quantity,summoney)
                     values('%s', '%s', '%s', '%s')
                  """ % (goodsnum, idcard, quantity, summoney)
            ConnectMysql(sql2)
        sql3 = "update goodsinformation set goodsquantity='%s' where goodsnum='%s'" % (res[0][0] - quantity, goodsnum)
        ConnectMysql(sql3)

        # sql7 = "select sum(summoney) from billinformation where idcard='%s'"%idcard
        # res7 = ConnectMysql(sql7)
        # sql8 = "select total from payinformation where idcard='%s'"%idcard
        # res8=ConnectMysql(sql8)
        # sql4 = "update payinformation set paytime='%s',total='%s' where idcard='%s'"%(today, (res8[0][0] if res8[0][0] is not None else 0) +summoney, idcard)
        sql4 = "insert into payinformation(idcard,paytime,total) value('%s','%s','%s')" % (idcard, today, summoney)
        ConnectMysql(sql4)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "账单信息添加"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "goodsnum": goodsnum,
            "idcard": idcard,
            "quantity": quantity,
            "summoney": summoney,
            "status": True
        })
    else:
        return Error()


@app.route("/Bill/Modify")
def ModifyBill():
    goodsnum = request.args.get("goodsnum")
    idcard = request.args.get("idcard")
    quantity = request.args.get("quantity")

    if goodsnum and idcard:

        sql1 = "select goodsquantity,goodsprice from goodsinformation where goodsnum='%s'" % goodsnum
        res = ConnectMysql(sql1)
        if res.__len__() == 0:
            return Error()

        sql5 = "select * from payinformation where idcard='%s'" % idcard
        res5 = ConnectMysql(sql5)
        if res5.__len__() == 0:
            sql6 = "insert into payinformation(idcard) value ('%s')" % idcard
            ConnectMysql(sql6)

        summoney = res[0][1] * float(quantity)
        today = strftime("%Y-%m-%d %H:%M:%S", localtime())

        sql2 = """update billinformation
                    set summoney='%s',quantity='%s'
                    where goodsnum='%s',idcard='%s'
                """ % (summoney, quantity, goodsnum, idcard)
        sql3 = "update goodsinformation set goodsquantity='%s' where goodsnum='%s'" % (res[0][0] - quantity, goodsnum)
        ConnectMysql(sql2)
        ConnectMysql(sql3)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "账单信息修改"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "goodsnum": goodsnum,
            "idcard": idcard,
            "quantity": quantity,
            "summoney": summoney,
            "status": True
        })
    else:
        return Error()


@app.route("/Bill/Delete")
def DeleteBill():
    goodsnum = request.args.get("goodsnum")
    idcard = request.args.get("idcard")

    if goodsnum:
        sql = "delete from billinformation where goodsnum='%s' and idcard='%s'" % (goodsnum, idcard)
        ConnectMysql(sql)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "账单信息删除"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "goodsnum": goodsnum,
            "idcard": idcard,
            "status": True
        })
    else:
        return Error()


# 所有账单获取
@app.route("/Bill/Get")
def GetBill():
    sql = "select * from billinformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "goodsnum": type[0], "idcard": type[1],
                     "quantity": type[2], "summoney": type[3]})
        list.append(item)

    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sss = "所有账单信息获取"
    sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
    ConnectMysql(sqlr)

    return jsonify({
        "Room": list,
        "status": True
    })


# 关键词获取账单
@app.route("/Bill/KeyGet")
def KeyGetBill():
    keyword = request.args.get("keyword")
    if keyword:
        sql = "select * from billinformation where goodsnum ='%s' or idcard = '%s'" % (keyword, keyword)
        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "goodsnum": type[0], "idcard": type[1],
                         "quantity": type[2], "summoney": type[3]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "账单信息关键词获取"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "Room": list,
            "status": True
        })
    else:
        sql = "select * from billinformation"
        res = ConnectMysql(sql)
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "goodsnum": type[0], "idcard": type[1],
                         "quantity": type[2], "summoney": type[3]})
            list.append(item)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "所有账单信息获取"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "Room": list,
            "status": True
        })


# 获得所有可预定的房间
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

    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sss = "可预订房间获取"
    sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
    ConnectMysql(sqlr)

    return jsonify({
        "CanBookRoom": list,
        "status": True
    })


# 预定房间
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
        sql0 = "select stayroom from tenantinformation where idcard='%s'" % idcard
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

                td = strftime("%Y-%m-%d %H:%M:%S", localtime())
                sss = "预定房间"
                sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
                ConnectMysql(sqlr)

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


# 获得所有已预定的房间
@app.route("/Tenant/GetBook")
def GetBookTenant():
    nowtime = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sql = """select idcard, stayroom, tenantname, tenantsex, checkin, checkout
             from tenantinformation
             where datediff(checkin, '%s')>0
          """ % nowtime
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "idcard": type[0], "stayroom": type[1], "tenantname": type[2],
                     "tenantsex": type[3], "checkin": type[4], "checkout": type[5]})
        list.append(item)

    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sss = "获得已预定的所有房间"
    sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
    ConnectMysql(sqlr)

    return jsonify({
        "BookRoom": list,
        "status": True
    })


# 住的房间和idcard是改不了的 房间在另外一个部分转出
# 修改住房信息
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
              """ % (tenantname, tenantsex, checkin, checkout, idcard)
        ConnectMysql(sql)

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "修改住房信息"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

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


# 一张idcard只能订一个房间
# 删除预定信息
@app.route("/Tenant/Delete")
def DeleteTenant():
    idcard = request.args.get("idcard")
    if idcard:
        sql1 = "select stayroom from tenantinformation where idcard='%s'" % idcard
        res = ConnectMysql(sql1)
        if res.__len__() == 0:
            return Error()
        else:
            roomnum = res[0][0]
            sql2 = """update roominformation, roomtypeinformation 
                      set isempty='1',roomquantity=roomquantity+1
                      where roominformation.roomtypenum=roomtypeinformation.roomtypenum
                      and roomnum='%s'
                   """ % roomnum
            ConnectMysql(sql2)
            sql3 = "delete from tenantinformation where idcard='%s'" % idcard
            ConnectMysql(sql3)

            td = strftime("%Y-%m-%d %H:%M:%S", localtime())
            sss = "删除预定信息"
            sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
            ConnectMysql(sqlr)

            return jsonify({
                "idcard": idcard,
                "status": True
            })
    else:
        return Error()


@app.route("/Tenant/CheckinA")
def CheckinATenant():
    idcard = request.args.get("idcard")
    checkin = strftime("%Y-%m-%d %H:%M:%S", localtime())
    if idcard:
        sql = """update tenantinformation
                 set checkin='%s'
                 where idcard='%s'
              """ % (checkin, idcard)
        ConnectMysql(sql)
        return jsonify({
            "idcard": idcard,
            "checkin": checkin,
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

    if idcard and stayroom:
        # 一张idcard只能订一个房间
        sql0 = "select stayroom from tenantinformation where idcard='%s'" % idcard
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

                td = strftime("%Y-%m-%d %H:%M:%S", localtime())
                sss = "今天登记入住"
                sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
                ConnectMysql(sqlr)
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



# 入住预定的单子可以从前面的预定信息的返回里得到


# 获取所有的住客信息
@app.route("/Tenant/GetAll")
def GetAllTenant():
    sql = "select * from tenantinformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "idcard": type[0], "stayroom": type[1], "tenantname": type[2],
                     "tenantsex": type[3], "checkin": type[4], "checkout": type[5]})
        list.append(item)

    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
    sss = "获取所有的住客信息"
    sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
    ConnectMysql(sqlr)

    return jsonify({
        "AllTenant": list,
        "status": True
    })


# 换房间
@app.route("/Tenant/ChangeRoom")
def ChangeRoomTenant():
    idcard = request.args.get("idcard")
    changeroom = request.args.get("changeroom")
    if idcard and changeroom:
        sql1 = "select stayroom from tenantinformation where idcard='%s'" % idcard
        res1 = ConnectMysql(sql1)
        if res1.__len__() == 1:
            stayroom = res1[0][0]
            sql2 = "select isempty from roominformation where roomnum='%s'" % changeroom
            res2 = ConnectMysql(sql2)
            if res2.__len__() == 0:
                return Error()
            elif res2[0][0] == "1":
                sql3 = "update tenantinformation set stayroom='%s' where idcard='%s'" \
                       % (changeroom, idcard)
                ConnectMysql(sql3)
                sql4 = """update roominformation, roomtypeinformation
                          set isempty=1, roomquantity=roomquantity+1
                          where roominformation.roomtypenum=roomtypeinformation.roomtypenum
                          and roomnum='%s'
                       """ % stayroom
                ConnectMysql(sql4)
                sql5 = """update roominformation, roomtypeinformation
                         set isempty=0, roomquantity=roomquantity-1
                         where roominformation.roomtypenum=roomtypeinformation.roomtypenum
                         and roomnum='%s'
                      """ % changeroom
                ConnectMysql(sql5)

                td = strftime("%Y-%m-%d %H:%M:%S", localtime())
                sss = "换房间"
                sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
                ConnectMysql(sqlr)

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
        sql1 = "select datediff(checkout, checkin)+1 from tenantinformation where idcard='%s'" % idcard
        res1 = ConnectMysql(sql1)
        if res1.__len__() == 0:
            return Error()
        elif res1.__len__() > 0:
            day = res1[0][0]
            sql2 = """select roomprice from tenantinformation, roominformation, roomtypeinformation
                      where idcard = '%s' and roomnum = stayroom
                      and roominformation.roomtypenum = roomtypeinformation.roomtypenum
                   """ % idcard
            res2 = ConnectMysql(sql2)
            if res2.__len__() == 0:
                return Error()
            elif res2.__len__() > 0:
                money = res2[0][0]
                total = day*money
                today = strftime("%Y-%m-%d %H:%M:%S", localtime())
                sql3 = """insert into payinformation(idcard, paytime, total)
                          value('%s', '%s', '%s')
                       """ % (idcard, today, total)
                ConnectMysql(sql3)

                sql4 = "select total from payinformation where idcard='%s'"%idcard
                res4 = ConnectMysql(sql4)
                if res4.__len__() == 0:
                    return Error()
                elif res4.__len__() > 0:
                    total1 = 0
                    for type in res4:
                        total1 += type[0]
                else:
                    return Error()

                td = strftime("%Y-%m-%d %H:%M:%S", localtime())
                sss = "房客账单付费"
                sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
                ConnectMysql(sqlr)
                sqla = "select stayroom from tenantinformation where idcard='%s'" % idcard
                resa = ConnectMysql(sqla)
                if resa.__len__() == 0:
                    return Error()
                else:
                    roomnum = resa[0][0]
                    sqlb = """update roominformation, roomtypeinformation 
                              set isempty='1',roomquantity=roomquantity+1
                              where roominformation.roomtypenum=roomtypeinformation.roomtypenum
                              and roomnum='%s'
                           """ % roomnum
                    ConnectMysql(sqlb)
                    sqlb = "delete from tenantinformation where idcard='%s'" % idcard
                    ConnectMysql(sqlb)

                    td = strftime("%Y-%m-%d %H:%M:%S", localtime())
                return jsonify({
                    "idcard": idcard,
                    "day": day,
                    "money": money,
                    "total": total1,
                    "status": True
                })
            else:
                return Error()
        else:
            return Error()
    else:
        return Error()


@app.route("/Tenant/GetByid")
def GetByidTenant():
    idcard = request.args.get("idcard")
    sql = "select * from tenantinformation where idcard='%s'" % idcard
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "idcard": type[0], "stayroom": type[1], "tenantname": type[2],
                     "tenantsex": type[3], "checkin": type[4], "checkout": type[5]})
        list.append(item)
    return jsonify({
        "Tenant": list,
        "status": True
    })


# 一段时间的入住等报表
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

        td = strftime("%Y-%m-%d %H:%M:%S", localtime())
        sss = "一段时间的入住等报表查询"
        sqlr = "insert into loginformation(logdate,detail) value('%s','%s')" % (td, sss)
        ConnectMysql(sqlr)

        return jsonify({
            "BookRoom": list,
            "status": True
        })
    else:
        return Error()


# 当日入住和离开
@app.route("/Report/Checkin")
def CheckinReport():
    today = strftime("%Y-%m-%d", localtime())
    sql1 = "select * from tenantinformation where checkin like '%%%s%%'"%today
    res1 = ConnectMysql(sql1)
    if res1.__len__() > 0:
        list1 = []
        for num, type in enumerate(res1):
            item = dict({"index": num, "idcard": type[0], "stayroom": type[1], "tenantname": type[2],
                         "tenantsex": type[3], "checkin": type[4], "checkout": type[5]})
            list1.append(item)
        return jsonify({
            "checkin": list1,
            "status": True
        })
    else:
        return Error()


@app.route("/Report/Checkout")
def CheckoutReport():
    totay = strftime("%Y-%m-%d", localtime())
    sql = "select * from tenantinformation where checkout like '%%%s%%'"%totay
    res = ConnectMysql(sql)
    if res.__len__() > 0:
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "idcard": type[0], "stayroom": type[1], "tenantname": type[2],
                         "tenantsex": type[3], "checkin": type[4], "checkout": type[5]})
            list.append(item)
        return jsonify({
            "checkout": list,
            "status": True
        })
    else:
        return Error()


@app.route("/Report/Money")
def MoneyReport():
    totay = strftime("%Y-%m-%d", localtime())
    sss = "查询钱的报表"
    sql = "select * from payinformation where paytime like '%%%s%%'"%totay
    res = ConnectMysql(sql)
    sql1 = """insert into loginformation(totay, describe)
              value('%s', '%s')
           """ % (totay, sss)
    ConnectMysql(sql1)
    if res.__len__() > 0:
        list = []
        for num, type in enumerate(res):
            item = dict({"index": num, "idcard": type[0], "paytime": type[1], "total": type[2]})
            list.append(item)
    else:
        return Error()
    return jsonify({
        "money": list,
        "status": True
    })


# 获取日志信息
@app.route("/Log/Get")
def GetLog():
    sql = "select * from loginformation"
    res = ConnectMysql(sql)
    list = []
    for num, type in enumerate(res):
        item = dict({"index": num, "logdate": type[0], "detail": type[1]})
        list.append(item)
    return jsonify({
        "Log": list,
        "status": True
    })


# 统一错误类型 后面可以改
def Error():
    return jsonify({"status": False})


if __name__ == '__main__':
    app.run()