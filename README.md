# Web Scraper for Michigan Tech CS Graduate Page

This Python script fetches the content of the Michigan Tech University Computer Science graduate program webpage and processes it using BeautifulSoup.

## 🔍 What the Script Does

1. **Downloads the Webpage**  
   The script sends a request to `https://www.mtu.edu/cs/graduate/computer-science/` and saves the entire HTML content into a file named `index.html` inside a folder called `data`.

2. **Extracts Text Content**  
   It reads the saved `index.html`, parses it using BeautifulSoup, and extracts the readable text (ignoring HTML tags).

3. **Saves Clean Text to File**  
   The readable content is then saved to a new file called `hello.txt`.

## 📂 Output Files

Both files are generated automatically by the script:

- `data/index.html`:  
  This file contains the **raw HTML** code of the webpage. It is useful if you want to inspect or analyze the structure of the webpage later.

- `hello.txt`:  
  This file contains the **cleaned-up, human-readable text** extracted from the HTML. It includes all the visible text content from the webpage like headings, paragraphs, links, etc.

## 🛠 Requirements

Install the required libraries before running:

```bash
pip install requests beautifulsoup4
