# export_barcodes_hack

From the UC Jaggaer Stocktake - Scan Functions quick user guide:


> Generate Barcodes for Sublocation:
> 4. Under Locations, go manage sub locations
> 5. Select the desired room and select export sublocations
> 6. Convert sublocation barcode coulmn "xxxxx" into barcodes using __external application__

This script is one option for the external application to generate a pdf of the sublocation barcodes.

## Run using python
1. clone repository, navigate to the folder
2. Run the python script from the command line:
```
pip install -r requirements.txt
python export_barcodes.py
```

## Run using the supplied exe
download and double click it. 

N.B. exe generated by:
```
pyinstaller export_barcodes.py --collect-all barcode --onefile --noconsole
```

## How to use

- Select the csv file of barcodes that was generated by step 5 by clicking on the top "select csv" button
- Save and export the pdf file by clicking the "generate pdf" button

