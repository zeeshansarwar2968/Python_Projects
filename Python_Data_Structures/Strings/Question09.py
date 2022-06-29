"""
9. Write a Python program to display formatted text (width=50) as output.
"""
import textwrap

lorem_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi 
ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
deserunt mollit anim id est laborum."""

"""
fill(text, width=70, **kwargs)
    Fill a single paragraph of text, returning a new string.
    
    Reformat the single paragraph in 'text' to fit in lines of no more
    than 'width' columns, and return a new string containing the entire
    wrapped paragraph.  As with wrap(), tabs are expanded and other
    whitespace characters converted to space.  See TextWrapper class for
    available keyword args to customize wrapping behaviour.
"""

print(f"\nText Data : \n{textwrap.fill(lorem_text,width=50)}")

# print(f"sample_text:\n{sample_text[:50]}")
# print(help(textwrap.fill))
