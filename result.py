def main():
    dollars = dollars_to_float(input("How much was the meal? ").rstrip())
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # TODO
    d = d.strip("$")
    return float(d)

def percent_to_float(p):
    # TODO
    p = p.strip("%")
    return float(p) / 100

main()