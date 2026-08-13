#### Statistics
# What is Statistics ?
## Statistics is the study of data -- collecting, understanding, and summarizing data.
### Examples :
# Class Marks
# Salaries
# Ages
# Sales Numbers

# Why Statistics is Important ?
## Statistics is the foundation of:
### Data Analysis
### Machine Learning
### AI
### Decision Making
#### Python uses statistics everywhere (Pandas, ML, AI)

# 1. Types of Statistics
## Descriptive Statistics 
### Mean
### Median
### Mode
### Min/ Max
### Range

## Inferential Statistics
### Probability
### Hypothesis testing

# 2. Dataset Example
marks = [70,80,90,100,60]

# 3. Mean (Average)
## Meaning:
### Sum of all values + number of values
# Formula
## Mean = (sum of values) / (count)

mean = sum(marks) / len(marks)
print(mean)

# 4. Median (Middle Value)
## The middle number when data is sorted

# Steps:
## 1. Sort data
## 2. Pick middle

marks.sort()
median = marks[len(marks)//2]
print(median)

# If Even Number of Values
nums = [10,20,30,40,50,60]
nums.sort()
median = (nums[2] + nums [3]) / 2
print(median)

# 5. Mode
## Value that appears most times

nums = [1,2,2,3,4,2,5]
mode = max(set(nums), key = nums.count)
print(mode)

# 6. Min, Max, Range
nums = [10,30,20,50,78]
print(min(nums))
print(max(nums))
print(max(nums) - min(nums))

# 7. Using Python statistics module
## Python already gives this
import statistics
data = [70,80,90,100,80,60]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))

data = [2,4,6,8,10]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))

# 8. Variance
## What problem does variance solve?
# Mean tells average
# Variance tells how spread out the data is means average of squared distances from the mean
## If the numbers are:
### close to mean --> small variance
### far from mean --> large variance

# Example 1 (Low Variance)
data = [9,10,11]
mean = 10
# Distances from mean:
## 9 --> -1
## 10 -> 0
## 11 -> +1

# Squared distances
## 1,0,1
# Average:
## (1+0+1)/3 = 0.67
#### Variance is small

# Example 2 (High Variance)
data = [1,10,100]
mean = 37
# Distances :
## -36,-27,+63
# Squares:
## 1296,729,3969

# Average is huge
## Variance is large
print("#######")
import statistics
data = [2,4,6,8,10]
print(statistics.mean(data))
print(statistics.variance(data))

# 9. Standard Deviation
## Why not just use variance?
### Because:
#### Variance units are squared
#### Hard to understand in real life
# So we take:
## Square root of variance

# Standard deviation = average spread in original units

import statistics
data = [2,4,6,8,10]
print(statistics.stdev(data))

# Standard Deviation = square root(variance)

# 10. Population vs Sample
## Population
### Entire data
### Example: marks of all students in college

## Sample
### Part of data
### Example: marks of some students

##### Python Difference
'''
| Type                | Function      |
| ------------------- | ------------- |
| Population variance | `pvariance()` |
| Sample variance     | `variance()`  |
| Population SD       | `pstdev()`    |
| Sample SD           | `stdev()`     |

'''


import statistics
data = [10,12,14,16]
print("Sample Variance: ",statistics.variance(data))
print("Population Variance:",statistics.pvariance(data))
# Output
## Sample Variance:  6.666666666666667
## Population Variance: 5

# Why sample variance is bigger?
## Because Sample tries to estimate unknown population
### So Python divides by:
#### n-1 (sample)
#### n (population)
##### This is called "Bessel's Correction"

import statistics

a = [50, 51, 49, 50, 50]
b = [10, 90, 30, 80, 40]

print(statistics.mean(a), statistics.stdev(a))
print(statistics.mean(b), statistics.stdev(b))


# 11. Covariance
## Covariance tells how two variables move together
### One value increases --> what happens to the other?

# Example:

'''
Dataset A (VERY STRONG relationship) 

Study Hours        Marks
--------------------------
1                    10
2                    20
3                    30
4                    40

# Every +1 hour --> exactly +10 marks
# Perfectly predictable
'''
# What covariance tells here
## As study hours increase
## marks also increase
### So covariance is POSITIVE

# What covariance DOES NOT tell
## How strong is the relationship?
## Is it weak or very strong?
### Covariance only says:
#### They move together

# For example:
'''
Dataset B (WEAK realtionship)

Study Hours         Marks
---------------------------
1                     15
2                     18
3                     25
4                     27
# Marks increases, BUT not consistently
# Sometimes +3, sometimes +7
'''

# Here What Does Covariance Say For Both?
## For both datasets:
### Study hours increases
### Marks increases
#### Covariance is POSITIVE in both cases

# BUT covariance cannot tell :
## DATASET A is perfect
## DATASET B is shaky 
### Covariance gives same type of answer for both
#### Only direction, not strength

# 12. Correlation
## Correlation measures strength + direction of relationship
## Now correlation PROVES "strength"
### Dataset A
#### Correlation = +1
# Meaning:
## When study hours increases, marks increase almost perfectly
### Dataset B
#### Correlation = + 0.6
# Meaning:
## Marks increases, but not very reliably

# This proves Correlation tells how strong the relationship is

# Covariance ---> Do they move together?
# Correlation --> How reliably do they move together?


# 13. Quartiles 
## Quartiles divide sorted data into 4 equal parts
'''
|----|----|----|----|
     Q1   Q2   Q3
'''

# Q1 --> first cut(25%)
# Q2 --> second cut(50%,median)
# Q3 --> third cut (75%)
## These 3 cuts divide the data into 4 parts

'''
| Quartile | Meaning                       |
| -------- | ----------------------------- |
| Q1       | 25% of data is **below** this |
| Q2       | 50% (this is the **median**)  |
| Q3       | 75% of data is **below** this |

'''
# Example
data = [2,4,6,8,10,12,14,16]
## Already sorted
### Q2(Median) = average of 8 & 10 = 9
### Lower half --> [2,4,6,8]
### Upper half --> [10,12,14,16]
### Q1 = median of lower half = 5
### Q3 = median of upper half = 13


# 14. Percentiles
## Percentiles divide data into 100 equal parts
### 10th percentile
### 37th percentile
### 90th percentile
### Any percentage we want

# Why Quartiles are NOT enough
## Quartiles give only rough division:
### Lower
### Middle
### Upper
#### But sometimes we need finer comparison

# 15. Interquartile Range (IQR)
## IQR measures spread of the middle 50% of data
### IQR = Q3 - Q1

# 16. Outliers
## A value far away from most of the data
### Outlier detection rule (IQR method)

# Lower bound = Q1 - 1.5 * IQR
# Upper bound = Q3 + 1.5 * IQR

## Anything outside --> outlier
import numpy_practise as np
data = [2,4,6,8,10,12,14,100]

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = [x for x in data if x < lower or x > upper]
print(outliers)

# Why Outliers matter?
## Can mislead mean
## Affects ML models
## Often indicates:
### Error
### Fraud
### Rare but important event


#### DAY 28 CHEAT SHEET
'''
📊 DAY 28 — STATISTICS (COMPLETE CHEAT SHEET)
1️⃣ Mean (Average)

What it tells: Center of data

import statistics
statistics.mean(data)


Formula:

Mean = sum(data) / n

2️⃣ Median

What it tells: Middle value after sorting

statistics.median(data)


Odd count → middle value

Even count → average of two middle values

3️⃣ Mode

What it tells: Most frequent value

statistics.mode(data)


⚠️ Notes:

No repetition → No mode (theory)

Python may return first value

4️⃣ Variance

What it tells: Spread of data (squared)

5️⃣ Population Variance

Use when ALL data is available

statistics.pvariance(data)


Formula:

Σ(x − μ)² / n

6️⃣ Sample Variance

Use when data is a sample

statistics.variance(data)


Formula:

Σ(x − x̄)² / (n − 1)


📌 Uses Bessel’s correction

7️⃣ Standard Deviation (SD)

What it tells: Spread in original units

Population SD
statistics.pstdev(data)

Sample SD
statistics.stdev(data)


Formula:

SD = √Variance

8️⃣ Population vs Sample
Type	Divide by	Python
Population Variance	n	pvariance
Sample Variance	n − 1	variance
Population SD	√var	pstdev
Sample SD	√var	stdev
9️⃣ Quartiles

Divide data into 4 equal parts

Quartile	Meaning
Q1	25% below
Q2	50% (Median)
Q3	75% below

⚠️ No Q4
Q1, Q2, Q3 are cut points, not parts.

🔟 Percentiles

Divide data into 100 equal parts

import numpy as np
np.percentile(data, 90)


Relation:

Q1 = 25th percentile
Q2 = 50th percentile
Q3 = 75th percentile

1️⃣1️⃣ Interquartile Range (IQR)

Spread of middle 50%

IQR = Q3 − Q1

1️⃣2️⃣ Outliers (IQR Method)
Lower bound = Q1 − 1.5 × IQR
Upper bound = Q3 + 1.5 × IQR


Outside this → Outlier

1️⃣3️⃣ Covariance

What it tells: Direction of relationship

Value	Meaning
+	Move together
−	Move opposite
0	No relation

❌ No strength information

1️⃣4️⃣ Correlation

What it tells: Direction + Strength

Range:

-1  →  0  →  +1

Value	Meaning
+1	Perfect positive
0	No relation
-1	Perfect negative
import numpy as np
np.corrcoef(x, y)

🔑 Covariance vs Correlation
Feature	Covariance	Correlation
Direction	✅	✅
Strength	❌	✅
Scale-free	❌	✅
Range	No limit	−1 to +1
🧠 One-Line Memory Tricks (VERY IMPORTANT)
Mean → center
Variance → spread²
SD → spread
Quartiles → 4 parts
Percentiles → ranking
IQR → middle 50%
Covariance → direction
Correlation → direction + strength

🎯 Interview-Ready Lines

Why sample variance bigger?
→ Because of uncertainty (n−1)

Why SD preferred over variance?
→ Same units as data

Why correlation over covariance?
→ Standardized and interpretable

Median vs Mean with outliers?
→ Median is safer
'''