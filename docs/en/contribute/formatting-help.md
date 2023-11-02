---
title: Formatting Help
description: Page explaining the details about formatting those docs.
---

[pymdownx]: https://facelessuser.github.io/pymdown-extensions/
[MkDocs]: https://www.mkdocs.org
[MkDocs-Material extension]: https://github.com/facelessuser/mkdocs-material-extensions

[FontAwesome]: https://fontawesome.com/icons?d=gallery&m=free
[Material Design]: https://materialdesignicons.com/
[Octicons]: https://octicons.github.com
[Simple-Icons]: https://simpleicons.org

This page lists all the different Markdown formatting syntaxes, which are used across the documentation.  
Please not that not all Styles are available for the default Markdown shipped with MkDocs and require extensions to be installed.  
Any extension required will be mentioned.

## Lists
Unordered and ordered lists have a slightly different formatting than the one you're probably used to.  
In order for the list to work will they require an empty line between the list, and any displayed text above them.

//// example | List example
/// tab | Markdown
```markdown
This list below will work.

- Entry 1
- Entry 2
- Entry 3

----  
This list, however, won't work.
- Entry 1
- Entry 2
- Entry 3
```
///

/// tab | Result
This list below will work.

- Entry 1
- Entry 2
- Entry 3

----  
This list, however, won't work.
- Entry 1
- Entry 2
- Entry 3
///
////

In addition to the above requirement will you also need to use 4 spaces compared to the usual 2, when you want to indent the list.

//// example | Indent example
/// tab | Markdown
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
///

/// tab | Result
Working indents:

- Entry 1
    - Entry 1.1
- Entry 2

----  
Not working indents:

- Entry 1
  - Entry 1.1
- Entry 2
///
////

## Info boxes
You sure have noticed those neat looking boxes that contain various information of stuff.  
These are known as "callouts" or "admonitions" and are provided through the [Pymdown extension `blocks.admonition`][pymdownx].

///// example | Box examples
//// tab | Markdown
```markdown
/// info | Title
Rules about Markdown still apply.

- F.e. Lists
- Still need an empty line
///
 
----

/// info
The title can be omited.  
The box will then use the name of its type.
///
```
////

//// tab | Result
/// info | Title
Rules about Markdown still apply.

- F.e. Lists
- Still need an empty line
///

----

/// info
The title can be omited.  
The box will then use the name of its type.
///
////
/////

### Types
Admonition boxes have different types available that you can choose from:

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

## Collapsable info boxes (Details) { #details }
This feature requires the `blocks.details` extension from [Pymdown extensions][pymdownx].

Details have the same design as admonition boxes, but are different in that they can be opened and closed.  
The syntax is the same as with [Admonition boxes](#info-boxes) with the difference that they use `details` as identifier and that you have to define the `type` as an option inside it.

///// example | Collapsable Box example
//// tab | Markdown
```markdown
/// details | Title
    type: info

This box is closed by default
///

----

/// details | Title
    type: info
    open: true

Adding `open: true` opens it by default
///
```
////
    
//// tab | Result
/// details | Title
    type: info

This box is closed by default
///

----

/// details | Title
    type: info
    open: true

Adding `open: true` opens it by default
///
////
/////

## Tabs
This feature requires the `blocks.tab` extension from [Pymdown extensions][pymdownx].

It allows to create tabs to switch in-between to display content. On this page is it used for the `Markdown` and `Result` tabs.  
The syntax is the same as with [Admonition boxes](#info-boxes) with the difference that they use `tab` as identifier and that you cannot define any type for it.

///// example | Tabs example
//// tab | Markdown
```markdown
/// tab | Tab 1
You can add more tabs...
///

/// tab | Tab 2
...by just adding additional `/// tab | title ... ///` content.
///

/// tab | Tab A
    new: true

Adding `new: true`...
///

/// tab | Tab B
...creates a new set of tabs.
///
```
////

//// tab | Result
/// tab | Tab 1
You can add more tabs...
///

/// tab | Tab 2
...by just adding additional `/// tab | title ... ///` content.
///

/// tab | Tab A
    new: true

Adding `new: true`...
///

/// tab | Tab B
...creates a new set of tabs.
///
////
/////

## Links
We use `MagicLink` from [Pymdown extensions][pymdownx] to automatically make links clickable. This unfortunately is not a default behaviour in Markdown.

//// example | Link example
/// tab | Markdown
```markdown
https://purrbot.site
```
///

/// tab | Result
https://purrbot.site
///
////

Additionally can we link to a repository or GitHub user by just using the format `@user/repo` and `@user` respectively.  
This also works with Twitter-users by prefixing the name with `twitter:` (`@twitter:username`)

//// example | Mention examples
/// tab | Markdown
```markdown
@purrbot-site  
@purrbot-site/Docs  
@twitter:TruePurrBot
```
///

/// tab | Result
@purrbot-site  
@purrbot-site/Docs  
@twitter:TruePurrBot
///
////

## Emojis
We use the `Emojis` extension from [Pymdown extensions][pymdownx] to allow the usage of emojis through the common `:emoji:` pattern.  
We also use the [MkDocs-Material Extension] which adds support for using SVG icons of [FontAwesome], [Material Design], [Octicons] and [Simple-Icons] using the same format.

Note that unlike emojis, the custom ones added by the MkDocs-Material Extension require to be prefixed with the site they should come from.

- `fontawesome-brands` for brand icons
- `fontawesome-regular` for all regular icons
- `fontawesome-solid` for all Solid icons
- `material` for the Material Design icons
- `octicons` for the Octicons icons
- `simple` for the Simple-Icons icons

//// warning | Note about FontAwesome and Octicons
/// tab | FontAwesome
The MkDocs-Material Extension will only be able to use free FontAwesome icons! Paid ones aren't supported.
///

/// tab | Octicons
Due to Octicons being offered in 16px and 24px format, are you required to suffix the icon name with either `-16` or `-24` depending on which you want to use.  
As an example: Instead of `:octicon-repo:` would you use `:octicon-repo-16:` or `:octicon-repo-24:`
///
////

//// example | Emoji/Icons Examples
/// tab | Markdown
```markdown
Normal Emojis:

- :smile:
- :heart:

FontAwesome Icons (Brands):  

- :fontawesome-brands-github:
- :fontawesome-brands-discord:

FontAwesome Icons (Regular):

- :fontawesome-regular-bell:
- :fontawesome-regular-bell-slash:

FontAwesome Icons (Solid):

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
    
/// tab | Result
Normal Emojis:

- :smile:
- :heart:

FontAwesome Icons (Brands):  

- :fontawesome-brands-github:
- :fontawesome-brands-discord:

FontAwesome Icons (Regular):

- :fontawesome-regular-bell:
- :fontawesome-regular-bell-slash:

FontAwesome Icons (Solid):

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

## Buttons
Using the List Attribute extension we can turn embedded Links (`[text](link)`) into buttons by appending `{ .md-button }` to it.

//// example | Button Example
/// tab | Markdown
```markdown
[To the Website](https://purrbot.site){ .md-button }
```
///
    
/// tab | Result
[To the Website](https://purrbot.site){ .md-button }
///
////

## Final Words
Those are all the important parts you need to know about the markdown syntax for the documentation.  
Anything Markdown-related that wasn't mentioned here is assumed to be the normal formatting (e.g. `*italic*`, `**bold**`, etc.).
