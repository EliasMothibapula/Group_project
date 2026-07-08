import io
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Provide the raw structural dataset
csv_data = """Person ID,Gender,Age,Occupation,Sleep Duration,Quality of Sleep,Physical Activity Level,Stress Level,BMI Category,Blood Pressure,Heart Rate,Daily Steps,Sleep Disorder
1,Male,27,Software Engineer,6.1,6,42,6,Overweight,126/83,77,4200,None
2,Male,28,Doctor,6.2,6,60,8,Normal,125/80,75,10000,None
3,Male,28,Doctor,6.2,6,60,8,Normal,125/80,75,10000,None
4,Male,28,Sales Representative,5.9,4,30,8,Obese,140/90,85,3000,Sleep Apnea
5,Male,28,Sales Representative,5.9,4,30,8,Obese,140/90,85,3000,Sleep Apnea
6,Male,28,Software Engineer,5.9,4,30,8,Obese,140/90,85,3000,Insomnia
7,Male,29,Teacher,6.3,6,40,7,Obese,140/90,82,3500,Insomnia
8,Male,29,Doctor,7.8,7,75,6,Normal,120/80,70,8000,None
9,Male,29,Doctor,7.8,7,75,6,Normal,120/80,70,8000,None
17,Female,29,Nurse,6.5,5,40,7,Normal Weight,132/87,80,4000,Sleep Apnea
135,Male,38,Lawyer,7.3,8,60,5,Normal,130"""

# Read the data into a Pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# 2. Standardize categorical inconsistencies ("Normal Weight" -> "Normal")
df["BMI Category"] = df["BMI Category"].replace("Normal Weight", "Normal")

# Fill missing categorical fields with standard defaults
df["Sleep Disorder"] = df["Sleep Disorder"].fillna("None")

# Drop critical records if they completely lack clean sleep values
df.dropna(subset=["Sleep Duration", "Quality of Sleep"], inplace=True)

# Split Blood Pressure text ("120/80") into individual numeric tracking columns
bp_split = df["Blood Pressure"].str.split("/", expand=True)
df["Systolic BP"] = pd.to_numeric(bp_split[0], errors='coerce')
df["Diastolic BP"] = pd.to_numeric(bp_split[1], errors='coerce')

# Drop the original messy text column
df.drop(columns=["Blood Pressure"], inplace=True)
