# Heading generator creates different styles of headers and section dividers for note taking in Python for better organizing
# It takes a user input of a text string to be decorated, and a style.


# Style sheet
separator = {'name': 'separator', 'depth': 5, 'width': 120, 'symbol': "-"}
h1 = {'name': 'h1', 'depth': 3, 'width': 120, 'symbol': "*"}
h2 = {'name': 'h2', 'depth': 3, 'width': 120, 'symbol': "#"}

custom = {'name': "custom_style"}

style_list = [separator, h1, h2]


# define heading section
def generate_heading(text, style):
    text_line = ("   " + text +
                 "   ").center(style['width'], style['symbol'])
    depth_on_each_side = (style['depth'] - 1) // 2
    if depth_on_each_side < 1:
        return text_line

    depth_padding = ("".center(style['width'], style['symbol']) + '\n')

    output = f"""{depth_padding * depth_on_each_side}{text_line}\n{depth_padding * depth_on_each_side}

    """

    return output



# user interaction
print("Welcome to heading generator, here are the styles you have available: \n")

for style in style_list:
    print(f"{style.get('name')}: \nDepth: {style.get('depth')} \nWidth: {style.get('width')} \nSymbol: {style.get('symbol')} \nExample:\n" +
          generate_heading("TEST", style) + ' \n')


txt_input = input("Please enter the text you would like to decorate: \n")
style_input = input(
    "Please enter the style you want this in, we'll create a new style if it doesn't exist: \n")


if style_input not in [style['name'] for style in style_list]:
    custom['name'] = style_input
    custom['depth'] = int(input(
        "Please enter the depth of the header, ideally an odd number: "))
    custom['width'] = int(input("Please enter the width of the header: "))
    custom['symbol'] = input("Please enter the symbol of the header: ")
    style_input = custom


else:
    style_idx = [style['name'] for style in style_list].index(style_input)
    style_input = style_list[style_idx]

output = generate_heading(txt_input, style_input)


print(output)
