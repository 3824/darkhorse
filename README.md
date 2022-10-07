
MySQL立ち上げ  
`docker-compose up`  
テーブル初期化  
`setup_db.sh`


### 手順

1. dark_horse/scrape/parse_race_list.py
日付を指定して、その日のレース情報を取得する。
2. dark_horse\scrape\proceed_get_summary_list.py
上記のレース情報をまとめて取得してtxtに書き出す。日付ごとにレース一覧URLを書き出す。
3. dark_horse\scrape\parse_each_day_race.py
2で取得したある日付のレース一覧URLから、その日のレースURLを取得する。
in: https://db.netkeiba.com/race/sum/55/20210306/  
out: ['https://db.netkeiba.com/race/202155030611/', ...]
4. dark_horse\parse_race_result.py
in: 202035060701
out: MySQLにRaceInfo書き込む
5. dark_horse\scrape\parse_horse.py
in: https://db.netkeiba.com/horse/2018106461/
out: MySQLにHorse書き込む
6. TODO ~~馬ページから血統ページに飛んで血統情報を紐づける~~
　　馬ページの「血統」欄からデータ取得（2世帯前までくらいで）
7. 


