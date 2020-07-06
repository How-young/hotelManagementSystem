# 

**客房类型管理**

##### **简要描述**

·    增加客房类型

##### **请求URL**

·    http://xx.com/api/user/addroomtype

##### **请求方式**

·    POST 

##### **参数**



| **参数名**   | **必选** | **类型** | **说明**     |
| ------------ | -------- | -------- | ------------ |
| roomtypenum  | 是       | string   | 类型编号     |
| roomtype     | 否       | string   | 类型         |
| roomprice    | 否       | double   | 价格         |
| roomquantity | 否       | string   | 房间剩余数量 |
| roomdescribe | 否       | string   | 描述         |



##### **返回示例**



 {  "error_code": 0,  "data": {   "success": true,  } }



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

#  

##### **简要描述**

·    修改客房类型

##### **请求URL**

·    http://xx.com/api/user/modifyroomtype

##### **请求方式**

·    POST 

##### **参数**



| **参数名**   | **必选** | **类型** | **说明**     |
| ------------ | -------- | -------- | ------------ |
| roomtypenum  | 是       | string   | 类型编号     |
| roomtype     | 是       | string   | 类型         |
| roomprice    | 是       | double   | 价格         |
| roomquantity | 是       | string   | 房间剩余数量 |
| roomdescribe | 是       | string   | 描述         |



##### **返回示例**



```
 {
 "error_code": 0, 
 "data": {   
 	"success": true,
 } }
```





##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述



##### **简要描述**

·    删除客房类型

##### **请求URL**

·    http://xx.com/api/user/deleteroomtype

##### **请求方式**

·    POST 

##### **参数**



| **参数名**   | **必选** | **类型** | **说明**     |
| ------------ | -------- | -------- | ------------ |
| roomtypenum  | 是       | string   | 类型编号     |
| roomtype     | 否       | string   | 类型         |
| roomprice    | 否       | double   | 价格         |
| roomquantity | 否       | string   | 房间剩余数量 |
| roomdescribe | 否       | string   | 描述         |



##### **返回示例**

```
 {  
 "error_code": 0,
 "data": {  
 		"success": true,
 } }
```



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

##### **简要描述**

·    返回客房类型信息列表

##### **请求URL**

·    http://xx.com/api/user/getallroomtype

##### **请求方式**

·    POST 

##### **参数**



| **参数名** | **必选** | **类型** | **说明** |
| ---------- | -------- | -------- | -------- |
|            |          |          |          |



##### **返回示例**

```
 {  
 "error_code": 0,  
 "data": {     
 		[“roomtypenum”:”示例”,“roomtype”:”示例”,“roomprice”:123,“roomquantity”:123,      “roomdecribe”:”示例”],   
 		[“roomtypenum”:”示例1”,“roomtype”:”示例1”,“roomprice”:123,“roomquantity”:123,      “roomdecribe”:”示例1”]  
 } }
```



##### **返回参数说明**



| **参数名**   | **类型** | **说明**     |
| ------------ | -------- | ------------ |
| roomtypenum  | string   | 类型编号     |
| roomtype     | string   | 类型         |
| roomprice    | double   | 价格         |
| roomquantity | string   | 房间剩余数量 |
| roomdescribe | string   | 描述         |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

**1.2楼层管理**

##### **简要描述**

·    增加楼层类型

##### **请求URL**

·    http://xx.com/api/user/addfloortype

##### **请求方式**

·    POST 

##### **参数**



| **参数名**    | **必选** | **类型** | **说明**         |
| ------------- | -------- | -------- | ---------------- |
| floornum      | 是       | string   | 楼层号           |
| floordescribe | 否       | string   | 楼层描述         |
| remainroom    | 否       | int      | 楼层剩下的房间数 |



##### **返回示例**



 {  "error_code": 0,  "data": {   "success": true,  } }



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

##### **简要描述**

·    修改楼层类型

##### **请求URL**

·    http://xx.com/api/user/modifyfloortype

##### **请求方式**

·    POST 

##### **参数**



| **参数名**    | **必选** | **类型** | **说明**         |
| ------------- | -------- | -------- | ---------------- |
| floornum      | 是       | string   | 楼层号           |
| floordescribe | 是       | string   | 楼层描述         |
| remainroom    | 是       | int      | 楼层剩下的房间数 |



##### **返回示例**



 {  "error_code": 0,  "data": {   "success": true,  } }



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

##### **简要描述**

·    删除楼层类型

##### **请求URL**

·    http://xx.com/api/user/deletefloortype

##### **请求方式**

·    POST 

##### **参数**



| **参数名**    | **必选** | **类型** | **说明**         |
| ------------- | -------- | -------- | ---------------- |
| floornum      | 是       | string   | 楼层号           |
| floordescribe | 否       | string   | 楼层描述         |
| remainroom    | 否       | int      | 楼层剩下的房间数 |



##### **返回示例**

```
 {  
 "error_code": 0,  
 "data": {   
 		"success": true,
 } }
```



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

##### **简要描述**

·    返回楼层类型列表

##### **请求URL**

·    http://xx.com/api/user/getallfloortype

##### **请求方式**

·    POST 

##### **参数**



| **参数名**    | **必选** | **类型** | **说明**         |
| ------------- | -------- | -------- | ---------------- |
| floornum      | 是       | string   | 楼层号           |
| floordescribe | 否       | string   | 楼层描述         |
| remainroom    | 否       | int      | 楼层剩下的房间数 |



##### **返回示例**

```json
 {  
	 "error_code": 0,  
	 "data": {        
 			[“floornum”:”示例”,“floordecribe”:”示例”,“remainroom”:123],   
 			[“floornum”:”示例1”,“floordecribe”:”示例1”,“remainroom”:123]
  			} 
 }
```



##### **返回参数说明**



| **参数名**    | **类型** | **说明** |
| ------------- | -------- | -------- |
| floornum      | 是       | string   |
| floordescribe | 否       | string   |
| remainroom    | 否       | int      |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

**1.3商品类别管理**

##### **简要描述**

·    增加商品类型

##### **请求URL**

·    http://xx.com/api/user/addgoodstype

##### **请求方式**

·    POST 

##### **参数**



| **参数名**   | **必选** | **类型** | **说明** |
| ------------ | -------- | -------- | -------- |
| goodstypenum | 是       | string   | 类别编号 |
| goodstype    | 否       | string   | 类别     |
| typedescribe | 否       | string   | 简述     |



##### **返回示例**

```json
 {  
     "error_code": 0,  
     "data": {   
         "success": true,  
     } 
 }
```



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

##### **简要描述**

·    修改商品类型

##### **请求URL**

·    http://xx.com/api/usermodifygoodstype

##### **请求方式**

·    POST 

##### **参数**



| **参数名**   | **必选** | **类型** | **说明** |
| ------------ | -------- | -------- | -------- |
| goodstypenum | 是       | string   | 类别编号 |
| goodstype    | 是       | string   | 类别     |
| typedescribe | 是       | string   | 简述     |



##### **返回示例**

```json
 {  
     "error_code": 0,  
     "data": {   
         "success": true,  
     } 
 }
```



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

##### **简要描述**

·    删除商品类型

##### **请求URL**

·    http://xx.com/api/user/deletegoodstype

##### **请求方式**

·    POST 

##### **参数**



| **参数名**   | **必选** | **类型** | **说明** |
| ------------ | -------- | -------- | -------- |
| goodstypenum | 是       | string   | 类别编号 |
| goodstype    | 否       | string   | 类别     |
| typedescribe | 否       | string   | 简述     |



##### **返回示例**

```json
 {  
     "error_code": 0,  
     "data": {   
         "success": true,  
     } 
 }
```



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

##### **简要描述**

·    返回楼层类型列表

##### **请求URL**

·    http://xx.com/api/user/getallfloortype

##### **请求方式**

·    POST 

##### **参数**



| **参数名**    | **必选** | **类型** | **说明**         |
| ------------- | -------- | -------- | ---------------- |
| floornum      | 是       | string   | 楼层号           |
| floordescribe | 否       | string   | 楼层描述         |
| remainroom    | 否       | int      | 楼层剩下的房间数 |



##### **返回示例**

```json
 {  
     "error_code": 0,  
     "data": {        
         [“floornum”:”示例”, “floordecribe”:”示例”,“remainroom”:123],   
         [“floornum”:”示例1”,“floordecribe”:”示例1”,“remainroom”:123]  
     } 
 }
```



##### **返回参数说明**



| **参数名**    | **类型** | **说明** |
| ------------- | -------- | -------- |
| floornum      | 是       | string   |
| floordescribe | 否       | string   |
| remainroom    | 否       | int      |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

**1.4商品管理**

##### **简要描述**

·    增加商品

##### **请求URL**

·    http://xx.com/api/user/addgoods

##### **请求方式**

·    POST 

##### **参数**



| **参数名**    | **必选** | **类型** | **说明**   |
| ------------- | -------- | -------- | ---------- |
| goodsnum      | 是       | string   | 商品号     |
| goodstypenum  | 否       | string   | 商品类别号 |
| goodsprice    | 否       | double   | 价格       |
| goodsquantity | 否       | int      | 数量       |



##### **返回示例**

```json
{  
    "error_code": 0,  
    "data": {   
        "success": true,  
    } 
}
```



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

##### **简要描述**

·    修改商品

##### **请求URL**

·    http://xx.com/api/user/modifygoods

##### **请求方式**

·    POST 

##### **参数**



| **参数名**    | **必选** | **类型** | **说明**   |
| ------------- | -------- | -------- | ---------- |
| goodsnum      | 是       | string   | 商品号     |
| goodstypenum  | 是       | string   | 商品类别号 |
| goodsprice    | 是       | double   | 价格       |
| goodsquantity | 是       | int      | 数量       |



##### **返回示例**

```json
 {  
     "error_code": 0,  
     "data": {   
         "success": true,  
     } 
 }
```



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

##### **简要描述**

·    删除商品

##### **请求URL**

·    http://xx.com/api/user/deletegoods

##### **请求方式**

·    POST 

##### **参数**



| **参数名**    | **必选** | **类型** | **说明**   |
| ------------- | -------- | -------- | ---------- |
| goodsnum      | 是       | string   | 商品号     |
| goodstypenum  | 否       | string   | 商品类别号 |
| goodsprice    | 否       | double   | 价格       |
| goodsquantity | 否       | int      | 数量       |



##### **返回示例**

```json
 {  
     "error_code": 0,  
     "data": {   
         "success": true,  
     } 
 }
```



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

**1.5会员管理**

##### **简要描述**

·    增加会员

##### **请求URL**

·    http://xx.com/api/user/addvip

##### **请求方式**

·    POST 

##### **参数**



| **参数名** | **必选** | **类型** | **说明** |
| ---------- | -------- | -------- | -------- |
| vipnum     | 是       | string   | 会员号   |
| idcard     | 否       | string   | 身份证号 |
| vipname    | 否       | string   | 姓名     |
| vipsex     | 否       | string   | 性别     |



##### **返回示例**

```json
{  
    "error_code": 0,  
    "data": {   
        "success": true,  
    } 
}
```



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

##### **简要描述**

·    修改会员

##### **请求URL**

·    http://xx.com/api/user/modifyvip

##### **请求方式**

·    POST 

##### **参数**



| **参数名** | **必选** | **类型** | **说明** |
| ---------- | -------- | -------- | -------- |
| vipnum     | 是       | string   | 会员号   |
| idcard     | 是       | string   | 身份证号 |
| vipname    | 是       | string   | 姓名     |
| vipsex     | 是       | string   | 性别     |



##### **返回示例**

```json
 {  
     "error_code": 0,  
     "data": {   
         "success": true,  
     } 
 }
```



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

##### **简要描述**

·    删除会员

##### **请求URL**

·    http://xx.com/api/user/deletevip

##### **请求方式**

·    POST 

##### **参数**



| **参数名** | **必选** | **类型** | **说明** |
| ---------- | -------- | -------- | -------- |
| vipnum     | 是       | string   | 会员号   |
| idcard     | 否       | string   | 身份证号 |
| vipname    | 否       | string   | 姓名     |
| vipsex     | 否       | string   | 性别     |



##### **返回示例**

```json
{  
    "error_code": 0,  
    "data": {   
        "success": true,  
    } 
}
```



##### **返回参数说明**



| **参数名** | **类型** | **说明**             |
| ---------- | -------- | -------------------- |
| success    | boolen   | true 成功 flase 失败 |



##### **备注**

·    更多返回错误代码请看首页的错误代码描述

 

**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 查询用户列表接口

**查询用户列表**

- http://xx.com/api/user/selectEmployee

**请求方式**

- GET

**参数**

无

**返回示例**

```json
{
    "error_code": 0,
    "data": {
        "true": true，    
        "employees":{
        	{"employeenum"：xxx，
        	"employeeemail"：xxx，
        	"employeename":xxx,"employeesex":xxx},
    		{"employeenum"：xxx，"employeeemail":xxx，"employeename":xxx,"employeesex":xxx}
		}
	}
}
```



**返回参数说明**



| **参数名** | **类型**   | **说明**                       |
| ---------- | ---------- | ------------------------------ |
| true       | Boolean    | true:添加成功，false：添加失败 |
| employees  | String[][] | 员工二维数组                   |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 添加员工接口

**添加员工**

- http://xx.com/api/user/addEmployee

**请求方式**

- POST

**参数**



| **参数名**    | **必选** | **类型** | **说明** |
| ------------- | -------- | -------- | -------- |
| employeeemail | 是       | string   | 邮箱地址 |
| employeename  | 是       | string   | 员工姓名 |
| employeesex   | 否       | string   | 员工性别 |



**返回示例**

```json
{
    "error_code":0,
    "data":{
        "true":true
    }
}
```



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 修改员工信息接口

**修改员工信息**

- http://xx.com/api/user/updateEmployee

**请求方式**

- POST

**参数**

| **参数名**    | **必选** | **类型** | **说明** |
| ------------- | -------- | -------- | -------- |
| employeenum   | 是       | string   | 员工号   |
| employeeemail | 是       | string   | 邮箱地址 |
| employeename  | 是       | string   | 员工姓名 |
| employeesex   | 否       | string   | 员工性别 |



**返回示例**

```json
{
    "error_code":0,
    "data":{
        "true":true
    }
}
```

**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 删除员工信息接口

**删除员工信息**

- http://xx.com/api/user/deleteEmployee

**请求方式**

- POST

**参数**



| **参数名**  | **必选** | **类型** | **说明** |
| ----------- | -------- | -------- | -------- |
| Employeenum | 是       | string   | 员工号   |



**返回示例**

```json
{
    "error_code":0,
    "data":{
        "true":true
    }
}
```

**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 查询日志接口

**查询日志**

- ` http://xx.com/api/log/getLog

**请求方式**

- GET

**参数**

无

**返回示例**

```json
{
    "srror_code":0,
    "data":{
        "success":true,
        "logInformation":{data,detail}
    }
}
```

**返回参数说明**



| **参数名**    | **类型** | **说明**                       |
| ------------- | -------- | ------------------------------ |
| success       | Boolean  | true:返回成功，false：返回失败 |
| logInfomation | varchar  | 日志信息                       |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 删除日志接口

**删除日志**

- http://xx.com/api/log/deleteLog

**请求方式**

- DELETE

**参数**

无

**返回示例**

```json
{
    "error_code":0, 
    "data":{
        "success":true
    }
}
```

**返回参数说明**



| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:删除成功，false：删除失败 |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 预定客人报表接口

**预定客人报表**

- http://xx.com/api/report/scheduledTenantReport

**请求方式**

- POST

**参数**



| **参数名**       | **必选** | **类型** | **说明** |
| ---------------- | -------- | -------- | -------- |
| tenantinfomation | 是       | varchar  | 客人信息 |
| scheduletime     | 是       | varchar  | 预约时间 |



**返回示例**

```json
{
    "srror_code":0,
    "data":{
        "success":true
    }
}
```

**返回参数说明**



| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:报表成功，false：报表失败 |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 入住客人报表接口

**入住客人报表**

- http://xx.com/api/report/checkinTenantReport

**请求方式**

- POST

**参数**



| **参数名**       | **必选** | **类型** | **说明** |
| ---------------- | -------- | -------- | -------- |
| tenantinfomation | 是       | varchar  | 客人信息 |
| checkintime      | 是       | varchar  | 入住时间 |



**返回示例**

```json
{
    "error_code":0,
    "data":{
        "success":true
    }
}
```

**返回参数说明**



| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:报表成功，false：报表失败 |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 离店客人报表接口

**离店客人报表**

- http://xx.com/api/report/leaveTenantReport

**请求方式**

- POST

**参数**



| **参数名**       | **必选** | **类型** | **说明** |
| ---------------- | -------- | -------- | -------- |
| tenantinfomation | 是       | varchar  | 客人信息 |
| leavetime        | 是       | varchar  | 离店时间 |



**返回示例**

```json
{
    "erroe_code":0,
    "data":{
        "success":true
    }
}
```

**返回参数说明**



| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:报表成功，false：报表失败 |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 财务进账报表接口

**财务进帐报表**

- http://xx.com/api/report/incomeReport

**请求方式**

- POST

**参数**



| **参数名** | **必选** | **类型** | **说明** |
| ---------- | -------- | -------- | -------- |
| income     | 是       | varchar  | 酒店收入 |
| outcome    | 是       | varchar  | 酒店支出 |



**返回示例**

```json
{
    "erroe_code":0,
    "data":{
        "success":true
    }
}
```

**返回参数说明**



| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:报表成功，false：报表失败 |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 客房预订接口

**添加会员**

- http://xx.com/api/tenant/roomResrvation

**请求方式**

- POST

**参数**



| **参数名**        | **必选** | **类型** | **说明** |
| ----------------- | -------- | -------- | -------- |
| tenantinformation | 是       | varchar  | 房客信息 |
| scheduletime      | 是       | varchar  | 预定时间 |
| roomnum           | 否       | varchar  | 房间号   |



**返回示例**

```json
{
    "error_code":0,
    "data":{
        "success":true
    }
}
```

**返回参数说明**



| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:预定成功，false：预定失败 |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 修改预定信息接口

**修改预定信息**

- http://xx.com/api/tenant/changeReservation

**请求方式**

- POST

**参数**



| **参数名**   | **必选** | **类型** | **说明** |
| ------------ | -------- | -------- | -------- |
| scheduletime | 是       | varchar  | 预定时间 |
| roomnum      | 否       | varchar  | 房间号   |



**返回示例**

```json
{
    "error_code":0,
    "data":{
        "success":true
    }
}
```

**返回参数说明**



| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:修改成功，false：修改失败 |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 删除会员信息接口

**取消预定信息**

- http://xx.com/api/user/deleteVip

**请求方式**

- DELETE

**参数**

无

**返回示例**

```json
{
    "error_code":0,
    "data":{
        "success":true
    }
}
```

**返回参数说明**



| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:预定成功，false：预定失败 |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 转入住接口

**转入住**

- http://xx.com/api/user/toCheckin

**请求方式**

- POST

**参数**

无

**返回示例**

```json
{
    "error_code":0,
    "data":{
        "success":true
    }
}
```

**返回参数说明**



| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:入住成功，false：入住失败 |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 预定转入住登记接口

**预定转入住**

- http://xx.com/api/reservation/toCheckin

**请求方式**

- POST

**参数**



| **参数名**        | **必选** | **类型** | **说明** |
| ----------------- | -------- | -------- | -------- |
| tenantinformation | 是       | varchar  | 房客信息 |
| scheduletime      | 是       | varchar  | 预定时间 |
| roomnum           | 否       | varchar  | 房间号   |



**返回示例**

```json
{
    "error_code":0,
    "data":{
        "success":true
    }
}
```

| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:入住成功，false：入住失败 |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 入住单接口

**修改员工信息**

- http://xx.com/api/reservation/credential

**请求方式**

- POST

**参数**



| **参数名**        | **必选** | **类型** | **说明** |
| ----------------- | -------- | -------- | -------- |
| tenantinformation | 是       | varchar  | 房客信息 |
| scheduletime      | 是       | varchar  | 预定时间 |
| roomnum           | 否       | varchar  | 房间号   |



**返回示例**

```json
{
    "error_code":0,
    "data":{
        "success":true,
        "credential":{
            idcard,tenantname,tenantsex,scheduletime,checkintime
        }
    }
}
```

| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:入住成功，false：入住失败 |
| credential | varchar  | 入住信息                       |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 查询登记信息接口

**查询登记信息**

- http://xx.com/api/query/registeredRoomInfo

**请求方式**

- GET

**参数**

无

**返回示例**

```json
{
    "error_code":0,
    "data":{
        "success":true,
        "registerroominfo":{
            idcard,tenantname,tenantsex,scheduletime,checkintime
        }
    }
}
```

| **参数名**         | **类型** | **说明**                       |
| ------------------ | -------- | ------------------------------ |
| success            | Boolean  | true:查询成功，false：查询失败 |
| registeredroominfo | varchar  | 已登记的房间信息               |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 换房接口

**换房**

- http://xx.com/api/changeRoom/changeRoom

**请求方式**

- POST

**参数**



| **参数名**        | **必选** | **类型** | **说明** |
| ----------------- | -------- | -------- | -------- |
| tenantinformation | 是       | varchar  | 房客信息 |
| newroomnum        | 否       | varchar  | 新房间号 |



**返回示例**

```json
{
    "error_code":0,
    "data":{
        "success":true,
        "newroominfo":{
            idcard，tenantname，tenantsex，roomnum，checkintime
        }
    }
}
```

| **参数名**  | **类型** | **说明**                      |
| ----------- | -------- | ----------------------------- |
| success     | Boolean  | true:换房成功，false:换房失败 |
| newroominfo | varchar  | 新的房间信息                  |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 入住单接口

**换房入住单信息**

- http://xx.com/api/changeRoom/credential

**请求方式**

- GET

**参数**



| **参数名**        | **必选** | **类型** | **说明** |
| ----------------- | -------- | -------- | -------- |
| tenantinformation | 是       | varchar  | 房客信息 |
| newroomnum        | 否       | varchar  | 房间号   |



**返回示例**

```json
{
    "error_code":0,
    "data":{
        "success":true,
        "credential":{
            idcard,tenantname,tenantsex,roomnum,checkintime
        }
    }
}
```

| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:返回成功，false：返回失败 |
| credential | varchar  | 换房入住信息                   |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 结账接口

**结账**

- http://xx.com/api/checkout/pay

**请求方式**

- POST

**参数**



| **参数名** | **必选** | **类型** | **说明** |
| ---------- | -------- | -------- | -------- |
| billinfo   | 是       | varchar  | 账单信息 |



**返回示例**

```json
{
    "error_code": 0,
    "data":{
        "success":true
        "price":{money}
    }
}
```

| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:返回成功，false：返回失败 |
| price      | varchar  | 支付价格信息                   |



**备注**

- 更多返回错误代码请看首页的错误代码描述

**简要描述**

- 打印账单接口

**结账**

- http://xx.com/api/checkout/printBill

**请求方式**

- GET

**参数**

无

**返回示例**

```bash
{
	"error_code":0,
	"data":{
		"success":true,
		"billinfo":{money, time}
	}
}
```

| **参数名** | **类型** | **说明**                       |
| ---------- | -------- | ------------------------------ |
| success    | Boolean  | true:打印成功，false：打印失败 |
| money      | varchar  | 返回支付价格和支付时间         |



**备注**

- 更多返回错误代码请看首页的错误代码描述

#  