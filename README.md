# String-Compression-Problem-from-YouTube-Shorts

Inspired by this video: https://www.youtube.com/shorts/F8aSFGoUuMg

Basically, given a string (say "AAAABBCC"), how do you compress it such that repeated characters can be truncated?
The challenge is that you need to be able to expand the output without ambiguity on which part is the count, and which part is the actual string.
A common solution in the comment section is to store the count somewhere else (like a hashmap), but the way I see it is that the output should still be a string.

One solution is attaching the count at the end of the string, separated by a special character, say "(".
So something like "AAAABBCC" can be compressed to "ABC(4,2,2".
We can be sure that whatever the output string is, the count will always be at the end, marked by the last appearance of the character "(".
