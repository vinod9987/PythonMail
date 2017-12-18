#!/usr/bin/python
num_lines = sum(1 for line in open('access.log','r'))
if num_lines < 6000:
 with open('/var/www/html/abc.html','w') as fil:
  fil.write('Threshold not exceeded\n')
else:
 with open('/var/www/html/abc.html','w') as fil:
  fil.write('Threshold exceeded\n')
