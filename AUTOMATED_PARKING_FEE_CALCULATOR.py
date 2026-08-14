print("╔══════════════════════════════════════════╗")
print("║   🅿️  AUTOMATED PARKING FEE CALCULATOR    ║")
print("╚══════════════════════════════════════════╝")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
print("""Vehicle Type     Rate for First 2 Hours (Flat Hourly Rate)       Rate for Every Hour After (Subsequent Hours)            Maximum Total Cap (Daily Limit)
BIKE                 ₹10 per hour                                    ₹20 per hour                                             ₹500 maximum
CAR                   ₹20 per hour                                   ₹40 per hour                                             ₹500 maximum
TRUCK                ₹50 per hour                                    ₹100 per hour                                            ₹500 maximum""")

def parking_fee():
    vec=input("ENTER THE MODE OF VECHICLE: ").lower()
    hour=float(input("ENTER NO OF HOURS PARKED: "))
    fee=0
    if hour<=0:
        print("INVALID INPUT\nPLZ TRY AGAIN")
        return
    if vec=='bike':
        if hour<=2:
            fee1=hour*10
            fee+=fee1
        elif hour>2:
            rem_hour=hour-2
            fee1=10*2
            fee2=20*rem_hour
            fee+=fee1+fee2
    
    elif vec=='car':
        if hour<=2:
            fee1=hour*20
            fee+=fee1
        elif hour>2:
            rem_hour=hour-2
            fee1=20*2
            fee2=40*rem_hour
            fee+=fee1+fee2
            
    elif vec=='truck':
        if hour<=2:
            fee1=hour*50
            fee+=fee1
        elif hour>2:
            rem_hour=hour-2
            fee1=50*2
            fee2=100*rem_hour
            fee+=fee1+fee2
    else:
        print("INVAILD VECHICLE")
        return
    if fee>=500:
        fee=500
        print("Maximum Total Cap (Daily Limit)")
        print("₹",fee,"IS THE AMOUNT TO PAID FOR PARKING")
    else:
        print("₹",fee,"IS THE AMOUNT TO BE PAID")
        
parking_fee()
