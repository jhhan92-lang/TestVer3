from strategy.calculator import *
from strategy.buy_strategy import *
from broker.mock_broker import MockBroker
from strategy.sell_strategy import *   # ⭐ 이 줄 추가


# 테스트용 계좌 상태
broker = MockBroker(
    qty=13000,
    avg_price=50.5,
    total_buy_amount=656500
)

TOTAL_BUDGET = 10_000_000
MAX_T = 40
TARGET_YIELD_P = 0.20
PREV_CLOSE = 62.0

print("\n========== TQQQ AUTO TRADER TEST ==========")

unit_amt = calc_unit_amt(TOTAL_BUDGET, MAX_T)
semo = calc_semo(TARGET_YIELD_P, MAX_T)
cur_t = calc_cur_t(broker.get_total_buy_amount("TQQQ"), unit_amt)
star_p = calc_star_p(TARGET_YIELD_P, semo, cur_t)
star_price = calc_star_price(broker.get_avg_price("TQQQ"), star_p)

initial_buy(broker, PREV_CLOSE, unit_amt)

if cur_t <= MAX_T / 2:
    pre_buy(broker, unit_amt, star_price, broker.get_avg_price("TQQQ"), PREV_CLOSE)
else:
    after_buy(broker, unit_amt, star_price)

Sell_Process(broker, cur_t, MAX_T,star_price, TARGET_YIELD_P)

print("\n========== TEST END ==========")
