DROP TABLE IF EXISTS `horse`;

create table IF not exists `horse`
(
 `id`               VARCHAR(20) NOT NULL,
 `name`          VARCHAR(20) NOT NULL,
 `birth`           VARCHAR(20) NOT NULL,
 `trainer`        VARCHAR(20) NOT NULL,
 `owner`         VARCHAR(20) NOT NULL,
 `breeder`       VARCHAR(20) NOT NULL,
 `hometown`   VARCHAR(20) NOT NULL,
 `price`           INT(20),
 `get_price`     INT(20),
 `created_at`   Datetime DEFAULT NULL,
 `updated_at`  Datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
