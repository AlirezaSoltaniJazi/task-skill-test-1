# Skill Test

## Question 1

This question is about designing test cases for a specific flow.

[Solution: Test Cases](./documentations/question_1.xlsx)

About automation:

1. I'd prefer to execute all test cases manually for the first time.
2. I'd try to automate main functions or main scenario (smoke test)
3. I'd try to automate the test cases that cost a lot of resources, like checking on different devices or screen sizes.
4. I'd try to refactor previous steps to decrease maintenance cost.
5. I'd try to add all test cases to the test framework.

## Question 2

### Scenario 1

[Solution: Implementing Test by Appium + Python + pytest](./tests/test_purchase.py)

### Scenario 2

#### Question 1

a. We can be sure by asserting the title of the page. If not, it returns a `NoSuchElement` exception because it attempts
to address or locate an element on the wrong page. For slow connections, we can use wait. There are three types of
waits: implicit, explicit, and fluent. Choose the best one based on your requirements. Be careful, never mix implicit
and explicit waits together.

b. I've implemented the necessary wait for locating my elements. Also, I've logged what were necessary.

#### Question 2

As I see it, it depends on your context; however, there are some necessary requirements like:

- Required packages
- Required emulators or simulators
- Required mock setup or server setup
- Required test data
- Required time and resources, and so on.

#### Question 3

It's a good idea to verify page data. We can be sure that everything works correctly. Moreover, it gives us enough
confidence that we wrote perfect tests, also there is good idea to do data validation to have a full End-to-End (
Horizontal & Vertical) test.
