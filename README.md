*# py_export_icons v0.2

## How to install
To install required packages run this command
```
sudo pip3 install -r requirements.txt
```

## How to use
Just put your .svg files into /svg directory and run using ```python3 main.py```.
Exported to .png icons will be in ```dd_mm_YY_HH-MM-SS``` folder, but named using current datetime. Image with combined PNGS will be next to _main.py_.

## Settings and command-line arguments
```settings.json``` stores all customizable properties of an output file containing combined icons.

**RGB background color**
```
    background:{
        red:255,
        green:255,
        blue:255}
```
**Number of columns as an output**
```
columns: 15
```
**Number of rows as an output**
```
rows: 15
```
 **Height of single icon in an output image**
```
icon_height: 200
```
**Width of single icon in an output image**
```
icon_width: 200
```

### TODO
- [x] command line arguments
- [ ] logo in footer
- [ ] custom background
- [ ] custom icons color
- [ ] GUI?