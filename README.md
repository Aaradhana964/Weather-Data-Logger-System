# 🌦️ Weather Data Logger System

A Python-based Weather Data Logger System that fetches real-time weather information using WeatherAPI and stores the data in a MySQL database for future reference and analysis.

## 📖 Overview

This project allows users to search for weather information of any city and automatically saves the weather details into a MySQL database. It provides additional functionalities such as viewing search history, identifying the hottest and coldest cities searched, exporting weather records, and generating weather statistics.

The project demonstrates the integration of:

* Python Programming
* REST API Consumption
* MySQL Database Management
* File Handling
* Exception Handling
* Data Analysis

---

## 🚀 Features

* Get real-time weather data for any city
* Store weather records in a MySQL database
* View complete weather search history
* Display the most recently searched weather record
* Find the hottest city searched
* Find the coldest city searched
* Count total weather searches
* Delete all weather history
* Export weather history to a text file
* Generate weather statistics:

  * Total Searches
  * Highest Temperature
  * Lowest Temperature
  * Average Temperature

---

## 🛠️ Technologies Used

* Python 3.x
* MySQL
* WeatherAPI
* Requests Library
* python-dotenv

---

## 📂 Project Structure

```text
weather_project/
│
├── weather_logger.py
├── .env
├── weather_history.txt
├── README.md
└── requirements.txt
```

---

## ⚙️ Database Setup

Create a database named:

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

Create a `.env` file in the project folder:

```env
API_KEY=your_weatherapi_key_here
```

Get your free API key from WeatherAPI.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/weather-data-logger.git
```

Move into the project directory:

```bash
cd weather-data-logger
```

Install required packages:

```bash
pip install requests mysql-connector-python python-dotenv
```

---

## ▶️ Running the Project

```bash
python weather_logger.py
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
----Weather Report-----

City: Hyderabad
Country: India
Temperature: 31.5
Humidity: 62
Wind Speed: 15.4
Weather Condition: Sunny

Weather saved Successfully
```

---

## 🔒 Security Note

Do not upload your `.env` file or API keys to GitHub.

Create a `.gitignore` file:

```text
.env
env/
__pycache__/
.vscode/
```

---

## 🎯 Learning Outcomes

Through this project, you can learn:

* API Integration using Python
* Database Connectivity with MySQL
* CRUD Operations
* File Exporting
* Exception Handling
* Environment Variable Management
* Building Menu-Driven Applications

---

## 👩‍💻 Author

Aaradhana Prajapati

Python | MySQL | API Integration | Backend Development
