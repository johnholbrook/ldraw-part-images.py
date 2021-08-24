import csv, subprocess

subprocess.run("mkdir images", shell=True)
subprocess.run("mkdir ldr_files", shell=True)

parts = []

# open and parse the CSV file
with open("partslist.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for part in reader:
        parts.append(part)

for part in parts:
    pn = part["Number"]
    fn = part["File Name"]
    color = part["Color Code"]

    # create a temp.ldr file which has the part in it (required to make leocad zoom extents work properly)
    with open(f"ldr_files/{pn}.ldr", "w") as tmpldr:
        tmpldr.write(f"1 {color} 0 0 0 1 0 0 0 1 0 0 0 1 {fn}")
        tmpldr.close()
    
    # generate the image for this part
    # subprocess.run(f"LeoCAD -i output/{pn}.png -w 1000 -h 1000 --stud-style 6 --line-width 5 --edge-color '#FF000000' tmp/{pn}.ldr", shell=True)
    subprocess.run(f"LeoCAD -i images/{pn}.png -w 1000 -h 1000 ldr_files/{pn}.ldr", shell=True)
        