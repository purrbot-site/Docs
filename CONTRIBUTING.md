[mkdocs]: https://www.mkdocs.org
[material]: https://squidfunk.github.io/mkdocs-material/
[pymdown]: https://facelessuser.github.io/pymdown-extensions/

[nppp]: http://notepad-plus-plus.org/
[formatting]: https://docs.purrbot.site/contribute/formatting-help/

[discord]: https://purrbot.site/discord

# Contributing to the Documentation
The PurrBot Documentation is open-source to give everyone a chance to contribute towards it. If you want to help improving the pages of the Documentation by adding missing information, updating outdated one or just correct a Typo can you do that throught the creation of a Pull request.

To make sure that formatting and styling is alright will you need to read the following lines of this document to make sure that everything is the way it should be.

## Pre-Requisite
If you work on the documentation on your Desktop should you make the following first steps to have a working enviroment to edit the documentation in.

### Download MkDocs, Material for MkDocs and other dependencies
The Documentation uses [MkDocs], a static Site-generator that allows to turn Markdown files into HTML files. Alongside it do we use The "[Material for MkDocs][material]" (Or Material for short) theme and some Markdown Extensions such as [PyMdown].

You should download MkDocs and all required dependencies to allow having a live-preview of your changes set.  
The simplest way to do this is by just downloading Material for MkDocs as it automatically downloads all necessary dependencies, including MkDocs and PyMdown.

### Use Live-preview
Make sure to enable and use the Live-preview from MkDocs to see the changes you made to a file in real-time.  
To achieve this, simply run `mkdocs serve` and then head over to `localhost:8000` to see the page.

## Working on pages
Now that you've setup your enviroment to work properly will the next step be to actually editing the pages you want.  
We recommend to use [Notepad++][nppp], a free and open source Text Editor that is perfect for editing Markdown files. You can of course use whatever Text Editor you prefer as long as it keeps formatting intact and doesn't do things such as removing leading/trailing spaces.

### General Formatting
We have a [dedicated page][formatting] on our Documentation that explains the general formatting of certain aspects in our Documentation. Make sure to follow any mentioned rules/guidelines there to not have formatting issues.

### Header Structure
Headers need to follow some specific rules.  
There can only be one H1 Header (`# <text>`) at the very top of the page as adding multiple ones would break the Table of Contents shown, which is something we want to avoid.

The headers themself should be simple and easy to understand. If they're part of the API page and represent a path for the URL should they also link to the URL in question and also represent the actual path.  
Additionally, if the Header would result in a weird to read Link-text such as `imgsfwbackgroundimg` should you add `{ #<text> }` at the end of it to alter the resulting header link and make it more readable by f.e. adding `-` to separate words.

Bad Example:  
```markdown
<!-- No link to actual path -->
<!-- No altering of the link-text -->
# img/sfw/background/img
```

Good Example:  
```markdown
<!-- Links to the API Endpoint -->
<!-- Alters the Link-text to img-sfw-background-img -->
# [img/sfw/background/img](https://purrbot.site/api/img/sfw/background/img) { #img-sfw-background-img }
```

## That's all
That's everything you need to know!
If you have more questions, don't hesitate to ask us on our [Discord Server][discord]
