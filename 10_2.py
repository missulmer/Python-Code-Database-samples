"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below"""

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hour_to_count = {}
for line in handle:
    if line.strip().startswith('From '):
        hour = line.strip().lower().split()[5].split(':')[0] # example of consolidation of code into a single line.  Not a best practice due to brittleness
        hour_to_count[hour] = hour_to_count.get(hour, 0) + 1

hour_key = hour_to_count.keys()
hour_key.sort()

for h in hour_key:
    print h, hour_to_count[h]