A version of the FuzzyMatcher with manual conflict resolution for matching similarity cases

Ex:

Input: slavania
Expected Output: Slovenia
Actual Output: Slovakia

This occurs because both Slovenia and Slovakia are two changes away from slavania, and Slovakia occurs first in the countries list.

I think at this point it becomes less of a distance problem, and I would have to create a dataset of common typos.
