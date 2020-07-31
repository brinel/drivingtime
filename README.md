# Driving Time Calculator

This script returns the driving time from an inputted starting location to several destinations. It uses the Google Maps API and a csv created by the user to do so. The initial use case was to find the distances from a single warehouse to various ZIP codes to help create a service area for a delivery service.

## Getting Started

### Prerequisites

```
Python
Google Maps API key - credits I got with a free Google Cloud account have been sufficient for my level of usage.
```

### Installing


Create input file `zipslatlong.csv` with each line in the format `ZIP, Origin(latidude, longitude), Destination(latitude, longitude)`

```
ZIP,Origin,Destination,Duration (sec)
7001,"40.031544, -75.062044","40.58, -74.27",
7002,"40.031544, -75.062044","40.66, -74.11",
7003,"40.031544, -75.062044","40.81, -74.18",
```

Set environment variable `GAPI_KEY` to your Google Maps API key and run the script
```
GAPI_KEY=[Your API key] python3 drivingtime.py
```

View the file `results.csv` which was created in the main directory. Driving time will be displayed in the fourth column, in seconds.
```
ZIP	Origin	Destination	17202
7001	40.031544, -75.062044	40.58, -74.27	4252
7002	40.031544, -75.062044	40.66, -74.11	4783
7003	40.031544, -75.062044	40.81, -74.18	4909
7004	40.031544, -75.062044	40.88, -74.3	5832

```
