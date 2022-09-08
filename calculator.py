import json
import sys
from prettytable import PrettyTable

def main(fuelCons):
    f = open('config.json', 'r')

    data = json.load(f)

    table = PrettyTable(['Route / Week', 'Km', 'Times', 'TotalKm', 'l/100Km', 'Liters', 'Cost'])
    totals = [0, 0, 0]
    for rt in data['routes']:
        print(rt)
        totalDist = rt['distance'] * rt['times']
        fuel = totalDist / 100 * fuelCons
        fuelCost = fuel * data['fuelCost']

        totals[0] += totalDist
        totals[1] += fuel
        totals[2] += fuelCost

        table.add_row([rt['name'], rt['distance'], rt['times'], totalDist, fuelCons, f'{fuel:.2f}', f'{fuelCost:.2f} CHF']) 

    print(table)

    totalTable = PrettyTable(['Totals', 'Km', 'Liters', 'Cost'])
    totalTable.add_row(['Week', totals[0], f'{totals[1]:.2f}', f'{totals[2]:.2f} CHF'])
    totalTable.add_row(['Month', totals[0] * 4, f'{totals[1] * 4:.2f}', f'{totals[2] * 4:.2f}'])
    totalTable.add_row(['Year wo/ Vacation', totals[0] * 52, f'{totals[1] * 52:.2f}', f'{totals[2] * 52:.2f}'])
    totalTable.add_row(['Year w/ Vacation', totals[0] * 47, f'{totals[1] * 47:.2f}', f'{totals[2] * 47:.2f}'])

    print(totalTable)

    f.close()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(float(sys.argv[1]))
    else:
        main(float(input('What\'s the average fuel consumption / 100Km ? > ')))

