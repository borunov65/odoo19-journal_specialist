# Specialist Journal (Odoo Module)

## Odoo Version
Odoo 19.0

## Description
**Specialist Journal** is a custom Odoo module that allows specialists to keep structured journal entries for clients.

The module provides:
- Journal entries linked to clients (Contacts)
- Assignment of a responsible specialist (current user by default)
- Predefined journal templates
- Automatic insertion of template text into journal entries
- Printing a PDF report with all journal entries for a selected client

This module is designed as a test assignment and demonstrates basic Odoo development practices:
models, views, security, relations, and QWeb reports.

## Installation & Run Instructions

1. Clone this repository:
```bash
git clone <repository_url>

2. Place the module into the custom_addons directory:
odoo19/custom_addons/journal_specialist

3.Activate virtual environment (if used):
source .venv/bin/activate

4. Start Odoo server:
./odoo-bin -c odoo.conf

5. Open Odoo in browser:
http://localhost:8069

6. Enable Developer Mode
7. Go to Apps → Update Apps List
8. Search for Specialist Journal and install the module

Usage

Open Contacts

Select a client

Go to the Specialist Journal tab

Create journal entries or print a journal report

Author
Ihor Borunov  ihor.borunov@gmail.com
