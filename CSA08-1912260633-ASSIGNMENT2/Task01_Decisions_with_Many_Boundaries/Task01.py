# Q1 - Decisions with Many Boundaries
# State Electricity Subsidy Eligibility

def separate_if_rules(units, ration_card, age_above_80):
    """Intentionally demonstrates the overlapping-if bug."""
    decisions = []
    if units <= 100:
        decisions.append("FULL SUBSIDY")
    # BUG: this condition also includes units <= 100.
    if units <= 200 and ration_card:
        decisions.append("PARTIAL SUBSIDY")
    if units > 200 and age_above_80:
        decisions.append("SPECIAL SUBSIDY")
    if not decisions:
        decisions.append("NO SUBSIDY")
    return decisions


def correct_rules(units, ration_card, age_above_80):
    """Mutually exclusive decisions using if-elif-else."""
    if units <= 100:
        return "FULL SUBSIDY"
    elif 101 <= units <= 200 and ration_card:
        return "PARTIAL SUBSIDY"
    elif units > 200 and age_above_80:
        return "SPECIAL SUBSIDY"
    else:
        return "NO SUBSIDY"


households = [
    ("H1", 100, False, False),
    ("H2", 101, True, False),
    ("H3", 200, True, False),
    ("H4", 201, False, True),
    ("H5", 150, False, False),
    ("H6", 250, False, False),
    ("H7", 80, True, False),
    ("H8", 220, True, False),
]

print("ID  Units  Ration  Age>80  Separate-if result             Correct result")
for hid, units, ration, senior in households:
    old = ", ".join(separate_if_rules(units, ration, senior))
    new = correct_rules(units, ration, senior)
    print(f"{hid:<3} {units:<6} {str(ration):<7} {str(senior):<7} {old:<30} {new}")

print("\nDesign decision: if-elif-else is preferred because only one subsidy decision")
print("should be returned. Chained comparison 101 <= units <= 200 is readable.")
