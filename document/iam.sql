/*
Navicat MySQL Data Transfer

Source Server         : Localhost
Source Server Version : 60011
Source Host           : localhost:3306
Source Database       : test
source user           ；root
source password       ；test@root


Target Server Type    : MYSQL
Target Server Version : 60011
File Encoding         : 65001

Date: 2019-01-19 17:06:41
*/

SET FOREIGN_KEY_CHECKS=0;

--创建数据库：test
--CREATE DATABASE IF NOT EXISTS 表名 default charset utf8 COLLATE utf8_general_ci;

--选择数据库
USE test;

--创建表
--UNIQUE  ： 唯一约束
--primary key ：主键
--auto_increment ：自动增长
--comment "账号"  ： 字段描述
--NOT NULL ：  非空
--CHARSET=utf8  : 表编码
-- ----------------------------
-- Table structure for `account`
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `id` int(11) unsigned primary key auto_increment,
  `name` CHAR(20) UNIQUE NOT NULL  comment "账号",
  `password` CHAR(20) NOT NULL comment "密码",
  `createtime` TIMESTAMP NOT NULL comment "创建时间"
) ENGINE=InnoDB DEFAULT CHARSET=utf8 comment="创建account表";

-- ----------------------------
-- Records of fds
-- ----------------------------

--修改表结构

--alter table 表名 add 字段名 字段类型(大小) unsigned DEFAULT NULL COMMENT '字段描述';

--插入数据
INSERT INTO account (name,password) VALUES ('msmiles','msmiles');

--查询
SELECT * FROM account WHERE name = 'msmiles';

--更新
UPDATE account SET password= 'msmiles1' WHERE name = 'msmiles' AND id = 1;

--删除
DELETE FROM account WHERE name = 'msmiles' AND id = 1;

