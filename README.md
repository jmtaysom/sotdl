[![Build Status](https://travis-ci.org/jmtaysom/sotdl.svg?branch=master)](https://travis-ci.org/jmtaysom/sotdl)

### Shadow of the Demon Lord Character Generator

This is the very beginning of a character generator for the RPG game
Shadow of the Demon Lord. The system for creating characters is very
programmatic and lends itself to automation. 


#### Help needed
The most time consuming part of this project at first will be copying
the tables out of the book so that characters can be created. There 
are two main types of tables: those that need a roll of a d20 and have
20 unique values and those that need a roll of 3d6 and have several 
ranges of values that correspond to an answer. 

The 3d6 range tables will be represented by two lists. The first will be 
a breakpoint list and the second will be  a value list. The breakpoint
list will have one less item than the value list. Consider the following 
table:

**Human Religion**

|3d6  |Religion|
|:---:|--------|
|3|You belong to a cult dedicated to a dark power.|
|4|You belong to a heretical sect.|
|5–6 | You were raised in the teachings of witchcraft.|
|7–10| You follow the tenets of the Old Faith.|
|11–15| You belong to the Cult of the New God.|
|16–18|You have no religion.|

The human religion breakpoints are 4, 5, 7, 11, and 16. These are the 
numbers that separate each group. The list would be written as 
`human_religion_breakpoints = [4, 5, 7, 11, 16]`. The values would be
written as 
```python
human_religions = [
'You belong to a cult dedicated to a dark power.',
'You belong to a heretical sect.',
'You were raised in the teachings of witchcraft.',
'You follow the tenets of the Old Faith.',
'You belong to the Cult of the New God.',
'You have no religion.'
]
```

The d20 tables will be represented by a python dictionary like the 
human_background dictionary in the human.py file. The die roll will be 
the key and the result will be the value. The following table would be 
represented by the following code.

**Human Background**

|3d6|Background|
|:---:|---|
|1|You died and returned to life...|
|2|You were briefly possessed by a demon...|
|3|You spent {} years as a prisoner in a dungeon.|
|4|You murdered someone in cold blood...|
|5|You caught and recovered from a terrible disease.|

```python
human_background = {
    1: ("You died and returned to life. You start the game with {} Insanity.", "roll('1d6t')"),
    2: ("You were briefly possessed by a demon. You start the game with 1 Corruption.", "None"),
    3: ("You spent {} years as a prisoner in a dungeon.", "roll('1d6t')"),
    4: ("You murdered someone in cold blood. You start the game with 1 Corruption.", "None"),
    5: ("You caught and recovered from a terrible disease.", "None"),
}
```

Above you will also not that the values of the dictionary are tuples. 
The first value in the tuple is the string from the table. The second
is a expression that will be evaluated to give a random number. Many 
of the tables have a random value such as 1d6 years in prison. So the 
die roll in the sentence is replaced by `{}` and the expression is 
written as the value of the second value of the tuple. The roll 
function takes a string as the input with a die roll like 1d6 written
as `'1d6t'`. The t at the end tells roll to return the value of the 
roll instead of a list of the dice rolled.
 