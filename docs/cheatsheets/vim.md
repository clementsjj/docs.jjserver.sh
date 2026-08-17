---
title: Vim Cheatsheet
date: 2026-06-01
icon: material/code-block-tags
---

---

### Movement
| ⇐   | ⇓   | ⇑   | ⇒   |     | ∧ top | ∨ bottom |
| --- | --- | --- | --- | --- | ----- | -------- |
| h   | j   | k   | l   |     | gg    | g        |


| ![](/images/svg/right-arrow.svg) | Forward | ![](/images/svg/left-arrow.svg) | Backwards |
| -------------------------------- | ------- | ------------------------------- | --------- |
| Start of Word                    | `w`     | Start of Word                   | `b`       |
| Start of Word w/ Punctuation     | `W`     | Start of Word w/ Punctuation    | `B`       |
|                                  |         |                                 |           |
| End of Word                      | `e`     | End of Word                     | `ge`      |
| End of Word w/ Punctuation       | `E`     | End of Word w/ Punctuation      | `gE`      |
|                                  |         |                                 |           |
| End of Line                      | `$`     | Start of Line                   | `0`       |
| Last non-bolank char of Line     | `g_`    | First non-blank char of Line    | `^`       |
|                                  |         |                                 |           |
| Occurence of Character x         | `fx`    | Occurrence of Character x       | `Fx`      |
| Till before Character x          | `tx`    | Till after Character x          | `Tx`      |
|                                  |         |                                 |           |




| Up                  | ![](/images/svg/up-arrow.svg) |     | Down               | ![](/images/svg/down-arrow.svg) |
| ------------------- | ----------------------------- | --- | ------------------ | ------------------------------- |
| Move Cursor Up      | `gk`                          |     | Move Cursor Down   | `gj`                            |
| Back 1 Screen       | `ctrl` + `b`                  |     | Forward 1 Screen   | `ctrl` + `f`                    |
| Back 1/2 Screen     | `ctrl` + `u`                  |     | Forward 1/2 Screen | `ctrl` + `d`                    |
|                     |                               |     |                    |                                 |
|                     |                               |     |                    |                                 |
| Paragraph Up        | `{`                           |     | Paragraph Down     | `}`                             |
| Previous Section    | `[[`                          |     | Next Section       | `]]`                            |
| Previous Line Start | `-`                           |     | Next Line Start    | `+`                             |
| Scroll Line Up      | `ctrl` + `y`                  |     | Scroll Line Down   | `ctrl` + `e`                    |
|                     |                               |     |                    |                                 |
| Top of File         | `gg`                          |     | Bottom of File     | `G`                             |
| Cursor to Top       | `zt`                          |     | Cursor to Bottom   | `zb`                            |
|                     |                               |     |                    |                                 |




| Reposition Cursor Line to...|     |
| ---------------- | --- |
| Top of Screen    | `H` |
| Middle of Screen | `M` |
| Bottom of Screen | `L` |

| Reposition Cursor Line without moving the cursor itself |      |
| ------------------------------------------------------- | ---- |
| Scroll so cursor line is at the top of the screen       | `zt` |
| Center                                                  | `zz` |
| Scroll so cursor line is at the bottom of the screen    | `zb` |

### Edit

| Normal Mode              |     | Hint |
| ------------------------ | --- | ---- |
| Insert end of line       | `A` |      |
| Insert beginning of line | `I` |      |
| Insert next line         | `o` |      |
| Insert before line       | `O` |      |
| Insert after cursor      | `a` |      |
| Insert before cursor     | `i` |      |



### Delete or Change
Delete is handled like <delete> then the modifier, like w for word; <br> <br> You can also us `c` for change instead of delete, which will automatically put you in insert mode

|               |                                             |     |            |                                           |
| ------------- | ------------------------------------------- | --- | ---------- | ----------------------------------------- |
| dw            | delete word (to next word start)            |     | dG         | delete to end of file                     |
| de            | delete to End of word                       |     | dgg        | delete to beginning of file               |
| db            | delete back a word                          |     | di<symbol> | delete between symbol, like (, {, ", etc. |
| D or d$       | delete from cursor to end of line           |     | dip        | delete paragraph                          |
| dt X           | delete everything up to (but not including) |     |            |                                           |
| dd or <NUM>dd | delete line or multiple lines               |     | x          | delete single character                   |




### Search
Use `/` to search, `n` to go to next, and `N` to go to previous.

You can also use `?` to search, but in reverse, and that reverses the `n` and `N`.

When searching and you are under a word, you can hit `*` and `#` to go forward and back searching for that word under the cursor.



### Indent

| Normal Mode |     |
| ----------- | --- |
| Indent Line | >>  |
| Dedent Line | <<  |

 Examples:
- `3>>` - indent 3 lines
- `>j` - indent current line and the one below
- `>ap` - indent a paragraph
- `>i}` - indent everything inside {}


| Insert Mode  |              | hint              |
| ------------ | ------------ | ----------------- |
| Indent Right | `ctrl` + `t` | t for "tab"       |
| Indent Left  | `ctrl` + `d` | d for "DE-indent" |



### Nifty Commands

|                              |          |
| ---------------------------- | -------- |
| Select All                   | `ggVG`   |
| Copy all to system clipboard | `gg"+yG` |
|                              |          |


### Navigation
|              |                                                                     |
| ------------ | ------------------------------------------------------------------- |
| `gf`         | opens the filename currently under the cursor in the current window |
| `gd`         | jump to the local declaration of the keyword (current file)         |
| `gD`         | go to global declaration                                            |
| `ctrl` + `]` | return to previous location                                         |
|              |                                                                     |


### Screen Split


| Create                       |                        |
| ---------------------------- | ---------------------- |
| :split or :sp                | Horizontal Split       |
| :vsplit or :vs               | Vertical Split         |
| :sp filename or :vs filename | Open File in New Split |
| Ctrl+w then s                | Horizontal Split       |
| Ctrl+w then v                | Vertical Split         |




| Navigate   |                         |
| ---------- | ----------------------- |
| Ctrl+w + h | Move to the left split  |
| Ctrl+w + j | Move to split below     |
| Ctrl+w + k | Move to split above     |
| Ctrl+w + l | Move to the right split |
| Ctrl+w + w | Cycle through windows   |


---
