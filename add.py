"""A simple API to enable adding two numbers together"""
import hug

@hug.get()
@hug.cli()
def add(number_1: hug.types.number, number_2: hug.types.number):
    """Returns the result of adding number_1 to number_2"""
    return number_1 + number_2

@hug.get(examples=['n1=8&n2=7', 'n1=21&n2=3'])
@hug.cli()
def multiply(n1: hug.types.number, n2: hug.types.number):
    """Returns the result of multiplying n1 with n2"""
    return n1 * n2

@hug.get(examples='order_id=e577ba20-d659-4c70-9c4d-0ba364bb35e7')
@hug.cli()
def get_fills(order_id: hug.types.text):
    """Returns a sample list of fills for a sample order"""
    return [{'created_at': '2017-09-19T20:24:28.032Z', 'trade_id': 4189002, 'product_id': 'BTC-EUR',
       'order_id': 'e577ba20-d659-4c70-9c4d-0ba364bb35e7', 'user_id': '5299b2b915457c9d54000288',
       'profile_id': '04656a4b-a9d2-4a22-9362-8550f5abac73', 'liquidity': 'M', 'price': '3263.08000000',
       'size': '0.00315624', 'fee': '0.0000000000000000', 'side': 'sell', 'settled': True},
      {'created_at': '2017-09-19T20:24:18.017Z', 'trade_id': 4189001, 'product_id': 'BTC-EUR',
       'order_id': 'e577ba20-d659-4c70-9c4d-0ba364bb35e7', 'user_id': '5299b2b915457c9d54000288',
       'profile_id': '04656a4b-a9d2-4a22-9362-8550f5abac73', 'liquidity': 'M', 'price': '3263.08000000',
       'size': '0.97684376', 'fee': '0.0000000000000000', 'side': 'sell', 'settled': True},
      {'created_at': '2017-09-19T20:23:36.338Z', 'trade_id': 4188998, 'product_id': 'BTC-EUR',
       'order_id': 'e577ba20-d659-4c70-9c4d-0ba364bb35e7', 'user_id': '5299b2b915457c9d54000288',
       'profile_id': '04656a4b-a9d2-4a22-9362-8550f5abac73', 'liquidity': 'M', 'price': '3263.08000000',
       'size': '0.47000000', 'fee': '0.0000000000000000', 'side': 'sell', 'settled': True}]

if __name__ == '__main__':
    add.interface.cli()
