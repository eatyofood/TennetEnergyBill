# === Energy Bill Calculator === 
For quickly determining  each tennets power consumption times the price per watt. 


## Installation

####  Install script
`git clone {repo} `

#### Install Dependencies
`pip install -r requirements.txt`



## To Run Script

#### from the repo-directory
`python go.py`

#### to run the notebook version with Plots
`python note-go.py`

##### ( linux and mac users may have to use `pip3` & `python3` ) 


### 1) First Run Through 
- it will ask the names of the tennets on a loop until you type `done` and press enter
- it uses the givin list of tennets to generate a 'refrence_sheet.csv'
- you only have to do this the first time you run through 
    - from then on if you want to add or remove a tennet add or remove a row from `refrence_sheet.csv`


### 2) Then Enter Power Bill & Total watts according to the meter 
- enter power bill
- watt usage
- and each tennets power consumption once prompted

### 3) Output Bill
- outputs a pandas DataFrame and Saves a csv file with the current days date. 
    - if you run it twice in the same day it will overwrite the sheet 

# Corrisponding Colab Link
`https://colab.research.google.com/drive/1xgJgkXzs_rkpOtWY_v3qfSwnYibX5ujt?usp=sharing`