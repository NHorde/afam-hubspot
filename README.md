# AFAM HubSpot

# Goal
Backfilling data from the AFAM account

## Steps
### Manual

### Script
Create and activate a virtual environment (Mac):
```shell script
python -m venv env  
source env\bin\activate
```

Install requirements
``` shell script
pip install -r requirements.txt
```
Run script
```shell script
python main.py
```
The result will be called `backfill_{date}.csv` and will be placed in the `results` folder
