# Count the first non repeating character in a String.

Time Complexity-O(n)
Solution 1 python

Solution-To count the first non repeating character in a string the working is as follows-


1. Create a set that will store the unique characters of the string and an array that will store our unique letters.
2. Loop through the string in reverse.
3. Check if letter is not in set.If it is there proceeed to step 5.
4. Add the letter to the array and store the letter in the set
5. If the letter is already there in the set then remove the letter from the array
6. When the loop ends check if there is any character in the array at the end of it
7. The character is the first non recurring character in the list.

Solution 2 python
Solution -Use a stack along with an set

1. Create a set and a empty stack.
2. Loop though the letters in reverse and repeat next step
3. If the letter is not in set repeat the steps 4 and 5 else go to step 6.
4. Store the current letter in the set
5. Store the current letter in the stack.
6. Check if the top of stack is current letter and if it is remove the letter from the stack.
7. The letter at the top of the stack is your result.


=======


1.Create a set that will store the unique characters of the string and an array that will store our unique letters.

2 Loop through the string in reverse.

3.Check if letter is not in set.If it is there proceeed to step 5.

4.Add the letter to the array and store the letter in the set

5.If the letter is already there in the set then remove the letter from the array

6.When the loop ends check if there is any character in the array at the end of it

7.The character is the first non recurring character in the list.
