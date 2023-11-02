---
title: Dokumentation übersetzen
description: Wie du diese Dokumentation in eine andere Sprache übersetzen kannst.
---

Unser Ziel ist es, diese Doks in so vielen Sprachen wie nur möglich anzubieten, um sie jedem verfügbar zu machen.

Um dies zu erreichen benötigen wir deine Hilfe! Solltest du eine andere Sprache kennen, welche hier nicht gezeigt wird, und möchtest du beim übersetzen mithelfen, dann lies weiter.

## Vorraussetzungen { #prerequisites }

Bevor du mit dem übersetzen startest, solltest du sicherstellen, dass du folgendes vorbereitet hast:

- Du hast Erfahrung mit Git (Zum pullen und committen von Änderungen)
- Du hast mindestens Python 3.11 installiert
- Du hast MkDocs und alle nötigen Abhängigkeiten installiert.  
  Verwende einfach `pip install -U -r requirements.txt` im root deiner lokalen Repo um alle Abhängigkeiten zu installieren und zu aktualisieren.

## Übersetzen { #translating }

### Doks Struktur { #docs-structure }

Wir verwenden das `mkdocs-static-i18n` Plugin mit der `folder` Einstellung um die verschiedenen Übersetzungen zu erstellen. Was dies bedeutet ist, dass jede Sprache in ihrem eigenen Ordner ist.

Als ein Beispiel ist hier die Struktur der Englischen (Standard) Sprache innerhalb des `docs` Ordners:
```txt title="Ordnerstruktur"
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

Um mit dem übersetzen der Doks zu starten, kopiere die folgenden Dateien und Ordner vom `en` Ordner in deinen eigenen Unterordner. Stelle sicher dass der Name des Unterordners einem [existierenden Sprach Identifier][languages]{ target="_blank" rel="nofollow" } entspricht:
```txt title="Dateien zum kopieren"
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

### Deine Sprache hinzufügen { #adding-your-language }

Damit das `mkdocs-static-i18n` Plugin deine Sprache erkennt musst du diese als neuen Eintraf zur `languages` Einstellung des `i18n` Plugin in der `mkdocs.yml` hinzufügen.  
Die einfachste Struktur sieht ähnlich wie diese aus (`de-CH` (Schweizer Hochdeutsch) wird als Beispiel verwendet):

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
        - locale: de-CH # (1)
          name: Deutsch (Schweiz) # (2)
          build: true
          site_name: PurrBot Dokumentation
          site_description: 'API-Dokumentation und Wiki von *Purr*'
          copyright: | # (3)
            Dokumentation mit 
            <img alt="❤" class="twemoji heart-anim md-footer-custom-text" src="https://twemoji.maxcdn.com/v/latest/svg/2764.svg" title="Liebe"> 
            gemacht und unter der
            <a href="https://github.com/purrbot-site/Docs/blob/master/LICENSE" target="_blank" rel="nofollow">MIT-Lizenz</a> geteilt.
          extra: # (4)
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

  1. Ersetze diesen Eintrag mit einer [gültigen Sprache Option][languages]{ target="_blank" rel="nofollow" }.
  2. Dies wird in der Sprachauswahl angezeigt.
  3. Dies wird zum ändern des Copyright text im Footer verwendet. Die `<img>` class sollte - Mit ausnahme des `title` Attributes - nicht geändert werden.
  4. Dies wird verwendet um Zeilen im "extra" Abschnitt der Config zu übersetzen.  
     
     - `missing_translation` wird auf Seiten angezeigt, welche noch nicht für diese Sprache existieren.
     - `not_translatable` wird auf Seiten angezeigt, welche nicht übersetzt werden können (Seiten mit `not_translatable: true` im Frontmatter).
     - `footer` ändert den `Erstellt mit ...` text im Footer der Seite.
  5. Dies wird verwendet, um bestimmte deile der Navigation zu übersetzen, welche nicht durch andere Methoden übersetzt werden können.

Dieses Beispiel würde nun nach Dateien im `de-CH` Ordner schauen und diese laden. Du solltest natürlich deinen eigenen Sprach Identifikator als Ordnername verwenden.

### Spezielle Hinweise { #special-notes }

#### Seitentitel und -beschreibung { #page-title-and-description }

Der Seitentitel sollte wann immer über das YAML Frontmatter übersetzt werden.

#### Kopfzeilen { #headers }

Kopfzeilen sollten übersetzt werden. Um jedoch Kreuz-Sprach-Navigation zu ermöglichen, solltest du `{ #:id }` nach der Kopfzeile hinzufügen wo `:id` die ID der originalen Kopfzeile ist.

Als ein Beispiel: `## Some header` wird zu `## Lorem ipsum { #some-header }`, wodurch die Kopfzeile übersetzt, nicht aber deren ID geändert wird.  
Sollte die Kopfzeile bereits eine `{ #:id }` am Ende besitzen musst du nur die Kopfzeile übersetzen, jedoch nicht eine weitere id hinzufügen.

#### Unübersetzbare Seiten { #untranslatable-pages }

Es gibt einige Seiten welche aus verschiedenen Gründen nicht übersetzt werden können.  
Um Fehler zu vermeide, füge diese Seiten nicht in deiner Übersetzung hinzu (Lösche sie, sollten sie in deinem Ordner existieren).

Die folgenden Seiten sollten nicht in deiner Übersetzung existieren (Pfad relativ zu `docs/en/`):

- `api/index.md`
- `legal/api.md`
- `legal/bot.md`
- `legal/website.md`

#### Snippets

Snippets sind Dateien welche in `theme/.snippets/` existieren und sollten auch übersetzt werden.  
Um dies zu tun, kopiere das Snippet, ändere das `__en` zu deinem Sprachcode (z.B. `__de-CH`) und übersetze den Inhalt. Stell sicher, dass du dinge wie Admonition formatierung beibehälst.

#### Nicht zu übersetzende Inhalte { #untranslatable-content }

Die folgenden Inhalte sollten **nicht** übersetzt werden und als solche beibehalten werden:

- Kopfzeilen von Bildnamen in [Bilder](../../bot/welcome-images.md) (z.B. `color_black`).
- Befehlsnamen und Aliasse in [Befehle](../../bot/commands.md) (z.B. `bite`).
- Der Name des Bot (`*Purr*`).
- Projektnamen und Benutzernamen in [`Credits`](../../credits/index.md).
- Jegliche Markennamen (Discord, YouTube, etc.) ausser sie haben einen Namen speziell für deine Sprache.

[languages]: https://squidfunk.github.io/mkdocs-material/setup/changing-the-language/#site-language