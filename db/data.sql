create database if not exists `crawler`;
use `crawler`;
DROP TABLE IF EXISTS `enterprise`;
CREATE TABLE `enterprise` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'PK',
  `name` varchar(128) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '公司名',
  `representative` varchar(20) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '法人代表',
  `address` varchar(200) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '公司地址',
  `region` varchar(15) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '所属地区',
  `biz_status` varchar(20) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '经营状态',
  `credit_code` varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '统一社会信用代码',
  `register_code` varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '注册号',
  `phone` varchar(20) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '电话',
  `email` varchar(50) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '邮箱',
  `setup_time` varchar(20) NOT NULL DEFAULT '-' COMMENT '成立时间',
  `industry` varchar(50) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '所属行业',
  `biz_scope` varchar(1200) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '经营范围',
  `company_type` varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '公司类型',
  `registered_capital` varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '注册资本',
  `paid_capital` varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '实缴资本',
  `taxpayer_code` varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '纳税人识别号',
  `organization_code` varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '组织机构代码',
  `english_name` varchar(128) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '公司英文名',
  `authority` varchar(50) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '登记机关',
  `homepage` varchar(30) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '公司官网',
  `desc` varchar(800) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '企业简介',
  `used_name` varchar(128) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '公司曾用名',
  `insert_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  `last_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后操作时间',
  PRIMARY KEY (`id`),
  unique key (`credit_code`, register_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;