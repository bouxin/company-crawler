DROP TABLE IF EXISTS `company`;
CREATE TABLE `company` (
  `id` int(11) unsigned not NULL AUTO_INCREMENT primary key COMMENT 'PK',
  `name` varchar(128) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '公司名',
  `representative` varchar(40) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '法人代表',
  `address` varchar(200) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '公司地址',
  `region` varchar(15) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '所属地区(省)',
  `city` varchar(15) character set utf8mb4  null default '-' COMMENT '城市',
  `district` varchar(15) character set utf8mb4  null default '-' COMMENT '区/县',
  `geoloc` varchar(80) character set utf8mb4  null default '-'
  comment '经纬度，json -> {"lat": "30.18484477830133", "long": "120.06383340659741"}',
  `biz_status` varchar(20) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '经营状态',
  `credit_code` varchar(32) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '统一社会信用代码',
  `register_code` varchar(32) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '注册号',
  `phone` varchar(20) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '电话',
  `email` varchar(50) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '邮箱',
  `setup_time` varchar(20)  NULL DEFAULT '-' COMMENT '成立时间',
  `industry` varchar(64) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '所属行业',
  `biz_scope` varchar(1200) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '经营范围',
  `company_type` varchar(32) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '公司类型',
  `registered_capital` varchar(32) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '注册资本',
  `actual_capital` varchar(32) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '实缴资本',
  `taxpayer_code` varchar(32) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '纳税人识别号',
  `organization_code` varchar(32) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '组织机构代码',
  `english_name` varchar(128) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '公司英文名',
  `authorization` varchar(64) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '登记机关',
  `homepage` varchar(64) CHARACTER SET utf8mb4 NULL DEFAULT '-' COMMENT '公司官网',
  `used_name` varchar(500) CHARACTER SET utf8mb4  NULL DEFAULT '-' COMMENT '公司曾用名',
  `search_key` varchar(64) character set utf8mb4  null default '-' comment '搜索关键字',
  `create_at` timestamp not NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  `modify_at` timestamp DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后操作时间',
#   index un_key() comment '联合索引',
  unique key uq_credit_reg_code(`credit_code`, `register_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '企业信息表';

# 股东信息
drop table if exists `dim_shareholder`;
create table `dim_shareholder`(
    `id` integer not null primary key auto_increment comment 'pk',
    `credit_code` varchar(255) default null comment '企业社会信用代码',
    `name` varchar(255) default null comment '股东名称',
    `alias` varchar(255) default null comment '别称',
    `avatar` varchar(255) default null comment '股东头像',
    `control_ratio` varchar(255) default null comment '股东控股比例',
    `tags` json default null comment '股东信息',
    constraint unique index unq_index(`credit_code`, `name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '企业股东信息表';

drop table if exists `dim_company_manager`;
create table `dim_company_manager`(
    `id` integer not null primary key auto_increment comment 'pk',
    `credit_code` varchar(255) default null comment '企业社会信用代码',
    `name` varchar(255) default null comment '企业高管名称',
    `titles` json default null comment '高管title',
    `manager_type` varchar(255) default null comment '高管类型',
    constraint unique index unq_index(`credit_code`, `name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '企业高管信息表';

drop table if exists `province`;
create table `province`(
  `id` integer unsigned not null primary key auto_increment comment 'pk',
  `simple` char(3)  null default 'CN' comment '省份拼音简写',
  `code` varchar(6)  null default '000000' comment '全国代码',
  `name` varchar(10)  null default '全国' comment '省份中文',
  index idx_code(`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '地区省份表';

drop table if exists `city`;
create table `city`(
  `id` integer unsigned not null primary key auto_increment comment 'pk',
  `parent` varchar(6)  null comment '父级省',
  `code` varchar(6)  null comment '市、区级代码',
  `name` varchar(10)  null comment '市、区级名',
  index un_key(`parent`, `code`)
) ENGINE = InnoDB default CHARSET = utf8mb4 COMMENT '市区级表';

# drop table if exists `keyword`;
# create table `keyword` (
#   `id` int(11) unsigned not null auto_increment primary key comment 'pk',
#   `name` varchar(40) character set utf8mb4  null comment '关键字',
#   `status` unsigned tinyint(1)  null default 0 comment '状态, 0: 未爬取，1: 爬取中，2: 已爬取，3: 爬取失败, 4: 丢弃',
#   `insert_at` timestamp not null default current_timestamp() comment '添加时间'
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT '关键字表';

