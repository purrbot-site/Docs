[mkdocs]: https://www.mkdocs.org
[material]: https://squidfunk.github.io/mkdocs-material/
[pymdown]: https://facelessuser.github.io/pymdown-extensions/

[nppp]: http://notepad-plus-plus.org/
[vsc]: https://code.visualstudio.com/
[formatting]: https://docs.purrbot.site/contribute/formatting-help/

[discord]: https://purrbot.site/discord

# Contributing to the Documentation
The PurrBot Documentation is open-source to give everyone a chance to contribute towards it. If you want to help improving the pages of the Documentation by adding missing information, updating outdated one or just correct a Typo can you do that throught the creation of a Pull request.

To make sure that formatting and styling is alright will you need to read the following lines of this document to make sure that everything is the way it should be.

## Pre-Requisite
If you work on the documentation on your Desktop should you make the following first steps to have a working enviroment to edit the documentation in.

### Download MkDocs, Material for MkDocs and other dependencies
The Documentation uses [MkDocs], a static Site-generator that allows to turn Markdown files into HTML files. Alongside it do we use The "[Material for MkDocs][material]" (Or Material for short) theme and some Markdown Extensions such as [PyMdown].

You should download MkDocs and all required dependencies to allow having a live-preview of your changes while editing content.  
The simplest way to do this is by just running `pip install -r requirements.txt` in the root directory of the repository you forked to your desktop. This will install all necessary dependencies used for the documentation to work.

### Use Live-preview
Make sure to enable and use the live-preview from MkDocs to see the changes you made to a file in real-time.  
To achieve this, simply run `mkdocs serve` in the root directory of your forked repo and then open `localhost:8000` to see the live-preview. Any changes you make to a file should be reflected nearly instantly once the file is saved.

## Working on pages
Now that you've setup your enviroment to work properly will the next step be to actually editing the pages you want.  
We recommend to use a a more sophisticated text editor such as [Notepad++][nppp], a free and open source Text Editor, or [Visual Studio Code][vsc], a highly advanced editor, to edit markdown files with code highlighting and alike. You can of course use whatever Text Editor you prefer as long as it keeps formatting intact and doesn't do things such as removing leading/trailing spaces.

### General Formatting
We have a [dedicated page][formatting] on our Documentation that explains the general formatting of certain aspects in our Documentation. Make sure to follow any mentioned rules/guidelines there to not have formatting issues.

### Header Structure
Headers need to follow some specific rules.  
There can only be one H1 Header (`# <text>`) at the very top of the page as adding multiple ones would break the Table of Contents shown, which is something we want to avoid.

Headers should always be easy to read. If the actual header link would not be easy to read (i.e. have everything condensed into one String, should you add `{ #<text> }` at the end of the header. This alters the final header link to be whatever you defined as `<text>`.

## That's all
That's everything you need to know!
If you have more questions, don't hesitate to ask us on our [Discord Server][discord]
