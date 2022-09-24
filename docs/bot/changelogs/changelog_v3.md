---
title: v3 Changelogs
description: Changes of version 3.x for the bot.
---

# v3.x Changelogs

Latest v3.x changes of \*Purr\*.

## 3.0.0

### Commands

- Switched over to Discord's Slash commands system. This means that all commands now use `/` as their prefix.
    - Updated commands:
        - Merged `eevee`, `holo`, `kitsune`, `neko`, `okami` and `senko` into a single `img` command.  
          Each of the commands has become a subcommand for `img`.
        - `language` now has the subcommands `list`, `set` and `reset`.
        - `welcome` now has a subcommand `reset` to reset one or all welcome settings.
        - `help` was renamed to `purrhelp`
        - `emote` now has the subcommands `get` and `search`.
    - Removed commands:
        - Removed `prefix`
- Welcome images will now be loaded asynchronosly using Java's `CompletableFuture`.
