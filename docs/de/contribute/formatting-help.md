---
title: Formattierungshilfe
description: Seite welche die Details über das formattieren dieser Dokumentation erklärt.
---

[PyMdown]: https://facelessuser.github.io/pymdown-extensions/
[MkDocs]: https://www.mkdocs.org
[MkDocs-Material extension]: https://github.com/facelessuser/mkdocs-material-extensions

[FontAwesome]: https://fontawesome.com/icons?d=gallery&m=free
[Material Design]: https://materialdesignicons.com/
[Octicons]: https://octicons.github.com

Diese Seite listet alle verschiedenen Markdown formattierungssyntaxe welche in der Dokumentation verwendet werden.  
Beachte bitte dass nicht alle Style im Standard Markdown für MkDocs verfügbar sind und gewisse Erweiterungen benötigen.  
Jegliche benötigte Erweiterung wird erwähnt.

## Listen
Ungeordnete und geordnete Listen haben ein leicht unterschiedliches verhalten von was du wahrscheinlich gewohnt bist.  
Damit eine Liste funktioniert benötigt sie eine leere Zeile zwischen der Liste selbst und dem Text davor.

!!! example "Listen Beispiel"
    === "Markdown"
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

    === "Resultat"
        Diese Liste funktioniert.
        
        - Eintrag 1
        - Eintrag 2
        - Eintrag 3
        
        ----  
        Diese Liste jedoch nicht.
        - Eintrag 1
        - Eintrag 2
        - Eintrag 3

Zusätzlich zu den oben genannten Bedingungen musst du auch 4 leerzeichen anstelle der standard 2 verwenden wenn du die Liste nach innen verschieben willst.

!!! example "Indent example"
    === "Markdown"
        ```markdown
        Working indents:
        
        - Entry 1
            - Entry 1.1
        - Entry 2
        
        ----  
        Not working indents:
        
        - Entry 1
          - Entry 1.1
        - Entry 2
        ```
	
    === "Result"
        Working indents:
        
        - Entry 1
            - Entry 1.1
        - Entry 2
        
        ----  
        Not working indents:
        
        - Entry 1
          - Entry 1.1
        - Entry 2

## Info boxes
You sure have noticed those neat looking boxes that contain various information of stuff.  
Those are provided through [MkDocs] and use a specific syntax, that you need to follow.

!!! example "Box examples"
    === "Markdown"
        ```markdown
        !!! info "Title"
            Rules about Markdown still apply.
            
            - F.e. Lists
            - Still need an empty line
            
        ----
        
        !!! info
            The title can be omited.  
            The box will then use the name of its type.
        ```
        	
    === "Result"
        !!! info "Title"
            Rules about Markdown still apply.
            
            - F.e. Lists
            - Still need an empty line
            
        ----
        
        !!! info
            The title can be omited.  
            The box will then use the name of its type.

!!! warning "Special rules"
    - You don't need to add two spaces after the `!!! <type> "<title>"`. MkDocs can handle this just fine.
    - You need to add at least one empty line before and after the info box to not have unwanted formatting issues.

### Types
The info boxes have various types available which you can choose from:

!!! note

!!! summary

!!! info

!!! tip

!!! success

!!! question

!!! warning

!!! failure

!!! danger

!!! bug

!!! example

!!! quote

## Collapsable info boxes (Details)
This feature requires the `Details` extension from [PyMdown].

Those boxes are similar to the normal info boxes, but can be collapsed (closed) or expanded (opened).  
They follow the same syntax as the info boxes, but use question marks (`?`) instead of exclamation marks (`!`).  
You can use the exact same [types](#types) as with the info boxes.


!!! example "Collapsable Box example"
    === "Markdown"
        ```markdown
        ??? info "Title"
            This box is closed by default
            
        ----
        
        ???+ info "Title"
            Adding a + after the question mark makes this box open by default.
        ```
    
    === "Result"
        ??? info "Title"
            This box is closed by default
        
        ----
        
        ???+ info "Title"
            Adding a + after the question mark makes this box open by default.

## Tabs
This feature requires the `Tabbed` extension from [PyMdown].

Adds tabbed Markdown to list content after each other. This was used here for the various Markdown examples and their results.  
The syntax is the same as with the info box, with the difference that it uses equal signs (`=`) instead of exclamation marks (`!`).  
Additionally does it also not have a type parameter, meaning you can only set the tile itself.

!!! example "Tabs example"
    === "Markdown"
        ```markdown
        === "Tab 1"
            You can add more tabs...
            
        === "Tab 2"
            ...by adding extra `===`.
            
        ===! "Tab A"
            Using a ! after the equal signs...
            
        === "Tab B"
            ...indicates a new set of tabs.
        ```
    
    === "Result"
        === "Tab 1"
            You can add more tabs...
            
        === "Tab 2"
            ...by adding extra `===`.
            
        ===! "Tab A"
            Using a ! after the equal signs...
            
        === "Tab B"
            ...indicates a new set of tabs.

## Links
We use the [PyMdown] extension `MagicLink` which allows us to automatically transform links into clickable links. This doesn't happen by default.

!!! example "Link example"
    === "Markdown"
        ```markdown
        https://purrbot.site
        ```
        
    === "Result"
        https://purrbot.site

Additionally can we link to a repository or GitHub user by just using the format `@user/repo` and `@user` respectively.  
This also works with Twitter-users by prefixing the name with `twitter:` (`@twitter:username`)

!!! example "Mention examples"
    === "Markdown"
        ```markdown
        @purrbot-site  
        @purrbot-site/Docs  
        @twitter:TruePurrBot
        ```
    
    === "Result"
        @purrbot-site  
        @purrbot-site/Docs  
        @twitter:TruePurrBot

## Emojis
We use the `Emojis` extension from [PyMdown] to allow the usage of emojis through the common `:emoji:` pattern.  
We also use the [MkDocs-Material Extension] which adds support for using SVG icons of [FontAwesome], [Material Design] and [Octicons] in the same format.

Note that unlike emojis, the custom ones added by the MkDocs-Material Extension require to be prefixed with the site they should come from.

- `fontawesome-brands` for brand icons
- `fontawesome-regular` for all regular icons
- `fontawesome-solid` for all Solid icons
- `material` for the Material Design icons
- `octicons` for the Octicons icons

!!! warning "Note about FontAwesome and Octicons"
    === "FontAwesome"
        The MkDocs-Material Extension will only be able to use free FontAwesome icons! Paid ones aren't supported.
    
    === "Octicons"
        Due to Octicons being offered in 16px and 24px format, are you required to suffix the icon name with either `-16` or `-24` depending on which you want to use.  
        As an example: Instead of `:octicon-repo:` would you use `:octicon-repo-16:` or `:octicon-repo-24:`

!!! example "Emoji/Icons Examples"
    === "Markdown"
        ```markdown
        Normal Emojis  
        
        - :smile:
        - :heart:
        
        FontAwesome Icons (Brands):  
        
        - :fontawesome-brands-github:
        - :fontawesome-brands-discord:
        
        FontAwesome Icons (Regular)  
        
        - :fontawesome-regular-bell:
        - :fontawesome-regular-bell-slash:
        
        FontAwesome Icons (Solid)  
        
        - :fontawesome-solid-bell:
        - :fontawesome-solid-bell-slash:
        
        Material Design:
        
        - :material-sync:
        - :material-alert:
        
        Octicons:
        
        - :octicons-repo-24:
        - :octicons-git-pull-request-24:
        ```
    
    === "Result"
        Normal Emojis  
        
        - :smile:
        - :heart:
        
        FontAwesome Icons (Brands):  
        
        - :fontawesome-brands-github:
        - :fontawesome-brands-discord:
        
        FontAwesome Icons (Regular)  
        
        - :fontawesome-regular-bell:
        - :fontawesome-regular-bell-slash:
        
        FontAwesome Icons (Solid)  
        
        - :fontawesome-solid-bell:
        - :fontawesome-solid-bell-slash:
        
        Material Design:
        
        - :material-sync:
        - :material-alert:
        
        Octicons:
        
        - :octicons-repo-24:
        - :octicons-git-pull-request-24:

## Buttons
Using the List Attribute extension can we turn embedded Links (`[text](link)`) into buttons by appending `{: .md-button }` to it.

!!! example "Button Example"
    === "Markdown"
        ```markdown
        [To the Website](https://purrbot.site){: .md-button }
        ```
    
    === "Result"
        [To the Website](https://purrbot.site){: .md-button }

## Final Words
Those are all the important parts you need to know about the markdown syntax for the documentation.  
Anything Markdown-related that wasn't mentioned here is assumed to be the normal formatting (e.g. `*italic*`, `**bold**`, etc.).
