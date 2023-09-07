---
title: Documentation of French Driver
author: Tautminas Cibulskis
date: September 8, 2023
---

# Future Improvements of the French Driver

Possibilities:
- Display different messages asking for a replay based on previous play. E.g. "New High Score! To Drive Again Press Enter." or "You won! To Repeat the Drive Press Enter.".
- Add a sound button at the right bottom corner. It could play a melody while playing and after a choice it could help indicate whether the choice was correct or not.
- Display 👍 or 👎 for a couple of seconds after a choice below the lives. It would easier indicate whether the made choice was good.
- Add options to a game. E.g. number of words or themes. Even a different langauge.
- Make sure that the icon picture will not disappear from the executable file.

Refactor the code 🙂:
- Handle Terminator exception without running the whole game in the try block.
- Avoid the repetition of prepare_turtle function inside multiple classes.
- Make main.py clearer by adding the game code into functions of by creating a new class.