from datetime import datetime, timedelta
from parse_race_list import load_list
import time

def get_summary_list(start_date, end_date):
    result = []
    for i in range((end_date - start_date).days + 1):
        d = start_date + timedelta(i)
        result.append(d.strftime("%Y%m%d"))
    return result

if __name__ == '__main__':
    start_date_str = "20200601"
    end_date_str = "20200731"
    out_path = "../summary/{}_{}.txt".format(start_date_str, end_date_str)

    total_end_date = datetime.strptime(end_date_str, "%Y%m%d")
    start_date = datetime.strptime(start_date_str, "%Y%m%d")
    end_date = datetime.strptime(end_date_str, "%Y%m%d")

    interval = 10 # days
    result = set()
    period_end_date = start_date + timedelta(days=interval)
    while start_date < total_end_date:
        date_list = get_summary_list(start_date, end_date)
        result = result.union(load_list(date_list))
        start_date = end_date + timedelta(days=1)
        period_end_date = period_end_date + timedelta(days=interval)
        print(start_date)
        time.sleep(2)

    with open(out_path, "w") as f:
        f.write("\n".join(result))
