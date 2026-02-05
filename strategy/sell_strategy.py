def Sell_Process(broker, cur_t, max_t, star_price,target_yield_p):
    print("\n[STEP 4] 매도 체크")
    if max_t - 1 <= cur_t <= max_t: #MOC 매도
        qty = broker.get_position_qty("TQQQ") // 4
        print(f"[MOC SELL] 매도수량={qty}")
        broker.sell_MOC("TQQQ", star_price, qty)
    else:
        qty = broker.get_position_qty("TQQQ") // 4
        print(f"[QUARTER SELL] 매도수량={qty}")
        broker.sell_loc("TQQQ", star_price, qty)
        print(f"[지정가 SELL] 매도수량={qty}")
        broker.sell_target_price("TQQQ", broker.avg_price*(1+target_yield_p), broker.qty - qty)



