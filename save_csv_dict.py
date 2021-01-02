import csv

with open('top_cities_dict.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, ['rank', 'city', 'population'])
    writer.writeheader()

    writer.writerows([
        ['1','上海','24150000'],
        ['2','からち','23500000'],
        ['3','北京','21516000'],
        ['4','天津','14722100'],
        ['5','イスタンブル','14160467'],
    ])
    