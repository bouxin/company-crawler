# 执行sql之前确认MySQL中crawler库不存在或无关紧要
create database if not exists `crawler`;
use `crawler`;
DROP TABLE IF EXISTS `enterprise`;
CREATE TABLE `enterprise` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'PK',
  `name` varchar(128) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '公司名',
  `representative` varchar(20) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '法人代表',
  `address` varchar(200) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '公司地址',
  `region` varchar(15) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '所属地区',
  `city` varchar(15) character set utf8mb4 not null default '-' COMMENT '城市',
  `district` varchar(15) character set utf8mb4 not null default '-' COMMENT '区/县',
  `lat_long` varchar(80) character set utf8mb4 not null default '-' comment '经纬度，json',
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
  `actual_capital` varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '实缴资本',
  `taxpayer_code` varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '纳税人识别号',
  `organization_code` varchar(32) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '组织机构代码',
  `english_name` varchar(128) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '公司英文名',
  `authorization` varchar(50) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '登记机关',
  `homepage` varchar(30) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '公司官网',
  `used_name` varchar(128) CHARACTER SET utf8mb4 NOT NULL DEFAULT '-' COMMENT '公司曾用名',
  `gmt_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  `gmt_modify` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后操作时间',
  PRIMARY KEY (`id`),
#   index uni_key() comment '自行添加索引',
  unique key (`credit_code`, `register_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '企业信息表';

# drop table if exists `keyword`;
# create table `keyword` (
#   `id` int(11) unsigned not null auto_increment comment 'pk',
#   `name` varchar(40) character set utf8mb4 not null comment '关键字',
#   `is_crawled` tinyint(1) not null default false comment '是否已爬取',
#   `insert_time` timestamp not null default current_timestamp() comment '入库时间',
#   `is_deleted` tinyint(1) not null default false comment '是否放弃爬取'
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '关键字表';

