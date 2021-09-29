import csv, subprocess, argparse, time
from os import path
from sys import stderr

# configure argument parser
parser = argparse.ArgumentParser(description="Batch-generate images of LDraw parts from a CSV file.")
parser.add_argument("-i", help="Input CSV file", default="", metavar="input.csv")
parser.add_argument("-o", help="Output directory (will be created if it doesn't exist)", default="output", metavar="path/to/dir")
parser.add_argument("--csv-template", help="Output a blank CSV file of the correct format to template.csv", action="count")
args = parser.parse_args()

# check if the --csv-template flag was included
if args.csv_template != None:
    header="File Name,Number,Color Code,Latitude,Longitude\n"
    if not path.exists("template.csv"):
        with open("template.csv", "w") as of:
            of.write(header)
            of.close()
    else:
        stderr.write("ERROR: template.csv already exists.\n")
    exit()

if args.i == "":
    stderr.write("ERROR: Must specify input file.\n")
    exit()

#create the directory for temporary ldraw files
tmp_dir_name = "ldr_files"
while path.exists(tmp_dir_name):
    tmp_dir_name += "_tmp"
subprocess.run(f"mkdir {tmp_dir_name}", shell=True)

# create the output directory
subprocess.run(f"mkdir {args.o}", shell=True)

# open and parse the CSV file
parts = []
with open(args.i) as csvfile:
    reader = csv.DictReader(csvfile)
    for part in reader:
        parts.append(part)

for part in parts:
    pn = part["Number"]
    fn = part["File Name"]
    color = part["Color Code"]
    lat = part["Latitude"]
    lon = part["Longitude"]

    # default values for color, lat, lon
    if color == "": color = 0
    if lat == "": lat = 0
    if lon == "": lon = 0
    print(color, lat, lon)

    # create a temporary ldr file which has the part in it (required to make leocad zoom extents work properly)
    with open(f"{tmp_dir_name}/{pn}.ldr", "w") as tmpldr:
        tmpldr.write(f"1 {color} 0 0 0 1 0 0 0 1 0 0 0 1 {fn}")
        tmpldr.close()
    
    # generate the image for this part
    subprocess.run(f"LeoCAD -i {args.o}/{pn}.png -w 1000 -h 1000 --camera-angles {lat} {lon} ldr_files/{pn}.ldr", shell=True)

# time.sleep(5)
# delete the temporary ldraw files
subprocess.run(f"rm -r {tmp_dir_name}", shell=True)