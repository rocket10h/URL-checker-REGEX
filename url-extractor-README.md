# URL Extractor

A small Python script that scans a text file and extracts all URLs using a regular expression.

## What it does

`urls.py` reads a text file (`webpage.txt`), then finds and prints all URLs found in the text.

**Example input** (`webpage.txt`):
```
Visit us at https://www.example.com or follow our blog at http://blog.example.com/page.
Also check our secure site: https://secure.example.org.
```

**Example output:**
```
 - https://www.example.com
 - http://blog.example.com/page
 - https://secure.example.org
```

## Files

- `urls.py` — main script
- `webpage.txt` — input text file to scan for URLs

## Requirements

- Python 3 (uses only the standard library — `re` module)

## Usage

1. Make sure `webpage.txt` is in the same directory as `urls.py`.
2. Run the script:

```bash
python urls.py
```

3. The extracted URLs will be printed to the console.

## How it works

URL extraction uses this pattern to match `http://` or `https://` links, stopping at whitespace or quote characters:

```python
r'https?://[^\s"\'>]+'
```

This pattern is applied with `re.findall`, which returns all non-overlapping matches in the text.
