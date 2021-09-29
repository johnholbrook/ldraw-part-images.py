# ldraw-part-images.py

Python script for batch-rendering images of individual LDraw parts from CSV input.

Requires [LeoCAD](https://www.leocad.org) to be isntalled and accessible from the command line – in macOS, I did this by adding `/Applications/LeoCAD.app/Contents/MacOS` to my `$PATH`.

## Example usage
```
$ python3 generate-images.py --csv-template
$ cat template.csv
File Name,Number,Color Code,Latitude,Longitude
```

```
$ python3 generate_images.py -i super-kit-tray.csv -o images
```

```
$ python3 generate_images.py --help
usage: generate_images.py [-h] [-i input.csv] [-o path/to/dir] [--csv-template]

Batch-generate images of LDraw parts from a CSV file.

optional arguments:
  -h, --help      show this help message and exit
  -i input.csv    Input CSV file
  -o path/to/dir  Output directory (will be created if it doesn't exist)
  --csv-template  Output a blank CSV file of the correct format to template.csv
```
