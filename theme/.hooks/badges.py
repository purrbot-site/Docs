# Copyright (c) 2016-2023 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from __future__ import annotations

import posixpath
import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page
from re import Match

#
# Slightly adjusted version of Squidfunk's shortcodes.py file
#

def on_page_markdown(
    markdown: str, *, page: Page, config: MkDocsConfig, files: Files
):
    
    def replace(match: Match):
        type, args = match.groups()
        args = args.strip()
        if type == "required": return _badge_for_required(args)
        elif type == "optional": return _badge_for_optional(args)
        elif type == "default": return _badge_for_default(args)
        elif type == "req_arg": return _badge_for_required_arg()
        elif type == "opt_arg": return _badge_for_optional_arg()
        elif type == "patreon": return _badge_for_patreon(args)
        
        raise RuntimeError(f"Unknown shortcode: {type}")
    
    return re.sub(
        r"<!-- md-badge:(\w+)(.*?) -->",
        replace, markdown, flags = re.I | re.M
    )

#------------------------------------------------------------------------------

def _resolve_path(path: str, page: Page, files: Files):
    path, anchor, *_ = f"{path}#".split("#")
    path = _resolve(files.get_file_from_path(path), page)
    return "#".join([path, anchor]) if anchor else path

def _resolve(file: File, page: Page):
    path = posixpath.relpath(file.src_uri, page.file.src_uri)
    return posixpath.sep.join(path.split(posixpath.sep)[1:])

#------------------------------------------------------------------------------

# Create badge
def _badge(icon: str, text: str = "", type: str = ""):
    icon_class = f"mdx-badge__icon {type}" if type else "mdx-badge__icon"
    return "".join([
        f"<span class=\"mdx-badge\">",
        *([f"<span class=\"{icon_class}\">{icon}</span>"] if icon else []),
        *([f"<span class=\"mdx-badge__text\">{text}</span>"] if text else []),
        f"</span>",
    ])

def _badge_for_required(args: str = ""):
    icon = "octicons-alert-24"
    return _badge(
        icon = f":{icon}:",
        text = f"{args}" if args else "Required"
    )

def _badge_for_optional(args: str = ""):
    icon = "octicons-issue-draft-24"
    return _badge(
        icon = f":{icon}:",
        text = f"{args}" if args else "Optional"
    )

def _badge_for_default(args: str):
    icon = "octicons-checklist-24"
    
    return _badge(
        icon = f":{icon}:",
        text = f"{args}"
    )

def _badge_for_required_arg():
    icon = "octicons-alert-24"
    return _badge(
        icon = f":{icon}:",
        type = "icon-only"
    )

def _badge_for_optional_arg():
    icon = "octicons-issue-draft-24"
    return _badge(
        icon = f":{icon}:",
        type = "icon-only"
    )

def _badge_for_patreon(args: str = ""):
    icon = "simple-patreon"
    text = f"{args}" if args else "Patreon Reward"
    
    return _badge(
        icon = f"[:{icon}:](https://patreon.com/andre_601)",
        text = f"[{text}](https://patreon.com/andre_601)",
        type = "patreon"
    )