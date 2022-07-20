#Scott Schmidl - COMP 660 - Programming with Python I - 02/01/2021 to 04/10/2021 - Section 6.4 Module 6 Assignment

#Question 4
def add_html_tags(tag, text):

    '''
    create the HTML string with tags around the word(s)
    '''

    return f'<{tag}>{text}</{tag}>\n'

tags = ['h1', 'p', 'h2', 'p']
texts = ['My First Page', 'This is my first page.', 'My secondary header.', 'some more text.']
tags_text = list(zip(tags, texts))

for tag, text in tags_text:
    html_stuff = add_html_tags(tag, text)
    print(html_stuff)


# for i in tags_text:

#     if i == 0: html1 = add_html_tags(tag=tags_text[0][0], text=tags_text[0][1])

#     elif i == 1: html2 = add_html_tags(tag=tags_text[1][0], text=tags_text[1][1])

#     elif i == 2: html3 = add_html_tags(tag=tags_text[2][0], text=tags_text[2][1])

#     else: html4 = add_html_tags(tag=tags_text[3][0], text=tags_text[3][1])
