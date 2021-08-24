import csv

output = []

with open('iq_parts.csv') as inf:
    reader = csv.reader(inf)
    for row in reader:
        fname = row[0]
        with open(f"/Users/john/Documents/iq_ldraw_parts/parts/{fname}", "r") as partfile:
            output.append({"number":fname.split(".")[0], "name":partfile.readlines()[0].strip()})

print(output)

with open("partslist.csv", "w") as outf:
    writer = csv.DictWriter(outf, fieldnames=["number", "name"])

    for row in output:
        writer.writerow(row)

    outf.close()