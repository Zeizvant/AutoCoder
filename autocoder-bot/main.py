```python
import argparse
from converter.core import MarkdownConverter
from converter.utils import read_file, write_file

parser = argparse.ArgumentParser(description='Convert Markdown to HTML')
parser.add_argument('input_file', help='Input Markdown file path')
parser.add_argument('output_file', help='Output HTML file path')
args = parser.parse_args()

md_converter = MarkdownConverter()
input_text = read_file(args.input_file)
if input_text:
    html_output = md_converter.convert_to_html(input_text)
    write_file(args.output_file, html_output)
```
