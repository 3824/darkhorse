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

create table If not exists 'race_result'
(
-- 1行 1レースの1馬ごとにして、index張っておくと。
 `race_id`               VARCHAR(20) NOT NULL,
 `rank`                   INT(20) NOT NULL,
 `frame_number`     INT(20) NOT NULL,
 `horse_number`     INT(20) NOT NULL,
 `horse_name`         VARCHAR(20) NOT NULL,
 `horse_gender`       VARCHAR(20) NOT NULL,
 `horse_age`            INT(20) NOT NULL,
 `time`                    INT(20) NOT NULL,
 `diff`                     FLOAT(20) NOT NULL,
 `weight`                 INT(20) NOT NULL,
 `weight_diff`          INT(20) NOT NULL,
 `trainer_stable`       VARCHAR(20) NOT NULL,
 `trainer_name`        VARCHAR(20) NOT NULL,
)

create table if not exists 'race_info'
(
 `race_id`                VARCHAR(20) NOT NULL,
 `cource`                 VARCHAR(20) NOT NULL,
 `direction`              VARCHAR(20) NOT NULL,
 `distance`               INT(20) NOT NULL,
 `weather`               VARCHAR(20) NOT NULL
 `condition`             VARCHAR(20) NOT NULL
)