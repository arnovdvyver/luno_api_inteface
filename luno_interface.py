from luno_python.client import Client

with open("pass.txt") as myfile:
    keys = (myfile.readline()).split(" ")

user = Client(api_key_id=keys[0], api_key_secret=keys[1])

def show_wallets(current_user):
    """Retrieve user asset balances"""
    data = current_user.get_balances()['balance']
    for wallet in data:
        print(f'{wallet["asset"]} - {wallet["balance"]}')
    print('\n\n')


def show_tickers(current_user):
    """Retrieve exchange tickers - pairs with ZAR only"""
    data = user.get_tickers()['tickers']
    for ticker in data:
        if (ticker["pair"])[-3:] == 'ZAR':
            print(f'{ticker["pair"]} - {ticker["bid"]}')
    print('\n\n')


def get_accountid(current_user, base_asset):
    """Retrieve account_id of asset for user"""
    data = current_user.get_balances()['balance']
    for wallet in data:
        if wallet['asset'] == base_asset.upper():
            return wallet['account_id']

def buy_order(current_user, counter_trade):
    """Place market order"""
    asset = counter_trade
    buy_volume = 123 #float
    acc_id = int(get_accountid(current_user, asset)) #integer

    #current_user.post_market_order('BTCZAR', type=asset, counter_account_id=acc_id, counter_volume=buy_volume)
    print(f'you are buying with {buy_volume} of {asset} in the BTCZAR mark')

def sell_order(current_user, base_trade):
    """Place market order"""
    asset = base_trade
    buy_volume = 123  # float
    acc_id = int(get_accountid(current_user, asset))  # integer

    current_user.post_market_order('BTCZAR', type=asset, base_account_id=acc_id, base_volume=buy_volume)
    pass

def main():
    app_active = True

    while (app_active):
        menu = ['View Markets (1)', 'View Wallet Balances (2)', 'Place Buy Order(3)', "Quit (Q/q)"]

        print("===== LUNO ACCOUNT =====")
        for option in menu:
            print(option)

        user_select = input()
        if user_select == '1':
            show_tickers(user)

        elif user_select == '2':
            show_wallets(user)

        elif user_select == '3':
            buy_order(user, 'ZAR')

        elif user_select == 'q' or user_select == 'Q':
            app_active = False

        else:
            print("Invalid Selection made, please try again.")
main()