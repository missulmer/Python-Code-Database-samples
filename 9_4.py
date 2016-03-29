""" 9.4 Write a program to read through the mbox-short.txt and
figure out who has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

Desired output = cwen@iupui.edu 5
"""

filename = raw_input("enter file name:")
handle = None

try:
    handle = open(filename)
except:
    print 'File cannot be opened or read.', filename
    exit()

counts = {}
for line in handle:
    if line.strip().startswith('From:'):
        line = line.strip().lower()
        words = line.split()

        for word in words:
            if '@' in word:
                counts[word] = counts.get(word, 0) + 1
handle.close()
# always close the file as soon as possible. Freeing resources asap is a best practice.

email = None
email_count = 0
for word,count in counts.items():
    if email is None or count > email_count:
        email = word
        email_count = count

print email, email_count

