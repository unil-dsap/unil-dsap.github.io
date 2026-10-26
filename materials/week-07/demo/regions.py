# regions.py — sales by region (review item 11)
def parse(line):
    region, amount = line.split(";")
    return region, float(amount)

def totals_by_region(lines):
    totals = {}
    for line in lines:
        region, amount = parse(line)
        if region in totals:
            totals[region] = totals[region] + amount
        else:
            totals[region] = amount
    return totals

lines = ["west;120.5", "east;80", "west;40", "north;15.5", "east;20"]
result = totals_by_region(lines)
for region in result:
    print(region, result[region])
print(len(result), "regions")
