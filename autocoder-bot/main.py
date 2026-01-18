import argparse
from converter.core import MarkdownConverter
from converter.utils import read_file, write_file

parser = argparse.ArgumentParser(description='Convert Markdown to HTML')
parser.add_argument('input_file', help='Input Markdown file path')
parser.add_argument('output_file', help='Output HTML file path')
args = parser.parse_args()

# Read input file
markdown_text = read_file(args.input_file)
if markdown_text:
    # Convert Markdown to HTML
    converter = MarkdownConverter()
    html_content = converter.convert(markdown_text)
    # Write HTML content to output file
    write_file(args.output_file, html_content)
