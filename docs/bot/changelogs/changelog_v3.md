---
title: v3 Changelogs
description: Changes of version 3.x for the bot.
---

# v3 Changelogs

Recent changes to \*Purr\* v3.

## 3.0.0

- Moved to Discord's integrated Slash commands  
  All commands are now prefixed with `/` rather than `p.`
- Updates commands
  - Combined `eevee`, `holo`, `kitsune`, `neko`, `okami` and `senko` into a main `img` command
  - `tail` is now `wag`
  - `language` has now `list`, `set` and `reset` sub-commands
  - `welcome` now has various set commands (i.e. `/welcome background <background>`) and a `reset` sub-command
  - `emote <:emote:>` is now `emote get <:emote:>` and `emote --search` is now `emote search [amount]`
  - Renamed `help` to `purrhelp`
- Welcome images are now loaded asynchronously using Java's `CompletableFuture`