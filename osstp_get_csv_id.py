#!/usr/bin/env python
# encoding: utf-8

import csv

id_list = []

with open('osstpmgt.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        id_list.append(row[1])
print len(id_list)
print ','.join(id_list)
