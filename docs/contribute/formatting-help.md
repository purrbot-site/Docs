[PyMdown]: https://facelessuser.github.io/pymdown-extensions/
[MkDocs]: https://www.mkdocs.org
[MkDocs-Material extension]: https://github.com/facelessuser/mkdocs-material-extensions

# Formatting Help
This page lists all the different Markdown formatting syntaxes, which are used across the documentation.  
Please not that not all Styles are available for the default Markdown shipped with MkDocs and require extensions to be installed.  
Any extension required will be mentioned.

## Lists
Unordered and ordered lists have a slightly different formatting than the one you're probably used to.  
In order for the list to work will they require an empty line between the list, and any displayed text above them.

!!! example "List example"
    === "Markdown"
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
    
	=== "Result"
		This list below will work.
		
		- Entry 1
		- Entry 2
		- Entry 3
		
		----  
		This list, however, won't work.
		- Entry 1
		- Entry 2
		- Entry 3

In addition to the above requirement will you also need to use 4 spaces compared to the usual 2, when you want to indent the list.

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

I want to point out those specific things:

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

Those boxes are similar to the normal info boxes, but can be collapsed (closed) or opened.  
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
Thanks to the [PyMdown] extension `Emojis` can we add emojis (From Twemoji) to this Documentation by just providing it as `:emoji_name:`

Additionally do we also use the [MkDocs-Material extension] which also adds icons from FontAwesome, Material Design and Octicons to this pages.  
You can use them like normal emojis, with the difference, that they are prefixed with one of the following namespaces:

- `fontawesome` FontAwesome icons. You also need to specify the type as listed below.
    - `fontawesome-brands` for brand icons
	- `fontawesome-regular` for regular icons
	- `fontawesome-solid` for solid icons
- `material` Material Design icons.
- `octicons` GitHub's Octicon icons.

## Final Words
Those are all the important parts you need to know about the markdown syntax for those documentations.  
Every other markdown format that wasn't mentioned here uses the default, most commonly known syntax (e.g. `*italic*` is *italic*, `**bold**` is **botld**, etc.)
