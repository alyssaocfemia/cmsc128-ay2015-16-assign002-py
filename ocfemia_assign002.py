#!/usr/bin/python

#AUTHOR: Alyssa Fae S. Ocfemia
#SECTION: AB-1L
#DATE: March 12, 2016

# Gets the Hamming Distance of two strings by the number of characters that
# differ in ith position from position 1 to strlen(str1).
# variable distance will be the counter for the number of characters that differs
# between the two strings
# The loop just traverse both strings and compares each characters
def getHammingDistance(string1,string2):
	print "FUNCTION 1: GET HAMMING DISTANCE";
	distance = 0
	if len(string1) == len (string2) and len(string1) > 0 and len(string2) > 0:
			for i in range(0, len(string1 )):
				if string1[i] != string2[i]:
					distance = distance + 1	
			return distance;
	else:
		print "Error! Strings are not equal!"; 
	return -1;
	
# Given a string original and pattern, we will count the number of occurrence
# of pattern in original.	
# variable count is the number of times that the pattern is a substring of the
# variable string
# The first loop just traverse through the string from the first position to the
# the position which is the difference of the length of string and the length of
# the pattern
# The second loop or the nested one traverse the characters of the pattern
# The if statements just checks if the the pattern exist in the given indices and
# counts it by adding 1 to the counter 'count'. 	
def countSubstrPattern(string, pattern):
	print "FUNCTION 2: COUNT SUBSTRING PATTERN";
	count = 0
	for i in range(0, len(string )-len(pattern)+1):
		k = 0
		for j in range(0, len(pattern)):
			if string[i+j] == pattern[j]:
				k = k + 1
			if k == len(pattern):
				count = count + 1
	return count;

# This function returns true if the string str is a valid string 
# based on the letters of alphabet.
# variable k is just a checker
# The first loop just traverse the characters of the string
# The second loop just traverse the characters of the alphabet
# It also contains the if statement that check if the letter from the
# string is included in the alphabet
def isValidString(string, alphabet):
	print "FUNCTION 3: VALID STRING";
	
	for i in range(0, len(string)):
		k = 0
		for j in range(0, len(alphabet )):
			if string[i] == alphabet[j]:
				k = k + 1
		if k == 0:
			return False;
	return True;

# It returns the number of Gs minus the number of Cs in the first n nucleotides (q>=n).
# The value can be zero, negative or positive. The first position is one (1) not zero(0)
# as we typically associate with string implementations.	
# Variable g is the counter for the number of Gs and variable c for the Cs
# The loop just traverse from the first position to the the nth position
# The if statements just checks if it is G or C or other letters. It also counts the
# occurences of G and C
def getSkew(string, n):
	print "FUNCTION 4: GET SKEW";
	g = 0
	c = 0
	for i in range(0, n):
		if string [i] == 'G':
			g = g + 1
		elif string [i] == 'C':
			c = c + 1
	
	return g - c;

# It returns the maximum value of the number of Gs minus the number of Cs in the first
# n nucleotides (q>=n). The value can be zero, negative or positive. The first position
# is one (1) not zero(0) as we typically associate with string implementations.	
# Variable g is the counter for the number of Gs and variable c for the Cs
# The loop just traverse from the first position to the the nth position
# The if statements just checks if it is G or C or other letters. It also counts the
# occurences of G and C
# It also has another if statement to store that maximum value of all the skews
def getMaxSkewN(string, n):
	print "FUNCTION 5: GET MAX SKEW N";
	g = 0
	c = 0
	maxskew = 0
	for i in range(0, n ):
		if string [i] == 'G':
			g = g + 1
		elif string [i] == 'C':
			c = c + 1
		if maxskew < (g - c):
			maxskew = g - c
	return maxskew;

# It returns the minimum value of the number of Gs minus the number of Cs in the first
# n nucleotides (q>=n). The value can be zero, negative or positive. The first position
# is one (1) not zero(0) as we typically associate with string implementations.
# Variable g is the counter for the number of Gs and variable c for the Cs
# The loop just traverse from the first position to the the nth position
# The if statements just checks if it is G or C or other letters. It also counts the
# occurences of G and C
# It also has another if statement to store that minimum value of all the skews
def getMinSkewN(string, n):
	print "FUNCTION 6: GET MIN SKEW N";	
	g = 0
	c = 0
	
	for i in range(0, n ):
		if string [i] == 'G':
			g = g + 1
		elif string [i] == 'C':
			c = c + 1
		if i == 0:
			minskew = g - c
		if minskew > (g - c):
			minskew = g - c
	return minskew;

#TEST CASES
print getHammingDistance("AACCTT","GGCCTT");
print getHammingDistance("TCGGA","AAAAG");
print getHammingDistance("A","AG");

print countSubstrPattern("AATATATAGG","GG");
print countSubstrPattern("AATATATAGG","ATA");
print countSubstrPattern("AATATATAGG","ACTGACTGACTG");

print isValidString("AAGGCTATGC","ACGT");
print isValidString("AAGGCTATGK","ACGT");
print isValidString("ACGT","ACGT");
print isValidString("ACGT101_","ACGT");
print isValidString("091212345","0123456789");

print getSkew("GGCCAC", 1); 
print getSkew("GGCCAC", 2);
print getSkew("GGCCAC", 3); 
print getSkew("GGCCAC", 4);
print getSkew("GGCCAC", 5);

print getMaxSkewN("GGCCAC", 1); 
print getMaxSkewN("GGCCAC", 2);
print getMaxSkewN("GGCCAC", 3); 
print getMaxSkewN("GGCCAC", 4);
print getMaxSkewN("GGCCAC", 5);

print getMinSkewN("GGCCAC", 1); 
print getMinSkewN("GGCCAC", 2);
print getMinSkewN("GGCCAC", 3); 
print getMinSkewN("GGCCAC", 4);
print getMinSkewN("GGCCAC", 5);
