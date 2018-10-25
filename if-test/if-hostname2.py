#!/usr/bin/env python3

#hostname = 'MTG'

hostname = input("What is your hostname? ")
hostname = hostname.upper()

if hostname == 'MTG':
  print('The hostname was found to be MTG.')
  print('The hostname matches expected config.')
else:
  print('The hostname does not match the expected config.')

print('Exiting the script...')

#Saving time by not commenting.

