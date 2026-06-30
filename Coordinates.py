#!/usr/bin/env python3

import serial

import pynmea2

import time

GPS_PORT = "/dev/ttyACM0"      # Change to /dev/ttyUSB0 if required

BAUD_RATE = 9600


class GPSReader:

    def __init__(self):

        self.data = {

            "fix": False,

            "latitude": None,

            "longitude": None,

            "altitude": None,

            "speed_kmh": 0.0,

            "utc_time": None,

            "satellites": 0,

        }

        try:

            self.ser = serial.Serial(

                GPS_PORT,

                BAUD_RATE,

                timeout=1

            )

            print(f"Connected to {GPS_PORT}")

        except Exception as e:

            print("Failed to open serial port:", e)

            exit()

    def display(self):

        print("\n" + "=" * 60)

        print(f"GPS Fix      : {self.data['fix']}")

        print(f"Latitude     : {self.data['latitude']}")

        print(f"Longitude    : {self.data['longitude']}")

        print(f"Altitude(m)  : {self.data['altitude']}")

        print(f"Speed(km/h)  : {self.data['speed_kmh']}")

        print(f"UTC Time     : {self.data['utc_time']}")

        print(f"Satellites   : {self.data['satellites']}")

        print("=" * 60)

    def read(self):

        while True:

            try:

                line = self.ser.readline().decode(

                    "ascii",

                    errors="ignore"

                ).strip()

                if not line:

                    continue

                # Print raw GPS sentence

                print("RAW:", line)

                # ---------------- GGA -----------------

                if line.startswith("$GPGGA") or line.startswith("$GNGGA"):

                    msg = pynmea2.parse(line)

                    self.data["latitude"] = msg.latitude

                    self.data["longitude"] = msg.longitude

                    self.data["altitude"] = msg.altitude

                    if msg.num_sats:

                        self.data["satellites"] = int(msg.num_sats)

                    else:

                        self.data["satellites"] = 0

                    if msg.gps_qual and int(msg.gps_qual) > 0:

                        self.data["fix"] = True

                    else:

                        self.data["fix"] = False

                # ---------------- RMC -----------------

                elif line.startswith("$GPRMC") or line.startswith("$GNRMC"):

                    msg = pynmea2.parse(line)

                    self.data["utc_time"] = msg.timestamp

                    if msg.spd_over_grnd:

                        self.data["speed_kmh"] = round(

                            float(msg.spd_over_grnd) * 1.852,

                            2

                        )

                    else:

                        self.data["speed_kmh"] = 0.0

                self.display()

            except pynmea2.ParseError as e:

                print("Parse Error:", e)

            except Exception as e:

                print("Error:", e)

            time.sleep(0.2)


if __name__ == "__main__":

    print("Starting GPS Reader...")

    print("Press Ctrl+C to Exit")

    gps = GPSReader()

    try:

        gps.read()

    except KeyboardInterrupt:

        print("\nGPS Reader Stopped.")
 