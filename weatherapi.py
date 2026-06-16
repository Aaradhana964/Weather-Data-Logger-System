import requests
import mysql.connector
import os
import re
import logging
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()
logging.basicConfig(
    filename="weather_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def validate_city(city):
    pattern= "^[A-Za-z ]+$"
    if re.match(pattern, city):
        return True
    return False
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="aaradhana_0910",
        database="weather_db"
    )
API_KEY=os.getenv("API_KEY")
def get_weather(city):
    try:
        url="http://api.weatherapi.com/v1/current.json"
        params={
            "key":API_KEY,
            "q":city       
            }
        response=requests.get(url,params=params)
        response.raise_for_status()
        data=response.json()
        if "error" in data:
            print("\n City not found!")
            return None
        return data
    except Exception as e:
        print("Error:",e)
        return None
def save(data):
    try:
        conn=connect_db()
        cursor=conn.cursor()
        city=data["location"]["name"]
        country=data["location"]["country"]
        temperature=data["current"]["temp_c"]
        humidity=data["current"]["humidity"]
        wind_speed=data["current"]["wind_kph"]
        weather_condition=data["current"]["condition"]["text"]
        now=datetime.now()
        search_date=now.date()
        search_time=now.time()
        query="""Insert into weather_reports(
        city,country,temperature,humidity,wind_speed,weather_condition,search_date,search_time)values
        (%s,%s,%s,%s,%s,%s,%s,%s)"""
        values=(
            city,
            country,
            temperature,
            humidity,
            wind_speed,
            weather_condition,
            search_date,
            search_time
        )
        cursor.execute(query, values)
        conn.commit()
        print("\n Weather saved Successfully")
        logging.info(f"Weather data saved for {city}")
    except Exception as e:
        print("Database Error:",e)

    finally:
        cursor.close()
        conn.close()
def check_weather():
    city=input("\nEnter city:").strip()
    if not validate_city(city):
        print("\nInvalid city name!!")
        logging.warning(f"Invalid city entered: {city}")
        return
    logging.info(f"valid city entered:{city}")
    data=get_weather(city)
    if data:
        print("----Weather Report-----")
        print("City:",data["location"]["name"])
        print("Country:",data["location"]["country"])
        print("Temperature:",data["current"]["temp_c"])
        print("Humidity:",data["current"]["humidity"])
        print("Wind Speed:",data["current"]["wind_kph"])
        print("Weather Condition:",data["current"]["condition"]["text"])
        logging.info(
            f"Weather checked for {data['location']['name']},"
            f"Temperature: {data['current']['temp_c']}°C"
        )
        save(data)
def view_history():
    try:
        conn=connect_db()
        cursor=conn.cursor()
        query="select * from weather_reports"
        cursor.execute(query)
        records=cursor.fetchall()
        print("\nWeather History\n")
        for row in records:
            print(row)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
def last_search():
    try:
        conn=connect_db()
        cursor=conn.cursor()
        query="""
        Select * From weather_reports
        ORDER BY id DESC
        LIMIT 1
        """
        cursor.execute (query)
        record=cursor.fetchone()
        record = cursor.fetchone()
        if record:
            print("\nLast Weather Search:\n")
            print(record)
        else:
            print("\nNo weather records found")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
def hottest_city():
    try:
        conn=connect_db()
        cursor=conn.cursor()
        query="""Select city,temperature from weather_reports 
        order by temperature desc
        limit 1"""
        cursor.execute(query)
        record=cursor.fetchone()
        if record:
            print("\nHottest City:")
            print(f"City: {record[0]}")
            print(f"Temperature: {record[1]}°C")
        else:
            print("\nNo weather records found")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
def coldest_city():
    try:
        conn=connect_db()
        cursor=conn.cursor()
        query="""select city,temperature from weather_reports 
        order by temperature asc
        limit 1"""
        cursor.execute(query)
        record=cursor.fetchone()
        if record:
            print("\nColdest City:")
            print(f"City: {record[0]}")
            print(f"Temperature: {record[1]}°C")
        else:
            print("\nNo weather records found")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
def search_count():
    try:
        conn=connect_db()
        cursor=conn.cursor()
        query="""select count(*) from weather_reports"""
        cursor.execute(query)
        count=cursor.fetchone()
        print("\nTotal Searches:",count[0])
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
def delete_history():
    try:
        conn=connect_db()
        cursor=conn.cursor()
        query="Delete from weather_reports"
        cursor.execute(query)
        conn.commit()
        print("\nHistory deleted Successfully!!!")
        logging.info("Weather history deleted")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
def export_history():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = """
        Select city,
               temperature,
               weather_condition
        from weather_reports
        """
        cursor.execute(query)
        records = cursor.fetchall()
        with open("weather_history.txt", "w") as file:
            for row in records:
                line = f"{row[0]} | {row[1]}°C | {row[2]}\n"
                file.write(line)
        print("\nExported to weather_history.txt")
        logging.info("Weather history exported to weather_history.txt")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def statistics():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = """
        Select
        Count(*),
        MAX(temperature),
        MIN(temperature),
        AVG(temperature)
        from weather_reports
        """
        cursor.execute(query)
        result = cursor.fetchone()
        if result[0]==0:
            print("No weather records found")
        else:
            print("\n__________Statistics__________")
            print("Total Searches :", result[0])
            print("Highest Temp :", result[1])
            print("Lowest Temp :", result[2])
            print("Average Temp :", round(result[3], 2))
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

while True:
    print("----------------WEATHER DATA LOGGER SYSTEM-------------------")
    print("1. Check Weather")
    print("2. View Weather History")
    print("3. Exit")
    print("4. View Last Weather Search")
    print("5. Hottest City Checked")
    print("6. Coldest City Checked")
    print("7. Weather Search Counter")
    print("8. Delete Weather History")
    print("9. Export Weather History")
    print("10. Statistics")
    choice = input("\nEnter Choice: ")
    if choice == "1":
        check_weather()
    elif choice == "2":
        view_history()
    elif choice == "3":
        logging.info("Application closed by user")
        print("\nThank You!")
        break
    elif choice == "4":
        last_search()
    elif choice == "5":
        hottest_city()
    elif choice == "6":
        coldest_city()
    elif choice == "7":
        search_count()
    elif choice == "8":
        delete_history()
    elif choice == "9":
        export_history()
    elif choice == "10":
        statistics()
    else:
        print("\nInvalid Choice!!")

