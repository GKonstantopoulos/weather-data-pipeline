import csv
import os
import smtplib
from datetime import datetime
from email.message import EmailMessage

import requests
from bs4 import BeautifulSoup

# Email credentials removed for security reasons
def send_email_alert(subject, body):
    sender = "YOUR_EMAIL@gmail.com"
    receiver = "RECEIVER_EMAIL@gmail.com"

    app_password = "YOUR_APP_PASSWORD"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)


def run_pipeline():
    url = "https://www.meteo.gr/cf.cfm?city_id=12"


    # Fetch page
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Temperature
    temperature = soup.find("div", class_="newtemp")

    if temperature is None:
        print("Temperature not found")
        return

    temp_text = temperature.text.strip()
    temp_clean = temp_text.replace("°C", "")
    temp_value = int(temp_clean)

    # Humidity
    humidity = soup.find("div", class_="ygrasia")

    if humidity is None:
        print("Humidity not found")
        return

    humidity_text = humidity.text.strip()
    humidity_clean = humidity_text.replace("Υγρασία:", "").replace("%", "").strip()
    humidity_value = int(humidity_clean)

    # Rain
    rain_value = None

    daily_data_items = soup.find_all("div", class_="dailydata")

    for item in daily_data_items:
        text = item.text.strip()

        if "Ημερήσια βροχή" in text:
            rain_text = text
            rain_clean = rain_text.replace("Ημερήσια βροχή:", "").replace("mm", "").strip()
            rain_value = float(rain_clean)
            break

    # Old define file path (relative path - breaks in Task Scheduler)
    # file_path = "data/weather_data.csv"

    # New path (absolute path based on script location)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "weather_data.csv")

    file_exists = os.path.isfile(file_path)

    # Read previous rain_value from CSV
    previous_rain = None

    if file_exists:
        with open(file_path, mode="r", encoding="utf-8") as file:
            lines = file.readlines()

            if len(lines) > 1:
                last_line = lines[-1]
                previous_rain = float(last_line.strip().split(",")[4])

    # Create current data record
    data = {
        "city": "Athens",
        "temperature": temp_value,
        "humidity": humidity_value,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "rain_mm": rain_value
    }

    # Alert only when rain starts
    if previous_rain is not None and rain_value is not None:
        if previous_rain == 0 and rain_value > 0:
            print("ALERT: Rain started!")

            send_email_alert(subject="Rain Alert - Athens",
                body=f"Rain started in Athens.\nCurrent rain: {rain_value} mm")

    # Write record to CSV
    with open(file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

    print("Pipeline executed:", data)


if __name__ == "__main__":
    run_pipeline()