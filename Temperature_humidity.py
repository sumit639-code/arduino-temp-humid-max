import serial
import csv
import datetime
import time
import pandas as pd
# print("wo")
def open_serial_connection(port, baud_rate, timeout):
    try:
        ser = serial.Serial(port, baud_rate, timeout=timeout)
        time.sleep(2)  # Wait for the serial connection to initialize
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

def read_from_serial(ser):
    try:
        line = ser.readline().decode('utf-8').strip()
        return line
    except Exception as e:
        print(f"Error reading from serial: {e}")
        return None

def write_to_csv(file, data):
    writer = csv.writer(file)
    writer.writerow(data)

def main():
    serial_port = 'COM3'  # Replace with your port
    baud_rate = 9600
    timeout = 2
    print("working")
    with open('sensor_readings.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Date  ', 'Time   ', 'Temperature (C)', 'Humidity (%)'])

        ser = open_serial_connection(serial_port, baud_rate, timeout)
        if ser is None:
            return

        try:
            while True:
                line = read_from_serial(ser)
                print(line)
                if line:
                    print(f"Raw data: {line}")  # Debug: print raw data

                    if "Temperature" in line and "Humidity" in line:
                        parts = line.split(' ')
                        # print(parts)
                        # print(parts[4])
                        hum = parts[1]
                        temp = parts[4]
                        # print("temp",temp)
                        now = datetime.datetime.now()
                        date = now.strftime("%Y-%m-%d")
                        time_str = now.strftime("%H:%M:%S")

                        data = [date, time_str, temp, hum]
                        write_to_csv(file, data)

                        print(f"{date} {time_str} - Humidity: {hum} %, Temperature: {temp} C")
                    else:
                        print("Invalid data format")
                else:
                    print("No data received")
        except KeyboardInterrupt:
            print("Exiting...")
        finally:
            if ser.is_open:
                ser.close()
            print("Serial connection closed")
main()
if __name__ == "_main_":
    main()