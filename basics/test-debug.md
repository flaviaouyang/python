# TESTING and DEBUGGING

## Defensive Programming

- write specifications for functions
- modularize programs
- check conditions on input/outputs (assertions)

## Good practices from the start

- break program up into modules that can be tested and debugged individually
- **Document constraints** on modules:
  - what's the expected input/output
- **Document assumptions** behind software design

## Classes of tests

1. Unit tests
   1. validate each piece of program
   2. test each function separately
2. Regression testing
   1. add tests for bugs as you find them
   2. catch reintroduced errors that were previously fixed
3. Integration testing
   1. does overall program work?

## Black Box Testing

- designed without looking at the code
- can be done by people other than the implementer to avoid implementer biases
- testing can be reused if implementation changes
- **paths** through specification
  - build test cases in different natural space partitions
  - consider boundary conditions (empty list, singleton list, large/small numbers, etc)
- test

## Glass Box Testing

- **use code** directly to guide design of test cases
- called **path-complete** if every potential path through code is tested at least once
- drawbacks:
  - can go through loops arbitrarily many times
  - missing paths
- guidelines
  - branches: exercise all parts of a conditional
  - for loops: loop not entered; executed exactly once; executed more than once
  - while loops: same as for loops; catch all ways to exit loops
