# **Hello PANDAS!!** 
## 🐼&nbsp;&nbsp;Overview
Welcome to the **Python Data Analysis (PANDAS)** assignment! If you've ever wondered how data scientists wrangle massive datasets with ease, you're in for a treat. In this assignment, you'll dive deep into the powerful Pandas library, a must-have tool in the world of data analysis and manipulation.
## 🐼&nbsp;&nbsp;It's Excel, but Make It... Pythonic!?
Pandas is like Excel’s cool sibling—it can handle data efficiently, whether it's just a few rows or millions of them, but with the full power and flexibility of Python. It makes data handling in Python simple, efficient, and fun because it equips you with intuitive and flexible tools to manipulate, clean, and analyze data. In this assignment, you'll explore how to unlock the full potential of Pandas to turn raw data into actionable insights.
## 🐼&nbsp;&nbsp;The Basics
This programming assignment covers the basics of data manipulation using the Pandas library. Through Jupyter Notebook, you will learn to:
- Create, load, and inspect datasets.
- Use Pandas data structures such as Series and DataFrames.
- Perform basic data manipulation tasks, including selecting, filtering, and modifying data using `.loc` and `.iloc` function.
- Understand the essential functions and methods in Pandas that will help you transform raw data into a structured format for analysis.
## 🐼&nbsp;&nbsp;Setup
1. Install Jupyter Notebook through [Anaconda Navigator](https://www.anaconda.com/download) or directly from their [website](https://jupyter.org)
2. Run the following command in the terminal to start Jupyter Notebook:
```
jupyter notebook
```
4. Download `cars.csv`.
5. Open `Aparicio_Pandas-P1.ipynb` or `Aparicio_Pandas-P2.ipynb` within the same file directory as `cars.csv`.
6. Execute the codes
## 🐼&nbsp;&nbsp;Usage
Access the data by inputting the following command:
```
pd.read_csv('cars.csv')
```
_This is will allow you to access the data that will be used as you perform data manipulation tasks_
> [!NOTE]
> Dataframes follow **zero-based indexing**, which means the counting of both row and columns start from 0.
### Running the Scripts
1. Open a terminal or command prompt.
2. Navigate to the project directory.<br>

Here are the following code snippets and their following outputs: <br>
```
cars.iloc[[23], [0,2]]
```
_Output:_<br>
|No.|Model|cyl|
|---|-----|---|
|23|Camaro Z28|8|
```
cars.loc[cars['Model'] == 'Mazda RX4'] 
```
_Output:_<br>
|No.|Model|mpg|cyl|disp|hp|drat|wt|qsec|vs|am|gear|carb|
|---|-----|---|---|----|--|----|--|----|--|--|----|----|
|0|Mazda RX4|21.0|6|6|160.0|110|3.9|2.62|16.46|0|1|4|4|<br>
## 🐼&nbsp;&nbsp;Takeaways
As a newbie who is new to Python, particularly in using PANDAS, it is very important to take note of the following:
1. Master the ways on how to manipulate data through subsetting, slicing, and indexing
2. Be mindful of the differences between `.loc` and `iloc` functon and when to apply them
3. Be careful when formulating a conditional statement in indexing.
## 🐼&nbsp;&nbsp;Contact
For any questions or feedback, please reach out to:<br>
- Email: johnmarkaparicio.eng@ust.edu.ph <br>
- GitHub: https://github.com/merkjunnie



