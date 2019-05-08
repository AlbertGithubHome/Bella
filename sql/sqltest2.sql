/*
 Navicat Premium Data Transfer

 Source Server         : me
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : sqltest2

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 28/04/2019 10:56:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for a
-- ----------------------------
DROP TABLE IF EXISTS `a`;
CREATE TABLE `a`  (
  `id` int(11) NULL DEFAULT NULL,
  `num` int(11) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of a
-- ----------------------------
INSERT INTO `a` VALUES (1, 100);
INSERT INTO `a` VALUES (2, 200);
INSERT INTO `a` VALUES (3, 300);

-- ----------------------------
-- Table structure for b
-- ----------------------------
DROP TABLE IF EXISTS `b`;
CREATE TABLE `b`  (
  `id` int(11) NULL DEFAULT NULL,
  `num` int(11) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of b
-- ----------------------------
INSERT INTO `b` VALUES (1, 100);
INSERT INTO `b` VALUES (2, 200);
INSERT INTO `b` VALUES (4, 400);

-- ----------------------------
-- Table structure for c
-- ----------------------------
DROP TABLE IF EXISTS `c`;
CREATE TABLE `c`  (
  `id` int(11) NULL DEFAULT NULL,
  `num` int(11) NULL DEFAULT NULL,
  INDEX `idindex`(`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of c
-- ----------------------------
INSERT INTO `c` VALUES (1, 103);
INSERT INTO `c` VALUES (2, 203);
INSERT INTO `c` VALUES (6, 603);

-- ----------------------------
-- Table structure for d
-- ----------------------------
DROP TABLE IF EXISTS `d`;
CREATE TABLE `d`  (
  `id` int(11) NOT NULL,
  `num` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of d
-- ----------------------------
INSERT INTO `d` VALUES (1, 104);
INSERT INTO `d` VALUES (2, 204);
INSERT INTO `d` VALUES (6, 504);

-- ----------------------------
-- Table structure for m
-- ----------------------------
DROP TABLE IF EXISTS `m`;
CREATE TABLE `m`  (
  `id` int(11) NULL DEFAULT NULL,
  `num` int(11) NULL DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Records of m
-- ----------------------------
INSERT INTO `m` VALUES (1, 1001);

-- ----------------------------
-- Table structure for p
-- ----------------------------
DROP TABLE IF EXISTS `p`;
CREATE TABLE `p`  (
  `id` int(11) NULL DEFAULT NULL,
  `num` int(11) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic PARTITION BY RANGE (id)
PARTITIONS 2
(PARTITION `p0` VALUES LESS THAN (3) ENGINE = InnoDB MAX_ROWS = 0 MIN_ROWS = 0 ,
PARTITION `p1` VALUES LESS THAN (6) ENGINE = InnoDB MAX_ROWS = 0 MIN_ROWS = 0 )
;

-- ----------------------------
-- Records of p
-- ----------------------------
INSERT INTO `p` VALUES (1, 111);
INSERT INTO `p` VALUES (2, 222);
INSERT INTO `p` VALUES (4, 444);
INSERT INTO `p` VALUES (5, 555);

SET FOREIGN_KEY_CHECKS = 1;
