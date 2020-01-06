import re

#Input - language = Latin.

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#The first code finds non-alpha-numeric characters in the text

#Creating a pattern to search for
pattern = '[^a-zA-Z0-9]'
#Searching for occurences in the pattern 
results = re.findall(pattern, lorem_ipsum)

#Printing the results
print(len(results))

##### END SECTION 1 #######

#The second code finds all occurances of sit amet with various
#intermediate symbols
#creates a searchable variable called patter2
pattern2 = 'sit[-:]amet'
#searches lorem_ipsum for pattern2
occurrance_sit_amet = re.findall(pattern2, lorem_ipsum)

#outputs the number of occurrances of pattern2
print(len(occurrance_sit_amet))

##### END SECTION 2 #######

#The last section here replaces the occurrances of sit amet
#which have the various errors with the corrected version.

#creates a variable for correcting the incorrect sit amet occurrances
correction = 'sit amet'
#replaces the erroneous sit[-:] amet with proper version
replace_results = re.sub(pattern2, correction, lorem_ipsum)
#finds the amount of times the correct sit amet occurs
occurrance_sit_amet = re.findall(correction, replace_results)

#outputs results
print(len(occurrance_sit_amet))

##### END SECTION 3 #######