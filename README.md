**Purpose & Backstory**
I wanted to create a java program that automatically retrieved the currency code of a country. This was super simple to do, so then I decided to challenge myself to create a simple 'autocorrect' so that the program could attempt to resolve small user errors without simply reprompting them to enter a valid country. The original solution can be found in my MadLib repository [here](https://github.com/n8zone/MadLib). This solution was ugly and used far too many loops for my liking, so I did a small amount of research and found the **Levenshtein Distance Algorithm**. This repository is my attempt at implementing the algorithm without using any references, just a brief description of how its supposed to work.

I am satisfied with where I got, and as a FuzzyMatching algorithm it works well, but ultimately I think I was creating the wrong tool for my original 'autocorrect' idea. I thought FuzzyMatching would work at first, but now I realize it is more useful for finding similar strings within a threshold. I would still like to make an autocorrection tool though.

**TODO:**
- Extract logger logic into a separate repo

**Planned Features**

**WIBNI**
- ~~Proper dataset of common typos to solve 2similar problem.~~
