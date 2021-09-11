# Count the first non repeating character in a String.

Time Complexity-O(n)

Solution-To count the first non repeating character in a string the working is as follows-

1.Create a set that will store the unique characters of the string and an array that will store our unique letters.

2 Loop through the string in reverse.

3.Check if letter is not in set.If it is there proceeed to step 5.

4.Add the letter to the array and store the letter in the set

5.If the letter is already there in the set then remove the letter from the array

6.When the loop ends check if there is any character in the array at the end of it

7.The character is the first non recurring character in the list.
