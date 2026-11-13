# Q2 - Loops that Count Attempts: OTP verification

def verify_with_while(correct_otp, entries):
    attempts = 0
    max_attempts = 3
    locked = False
    for entry in entries:
        if attempts >= max_attempts:
            locked = True
            break
        if entry.strip() == "":
            print("Blank entry: not counted.")
            continue
        attempts += 1
        if entry == correct_otp:
            print("OTP verified.")
            break
        print(f"Wrong OTP. Attempts used: {attempts}")
    else:
        if attempts == max_attempts:
            locked = True
    if locked:
        print("Account locked for 30 minutes.")
    elif attempts < max_attempts:
        print("Verification session ended.")
    return attempts, locked


def verify_with_for(correct_otp, entries):
    attempts = 0
    for entry in entries:
        if entry.strip() == "":
            print("Blank entry: not counted.")
            continue
        attempts += 1
        if entry == correct_otp:
            print("OTP verified.")
            break
        print(f"Wrong OTP. Attempts used: {attempts}")
    else:
        if attempts == 3:
            print("Account locked for 30 minutes.")
        else:
            print("Verification session ended.")
    return attempts


def verify_with_security(correct_otp, entries, security_verified):
    max_attempts = 3
    if security_verified:
        # pass is a placeholder for an optional additional verification action.
        pass
        max_attempts += 2
    attempts = 0
    for entry in entries:
        if entry.strip() == "":
            continue
        attempts += 1
        if entry == correct_otp:
            print("OTP verified.")
            break
        if attempts == max_attempts:
            print("Account locked for 30 minutes.")
            break
    return attempts


print("WHILE LOOP DEMO")
verify_with_while("4821", ["", "1111", "2222", "4821"])
print("\nFOR LOOP DEMO (three wrong entries)")
verify_with_for("4821", ["1000", "2000", "3000"])
print("\nCHANGED CONDITION: security question verified, five attempts")
verify_with_security("4821", ["1000", "2000", "3000", "4000", "5000"], True)
