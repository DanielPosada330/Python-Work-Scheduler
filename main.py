import pandas as pd
import openpyxl as xl
import seaborn as sns
from matplotlib import pyplot
from IPython.core.display_functions import display
from ipywidgets import widgets

# Variables for amount of officers per shift, + number of lanes open
officer_Number = input("Enter number of officers: ")
lanes_Opened = input("Enter number of lanes: ")

# Variable for choosing shift time

chosen_Shift = input("Enter shift number from the following: "
                     "1) Midnight 0000-0800\n"
                     "2) 6am-2pm\n "
                     "3) Day 0800-1600\n"
                     "4) 2pm-10pm\n"
                     "5) Evening 1600-2400")

# Create columns for spreadsheet for each of the five shifts
# Midnight 0000-0800, Day 0800-1600, and Evening 1600-2400
# Middle shifts of 0600-1400 & 1400-2200

midnight_Shift = ["0000-0030", "0030-0100", "0100-0130", "0130-0200", "0200-0230", "0230-0300", "0300-0330", "0330-0400"
                                                                                                             "0400-0430"
                  "0430-0500", "0500-0530", "0530-0600", "0600-0630", "0630-0700", "0700-0730",
                  "0730-0800"]

day_shift = ["0800-0830", "0830-0900", "0900-0930", "0930-1000", "1000-1030", "1030-1100", "1100-1130", "1130-1200"
                                                                                                        "1200-1230",
             "1230-1300", "1300-1330", "1330-1400", "1400-1430", "1430-1500", "1500-1530", "1530-1600"]

evening_Shift = ["1600-1630", "1630-1700", "1700-1730", "1730-1800", "1800-1830", "1830-1900", "1900-1930", "1930-2000",
                 "2000-2030", "2030-2100", "2100-2130", "2130-2200", "2200-2230", "2230-2300", "2300-2330", "2330-2400"]

day_Middle_Shift = ["0600-0630", "0630-0700", "0700-0730", "0730-0800", "0800-0830", "0830-0900", "0900-0930",
                    "0930-1000", "1000-1030", "1030-1100", "1100-1130", "1130-1200"
                                                                        "1200-1230", "1230-1300", "1300-1330",
                    "1330-1400"]

evening_Middle_Shift = ["1400-1430", "1430-1500", "1500-1530", "1530-1600", "1600-1630", "1630-1700", "1700-1730",
                        "1730-1800", "1800-1830", "1830-1900", "1900-1930", "1930-2000",
                        "2000-2030", "2030-2100", "2100-2130", "2130-2200"]


# Variable for lane numbers
vehicle_Lanes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

# Variable to hold commitments
commitment_Types = [vehicle_Lanes, "B", "B*", "Choke", "OPs 1", "OPs 2", ]

# Dataframes holding each shift to write to excel
df_Midnight_Shift = pd.DataFrame([["a"]], index=[officer_Number], columns=[midnight_Shift])
