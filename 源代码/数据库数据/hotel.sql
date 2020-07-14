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

 Date: 14/07/2020 12:11:14
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
  `idcard` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `quantity` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`goodsnum`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of billinformation
-- ----------------------------
INSERT INTO `billinformation` VALUES ('101', '12345', 2);

-- ----------------------------
-- Table structure for employeeinfromation
-- ----------------------------
DROP TABLE IF EXISTS `employeeinfromation`;
CREATE TABLE `employeeinfromation`  (
  `employeenum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `employeemail` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `employeepassword` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `employeename` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `employeesex` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`employeenum`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employeeinfromation
-- ----------------------------
INSERT INTO `employeeinfromation` VALUES ('1', '12345@gmail.com', '12345', '李军', '男');
INSERT INTO `employeeinfromation` VALUES ('2', '543212@qq.com', '54321', '张琪', '女');

-- ----------------------------
-- Table structure for floorinformation
-- ----------------------------
DROP TABLE IF EXISTS `floorinformation`;
CREATE TABLE `floorinformation`  (
  `floornum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `floordescribe` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `remainroom` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`floornum`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of floorinformation
-- ----------------------------
INSERT INTO `floorinformation` VALUES ('1', '便宜', 20);
INSERT INTO `floorinformation` VALUES ('2', '安静', 19);

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
INSERT INTO `goodsinformation` VALUES ('101', '可乐', '1', 3, 10);
INSERT INTO `goodsinformation` VALUES ('201', '吐司', '2', 7, 5);

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
  `logdate` timestamp(0) NOT NULL,
  `detail` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`logdate`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of loginformation
-- ----------------------------
INSERT INTO `loginformation` VALUES ('2020-03-01 00:00:00', '小明入住');
INSERT INTO `loginformation` VALUES ('2020-03-03 00:00:00', '小明退房');

-- ----------------------------
-- Table structure for payinformation
-- ----------------------------
DROP TABLE IF EXISTS `payinformation`;
CREATE TABLE `payinformation`  (
  `idcard` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `paytime` timestamp(0) NULL DEFAULT NULL,
  `total` double(50, 0) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for roominformation
-- ----------------------------
DROP TABLE IF EXISTS `roominformation`;
CREATE TABLE `roominformation`  (
  `roomnum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `roomtypenum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `isempty` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `roomfoolr` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`roomnum`) USING BTREE,
  INDEX `roomtypenum`(`roomtypenum`) USING BTREE,
  CONSTRAINT `roominformation_ibfk_1` FOREIGN KEY (`roomtypenum`) REFERENCES `roomtypeinformation` (`roomtypenum`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of roominformation
-- ----------------------------
INSERT INTO `roominformation` VALUES ('0101', '1', '0', '1');
INSERT INTO `roominformation` VALUES ('0201', '2', '1', '2');

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
INSERT INTO `roomtypeinformation` VALUES ('1', '双人', '400', '20', '空间大');
INSERT INTO `roomtypeinformation` VALUES ('2', '单人', '250', '20', '干净整洁');

-- ----------------------------
-- Table structure for tenantinfromation
-- ----------------------------
DROP TABLE IF EXISTS `tenantinfromation`;
CREATE TABLE `tenantinfromation`  (
  `idcard` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stayroom` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tenantname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tenantsex` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `checkin` timestamp(0) NULL DEFAULT NULL,
  `checkout` timestamp(0) NULL DEFAULT NULL,
  PRIMARY KEY (`idcard`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tenantinfromation
-- ----------------------------
INSERT INTO `tenantinfromation` VALUES ('10004', '101', '张三', '男', '2020-04-01 00:00:00', '2020-04-03 00:00:00');
INSERT INTO `tenantinfromation` VALUES ('20004', '201', '小丽', '女', '2020-04-23 00:00:00', '2020-04-24 00:00:00');

-- ----------------------------
-- Table structure for vipinformaition
-- ----------------------------
DROP TABLE IF EXISTS `vipinformaition`;
CREATE TABLE `vipinformaition`  (
  `vipnum` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `idcard` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `vipname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `vipsex` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `vipemail` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `registertime` date NULL DEFAULT NULL,
  `vipphone` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`vipnum`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of vipinformaition
-- ----------------------------
INSERT INTO `vipinformaition` VALUES ('1', '10004', '张三', '男', 'zhangsan@hotel.com', '2020-02-03', '123456789');
INSERT INTO `vipinformaition` VALUES ('2', '20004', '小丽', '女', 'xiaoli@hotel.com', '2020-04-05', '987654321');

SET FOREIGN_KEY_CHECKS = 1;
