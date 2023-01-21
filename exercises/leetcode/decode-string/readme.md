# decode-string

https://leetcode.com/problems/decode-string

## brief

- create a stack that will hold the history of chars
- insert until you get to a closer bracket `]`
- when you get to a closer bracket, you need to find:
  - the string between the brackets
  - the multiplier before the opening bracket `[`
- the string is easy, just connect chars until `[`
- the multiplier is from `[` until end of stack or char is not a digit
- as we get both values, we decode the string and push it to the stack
- we push back to the stack in case this is a string inside a string
