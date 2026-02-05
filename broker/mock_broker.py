# broker/mock_broker.py

class MockBroker:
    def __init__(self, qty, avg_price, total_buy_amount):
        self.qty = qty
        self.avg_price = avg_price
        self.total_buy_amount = total_buy_amount

    def get_position_qty(self, symbol):
        print(f"[ACCOUNT] {symbol} 보유수량 = {self.qty}")
        return self.qty

    def get_avg_price(self, symbol):
        print(f"[ACCOUNT] {symbol} 평균단가 = {self.avg_price}")
        return self.avg_price

    def get_total_buy_amount(self, symbol):
        print(f"[ACCOUNT] {symbol} 매수누적액 = {self.total_buy_amount}")
        return self.total_buy_amount

    def buy_loc(self, symbol, price, qty):
        print(f"[ORDER][BUY][LOC] {symbol} | 가격={price:.2f} | 수량={qty}")

    def sell_loc(self, symbol, price, qty):
        print(f"[ORDER][SELL][LOC] {symbol} | 가격={price:.2f} | 수량={qty}")

    def sell_MOC(self, symbol, price, qty):
        print(f"[ORDER][SELL][MOC] {symbol} | 가격={price:.2f} | 수량={qty}")

    def sell_target_price(self, symbol, price, qty):
        print(f"[ORDER][SELL][지정가] {symbol} | 가격={price:.2f} | 수량={qty}")
