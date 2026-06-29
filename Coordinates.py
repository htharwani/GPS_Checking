#!/usr/bin/env python3

import serial

import pynmea2

import time

GPS_PORT = "/dev/ttyACM0"

BAUD_RATE = 9600


class GPSReader:

    def __init__(self):

        self.ser = serial.Serial(

            GPS_PORT,

            BAUD_RATE,

            timeout=1

        )

        self.data = {

            "latitude": None,

            "longitude": None,

            "altitude": None,

            "speed_kmh": None,

            "utc_time": None,

            "satellites": None,

            "fix": False

        }

    def read(self):

        while True:

            try:

                line = self.ser.readline().decode(

                    "ascii",

                    errors="ignore"

                ).strip()

                if not line:

                    continue

                if line.startswith("$GPGGA") or line.startswith("$GNGGA"):

                    msg = pynmea2.parse(line)

                    self.data["latitude"] = msg.latitude

                    self.data["longitude"] = msg.longitude

                    self.data["altitude"] = msg.altitude

                    self.data["satellites"] = msg.num_sats

                    if int(msg.gps_qual) > 0:

                        self.data["fix"] = True

                    else:

                        self.data["fix"] = False

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

            except Exception:

                pass

    def display(self):

        print("=" * 60)

        print(f"GPS Fix      : {self.data['fix']}")

        print(f"Latitude     : {self.data['latitude']}")

        print(f"Longitude    : {self.data['longitude']}")

        print(f"Altitude(m)  : {self.data['altitude']}")

        print(f"Speed(km/h)  : {self.data['speed_kmh']}")

        print(f"UTC Time     : {self.data['utc_time']}")

        print(f"Satellites   : {self.data['satellites']}")

        print("=" * 60)


if __name__ == "__main__":

    print("Starting GPS Reader...")

    print("Press Ctrl+C to Exit")

    gps = GPSReader()

    try:

        gps.read()

    except KeyboardInterrupt:

        print("\nStopped.")
