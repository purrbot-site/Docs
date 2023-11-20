---
title: Translate the Documentation
description: How you can translate the documentation into your language.
---

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

To start with translating the docs, copy the following files and folders from the `en` folder into your own sub-folder. Make sure the sub-folder matches an [existing language identifier][languages]{ target="_blank" rel="nofollow" }:
```txt title="Files to copy over"
docs/
└── en/
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
    │   └── index.md
    └── index.md
```

### Adding your language

In order for the `mkdocs-static-i18n` to recognize your language will you need to add a new entry to the `languages` setting of the `i18n` plugin in the `mkdocs.yml`.  
The most basic structure looks similar to this (Using `de_CH` (Swiss german) as example):
```yaml title="mkdocs.yml"
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
        - locale: de_CH # (1)
          name: Deutsch (Schweiz) # (2)
          build: true
          site_name: PurrBot Dokumentation
          site_description: 'API-Dokumentation und Wiki von *Purr*'
          copyright: | # (3)
            Dokumentation mit 
            <img alt="❤" class="twemoji heart-anim md-footer-custom-text" src="https://twemoji.maxcdn.com/v/latest/svg/2764.svg" title="Liebe"> 
            gemacht und unter der
            <a href="https://github.com/purrbot-site/Docs/blob/master/LICENSE" target="_blank">MIT-Lizenz</a> geteilt.<br>
            <a href="#__consent">Cookie-Einstellungen verwalten</a>
          extra: # (4):
            consent:
              title: Cookie Zustimmung
              description: >
                Wir verwenden cookies um deine wiederholten Besuche und Einstellungen zu erkennen, aber auch um die Wirksamkeit unserer Dokumentation und ob Benutzer finden nach was sie suchen zu messen.
                Mit deiner Zustimmung hilfst du uns, unsere Dokumentation zu verbessern.
            translate:
              missing_translation: 'Diese Seite wurde noch nicht übersetzt.'
              not_translatable: 'Diese Seite kann nicht übersetzt werden und ist darum nur auf Englisch verfügbar.'
              footer: |
                Erstellt mit <a href="https://www.mkdocs.org" target="_blank" rel="noopener">MkDocs</a>,
                <a href="https://squidfunk.github.io/mkdocs-material" target="_blank" rel="noopener">Material for MkDocs</a> und
                <a href="https://facelessuser.github.io/pymdown-extensions/" target="_blank" rel="noopener">Pymdown Extensions</a>.
          nav_translations: # (5)
            # Welcome system
            Welcome-System: Willkommenssystem
            # Contributing
            Contributing: Mitmachen
            Translations: Übersetzungen
            # Legal
            Legal: Rechtliches
```

  1. Replace this entry with a [valid language option][languages]{ target="_blank" rel="nofollow" }.
  2. This will be displayed in the language selector.
  3. This will be used to change the text in the copyright footer. The `<img>` tag should - with exception of the `title` attribute - not be modified.
  4. This is used to translate Strings in the "extra" section of the config.  

     - `consent` contains title and description for the Cookie Consent banner that would be displayed on first visit of the site.
     - `missing_translation` will be displayed on pages that don't have a page in their language yet.
     - `not_translatable` will be displayed on pages that cannot be translated (That have `not_translatable: true` in their frontmatter).
     - `footer` changes the `Build using ...` text in the footer of the page.

  5. This is used to translate parts of the nav that can't be translated through other means.

This example would now look for and load files inside the `de_CH` folder. You obviously would need to use your language identifier here as folder name.

### Special notes

#### Page title and description

The page title should be translated wherever possible using the YAML frontmatter.

#### Headers

Headers should be translated. However, to allow cross-language navigation will you need to append `{ #:id }` to the header where `:id` is the id used in the original header.

As an example, `## Some header` would become `## Lorem ipsum { #some-header }`, translating the header but keeping its original ID.  
Should the header in question already have a `{ #:id }` at the end are you not required to add one and only need to translate the header itself.

#### Untranslatable pages

There are a few pages that cannot be translated for various reasons.  
To avoid any issues, do not include these pages in your translations folder (Delete them if they exist in your language folder).

The following pages are not to be included in your translation folder (Path relative to `docs/en/`):

- `api/index.md`
- `legal/api.md`
- `legal/bot.md`
- `legal/website.md`

#### Snippets

Snippets are files located in `theme/.snippets/` and should be translated too.

To translate a snippet, open the file and copy the content that is surrounded by `--8<-- [start:en]` and `--8<-- [end:en]` (Include these lines in the copy too!). Paste the content at the bottom of the file. You can leave an empty gap for spacing.  
Next, translate the content in-between the previously mentioned start and end lines. Make sure to keep the existing formatting (i.e. from admonition blocks). Once you're done, change the `en` in the start and end line to the language code you use. Don't forget to save your changes.

Finally, go to the pages where snippets are used (Shown as `--8<-- "<snippet_name>.md:en"`) and replace the `en` with the language code you added.

#### Untranslatable content

The following content should **not** be translated and kept as-is:

- Headers of image names in [Welcome Images](../../bot/welcome-images.md) (i.e. `color_black`).
- Command names and Aliases in [Commands](../../bot/commands.md) (i.e. `bite`).
- The name of the bot (`*Purr*`).
- Project and user names in [`Credits`](../../credits/index.md).
- Any brand name (Discord, YouTube, etc.) unless they have a brand name specific to your language.

[languages]: https://squidfunk.github.io/mkdocs-material/setup/changing-the-language/#site-language
