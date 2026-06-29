# GPS Reader for Raspberry Pi

A Python-based GPS reader that reads live GPS data from a USB GPS receiver (u-blox/G-MOUSE), parses NMEA sentences using `pynmea2`, and displays real-time GPS information.

## Features

- Automatically connects to USB GPS (`/dev/ttyACM0`)

- Reads live NMEA sentences

- Parses GPS data using `pynmea2`

- Displays:

  - Latitude

  - Longitude

  - Altitude

  - Speed (km/h)

  - UTC Time

  - Number of Satellites

  - GPS Fix Status

- Continuous real-time monitoring

- Exception handling for invalid GPS data

- Easy integration with AI, IoT, and Vehicle Tracking applications

---

## Hardware Requirements

- Raspberry Pi 5

- USB GPS Receiver (u-blox / G-MOUSE)

- USB Cable

---

## Software Requirements

- Python 3.8+

- pyserial

- pynmea2

---

## Installation

### Clone the repository

```bash

git clone <repository_url>

cd gps_reader

```

### Install dependencies

```bash

pip3 install pyserial pynmea2

```

Or install from requirements.txt

```bash

pip3 install -r requirements.txt

```

---

## Verify GPS Device

Check whether the GPS is detected.

```bash

lsusb

```

Check the serial device.

```bash

ls /dev/ttyACM*

```

Expected Output

```bash

/dev/ttyACM0

```

Verify GPS data.

```bash

cat /dev/ttyACM0

```

You should see NMEA sentences similar to:

```text

$GPGGA,...

$GPRMC,...

$GPGSV,...

```

Press **Ctrl + C** to exit.

---

## Running the Application

```bash

python3 gps_reader.py

```

---

## Sample Output

```text

============================================================

GPS Fix      : True

Latitude     : 18.520430

Longitude    : 73.856743

Altitude(m)  : 560.2

Speed(km/h)  : 18.45

UTC Time     : 09:42:18

Satellites   : 12

============================================================

```

---

## Output Description

| Parameter | Description |

|------------|-------------|

| GPS Fix | Indicates whether GPS has a valid fix |

| Latitude | Current Latitude |

| Longitude | Current Longitude |

| Altitude | Altitude above sea level (meters) |

| Speed | Speed in km/h |

| UTC Time | GPS Time |

| Satellites | Number of connected satellites |

---

## Project Structure

```

gps_reader/

│

├── gps_reader.py

├── requirements.txt

└── README.md

```

---

## requirements.txt

```

pyserial

pynmea2

```

---

## Integration Example

Access the latest GPS data using:

```python

gps.data["latitude"]

gps.data["longitude"]

gps.data["speed_kmh"]

gps.data["altitude"]

gps.data["utc_time"]

gps.data["satellites"]

gps.data["fix"]

```

Example:

```python

alert = {

    "latitude": gps.data["latitude"],

    "longitude": gps.data["longitude"],

    "speed": gps.data["speed_kmh"],

    "timestamp": gps.data["utc_time"]

}

```

This can be integrated with:

- YOLO Object Detection

- Vehicle Tracking

- AI Video Analytics

- REST APIs

- MQTT

- Cloud Platforms

- PostgreSQL / MySQL

- Elasticsearch

---

## Troubleshooting

### GPS not detected

```bash

lsusb

dmesg | grep tty

```

### Check GPS device

```bash

ls /dev/ttyACM*

```

### Read raw GPS data

```bash

cat /dev/ttyACM0

```

### No GPS Fix

If GPS Fix remains **False**:

- Move the GPS outdoors.

- Wait 1–2 minutes for satellite acquisition.

- Ensure the antenna has a clear view of the sky.

---

## Future Improvements

- Automatic serial port detection

- Multi-threaded GPS reader

- Automatic reconnection on disconnect

- JSON output support

- REST API integration

- MQTT publishing

- GPS logging to CSV/Database

- Integration with AI Video Analytics

---

## License

This project is intended for educational, research, and commercial applications involving Raspberry Pi, GPS tracking, and IoT systems.
 