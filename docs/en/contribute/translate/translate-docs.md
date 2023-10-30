# Translate the Documentation

Our goal is to provide these docs in as many languages as possible to make them accessible to everyone.

In order to achieve this goal do we require your help! If you know another language not shown here and want to contribute a translation, read on.

## Prerequisites

Before you start translating should you make sure you have the following prepared:

- You have knowledge with git (For pulling and committing changes)
- You have at least Python 3.11 installed
- You have MkDocs and all necessary dependencies installed.  
  Just use `pip install -U -r requirements.txt` in the root of your local repo to install and upgrade the dependencies.

## Translating

### Docs structure

We use the `mkdocs-static-i18n` plugin with the `folder` configuration to create the different translations. What this means is that every language is within its own folder.

As an example is here the structure of the English (Default) language inside `docs`:
```txt title="Folder structure"
docs/
└── en/
    ├── api/
    │   └── index.md
    ├── bot/
    │   ├── commands.md
    │   ├── index.md
    │   ├── selfhosting.md
    │   ├── welcome-channel.md
    │   └── welcome-images.md
    ├── contribute/
    │   ├── translate/
    │   │   ├── index.md
    │   │   └── translate-docs.md
    │   ├── formatting-help.md
    │   └── index.md
    ├── credits/
    │   └── index.md
    ├── legal/
    │   ├── api.md
    │   ├── bot.md
    │   ├── index.md
    │   └── website.md
    └── index.md
```

To start translating just copy the `en` folder and paste it in the `docs` folder. Don't forget to rename it to a [supported language identifier][languages]{ target="_blank" rel="nofollow" }.

### Adding your language

In order for the `mkdocs-static-i18n` to recognize your language will you need to add a new entry to the `languages` setting of the `i18n` plugin in the `mkdocs.yml`.  
The most basic structure looks similar to this:
```yaml title="mkdocs.yml"
plugins:
  - search
  - neoteroi.mkdocsoad:
      use_pymdownx: true
  - i18n:
      docs_structure: folder
      languages:
        - locale: en
          default: true
          name: English
          build: true
        # ...other languages
        - locale: example # (1)
          name: Example # (2)
          build: true
          nav_translations: # (3)
            # Welcome system
            Welcome-System: Lorem
            # Contributing
            Contributing: Ipsum
            Translations: Dolor
            # Legal
            Legal: Sit
```

  1. Replace this entry with a [valid language option][languages]{ target="_blank" rel="nofollow" }.
  2. This will be displayed in the language selector.
  3. This is used to translate parts of the nav that can't be translated through other means.

This should now load files inside the `example` folder, allowing you to translate them into your language.

### Special notes

#### Page title and description

The page title should be translated wherever possible using the YAML frontmatter.

#### Headers

Headers should be translated. However, to allow cross-language navigation will you need to append `{ #:id }` to the header where `:id` is the id used in the original header.

As an example, `## Some header` would become `## Lorem ipsum { #some-header }`, translating the header but keeping its original ID.  
Should the header in question already have a `{ #:id }` at the end are you not required to add one and only need to translate the header itself.

#### API Page

The API page's content is auto-generated from the `imageapi.json` file and is therefore not translatable by normal means.

Instead of having you translate an entire JSON file should you only translate the page title and description in the YAML frontmatter and add an admonition box informing about the untranslated docs.

Here is an example of how the file would look like:
```markdown title="api/index.md"
---
title: API
description: 'Documentation about the ImageAPI found at https://purrbot.site/api'

hide:
  - navigation
---

/// note | Note <!-- Translate Note -->
The shown API documentation is auto-generated and therefore only available in English. <!-- Translate this -->
///

<!-- ... OAD object here -->
```

#### Snippets

Snippets are files located in `theme/.snippets/` and should be translated too.  
To do this, copy the snippet in question, change the `__en` to your language code (i.e. `__de`) and translate the content inside it. Make sure to keep things such as Admonition formatting consistent.

#### Things NOT to translate

The following things should **not** be translated and kept as-is:

- Headers of image names in [Welcome Images](../../bot/welcome-images.md) (i.e. `color_black`).
- Command names and Aliases in [Commands](../../bot/commands.md) (i.e. `bite`).
- The name of the bot (`*Purr*`).
- Project names in [`Credits`](../../credits/index.md).
- Any brand name (Discord, YouTube, etc.).

[languages]: https://squidfunk.github.io/mkdocs-material/setup/changing-the-language/#site-language