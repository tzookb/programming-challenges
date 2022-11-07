# apply-operations-to-an-array

https://leetcode.com/problems/apply-operations-to-an-array

## brief

- running from first item till one before last
- for each pair if they are equal, perfom the rules
- now we need to move the zeros to the end
- create pointer for next_val, it will start from the beginning
- loop over the items, if item is 0
- continue to the next item, and count the zero in the zeros counter
- if item is not 0, set it to the "next_val" position, increment the next_pos to the next cell
- now the last step is just fill the counted zeros from the back
