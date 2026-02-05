import math

def initial_buy(broker, prev_close, unit_amt_buy):
    print("\n[STEP 1] 최초 매수 체크")

    if broker.get_position_qty("TQQQ") > 0:
        print("[SKIP] 이미 보유 중 → 최초 매수 스킵")
        return

    init_price = prev_close * 1.12
    init_qty = math.floor(unit_amt_buy / init_price)

    print(f"[INIT BUY] 전일종가={prev_close}")
    print(f"[INIT BUY] Init_Buy_Price = {init_price:.2f}")
    print(f"[INIT BUY] Init_Order_Qty = {init_qty}")

    broker.buy_loc("TQQQ", init_price, init_qty)

    print("[DEFENSE BUY] 급락 대비 추가 매수 시작")
    for i in range(3):
        below_price = unit_amt_buy / (init_qty + i + 1)
        print(f"[DEFENSE BUY] Below_Price={below_price:.2f}, Qty=1")
        broker.buy_loc("TQQQ", below_price, 1)

def pre_buy(broker, unit_amt_buy, star_price, avg_price, prev_close):
    print("\n[STEP 2] 전반전 매수 (Pre_Buy)")

    pre_price = star_price - 0.01
    if prev_close * 1.12 < pre_price :
        pre_price = prev_close * 1.12
        print("전일 급락으로 으로 인해 큰수가 별가격보다 낮아서 큰수 LOC로 매수한다.")
    half_amt = unit_amt_buy / 2

    pre_buy_qty = math.floor(half_amt / pre_price)
    print(f"[PRE BUY] Star_Price={star_price:.2f}")
    print(f"[PRE BUY] Pre_Price={pre_price:.2f}")
    print(f"[PRE BUY] Pre_Buy_Qty={pre_buy_qty}")

    broker.buy_loc("TQQQ", pre_price, pre_buy_qty)

    pre_avg_qty = math.floor((unit_amt_buy / avg_price) - pre_buy_qty)
    print(f"[PRE AVG BUY] Avg_Price={avg_price}")
    print(f"[PRE AVG BUY] Pre_Avg_Buy_Qty={pre_avg_qty}")

    broker.buy_loc("TQQQ", avg_price, pre_avg_qty)

    print("[DEFENSE BUY] 전반전 하락 대비")
    for i in range(3):
        below_price = unit_amt_buy / (pre_buy_qty + pre_avg_qty + i + 1)
        print(f"[DEFENSE BUY] Below_Price={below_price:.2f}")
        broker.buy_loc("TQQQ", below_price, 1)

def after_buy(broker, unit_amt_buy, star_price):
    print("\n[STEP 3] 후반전 매수 (After_Buy)")

    after_price = star_price - 0.01
    after_qty = math.floor(unit_amt_buy / after_price)

    print(f"[AFTER BUY] After_Buy_Price={after_price:.2f}")
    print(f"[AFTER BUY] After_Buy_Qty={after_qty}")

    broker.buy_loc("TQQQ", after_price, after_qty)

    for i in range(3):
        below_price = unit_amt_buy / (after_qty + i + 1)
        print(f"[DEFENSE BUY] Below_Price={below_price:.2f}")
        broker.buy_loc("TQQQ", below_price, 1)
