# Dice Paraodx - Odds of doubles are 1/6  or 1/11 ?

# Background and Explanation

A person rolls two dice, hidden from view.  They peek at one of the dice, and says "I saw one of the dice and it was a 1". You are then asked what are the odds that the other dice also is a 1? The official explanation is that the answer is 1/11 . The actual answer is 1/6. We will now explore why the official answer is wrong and why our python code detects 1/6. 

# About The Program
The program is designed to walk through the exact same scenario.  The dice are "rolled" using random number generation.  Another random number is generated to determine which dies is "peeked at".  We then check the other dice to see if its a double, and we record the success and failures of each individual number. At the end of the program, the results are displayed with the percents displayed in decimal form.  

# Probabilities and Explanation
There are 11 permutations of dice A and dice B with a 1 in it:
(1,1)  - the only set of doubles
(1,2) (1,3) (1,4) (1,5) (1,6)
(2,1) (3,1) (4,1) (5,1) (6,1)

If we were to (incorrectly) treat them all as being detected at equal rates, this would mean that double 1's would be 1 out of the 11 possibilities.  We can calculate this by simply counting the total possibilities (11) and counting how many times we have two 1's (only once). This seems mathematically correct and simple to calculate. However, the error is similar to that of 1/3 result in the Boy/Girl paradox. In a true random sampling, you will not detect all of our possibilities at the same rate.  The (1,1) roll will actually be detected twice as much as the others.

The reason is that the person rolling a dice will always peek and see a 1 when there are two 1's.  Every single time two 1's are rolled, and a person peeks, they have no choice but to see a 1.  There are no other possibilities. So when the roll is (1,1), a 1 will be detected on peeking 100% of the time.  

Now, this is not true for a roll with only a single 1 in it.  For example, lets take a look at rolls of 1,6 or 3,1 .  Half of the time, the dice roller will peek at one of the dice and simply not see a 1. So for pairs like 1,6 and 3,1 , we have only a 50% chance of detecting the 1.  For instance if we roll a 3,1 and randomly peak at one of the dice, we might see a 3 instead of the 1. If we detect a 3 when we peek, we would then be asked what are the odds that there is another 3.  Since we are determining the odds for double 1's, this incident where we peeked and detected a 3 is discarded. It is not relevant and we never learn about that other 1 in the roll. It is never detected.  Of course there is a 50% chance the dice roller will peek and see a 1, so sometimes they will in fact see a 1, but the main takeaway is that half the time this doesn't happen. 

The end result of the difference in the rate of detection between double 1's (1,1) and all other rolls with at least one 1 (1,x or x,1) is that the double 1's (1,1) are detected twice as much as all other pairs (1,x). This is what inevitable makes the 1/11 calculation wrong. Since we see the (1,1) double roll twice as much as the others, it changes the results from 1/11 to 2/12... making the actual result 1/6.  


# Intuitive Walkthrough
The 11 permutations of dice A and dice B:
(1,1)  - the only set of doubles
(1,2) (1,3) (1,4) (1,5) (1,6)
(2,1) (3,1) (4,1) (5,1) (6,1)

With two dice with six numbers each, we have 36 permutations of potential outcomes - 6 possibilities on dice A * 6 possibilities on dice B. Each permutation has a 1/36 chance of occurring.  Let's pretend we roll the dice 36 times, and pretend we get each of these results once (which is unlikely, but maintains the probabilities given). Each of the perrmutations that we care about (listed at the start of this section) appear once, as tehy are a part of the full set.  Now let's pretend we roll the dice another 36 times, and get the same results where we get every possible permutation a second time (again, very unlikely, but this maintains the probabilities). Every permutation that we care about has now appeared twice. 

We have now have the following results (non-relevant rolls with a 1 were discarded):
(1,1)
(1,1)
(1,2) (1,3) (1,4) (1,5) (1,6)
(1,2) (1,3) (1,4) (1,5) (1,6)
(2,1) (3,1) (4,1) (5,1) (6,1)
(2,1) (3,1) (4,1) (5,1) (6,1)

Now if these results had been hidden from a viewer, and this viewer randomly peaked at ONLY one of the dice in each roll, they will detect a 1 in both of the (1,1) rolls. As we discussed, there is a 100% chance a 1 will be detected upon peeking when the roll is (1,1). For all of the other rolls, if they only peak at one die, there is a 50% chance they will see a 1. In the roll (3,1) they might peak at a 3.  This result will be discarded. If we were to follow through with this, and pretend that the 1 was not seen in those with a 50% exactly half the time, we would be left with the following set:

(1,1)
(1,1)
(1,2) (1,3) (1,4) (1,5) (1,6)
(2,1) (3,1) (4,1) (5,1) (6,1)
*notice that both the double 1's remain, while half as many of the others remain

What this set represents is the outcomes that will be detected as having at least one 1 upon peaking, if we rolled the dice 72 times.  Now we can do our calculation on how many of the outcomes were dobule 1's (1,1).  There are 12 dice rolls that matched our criteria, and 2 had double 1's. The result is that 2/12 have doubles, or 1/6 .  

# Programming results:
Here is th output from my programming

Sample Size: 900000 

When the single, randomly observed dice is 1 :
  Total cases: 149896
  Match (success): 24800 (0.165448)
  No match (failure): 125096

When the single, randomly observed dice is 2 :
  Total cases: 149414
  Match (success): 25086 (0.167896)
  No match (failure): 124328

When the single, randomly observed dice is 3 :
  Total cases: 149817
  Match (success): 24966 (0.166643)
  No match (failure): 124851

When the single, randomly observed dice is 4 :
  Total cases: 150022
  Match (success): 25106 (0.167349)
  No match (failure): 124916

When the single, randomly observed dice is 5 :
  Total cases: 150161
  Match (success): 24827 (0.165336)
  No match (failure): 125334

When the single, randomly observed dice is 6 :
  Total cases: 150690
  Match (success): 25001 (0.16591)
  No match (failure): 125689



