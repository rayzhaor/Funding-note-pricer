
def calculate_funding_note(sofr, floating, currency, spot, swap_pts, months, scale=10000):
    """
    计算资金票据利率

    参数:
        sofr      : SOFR利率
        floating  : SOFR之上的浮动加点bps
        currency  : 票据币种
        spot      : 即期汇率
        swap_pts  : 掉期点
        months    : 票据期限
        scale     : 将掉期点转换为bps的缩放因子 (默认为10000 / 万分之一)
    """

    floating_rate = sofr + floating / scale * 100  # 将浮动加点转换为百分比

    swap_diff = swap_pts / scale

    relative_change = swap_diff / spot

    pct_change = relative_change * 100

    annualized_swap_yield = pct_change * (12 / months)

    note_rate = floating_rate + annualized_swap_yield

    return {
        "sofr": sofr,
        "floating": floating / scale,
        "currency": currency,
        "spot": spot,
        "swap_pts": swap_pts,
        "months": months,
        "scale": scale,
        "note_rate": note_rate
    }



def get_user_input():
    """
    获取用户输入参数
    """
    sofr = float(input("请输入 SOFR 利率 (例如 4.00): "))
    floating = float(input("请输入 SOFR 之上的浮动加点 (例如 20): "))
    currency = input("请输入票据币种 (例如 HKD): ")
    spot = float(input("请输入所选币种即期汇率 (例如 7.85): "))
    swap_pts = int(input("请输入掉期点 (例如 -50): "))
    months = int(input("请输入票据期限月数 (例如 1): "))
    scale = int(input("请输入缩放因子 (默认 10000): ") or 10000)

    return sofr, floating, currency, spot, swap_pts, months, scale



def print_result(result):
    """
    打印计算结果
    """
    print(f"SOFR: {result['sofr']}%")
    print(f"Currency: {result['currency']}")
    print(f"Spot Rate: {result['spot']}")
    print(f"Swap Points: {result['swap_pts']}")
    print(f"Months: {result['months']}")
    print(f"Scale: {result['scale']}")
    print(f"Funding Note Rate: {result['note_rate']:.2f}%") 



def main():
    """
    主函数
    """
    print()
    print("===================")
    print("票据定价计算器")
    print("===================")
    print()

    # get user input
    sofr, floating, currency, spot, swap_pts, months, scale = get_user_input()

    # calculate funding note rate
    result = calculate_funding_note(sofr, floating, currency, spot, swap_pts, months, scale)

    print_result(result)



if __name__ == "__main__":
    main()