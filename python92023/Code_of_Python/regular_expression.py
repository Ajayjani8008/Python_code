import re
text='''Refresh this list to see the latest articles.
21 February 2023: Former South ajaykumar878@email.com Carolina governor Nvirtually'''
pattern=r'\b\w+@\w+\.\w+\b'
matches=re.findall(pattern,text)

search=re.search(pattern,text)
print(search)
print(matches)

text1 = "My email addresses are example1@email.com and example2@email.com. Please contact me."

# Define a regular expression pattern to match email addresses
pattern1 = r'\b\w+@\w+\.\w+\b'
matches1=re.finditer(pattern1,text1)
# matches1=re.findall(pattern1,text1)

# Iterate through the matches and print them
for match in matches1:
    # print(match.group())
    print(text1[match.span()[0]:match.span()[1]])
    # print(match)

''' IMPORTANT WEBSITE FOR REGEX:    1.python docs 2.RegExr.com'''
