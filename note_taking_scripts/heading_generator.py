#! /usr/bin/env python3
# heading_generator.py creates different styles of headers and section dividers for note taking in Python for better organizing
# note taking within python scripts
# it takes a argument of the style, if left empty or invalid style entered displayes available styles and other options
# passing custom as a style when calling the function allows for custom design of a new style.


# TODO

import pyperclip
import sys


# Style sheet - this can later be ported out into a separate file
separator = {'name': 'separator', 'depth': 3, 'width': 120, 'symbol': "-"}
h1 = {'name': 'h1', 'depth': 1, 'width': 120, 'symbol': "*"}
h2 = {'name': 'h2', 'depth': 1, 'width': 120, 'symbol': "#"}
h3 = {'name': 'h3', 'depth': 0, 'width': 120, 'symbol': "#"}
custom = {'name': "custom"}

style_list = [separator, h1, h2, h3, custom]


# function definition
def generate_heading(text, style):
    text_line = ("   " + text +
                 "   ").center(style['width'], style['symbol'])
    if style['depth'] < 1:
        return ("\n\"\"\"\n" + text_line + "\n\"\"\"\n")

    depth_padding = ("".center(style['width'], style['symbol']) + '\n')

    output = f"""\"\"\"\n{depth_padding * style['depth']}{text_line}\n{depth_padding * style['depth']}\"\"\"
    """

    return output


# user interaction

if len(sys.argv) < 2 or sys.argv[1] not in [style['name'] for style in style_list]:
    print('Usage: python heading_generator.py [style] - choose a style;')
    print('Below are some of the styles available in the default stylesheet')

    for style in style_list:
        try:
            print(f"{style.get('name')}: \nDepth: {style.get('depth')} \nWidth: {style.get('width')} \nSymbol: {style.get('symbol')} \nExample:\n" +
                  generate_heading("TEST", style) + ' \n')
        except:
            pass

    print(
        "if none of them suit your style, use the keyword 'custom' as the argument for [style] when calling the program")
    sys.exit()


txt_input = input("Please enter the text you would like to decorate: \n")
style_input = sys.argv[1]  # a string is passed as stdin

if style_input == 'custom':
    custom['name'] = style_input
    custom['depth'] = int(input(
        "Please enter the depth of padding on each side (above and below) the text: "))
    custom['width'] = int(input("Please enter the width of the header: "))
    custom['symbol'] = input("Please enter the symbol of the header: ")
    style_input = custom  # changes the style input to point to the dictionary


else:
    style_idx = [style['name'] for style in style_list].index(style_input)
    style_input = style_list[style_idx]

output = generate_heading(txt_input, style_input)


print(output + '\n')
print("copied to clipboard")
pyperclip.copy(output)


# user interaction
# print("Welcome to heading generator, here are the styles you have available: \n")
