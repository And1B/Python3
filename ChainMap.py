
year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

from collections import ChainMap

profit_map = ChainMap(*year_profit_data)

def get_profits(chainmap):
  profit = 0
  holiday_profit = 0
  for key, value in chainmap.items():
    if not 'holiday' in key:
      profit += value
    elif 'holiday' in key:
      holiday_profit += value
  return profit, holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

for item in new_months_data:
  profit_map = profit_map.new_child(item)
current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)

year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit
