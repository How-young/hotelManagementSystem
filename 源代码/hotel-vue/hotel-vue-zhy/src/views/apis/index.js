import Axios from '@/assets/js/AxiosPlugin'

//查询商品信息
export const listGoods = () => {
  return Axios.get('/Goods/Get').then(res => res.data)
}

//修改商品信息
export const modifyGoods = (goodsnum, goodsname, goodstypenum, goodsprice, goodsquantity) => {
  return Axios.get('/Goods/Modify?goodsnum=' + goodsnum + '&goodsname=' + goodsname + '&goodstypenum=' +
  goodstypenum + '&goodsprice=' + goodsprice +'&goodsquantity=' + goodsquantity).then(res => res.data)
}


//增加商品信息
export const addGoods = (goodsnum, goodsname, goodstypenum, goodsprice, goodsquantity) => {
return Axios.get('/Goods/Add?goodsnum=' + goodsnum + '&goodsname=' + goodsname + '&goodstypenum=' +
goodstypenum + '&goodsprice=' + goodsprice +'&goodsquantity=' + goodsquantity).then(res => res.data)
}

//搜寻商品信息
export const searchGoods = (searchkey) => {
return Axios.get('/Goods/KeyGet?keyword=' + searchkey).then(res => res.data)
}

//删除商品信息
export const deleteGoods = (goodsnum) => {
return Axios.get('/Goods/Delete?goodsnum=' +  goodsnum).then(res => res.data)
}

//查询商品类别信息
export const listGoodsType = () => {
return Axios.get('/GoodsType/Get').then(res => res.data)
}

//修改商品类别信息
export const modifyGoodsType = (goodstypenum, goodstype, typedescribe) => {
return Axios.get('/GoodsType/Modify?goodstypenum=' + goodstypenum + '&goodstype=' + goodstype + '&typedescribe=' +
typedescribe).then(res => res.data)
}


//增加商品类别信息
export const addGoodsType = (goodstypenum, goodstype, typedescribe) => {
return Axios.get('/GoodsType/Add?goodstypenum=' + goodstypenum + '&goodstype=' + goodstype + '&typedescribe=' +
typedescribe).then(res => res.data)
}

//搜寻商品类别信息
export const searchGoodsType = (searchkey) => {
return Axios.get('/GoodsType/KeyGet?keyword=' + searchkey).then(res => res.data )
}

//删除商品类别信息
export const deleteGoodsType = (goodstypenum) => {
return Axios.get('/GoodsType/Delete?goodstypenum=' +  goodstypenum).then(res => res.data)
}

//查询客房信息
export const listRoom = () => {
return Axios.get('/Room/Get').then(res => res.data)
}

//修改客房信息
export const modifyRoom = (roomnum, roomtypenum, isempty, roomfloor) => {
return Axios.get('/Room/Modify?roomnum=' + roomnum + '&roomtypenum=' + roomtypenum + '&isempty=' +
isempty + '&roomfloor=' + roomfloor).then(res => res.data)
}


//增加客房信息
export const addRoom = (roomnum, roomtypenum, isempty, roomfloor) => {
return Axios.get('/Room/Add?roomnum=' + roomnum + '&roomtypenum=' + roomtypenum + '&isempty=' +
isempty + '&roomfloor=' + roomfloor)
}

//搜寻客房信息
export const searchRoom = (searchkey) => {
return Axios.get('/Room/KeyGet?keyword=' + searchkey).then(res => res.data )
}

//删除客房信息
export const deleteRoom = (roomnum) => {
return Axios.get('/Room/Delete?roomnum=' +  roomnum).then(res => res.data)
}

//查询客房类型信息
export const listRoomType = () => {
return Axios.get('/RoomType/Get').then(res => res.data)
}

//修改客房类型信息
export const modifyRoomType = (roomtypenum, roomtype, roomprice, roomquantity, roomdescribe) => {
return Axios.get('/RoomType/Modify?roomtypenum=' + roomtypenum + '&roomtype=' + roomtype + '&roomprice=' +
roomprice + '&roomquantity=' + roomquantity + '&roomdescribe=' + roomdescribe).then(res => res.data)
}


//增加客房类型信息
export const addRoomType = (roomtypenum, roomtype, roomprice, roomquantity, roomdescribe) => {
return Axios.get('/RoomType/Add?roomtypenum=' + roomtypenum + '&roomtype=' + roomtype + '&roomprice=' +
roomprice + '&roomquantity=' + roomquantity + '&roomdescribe=' + roomdescribe)
}

//搜寻客房类型信息
export const searchRoomType = (searchkey) => {
return Axios.get('/RoomType/KeyGet?keyword=' + searchkey).then(res => res.data )
}

//删除客房类型信息
export const deleteRoomType = (roomtypenum) => {
return Axios.get('/RoomType/Delete?roomtypenum=' +  roomtypenum).then(res => res.data)
}

//查询换房信息
export const listAllTenant = () => {
return Axios.get('/Tenant/GetAll').then(res => res.data)
}

//修改换房信息
export const changeRoomTenant = (idcard, stayroom, changeroom) => {
return Axios.get('/Tenant/ChangeRoom?idcard=' + idcard + '&stayroom=' + stayroom + '&changeroom=' +
changeroom ).then(res => res.data)
}

//搜寻换房信息
export const searchIdcard = (searchkey) => {
return Axios.get('/Tenant/GetByid?idcard=' + searchkey).then(res => res.data)
}

// 查询员工信息
export const listEmp = () => {
  return Axios.get('/Employee/Get').then(res => res.data)
}
// 搜索员工信息
export const searchEmp = (searchkey) => {
  return Axios.get('/Employee/NumGet?employeenumOrname=' + searchkey).then(res => res.data )
}
// 新增员工信息
export const addEmp = (employeenum, employeemail, employeepassword, employeename, employeesex) => {
  return Axios.get('/Employee/Add?employeenum=' + employeenum + '&employeemail=' + employeemail + '&employeepassword='
  + employeepassword + '&employeename=' + employeename + '&employeesex=' +employeesex).then(res => res.data)
}
// 删除员工信息
export const deleteEmp = (employeenum) => {
  return Axios.get('/Employee/Delete?employeenum=' +  employeenum).then(res => res.data)
}
// 修改员工信息
export const modifyEmp = (employeenum, employeemail, employeepassword, employeename, employeesex) => {
  return Axios.get('/Employee/Modify?employeenum=' + employeenum + '&employeemail=' + employeemail + '&employeepassword='
  + employeepassword + '&employeename=' + employeename + '&employeesex=' +employeesex).then(res => res.data)
}
// 获取当日入住，离店日志信息
export const listtodayCheckin = () => {
  return Axios.get('/Report/Checkin').then(res => res.data)
}
export const listtodayCheckout = () => {
  return Axios.get('/Report/Checkout').then(res => res.data)
}
//获取一段时间入住，离店信息
export const listCheckinCheckout = ( beginday , endday) => {
  return Axios.get('/Report/LongTime?beginday=' + beginday + '&endday=' + endday).then(res => res.data)
}
// 获取支付信息
export const listpay = () => {
  return Axios.get('/Report/Money').then(res => res.data)
}
// 获取所有可预定的房间信息
export const listbookavible = () => {
  return Axios.get('/Tenant/Get').then(res => res.data)
}
// 获取所有已预定的房间信息
export const listbookalready = () => {
  return Axios.get('/Tenant/GetBook').then(res => res.data)
}
// 预定新房间
export const bookavible = ( idcard,stayroom,tenantname,tenantsex,daterange) => {
  return Axios.get('/Tenant/Book?idcard=' + idcard + '&stayroom=' + stayroom
  + '&tenantname=' + tenantname + '&tenantsex='
  + tenantsex +'&checkin=' + daterange[0] + '&checkout=' + daterange[1]).then(res => res.data)
}
// 修改预定信息
export const editbookavible = ( idcard,tenantname,tenantsex,daterange) => {
  return Axios.get('/Tenant/Modify?idcard=' + idcard + '&tenantname=' + tenantname + '&tenantsex='
  + tenantsex +'&checkin=' + daterange[0] + '&checkout=' + daterange[1]).then(res => res.data)
}
// 删除预定信息
export const deletebook = (idcard) => {
  return Axios.get('/Tenant/Delete?idcard=' +  idcard).then(res => res.data)
}
// 获取所有账单
export const listbill = () => {
  return Axios.get('/Bill/Get').then(res => res.data)
}
// 修改账单信息
export const editbill = ( goodsnum,idcard,quantity) => {
  return Axios.get('/Tenant/Modify?goodsnum=' + goodsnum + '&idcard=' + idcard + '&quantity='
  + quantity).then(res => res.data)
}
// 新增账单信息
export const addbill = ( goodsnum,idcard,quantity) => {
  return Axios.get('/Bill/Add?goodsnum=' + goodsnum + '&idcard=' + idcard + '&quantity='
  + quantity).then(res => res.data)
}
// 删除订单信息
export const deletebill = (goodsnum , idcard) => {
  return Axios.get('/Bill/Delete?goodsnum=' +  goodsnum+ '&idcard=' + idcard).then(res => res.data)
}
// 搜索订单信息
export const searchbill = (searchkey) => {
  return Axios.get('/Bill/KeyGet?keyword=' + searchkey).then(res => res.data )
}


//查询会员信息
export const vipList = () => {
  return Axios.get('/Vip/Get').then(res => res.data)
}
// 搜索会员信息
export const searchVip = (searchkey) => {
  return Axios.get('/Vip/NumGet?vipnum=' + searchkey).then(res => res.data )
}
// 新增会员信息
export const addVip = (vipname, vipnum, idcard, vipsex, vipemail, vipphone) => {
  return Axios.get('/Vip/Add?vipnum=' + vipnum + '&vipname=' + vipname + '&idcard='
  + idcard + '&vipsex=' + vipsex + '&vipemail=' + vipemail
  + '&vipphone=' + vipphone).then(res => res.data)
}
// 删除会员信息
export const deleteVip = (vipnum) => {
  return Axios.get('/Vip/Delete?vipnum=' +  vipnum).then(res => res.data)
}
// 修改会员信息
export const modifyVip = (vipname, vipnum, idcard, vipsex, vipemail, vipphone, registertime) => {
  return Axios.get('/Vip/Modify?vipnum=' + vipnum + '&vipname=' + vipname + '&idcard='
  + idcard + '&vipsex=' + vipsex + '&vipemail=' + vipemail
  + '&vipphone=' + vipphone + '&registertime=' + registertime).then(res => res.data)
}

//查询楼层信息
export const floorList = () => {
  return Axios.get('/Floor/Get').then(res => res.data)
}
// 新增楼层信息
export const addFloor = (floornum, floordescribe) => {
  return Axios.get('/Floor/Add?floornum=' + floornum + '&floordescribe=' + floordescribe).then(res => res.data)
}
// 修改楼层信息
export const modifyFloor = (floornum, floordescribe) => {
  return Axios.get('/Floor/Modify?floornum=' + floornum + '&floordescribe=' + floordescribe).then(res => res.data)
}
// 删除楼层信息
export const deleteFloor = (floornum) => {
  return Axios.get('/Floor/Delete?floornum=' + floornum).then(res => res.data)
}

// 房客管理
export const listbook = () => {
  return Axios.get('/Tenant/GetBook').then(res => res.data)
}

export const checkBooking = (idcard) => {
  return Axios.get('/Tenant/CheckinA?idcard=' + idcard).then(res => res.data)
}
export const bookGetAll = () => {
  return Axios.get('/Tenant/GetAll').then(res => res.data)
}
export const deletebooking = (idcard) => {
  return Axios.get('/Tenant/Delete?idcard=' + idcard).then(res => res.data)
}

// 付款
export const pay = (idcard) => {
  return Axios.get('/Tenant/Pay?idcard=' + idcard).then(res => res.data)
}

export const check = (idcard, stayroom, tenantname, tenantsex, checkout) => {
  return Axios.get('/Tenant/Checkin?idcard=' + idcard + '&stayroom=' + stayroom + '&tenantname=' + tenantname
   + '&tenantsex=' + tenantsex + '&checkout=' + checkout).then(res =>res.data)
}
// 日志获取
export const listlog = () => {
  return Axios.get('/Log/Get').then(res => res.data)
}