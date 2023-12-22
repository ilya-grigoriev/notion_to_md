# notion_to_md

- If you export notes from Notion, you have encountred incorrect filename.
- This python script will help you to convert Notion "Markdown" file to markdown file by removing header and add it to filename.
- Files with gremlin will be deleted if they can be successfully converted.
- Note: this python script cannot convert directory path (unfortunately).

# Install

- If you're using \*nix:

```bash
git clone https://github.com/ilya-grigoriev/notion_to_md.git
cd notion_to_md
python -m venv venv
venv/bin/activate
pip install .
chmod +x converting_notion_to_md
```
