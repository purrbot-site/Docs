[purr]: https://purrbot.site/github

[formatting help]: https://docs.purrbot.site/contribute/formatting-help

[boxes]: https://squidfunk.github.io/mkdocs-material/extensions/admonition/#admonition
[MkDocs]: https://www.mkdocs.org

[squidfunk]: https://github.com/squidfunk
[henrywhitaker3]: https://github.com/henrywhitaker3
[facelessuser]: https://github.com/facelessuser

[Material Dark Theme]: https://github.com/henrywhitaker3/mkdocs-material-dark-theme
[pymdown]: https://github.com/facelessuser/pymdown-extensions/

[netlifyImg]: https://api.netlify.com/api/v1/badges/cb9acd27-d730-4526-b679-874c16894e14/deploy-status
[netlify]: https://app.netlify.com/sites/purrbot-site/deploys

[![netlifyImg]][netlify]

# Docs
This repository is home of the content found on https://docs.purrbot.site  
It currently houses the API-documentation for the various endpoints under https://purrbot.site/api and the official wiki of [\*Purr*][purr].

## Contributions
Any contributions to update and improve the wiki, as well as the API-documentation are welcome, but please follow those basic guidelines:

### Only edit the content in the docs-folder and mkdocs.yml
The content found under the "docs" folder is the place to edit files in. Each file is saved as a markdown (.md) file.  
Only the docs folder (and the mkdocs.yml file if new pages where added or got removed) should be altered.  
At no point should you touch the content of any other file outside the docs-directory.  
Any pull request which alters any file other than the above mentioned ones will be denied.

### Markdown formatting
We use [MkDocs] to turn Markdown files into static HTML pages.  
MkDocs *mostly* follows the basic markdown formatting with some minor exceptions and alterations.  
Please take a look at the [formatting help] page for important information about differences compared to the normal markdown syntax.

## Credits
A big thank you goes to the following people/groups:
- [MkDocs] for providing the software, to generate documentation.
- [squidfunk] for the MkDocs Material Theme.
- [henrywhitaker3] for the CSS file for the [Material Dark Theme]
- [facelessuser] for the [PyMdown Extensions][pymdown]
