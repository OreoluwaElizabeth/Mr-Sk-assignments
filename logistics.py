def calculate_payment(successful_deliveries):
    base_pay = 5000

    if successful_deliveries < 50:
        amount_per_parcel = 160
    elif successful_deliveries <= 59:
        amount_per_parcel = 200
    elif successful_deliveries <= 69:
        amount_per_parcel = 250
    else:
        amount_per_parcel = 500

    total_payment = successful_deliveries * amount_per_parcel + base_pay
    return total_payment