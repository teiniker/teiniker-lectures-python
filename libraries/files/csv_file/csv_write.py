import csv

with open('tmp.csv', 'w', encoding="utf-8") as file:
    csv_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    csv_writer.writerow([0, 3.14159, "PI"])
    csv_writer.writerow([1, 1.41421, "sqrt(2)"])
    csv_writer.writerow([2, 1.73205, "sqrt(3)"])
