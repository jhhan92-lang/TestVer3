# strategy/calculator.py

def calc_unit_amt(total_budget, max_t):
    unit = total_budget / max_t
    print(f"[CALC] Unit_Amt_Buy = Total_Budget / Max_T = {unit:.2f}")
    return unit


def calc_semo(target_yield_p, max_t):
    semo = (target_yield_p * 2) / max_t
    print(f"[CALC] SeMo = (Target_Yield_P * 2) / Max_T = {semo:.4f}")
    return semo


def calc_cur_t(total_buy_amount, unit_amt_buy):
    cur_t = total_buy_amount / unit_amt_buy
    print(f"[CALC] Cur_T = 매수누적액 / Unit_Amt_Buy = {cur_t}")
    return cur_t


def calc_star_p(target_yield_p, semo, cur_t):
    star_p = target_yield_p - (semo * cur_t)
    print(f"[CALC] Star_P = {star_p:.4%}")
    return star_p


def calc_star_price(avg_price, star_p):
    star_price = avg_price * (1 + star_p)
    print(f"[CALC] Star_Price = Avg_Price * (1 + Star_P) = {star_price:.2f}")
    return star_price
