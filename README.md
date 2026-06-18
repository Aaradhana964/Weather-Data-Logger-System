# 🌦️ Weather Data Logger System

A Python-based Weather Data Logger System that fetches real-time weather information using WeatherAPI, validates the data, stores it in a MySQL database, and provides weather analytics for future reference.

## 📖 Overview

This project allows users to search for weather information for any city and automatically save the weather details into a MySQL database. The application includes data validation, logging, weather history tracking, statistics generation, and export functionality.

The project demonstrates the integration of:

* Python Programming
* REST API Consumption
* MySQL Database Management
* Data Validation
* File Handling
* Logging
* Exception Handling
* Data Analysis

---

## 🚀 Features

* Get real-time weather data for any city
* Validate weather data before saving
* Store weather records in a MySQL database
* View complete weather search history
* Display the most recent weather search
* Find the hottest city searched
* Find the coldest city searched
* Count total weather searches
* Delete weather history
* Export weather history to a text file
* Generate weather statistics
* Maintain validation logs
* Maintain application logs

---

## 🛠️ Technologies Used

* Python 3.x
* MySQL
* WeatherAPI
* Requests Library
* mysql-connector-python
* python-dotenv

---

## 📂 Project Structure

```text
weather_project/
│
├── weatherapi.py
├── README.md
├── .env
├── weather_history.txt
├── validation_log.txt
├── weather_app.log
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Database Setup

Create a database:

```sql
CREATE DATABASE weather_db;
```

Use the database:

```sql
USE weather_db;
```

Create the table:

```sql
CREATE TABLE weather_reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100),
    country VARCHAR(100),
    temperature DECIMAL(5,2),
    humidity INT,
    wind_speed DECIMAL(5,2),
    weather_condition VARCHAR(100),
    search_date DATE,
    search_time TIME
);
```

---

## 🔑 API Configuration

Create a `.env` file in the project directory:

```env
API_KEY=your_weatherapi_key_here
```

Get your free API key from:

https://www.weatherapi.com/

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Aaradhana964/Weather-Data-Logger-System.git
```

Move into the project directory:

```bash
cd Weather-Data-Logger-System
```

Install required packages:

```bash
pip install requests mysql-connector-python python-dotenv
```

---

## ▶️ Running the Project

```bash
python weatherapi.py
```

---

## 📋 Menu Options

```text
1. Check Weather
2. View Weather History
3. Exit
4. View Last Weather Search
5. Hottest City Checked
6. Coldest City Checked
7. Weather Search Counter
8. Delete Weather History
9. Export Weather History
10. Statistics
```

---

## 📊 Sample Output

```text
---- Weather Report ----

City: Hyderabad
Country: India
Temperature: 31.5°C
Humidity: 62%
Wind Speed: 15.4 kph
Weather Condition: Sunny

----- Validation Report -----

City Validation        : Passed
Country Validation     : Passed
Temperature Validation : Passed
Humidity Validation    : Passed
Wind Speed Validation  : Passed
Condition Validation   : Passed

Weather Saved Successfully
```

---

## 📈 Statistics Available

The application generates:

* Total Searches
* Highest Temperature Recorded
* Lowest Temperature Recorded
* Average Temperature

---

## 📄 Export Feature

Weather history can be exported to:

```text
weather_history.txt
```

Example:

```text
Hyderabad | 31.5°C | Sunny
Mumbai | 29.0°C | Cloudy
Delhi | 35.2°C | Clear
```

---

## 🔒 Security Note

Do not upload your API key or virtual environment to GitHub.

Create a `.gitignore` file:

```text
.env
env/
__pycache__/
.vscode/

weather_app.log
validation_log.txt
weather_history.txt
```

---

## 🎯 Learning Outcomes

Through this project, you can learn:

* API Integration using Python
* Database Connectivity with MySQL
* CRUD Operations
* Data Validation Techniques
* Logging and Monitoring
* File Exporting
* Exception Handling
* Environment Variable Management
* Building Menu-Driven Applications

---

## 👩‍💻 Author

**Aaradhana Prajapati**

Python | MySQL | REST API | Data Validation | Backend Development
