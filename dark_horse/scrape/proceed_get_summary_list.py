from datetime import datetime, timedelta
from parse_race_list import load_list

def get_summary_list(start_date, end_date, out_path):
    start_d = datetime.strptime(start_date, "%Y%m%d")
    end_d = datetime.strptime(end_date, "%Y%m%d")

    result = []
    for i in range((end_d - start_d).days + 1):
        d = start_d + timedelta(i)
        result.append(d.strftime("%Y%m%d"))
    return result

if __name__ == '__main__':
    start_date = "20210301"
    end_date = "20210310"
    out_path = ""
    date_list = get_summary_list(start_date, end_date, out_path)
    sum_list = load_list(date_list)
    print(sum_list)
