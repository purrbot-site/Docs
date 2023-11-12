---
title: Formatierungshilfe
description: Seite welche die Details zum formatieren der Doks erklärt.
---

[pymdownx]: https://facelessuser.github.io/pymdown-extensions/
[MkDocs]: https://www.mkdocs.org
[MkDocs-Material extension]: https://github.com/facelessuser/mkdocs-material-extensions

[FontAwesome]: https://fontawesome.com/icons?d=gallery&m=free
[Material Design]: https://materialdesignicons.com/
[Octicons]: https://octicons.github.com
[Simple-Icons]: https://simpleicons.org

Diese Seite zeigt all die verschiedenen Markdown formatierungssyntaxe, welche in der Dokumentation verwendet werden können.  
Bitte beachte dass nicht alle Styles im Standard Markdown verfügbar sind, welche mit MkDocs kommen und bestimmte Erweiterungen benötigen.  
Jede benötigte Erweiterung wird erwähnt.

## Listen { #lists }
Unnummerierte und nummerierte Listen haben eine leicht andere Formatierung als die, welche du wahrscheinlich gewohnt bist.  
Damit eine Liste funktioniert benötigen sie eine leere Zeile zwischen der Liste selbst und jeglichem Text darüber.

//// example | Listen Beispiel
/// tab | Markdown
```markdown
Diese Liste funktioniert.

- Eintrag 1
- Eintrag 2
- Eintrag 3

----  
Diese Liste jedoch nicht.
- Eintrag 1
- Eintrag 2
- Eintrag 3
```
///

/// tab | Ergebnis
Diese Liste funktioniert.

- Eintrag 1
- Eintrag 2
- Eintrag 3

----  
Diese Liste jedoch nicht.
- Eintrag 1
- Eintrag 2
- Eintrag 3
///
////

Zusätzlich zu den obigen Bedingungen musst du auch 4 Leerzeichen verwenden anstelle der üblichen 2, sofern du die Liste einrücken willst.

//// example | Einrück Beispiel
/// tab | Markdown
```markdown
Funktionierendes Einrücken:

- Eintrag 1
    - Eintrag 1.1
- Eintrag 2

----  
Nicht funktionierendes Einrücken:

- Eintrag 1
  - Eintrag 1.1
- Eintrag 2
```
///

/// tab | Ergebnis
Funktionierendes Einrücken:

- Eintrag 1
    - Eintrag 1.1
- Eintrag 2

----  
Nicht funktionierendes Einrücken:

- Eintrag 1
  - Eintrag 1.1
- Eintrag 2
///
////

## Info boxen { #info-boxes }

Du hast doch sicher diese nett aussehenden Boxen bemerkt, welche unterschiedlichste Informationen enthalten.  
Diese sind alls "callouts" oder "admonitions" bekannt und werden durch die [Pymdown Erweiterung `blocks.admonition`][pymdownx] bereitgestellt.

///// example | Box Beispiel
//// tab | Markdown
```markdown
/// info | Titel
Regeln über Markdown sind immernoch aktiv.

- z.B. Listen
- benötigen noch immer eine leere Zeile
///
 
----

/// info
Der Titel kann weggelassen werden.  
Die Box wird dann den Namen des Typs verwenden.
///
```
////

//// tab | Ergebnis
/// info | Titel
Regeln über Markdown sind immernoch aktiv.

- z.B. Listen
- benötigen noch immer eine leere Zeile
///
 
----

/// info
Der Titel kann weggelassen werden.  
Die Box wird dann den Namen des Typs verwenden.
///
////
/////

### Arten { #types }

Admonition Boxen haben verschiedene Arten verfügbar von welchen du wählen kannst:

/// note
///

/// abstract
///

/// info
///

/// tip
///

/// success
///

/// question
///

/// warning
///

/// failure
///

/// danger
///

/// bug
///

/// example
///

/// quote
///

## Kollabierbare Info Boxen (Details) { #details }

Dieses Feature benötigt die `blocks.details` Erweiterung von [Pymdown extensions][pymdownx].

Details haben das selbe Design wie Admonition Boxen, sind aber darin anders, dass sie geöffnet und geschlossen werden können.  
Der Syntax ist derselbe wie mit [Admonition Boxes](#info-boxes) mit dem Unterschied, dass `details` als Identifier verwenden und dass du den `type` als Option angeben musst.

///// example | Kollabierbare Box Beispiel
//// tab | Markdown
```markdown
/// details | Titel
    type: info

Diese Box ist standardmässig zu.
///

----

/// details | Titel
    type: info
    open: true

Das hinzufügen von `open:true` öffnet sie standardmässig.
///
```
////
    
//// tab | Ergebnis
/// details | Titel
    type: info

Diese Box ist standardmässig zu.
///

----

/// details | Titel
    type: info
    open: true

Das hinzufügen von `open:true` öffnet sie standardmässig.
///
////
/////

## Tabs

Dieses Feature benötigt die `blocks.tab` Erweiterung von [Pymdown extensions][pymdownx].

Es erlaubt dir, Tabs zu erstellen zwischen welchen du hin und her wechseln kannst um unterschiedlichen Inhalt zu zeigen. Auf dieser seite wird es für die `Markdown` und `Ergebnis` tabs verwendet.  
Der Syntax ist derselbe wie mit [Admonition Boxes](#info-boxes) mit dem Unterschied, dass `details` als Identifier verwenden und dass du keine Art angeben kannst.

///// example | Tabs Beispiel
//// tab | Markdown
```markdown
/// tab | Tab 1
Du kannst weiter tabs hinzufügen...
///

/// tab | Tab 2
...indem du weitere `/// tab | title ... ///` anhängst.
///

/// tab | Tab A
    new: true

Das hinzufügen von `new: true`...
///

/// tab | Tab B
...erstellt ein neues Set von tabs.
///
```
////

//// tab | Ergebnis
/// tab | Tab 1
Du kannst weiter tabs hinzufügen...
///

/// tab | Tab 2
...indem du weitere `/// tab | title ... ///` anhängst.
///

/// tab | Tab A
    new: true

Das hinzufügen von `new: true`...
///

/// tab | Tab B
...erstellt ein neues Set von tabs.
///
////
/////

## Links

Wir verwenden `MagicLink` von [Pymdown extensions][pymdownx] um Links automatisch klickbar zu machen. Dies ist leider kein Standardverhalten in Markdown.

//// example | Link Beispiel
/// tab | Markdown
```markdown
https://purrbot.site
```
///

/// tab | Ergebnis
https://purrbot.site
///
////

Zusätzlich können wir eine Repository oder einen GitHub Benutzer verlinken, indem wir einfach die Formate `@benutzer/repo` respektive `@benutzer` verwenden.  
Dies funktioniert auch mit Twitter Benutzers, indem der Name mit `twitter:` als Präfix versehen wird (`@twitter:benutzername`).

//// example | Mention Beispiel
/// tab | Markdown
```markdown
@purrbot-site  
@purrbot-site/Docs  
@twitter:TruePurrBot
```
///

/// tab | Ergebnis
@purrbot-site  
@purrbot-site/Docs  
@twitter:TruePurrBot
///
////

## Emojis

Wir verwenden `Emojis` von [PyMdown extensions][pymdownx] um das verwenden von Emojis durch das bekannte `:emoji:` Muster zu ermöglichen.  
Zudem verwenden wir auch [MkDocs-Material Extension] welches Unterstützung für SVG Icons von [FontAwesome], [Material Design], [Octicons] und [Simple Icons][simple-icons] durch das selbe Format hinzufügt.

Beachte das anders als Emojis, die benutzerdefinierten welche von MkDocs-Material Extension hinzugefügt werden mit der seite von welcher sie kommen gepräfixt werden müssen.

- `fontawesome-brands` für Icons von Marken
- `fontawesome-regular` für alle Standardicons
- `fontawesome-solid` für alle soliden Icons
- `material` für die Material Design Icons
- `octicons` für die Octicons Icons
- `simple` für die Simple Icons Icons

//// warning | Hinweis über FontAwesome und Octicons
/// tab | FontAwesome
Die MkDocs-Material Extension ist nur in der lage, die gratis FontAwesome Icons zu verwenden! Premium Icons sind nicht unterstützt.
///

/// tab | Octicons
Da Octicons ihre Icons in 16px und 24px formaten anbietet musst du `-16` oder `-24` an den Namen anhängen, abhängig davon, welches format du verwenden willst.  
Beispie: Anstelle von `:octicons-repo:` verwendest du entweder `:octicons-repo-16:` oder `:octicons-repo-24:`
///
////

//// example | Emoji/Icons Beispiele
/// tab | Markdown
```markdown
Normale Emojis:

- :smile:
- :heart:

FontAwesome Icons (Marken):  

- :fontawesome-brands-github:
- :fontawesome-brands-discord:

FontAwesome Icons (Regulär):

- :fontawesome-regular-bell:
- :fontawesome-regular-bell-slash:

FontAwesome Icons (Solide):

- :fontawesome-solid-bell:
- :fontawesome-solid-bell-slash:

Material Design:

- :material-sync:
- :material-alert:

Octicons:

- :octicons-repo-24:
- :octicons-git-pull-request-24:

Simple-Icons:

- :simple-mastodon:
- :simple-simpleicons:
```
///
    
/// tab | Ergebnis
Normale Emojis:

- :smile:
- :heart:

FontAwesome Icons (Marken):  

- :fontawesome-brands-github:
- :fontawesome-brands-discord:

FontAwesome Icons (Regulär):

- :fontawesome-regular-bell:
- :fontawesome-regular-bell-slash:

FontAwesome Icons (Solide):

- :fontawesome-solid-bell:
- :fontawesome-solid-bell-slash:

Material Design:

- :material-sync:
- :material-alert:

Octicons:

- :octicons-repo-24:
- :octicons-git-pull-request-24:

Simple-Icons:

- :simple-mastodon:
- :simple-simpleicons:
///
////

## Knöpfe { #buttons }
Durch das verwenden der List Attribute Erweiterung können wir eingebettete Links (`[text](link)`) in Knöpfe verwandeln indem wir `{ .md-button }` anhängen.

//// example | Button Example
/// tab | Markdown
```markdown
[Zur Webseite](https://purrbot.site){ .md-button }
```
///
    
/// tab | Ergebnis
[Zur Webseite](https://purrbot.site){ .md-button }
///
////

## Letzte Worte { #final-words }

Dies sind all die Wichtigen dinge welche du über den markdown Syntax dieser Dokumentation wissen musst.  
Für alle anderen Markdown-relevanten Dinge welche hier nicht erwähnt wurden kann man davon ausgehen, dass die normale formatierung (z.B. `*kursiv*`, `**fett**`, etc.) verwendet wird.
