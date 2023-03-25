# scripts

This repo contains some of my daily driver scripts.
I try to keep it UNIX-style where one script is doing just one thing but is
doing it good and reliably.
I like Bash scripts for super simple things and plumbing other scripts together.
But for the more complex tasks I resort to Python as a scripting language as
it allows me to quickly model those domains and are usually more readable.

---

## Daily Notes

Create end edit daily notes:

```shell
$ ./edit_daily_note.sh
```

1. Runs `daily_note.py` with default settings which returns `$HOME/daily_notes/<yyyy>/<mm>/<yyyy>-<mm>-<dd>_note.md` and creates the file if it does not exist yet
2. Opens the note file with your default editor set in `$EDITOR`

I use this script by aliasing `~/scripts/edit_dayily_notes.sh` to `note`,
so I can always type

```shell
$ note
```

when I want to add something to my daily note.

---

## My Logo

```shell
$ ./makelogo.sh
```

Probly not too useful for anyone else :wink: but I use this to easily create my logo as a 1024x1024 png file in `/tmp`
