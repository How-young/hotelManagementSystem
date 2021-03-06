/*
 Navicat Premium Data Transfer

 Source Server         : fandw
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : localhost:3306
 Source Schema         : hotel

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 16/07/2020 14:11:56
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for administratorinfromation
-- ----------------------------
DROP TABLE IF EXISTS `administratorinfromation`;
CREATE TABLE `administratorinfromation`  (
  `adminnum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `adminpassword` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`adminnum`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of administratorinfromation
-- ----------------------------
INSERT INTO `administratorinfromation` VALUES ('admin', '123');

-- ----------------------------
-- Table structure for billinformation
-- ----------------------------
DROP TABLE IF EXISTS `billinformation`;
CREATE TABLE `billinformation`  (
  `goodsnum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `idcard` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `quantity` int(0) NULL DEFAULT NULL,
  `summoney` double(255, 0) NULL DEFAULT NULL,
  PRIMARY KEY (`goodsnum`, `idcard`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of billinformation
-- ----------------------------
INSERT INTO `billinformation` VALUES ('101', '12345', 2, 3);
INSERT INTO `billinformation` VALUES ('101', '54321', 3, 9);
INSERT INTO `billinformation` VALUES ('102', '12345', 3, 2);
INSERT INTO `billinformation` VALUES ('102', '54321', 8, 40);

-- ----------------------------
-- Table structure for employeeinformation
-- ----------------------------
DROP TABLE IF EXISTS `employeeinformation`;
CREATE TABLE `employeeinformation`  (
  `employeenum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `employeemail` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `employeepassword` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `employeename` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `employeesex` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`employeenum`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employeeinformation
-- ----------------------------
INSERT INTO `employeeinformation` VALUES ('1', '12345@gmail.com', '12345', '李军', '男');
INSERT INTO `employeeinformation` VALUES ('2', '543212@qq.com', '54321', '张琪', '女');

-- ----------------------------
-- Table structure for floorinformation
-- ----------------------------
DROP TABLE IF EXISTS `floorinformation`;
CREATE TABLE `floorinformation`  (
  `floornum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `floordescribe` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`floornum`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of floorinformation
-- ----------------------------
INSERT INTO `floorinformation` VALUES ('01', '便宜');
INSERT INTO `floorinformation` VALUES ('02', '安静');

-- ----------------------------
-- Table structure for goodsinformation
-- ----------------------------
DROP TABLE IF EXISTS `goodsinformation`;
CREATE TABLE `goodsinformation`  (
  `goodsnum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `goodsname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `goodstypenum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `goodsprice` double NULL DEFAULT NULL,
  `goodsquantity` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`goodsnum`) USING BTREE,
  INDEX `goodstypenum`(`goodstypenum`) USING BTREE,
  CONSTRAINT `goodsinformation_ibfk_1` FOREIGN KEY (`goodstypenum`) REFERENCES `goodstypeinformation` (`goodstypenum`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goodsinformation
-- ----------------------------
INSERT INTO `goodsinformation` VALUES ('101', '可乐', '1', 3, 50);
INSERT INTO `goodsinformation` VALUES ('102', '橙汁', '1', 5, 50);
INSERT INTO `goodsinformation` VALUES ('201', '吐司', '2', 7, 50);

-- ----------------------------
-- Table structure for goodstypeinformation
-- ----------------------------
DROP TABLE IF EXISTS `goodstypeinformation`;
CREATE TABLE `goodstypeinformation`  (
  `goodstypenum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `goodstype` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `typedescribe` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`goodstypenum`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goodstypeinformation
-- ----------------------------
INSERT INTO `goodstypeinformation` VALUES ('1', '饮料', '解渴');
INSERT INTO `goodstypeinformation` VALUES ('2', '面包', '充饥');

-- ----------------------------
-- Table structure for loginformation
-- ----------------------------
DROP TABLE IF EXISTS `loginformation`;
CREATE TABLE `loginformation`  (
  `logdate` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  `detail` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`logdate`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of loginformation
-- ----------------------------
INSERT INTO `loginformation` VALUES ('2020-03-01 00:00:00', '小明入住');
INSERT INTO `loginformation` VALUES ('2020-03-03 00:00:00', '小明退房');
INSERT INTO `loginformation` VALUES ('2020-07-14 00:00:00', 'vip用户信息修改');
INSERT INTO `loginformation` VALUES ('2020-07-15 00:00:00', '房间类别关键词获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:14:06', '关键词查询商品类型信息');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:34:01', '所有商品类别获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:34:55', '关键词查询商品类型信息');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:37:46', '客房信息关键词获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:37:53', '所有客房信息获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:38:23', '所有客房信息获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:39:00', '所有客房信息获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:45:01', '所有客房信息获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:48:13', '所有房间类型获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:48:21', '所有房间类型获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:48:37', '所有楼层信息获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:48:59', '所有商品信息获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:49:16', '所有商品类别获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:49:33', '所有客房信息获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 16:49:46', '所有账单信息获取');
INSERT INTO `loginformation` VALUES ('2020-07-15 20:08:07', '关键词查询商品信息');
INSERT INTO `loginformation` VALUES ('2020-07-15 21:02:06', '账单信息添加');
INSERT INTO `loginformation` VALUES ('2020-07-15 21:09:52', '账单信息添加');
INSERT INTO `loginformation` VALUES ('2020-07-15 23:48:24', '账单信息添加');
INSERT INTO `loginformation` VALUES ('2020-07-15 23:54:55', '账单信息添加');

-- ----------------------------
-- Table structure for payinformation
-- ----------------------------
DROP TABLE IF EXISTS `payinformation`;
CREATE TABLE `payinformation`  (
  `idcard` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `paytime` timestamp(0) NULL DEFAULT NULL,
  `total` double(50, 0) NULL DEFAULT NULL,
  PRIMARY KEY (`idcard`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of payinformation
-- ----------------------------
INSERT INTO `payinformation` VALUES ('12345', NULL, NULL);
INSERT INTO `payinformation` VALUES ('54321', '2020-07-15 23:54:55', 78);

-- ----------------------------
-- Table structure for roominformation
-- ----------------------------
DROP TABLE IF EXISTS `roominformation`;
CREATE TABLE `roominformation`  (
  `roomnum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `roomtypenum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `isempty` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `roomfloor` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`roomnum`) USING BTREE,
  INDEX `roomtypenum`(`roomtypenum`) USING BTREE,
  CONSTRAINT `roominformation_ibfk_1` FOREIGN KEY (`roomtypenum`) REFERENCES `roomtypeinformation` (`roomtypenum`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of roominformation
-- ----------------------------
INSERT INTO `roominformation` VALUES ('101', 'a', '0', '01');
INSERT INTO `roominformation` VALUES ('102', 'a', '1', '01');
INSERT INTO `roominformation` VALUES ('103', 'b', '1', '01');
INSERT INTO `roominformation` VALUES ('201', 'b', '0', '02');
INSERT INTO `roominformation` VALUES ('202', 'a', '1', '02');
INSERT INTO `roominformation` VALUES ('203', 'b', '1', '02');

-- ----------------------------
-- Table structure for roomtypeinformation
-- ----------------------------
DROP TABLE IF EXISTS `roomtypeinformation`;
CREATE TABLE `roomtypeinformation`  (
  `roomtypenum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `roomtype` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `roomprice` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `roomquantity` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `roomdescribe` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`roomtypenum`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of roomtypeinformation
-- ----------------------------
INSERT INTO `roomtypeinformation` VALUES ('a', '双人', '400', '2', '空间大');
INSERT INTO `roomtypeinformation` VALUES ('b', '单人', '250', '2', '干净整洁');

-- ----------------------------
-- Table structure for tenantinformation
-- ----------------------------
DROP TABLE IF EXISTS `tenantinformation`;
CREATE TABLE `tenantinformation`  (
  `idcard` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stayroom` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tenantname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tenantsex` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `checkin` timestamp(0) NULL DEFAULT NULL,
  `checkout` timestamp(0) NULL DEFAULT NULL,
  PRIMARY KEY (`idcard`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tenantinformation
-- ----------------------------
INSERT INTO `tenantinformation` VALUES ('10004', '101', '张三', '男', '2020-04-01 00:00:00', '2020-04-03 00:00:00');
INSERT INTO `tenantinformation` VALUES ('20004', '201', '小丽', '女', '2020-04-23 00:00:00', '2020-04-24 00:00:00');

-- ----------------------------
-- Table structure for vipinformation
-- ----------------------------
DROP TABLE IF EXISTS `vipinformation`;
CREATE TABLE `vipinformation`  (
  `vipnum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `idcard` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `vipname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `vipsex` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `vipemail` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `registertime` timestamp(0) NULL DEFAULT NULL,
  `vipphone` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`vipnum`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of vipinformation
-- ----------------------------
INSERT INTO `vipinformation` VALUES ('1', '10004', '张三', '女', 'zhang@gmal.com', '2020-07-14 00:00:00', '520888');
INSERT INTO `vipinformation` VALUES ('2', '20004', '小丽', '女', 'xiaoli@hotel.com', '2020-04-05 00:00:00', '987654321');

SET FOREIGN_KEY_CHECKS = 1;
