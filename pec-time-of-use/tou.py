#!/usr/bin/env python

import csv
from datetime import datetime

_format = "%Y-%m-%d %H:%M"
_normrate = (0.02712+0.0605+0.01256)
_normrate = 0.0605

def main():
    filename="unbilled.csv"
    output="unbilled.out.csv"
    toutotal = 0
    normtotal = 0
    with open(filename, 'r') as csvfile, open(output, "w") as outfile:
        usageinfo = csv.reader(csvfile)
        writer = csv.writer(outfile)
        for row in usageinfo:
            if not row:
                continue
            cost = process_row(row)
            toutotal += cost
            normtotal += float(row[2]) * _normrate
            writer.writerow(row + [cost])
    print("Normal: {}, Tou: {}".format(normtotal, toutotal))


def process_row(row):
    starttime = datetime.strptime(row[0], _format)
    endtime = datetime.strptime(row[1], _format)
    kWh = float(row[2])
    return kWh * time_to_rate(starttime)


def time_to_rate(dt):
    # summar June to Sept
    if dt.month > 5 and dt.month < 10:
        return summer_rate(dt)
    return winter_rate(dt)


def summer_rate(dt):
    if dt.hour >= 0 and dt.hour < 3:
        return 0.0436  # economy
    elif dt.hour >= 3 and dt.hour < 5:
        return 0.039  # super economy
    elif dt.hour >= 5 and dt.hour < 7:
        return 0.0436  # economy
    elif dt.hour >= 7 and dt.hour < 12:
        return 0.0536  # normal
    elif dt.hour >= 12 and dt.hour < 14:
        return 0.0698  # peak
    elif dt.hour >= 14 and dt.hour < 18:
        return 0.1026  # super peak
    elif dt.hour >= 18 and dt.hour < 20:
        return 0.0698  # peak
    elif dt.hour >= 20 and dt.hour < 23:
        return 0.0536  # normal
    elif dt.hour >= 23:
        return 0.0436  # economy


def winter_rate(dt):
    if dt.hour >= 0 and dt.hour < 2:
        return 0.0426  # economy
    elif dt.hour >= 2 and dt.hour < 4:
        return 0.0376  # super economy
    elif dt.hour >= 4 and dt.hour < 5: 
        return 0.0426  # economy
    elif dt.hour >= 5 and dt.hour < 8: 
        return 0.0677  # peak
    elif dt.hour >= 8 and dt.hour < 16: 
        return 0.0586  # normal
    elif dt.hour >= 16 and dt.hour < 19: 
        return 0.0677  # peak
    elif dt.hour >= 19 and dt.hour < 23: 
        return 0.0586  # normal
    elif dt.hour >= 23:
        return 0.0426  # economy


if __name__ == "__main__":
    main()

