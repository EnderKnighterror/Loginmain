import csv

field_names = ['Name', 'Keeper Y/N', 'Fish Y/N', 'Points if kept', 'Points if released']

Fish = [
    {'Name': 'King George Whiting', 'Keeper Y/N': 'Y', 'Fish Y/N': 'Y', 'Points if kept': 50, 'Points if released': 70},
    {'Name': 'Lost Bait', 'Keeper Y/N': 'N', 'Fish Y/N': 'N', 'Points if kept': -10, 'Points if released': 0},
    {'Name': 'Small Mulloway', 'Keeper Y/N': 'N', 'Fish Y/N': 'Y', 'Points if kept': -10, 'Points if released': 10},
    {'Name': 'Snapper', 'Keeper Y/N': 'Y', 'Fish Y/N': 'Y', 'Points if kept': 30, 'Points if released': 40},
    {'Name': 'Large Mullet', 'Keeper Y/N': 'Y', 'Fish Y/N': 'Y', 'Points if kept': 20, 'Points if released': 20},
    {'Name': 'King George Whiting', 'Keeper Y/N': 'N', 'Fish Y/N': 'Y', 'Points if kept': 5, 'Points if released': -5},
]

with open('Fish.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(Fish)
