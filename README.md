# Django Tree Menu

A Django app that implements a dynamic tree menu.

## Features

- Menu is implemented via a template tag
- Everything above the selected item is expanded
- First level of nesting under the selected item is also expanded
- Menu items are stored in the database and edited via the Django admin panel
- The active menu item is determined based on the URL of the current page
- Supports multiple menus on one page, determined by their name
- Menu navigation via specified URLs or named URLs
- Each menu requires exactly one query to the database to render

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Bakhti-developer/tree_menu.git
