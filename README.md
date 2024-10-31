# sbeditor

#### A parser for all things sb3 (and sprite3), created by [faretek1](https://scratch.mit.edu/users/faretek1/)

---

Lets you read **and write** sb3 files!

This is a very much work-in-progress project but the underlying functionality is complete. Currently adding a ton of
classes to `sbuild.py` so that you don't need to remember/look up block opcodes/input names

## Features

---

- An object-oriented format for a sb3 or sprite3 file (Project, Target, Block, etc.)
- Supports writing Scratch code
- Allows for easy creation of hacked scripts
- And so much more (as well as so much more to come)

## Installing

---

You can install sbeditor using pip:
`pip install sbeditor`

## Documentation

---

Unfortunately, there is not yet any documentation. However, it is planned.

## Helpful resources

---

- [The Scratch file format](https://en.scratch-wiki.info/wiki/Scratch_File_Format)
- [List of block opcods](https://en.scratch-wiki.info/wiki/List_of_Block_Opcodes)
- [GitHub repo](https://github.com/FAReTek1/sbeditor)

## Example code

---

```py
from sbeditor import *
# pip install printbeautifully
from beautifulprint import bprint

proj = Project.from_sb3("Project.sb3")

block = proj.stage.get_blocks_by_opcode("event_whenflagclicked")[0]


bprint(block.subtree)

proj.save_json()
```