#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:58:43 2018
@author: phil
"""

import os
import sys
from math import *
import csv
import datetime
from datetime import date
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pandas as pandas
import matplotlib.pyplot as plt


now = datetime.datetime.today()
sep = '\n' + '\t' + 40 * '=' + '\n'
my_amount = 300
val = "Estimated value with 300 stocks:"

urls = ['https://web.tmxmoney.com/quote.php?qm_symbol=TGOD&locale=EN', 'https://web.tmxmoney.com/quote.php?qm_symbol=HEXO&locale=EN', 'https://web.tmxmoney.com/quote.php?qm_symbol=HIP&locale=EN', 'https://web.tmxmoney.com/quote.php?qm_symbol=TLRY:US', 'https://web.tmxmoney.com/quote.php?qm_symbol=WEED', 'https://web.tmxmoney.com/quote.php?qm_symbol=FIRE&locale=EN', 'https://web.tmxmoney.com/quote.php?qm_symbol=ALEF', 'https://web.tmxmoney.com/quote.php?qm_symbol=GLH:CNX', 'https://web.tmxmoney.com/quote.php?qm_symbol=N&locale=EN']

res = [get(urls[0]), get(urls[1]), get(urls[2]), get(urls[3]), get(urls[4]), get(urls[5]), get(urls[6]), get(urls[7]), get(urls[8])]

soup = [BeautifulSoup(res[0].text, 'html.parser'), BeautifulSoup(res[1].text, 'html.parser'), BeautifulSoup(res[2].text, 'html.parser'), BeautifulSoup(res[3].text, 'html.parser'), BeautifulSoup(res[4].text, 'html.parser'), BeautifulSoup(res[5].text, 'html.parser'), BeautifulSoup(res[6].text, 'html.parser'), BeautifulSoup(res[7].text, 'html.parser'), BeautifulSoup(res[8].text, 'html.parser')]

if len(urls) == len(res) == len(soup):
    print('\n', "Ok all list lenght match!", "#items:", len(urls))
	print('\n', "Today date:", date.today())
	print('\n', "To print all data use function print_data()")

URLS = list(enumerate(urls, start=1))
# #####################
# ###TGOD####
# #####################
# Get url
# tgod_url = 'https://web.tmxmoney.com/quote.php?qm_symbol=TGOD&locale=EN'
# response = get(urls[0])
# Parse html
# Find name
tgod_name_box = soup[0].find('div', class_='quote-ticker tickerLarge')
tgod_name = tgod_name_box.text.strip()
# Find price
tgod_price_full = soup[0].find('div', class_ = 'quote-price priceLarge')
tgod_price_full = tgod_price_full.text.strip()
tgod_price_full = tgod_price_full.strip('$\t')
tgod_price_str = str(tgod_price_full)
tgod_price = float(tgod_price_str)
# Find Open day price
tgod_Open_High = soup[0].find('table', class_ = 'detailed-quote-table')
tgod_Open_High = tgod_Open_High.text.strip()
tgod_Open_High = tgod_Open_High.strip('')
tgod_Open = tgod_Open_High.strip('\n\nHigh:\n10.24\n\n\n\nShares Out.:\n247,899,099\n\n\nBeta:\n-8.984')
# Find prev close price
tgod_high_low = soup[0].find('table', class_ = '')
tgod_high_low = tgod_high_low.text.strip('52 Week Information\nclose')
# Find full_name
tgod_full_name = soup[0].find('h2', class_ = '')
tgod_full_name = tgod_full_name.text.strip()
# Find volume
tgod_volume = soup[0].find('div', class_='quote-volume volumeLarge')
tgod_volume = tgod_volume.text.strip('\nVolume:\r\n\t\t\t\t\t\t\t\t\t\t\t\t')
# Find prev close
tgod_prev = soup[0].find('td', class_ = '')
tgod_prev = tgod_prev.text.strip()
# Find low
tgod_high = soup[0].find('tr', class_ = 'alt')
tgod_high = tgod_high.text.strip()
# Write to csv
with open('tgod_data.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([tgod_name, tgod_price_str+'$', now])

my_tgod_value = int(my_amount*tgod_price)
# tgod_Close =
# tgod_Prev_Close =
# Print some data


def TGOD():
    print('\n', "Request Date: ", now)
    print('\n', '\t', tgod_full_name, '\n', 2*'\t', '\n', tgod_name, 3*'\t', tgod_price_str, '$')
    print('\n', val, my_tgod_value, '$')
    print(2*'\n', 2*'\t', "STATISTICS", '\n')
    print('VOLUME =', tgod_volume, '\n')
    print(tgod_Open_High.strip('\n\n\nBeta:\n-12.916'))
    print(tgod_high_low.strip())
    print(sep)
# ###########################
# ###HEXO####
# ###########################
# Get url
# hexo_url = 'https://web.tmxmoney.com/quote.php?qm_symbol=HEXO&locale=EN'
# hexo_response = get(urls[1])
# Parse html
# hexo_soup = BeautifulSoup(res[1].text, 'html.parser')
# Find name
hexo_name_box = soup[1].find('div', class_ = 'quote-ticker tickerLarge')
hexo_name = hexo_name_box.text.strip()
# Find price
hexo_price_full = soup[1].find('div', class_ = 'quote-price priceLarge')
hexo_price_full = hexo_price_full.text.strip()
hexo_price_full = hexo_price_full.strip('$\t')
hexo_price_str = str(hexo_price_full)
hexo_price = float(hexo_price_str)
# Find Open day price
hexo_Open_High = soup[1].find('table', class_ = 'detailed-quote-table')
hexo_Open_High = hexo_Open_High.text.strip('Beta:\n2.082')
hexo_Open = hexo_Open_High.strip('\n')
# Find prev close price
hexo_high_low = soup[1].find('table', class_ = '')
hexo_prev_close = hexo_high_low.text.strip()
hexo_prev_close = hexo_prev_close.strip('\nVolume:\r\n\t\t\t\t\t\t\t\t\t\t\t\t')
# Find full_name
hexo_full_name = soup[1].find('h2', class_ = '')
hexo_full_name = hexo_full_name.text.strip()
# Find volume
hexo_volume = soup[1].find('div', class_ = 'quote-volume volumeLarge')
hexo_volume = hexo_volume.text.strip()
# Write to csv file
with open('hexo_data.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([hexo_name, hexo_price_str+'$', now])

my_hexo_value = int(my_amount*hexo_price)
# Print some data


def HEXO():
    print('\n', "Request Date: ", now)
    print('\n', '\t', hexo_full_name, '\n', 2*'\t', '\n', hexo_name, 3*'\t', hexo_price, '$')
    print('\n', val, my_hexo_value, '$')
    print(2*'\n', 2*'\t', "STATISTICS", '\n')
    print('VOLUME =', hexo_volume, '\n')
    print(hexo_Open_High.strip('\n\n\nBeta:\n '))
    print(hexo_prev_close.strip('52 Week Information\nclose\n\n\n\r\n\t\t\t'))
    print(sep)
# ###########################
# ###HIP####
# ###########################
# Get url
# hip_url = 'https://web.tmxmoney.com/quote.php?qm_symbol=HIP&locale=EN'
# response = get(urls[2])
# Parse html
# hip_soup = BeautifulSoup(res[2].text, 'html.parser')
# Find name
hip_name_box = soup[2].find('div', class_ = 'quote-ticker tickerLarge')
hip_name = hip_name_box.text.strip()
# Find price
hip_price_full = soup[2].find('div', class_ = 'quote-price priceLarge')
hip_price_full = hip_price_full.text.strip()
hip_price_full = hip_price_full.strip('$\t')
hip_price = float(hip_price_full)
hip_price_str = str(hip_price)
# Find Open day price
hip_Open_High = soup[2].find('table', class_ = 'detailed-quote-table')
hip_Open_High = hip_Open_High.text.strip()
hip_Open_High = hip_Open_High.strip()
hip_Open = hip_Open_High.strip('Open:\n\n\nHigh:\n10.24\n\n\n\nShares Out.:\n247,899,099\n\n\nBeta:\n-8.984')
# Find prev close price
hip_high_low = soup[2].find('table', class_ = '')
hip_high_low = hip_high_low.text.strip('52 Week Information\nclose')
# Find full_name
hip_full_name = soup[2].find('h2', class_ = '')
hip_full_name = hip_full_name.text.strip()
# Find volume
hip_volume = soup[2].find('div', class_ = 'quote-volume volumeLarge')
hip_volume = hip_volume.text.strip('\nVolume:\r\n\t\t\t\t\t\t\t\t\t\t\t\t')
# Find prev close
hip_prev = soup[2].find('td', class_ = '')
hip_prev = hip_prev.text.strip()
# Find low
hip_low = soup[2].find('tr', class_ = 'alt')
hip_low = hip_low.text.strip()
# Write to csv
with open('hip_data.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([hip_name, hip_price_str+'$', now])

my_hip_value = int(my_amount*hip_price)
# Print some data


def HIP():
    print('\n', "Request Date: ", now)
    print('\n', '\t', hip_full_name, '\n', 2*'\t', '\n', hip_name, 3*'\t', hip_price, '$')
    print('\n', val, my_hip_value, '$')
    print(2*'\n', 2*'\t', "STATISTICS", '\n')
    print('VOLUME =', hip_volume, '\n')
    print(hip_Open_High.strip('\n\n\nBeta:\n-12.916'))
    print(hip_high_low.strip())
    print(sep)
# ###########################
# ###TLRAY####
# ###########################
# tlry_url = 'https://web.tmxmoney.com/quote.php?qm_symbol=TLRY:US'
# response = get(urls[3])
# tlry_soup = BeautifulSoup(res[3].text, 'html.parser')
# Find full name
tlry_full_name = soup[3].find('h2', class_ = '')
tlry_full_name = tlry_full_name.text.strip()
# Find name
tlry_name_box = soup[3].find('div', class_ = 'quote-ticker tickerLarge')
tlry_name = tlry_name_box.text.strip()
# Find price
tlry_price_full = soup[3].find('div', class_ = 'quote-price priceLarge')
tlry_price_full = tlry_price_full.text.strip()
tlry_price_full = tlry_price_full.strip('$\t')
tlry_price = float(tlry_price_full)
tlry_price_str = str(tlry_price)
# Find Open day price
tlry_Open_High = soup[3].find('table', class_ = 'detailed-quote-table')
tlry_Open_High = tlry_Open_High.text.strip()
tlry_Open_High = tlry_Open_High.strip()
tlry_Open = tlry_Open_High.strip('Open:\n\n\nHigh:\n10.24\n\n\n\nShares Out.:\n247,899,099\n\n\nBeta:\n-8.984')
my_tlry_value = int(my_amount*tlry_price)


def TLRY():
    print('\n', "Request Date: ", now)
    print('\n', '\t', tlry_full_name, '\n', 2*'\t', '\n', tlry_name, 3*'\t', tlry_price, '$')
    print('\n', val, my_tlry_value, '$')
    print(2*'\n', 2*'\t', "STATISTICS", '\n')
    print(tlry_Open_High.strip('\n\n\nBeta:\n-12.916'))
    print(sep)
# print(tlry_high_low.strip())
# tlry_soup = str(tlry_soup)

with open('tlry_data.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([tlry_name, tlry_price_str+'$', now])
############################
# #WEED##
############################
weed_name_box = soup[4].find('div', class_ = 'quote-ticker tickerLarge')
weed_name = weed_name_box.text.strip()
weed_full_name = soup[4].find('h2', class_ = '')
weed_full_name = weed_full_name.text.strip()
# Find name
weed_name_box = soup[4].find('div', class_ = 'quote-ticker tickerLarge')
weed_name = weed_name_box.text.strip()
# Find price
weed_price_full = soup[4].find('div', class_ = 'quote-price priceLarge')
weed_price_full = weed_price_full.text.strip()
weed_price_full = weed_price_full.strip('$\t')
weed_price = float(weed_price_full)
weed_price_str = str(weed_price)
# Find Open day price
weed_Open_High = soup[4].find('table', class_ = 'detailed-quote-table')
weed_Open_High = weed_Open_High.text.strip()
weed_Open_High = weed_Open_High.strip()
weed_Open = weed_Open_High.strip('Open:\n\n\nHigh:\n10.24\n\n\n\nShares Out.:\n247,899,099\n\n\nBeta:\n-8.984')
my_weed_value = int(my_amount*weed_price)

with open('weed_data.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([weed_name, weed_price_str+'$', now])


def WEED():
    print('\n', "Request Date: ", now)
    print('\n', '\t', weed_full_name, '\n', 2*'\t', '\n', weed_name, 3*'\t', weed_price, '$')
    print('\n', val, my_weed_value, '$')
    print(2*'\n', 2*'\t', "STATISTICS", '\n')
    print(weed_Open_High.strip('\n\n\nBeta:\n-12.916'))
    print(sep)
###################
# FIRE
##################
fire_name_box = soup[5].find('div', class_ = 'quote-ticker tickerLarge')
fire_name = fire_name_box.text.strip()
fire_full_name = soup[5].find('h2', class_ = '')
fire_full_name = fire_full_name.text.strip()
# Find name
fire_name_box = soup[5].find('div', class_ = 'quote-ticker tickerLarge')
fire_name = fire_name_box.text.strip()
# Find price
fire_price_full = soup[5].find('div', class_ = 'quote-price priceLarge')
fire_price_full = fire_price_full.text.strip()
fire_price_full = fire_price_full.strip('$\t')
fire_price = float(fire_price_full)
fire_price_str = str(fire_price)
# Find Open day price
fire_Open_High = soup[5].find('table', class_ = 'detailed-quote-table')
fire_Open_High = fire_Open_High.text.strip()
fire_Open_High = fire_Open_High.strip()
fire_Open = fire_Open_High.strip('Open:\n\n\nHigh:\n10.24\n\n\n\nShares Out.:\n247,899,099\n\n\nBeta:\n-8.984')
my_fire_value = int(my_amount*fire_price)

with open('fire_data.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([fire_name, fire_price_str+'$', now])


def FIRE():
    print('\n', "Request Date: ", now)
    print('\n', '\t', fire_full_name, '\n', 2*'\t', '\n', fire_name, 3*'\t', fire_price, '$')
    print('\n', val, my_fire_value, '$')
    print(2*'\n', 2*'\t', "STATISTICS", '\n')
    print(fire_Open_High.strip('\n\n\nBeta:\n-12.916'))
    print(sep)

#######################
	# ALEF
#######################
alef_name_box = soup[6].find('div', class_ = 'quote-ticker tickerLarge')
alef_name = alef_name_box.text.strip()
alef_full_name = soup[6].find('h2', class_ = '')
alef_full_name = alef_full_name.text.strip()
# Find name
alef_name_box = soup[6].find('div', class_ = 'quote-ticker tickerLarge')
alef_name = alef_name_box.text.strip()
# Find price
alef_price_full = soup[6].find('div', class_ = 'quote-price priceLarge')
alef_price_full = alef_price_full.text.strip()
alef_price_full = alef_price_full.strip('$\t')
alef_price = float(alef_price_full)
alef_price_str = str(alef_price)
# Find Open day price
alef_Open_High = soup[6].find('table', class_ = 'detailed-quote-table')
alef_Open_High = alef_Open_High.text.strip()
alef_Open_High = alef_Open_High.strip()
alef_Open = alef_Open_High.strip('Open:\n\n\nHigh:\n10.24\n\n\n\nShares Out.:\n247,899,099\n\n\nBeta:\n-8.984')
my_alef_value = int(my_amount*alef_price)

with open('alef_data.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([alef_name, alef_price_str+'$', now])


def ALEF():
    print('\n', "Request Date: ", now)
    print('\n', '\t', alef_full_name, '\n', 2*'\t', '\n', alef_name, 3*'\t', alef_price, '$')
    print('\n', val, my_alef_value, '$')
    print(2*'\n', 2*'\t', "STATISTICS", '\n')
    print(alef_Open_High.strip('\n\n\nBeta:\n-12.916'))
    print(sep)
##################
	# Glh
##################
glh_name_box = soup[7].find('div', class_ = 'quote-ticker tickerLarge')
glh_name = glh_name_box.text.strip()
glh_full_name = soup[7].find('h2', class_ = '')
glh_full_name = glh_full_name.text.strip()
# Find name
glh_name_box = soup[7].find('div', class_ = 'quote-ticker tickerLarge')
glh_name = glh_name_box.text.strip()
# Find price
glh_price_full = soup[7].find('div', class_ = 'quote-price priceLarge')
glh_price_full = glh_price_full.text.strip()
glh_price_full = glh_price_full.strip('$\t')
glh_price = float(glh_price_full)
glh_price_str = str(glh_price)
# Find Open day price
glh_Open_High = soup[7].find('table', class_ = 'detailed-quote-table')
glh_Open_High = glh_Open_High.text.strip()
glh_Open_High = glh_Open_High.strip()
glh_Open = glh_Open_High.strip('Open:\n\n\nHigh:\n10.24\n\n\n\nShares Out.:\n247,899,099\n\n\nBeta:\n-8.984')
my_glh_value = int(my_amount*glh_price)

with open('glh_data.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([glh_name, glh_price_str+'$', now])


def GLH():
    print('\n', "Request Date: ", now)
    print('\n', '\t', glh_full_name, '\n', 2*'\t', '\n', glh_name, 3*'\t', glh_price, '$')
    print('\n', val, my_glh_value, '$')
    print(2*'\n', 2*'\t', "STATISTICS", '\n')
    print(glh_Open_High.strip('\n\n\nBeta:\n-12.917'))
    print(sep)

#######################
# NAMASTE
######################
n_name_box = soup[8].find('div', class_ = 'quote-ticker tickerLarge')
n_name = n_name_box.text.strip()
n_full_name = soup[8].find('h2', class_ = '')
n_full_name = n_full_name.text.strip()
# Find name
n_name_box = soup[8].find('div', class_ = 'quote-ticker tickerLarge')
n_name = n_name_box.text.strip()
# Find price
n_price_full = soup[8].find('div', class_ = 'quote-price priceLarge')
n_price_full = n_price_full.text.strip()
n_price_full = n_price_full.strip('$\t')
n_price = float(n_price_full)
n_price_str = str(n_price)
# Find Open day price
n_Open_High = soup[8].find('table', class_='detailed-quote-table')
n_Open_High = n_Open_High.text.strip()
n_Open_High = n_Open_High.strip()
n_Open = n_Open_High.strip('Open:\n\n\nHigh:\n10.24\n\n\n\nShares Out.:\n247,899,099\n\n\nBeta:\n-8.984')
my_n_value = int(my_amount*n_price)

with open('n_data.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([n_name, n_price_str+'$', now])


def N():
    print('\n', "Request Date: ", now)
    print('\n', '\t', n_full_name, '\n', 2*'\t', '\n', n_name, 3*'\t', n_price, '$')
    print('\n', val, my_n_value, '$')
    print(2*'\n', 2*'\t', "STATISTICS", '\n')
    print(n_Open_High.strip('\n\n\nBeta:\n-12.917'))
    print(sep)

########################
# #PRINT##
########################
# comp_data = [TGOD(),HEXO(),HIP(),TLRY(),WEED(),FIRE(),ALEF(),GLH(),N()]


def print_data():
	TGOD()
	HEXO()
	HIP()
	TLRY()
	WEED()
	FIRE()
	ALEF()
	GLH()
    N()

print_data()
