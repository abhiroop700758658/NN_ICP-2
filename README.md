# NN_ICP-2

**Code Execution Link :**  https://drive.google.com/file/d/1MmOsbuDIS8fCxthBMxx1r2ShKTEo1NOt/view?usp=sharing

**ICP_2_1_fullname**

**Description:**
This Python script defines two functions: `fullname` and `string_alternative`. The `fullname` function takes a first name (`fname`) and a last name (`lname`) as parameters, concatenates them with a space in between, and returns the full name. The `string_alternative` function takes a string (`funame`) as input and extracts the characters at even indices, creating a new string of alternate characters. The script then takes user input for first and last names, calls the functions, and prints the full name followed by the string of alternate characters.

**Usage:**
1. The user is prompted to enter their first name.
2. The user is prompted to enter their last name.
3. The script calls the `fullname` function to concatenate the first and last names and prints the full name.
4. The script calls the `string_alternative` function to extract alternate characters from the full name and prints the result.

**Example:**
Enter your first name:
Good 
Enter your last name:
evening
Full Name: Good evening
Alternate Characters: Go vnn

The time complexity is O(n)  and the space complexity is O(m)

**ICP_2_2_wordcount**

**Description:**
This Python script reads content from an input text file, prints the content, counts the occurrences of each unique word, and writes the results to an output text file. It utilizes file I/O operations and basic string processing.

**Usage:**
1. The script reads content from an input text file named "input.txt".
2. It prints the content of the input file.
3. It counts the occurrences of each unique word in the content.
4. The results, including the word count, are written to an output text file named "output.txt".
5. The script prints each unique word and its count to the console.

**Example:**
Input File (input.txt):
This is a sample text. Text contains words. This is a sample.

Python Course
Deep Learning Course

Output File (output.txt):
This is a sample text. Text contains words. This is a sample.

Python Course
Deep Learning Course
Word_Count:
Python: 1
Course: 2
Deep: 1
Learning: 1

The time complexity is O(n)  and the space complexity is O(m)

**ICP_2_3_intocm.py**

**Description:**
This Python script takes the number of values to be converted from inches to centimeters as input. It then prompts the user to enter inches values, converts each value to centimeters, and prints the original inches values along with their corresponding centimeter values.

**Usage:**
1. The user is prompted to enter the number of values to be converted.
2. The script then takes input for each inches value and converts it to centimeters (1 inch = 2.54 cm).
3. The original inches values and their corresponding centimeter values are printed to the console.

Example:
Enter number of values to be converted: 3
Enter inches values:
1.5
2.0
3.25
Inches: [1.5, 2.0, 3.25]
CM: [3.81, 5.08, 8.255]

The time complexity is O(x)  and the space complexity is O(x)
