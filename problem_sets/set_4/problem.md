# First Part
In this problem set, you'll implement two versions of a wordgame!

Don't be intimidated by the length of this problem set. There is a lot of reading, but it can be done with a reasonable amount of thinking and coding. It'll be helpful if you start this problem set a few days before it is due!

Let's begin by describing the 6.00 wordgame: This game is a lot like Scrabble or Words With Friends, if you've played those. Letters are dealt to players, who then construct one or more words out of their letters. Each valid word receives a score, based on the length of the word and the letters in that word.

The rules of the game are as follows:

**Dealing**
- A player is dealt a hand of _n_ letters chosen at random (assume _n=7_ for now).

- The player arranges the hand into as many words as they want out of the letters, using each letter at most once.

- Some letters may remain unused (these won't be scored).

**Scoring**
- The score for the hand is the sum of the scores for each word formed.

- The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all _n_ letters are used on the first word created.

- Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary `SCRABBLE_LETTER_VALUES` that maps each lowercase letter to its Scrabble letter value.

- For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by `len('weed')` to get (4+1+1+2)*4 = 32). Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

- As another example, if _n=7_ and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all _n_ letters).

**Sample Output**
**Here is how the game output will look!**

```
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points
Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
Invalid word, please try again.
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points
Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points
Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points
Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```

# Second Part
**Part B is dependent on your functions from `ps4a.py`, so be sure to complete `ps4a.py` before working on `ps4b.py`**
Now that you have completed your word game code, you decide that you would like to enable your computer (SkyNet) to play the game (your hidden agenda is to prove once and for all that computers are inferior to human intellect!) In this part, you will be able to compare how you as a user succeed in the game compared to the computer's performance.

You should look at the following two functions: `compChooseWord` and `compPlayHand`, before moving on to Problem 7 on the next page.

### compChooseWord
If you follow the pseudocode for `compChooseWord`, you'll see that the code creates a computer player that is legal, but not always the best. Try to walk through and understand our implementation.

**A Note On Runtime**: You may notice that things run a bit slowly when the computer plays. This is to be expected - the wordList has 83667 words, after all! 

**Test Cases to Understand the Code:** 
```
>>> compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6) 
appels 
>>> compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5) 
acta 
>>> compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12) 
immanent 
>>> compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12) 
None
```

### compPlayHand
Now that we have the ability to let the computer choose a word, we need to set up a function to allow the computer to play a hand - in a manner very similar to Part A's `playHand` function. This function allows the computer to play a given hand and is very similar to the earlier version in which a user selected the word, although deciding when it is done playing a particular hand is different

**Test Cases to Understand the Code:**

```
compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
Current Hand: a p p s e l
"appels" earned 110 points. Total: 110 points
Total score: 110 points.

compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
Current Hand: a a c b t "acta" 
earned 24 points. Total: 24 points 
Current Hand: b Total score: 24 points. 

compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
Current Hand: a a e e i i m m n n t t
"immanent" earned 96 points. Total: 96 points
Current Hand: a e t i
"ait" earned 9 points. Total: 105 points
Current Hand: e
Total score: 105 points.
```