'''Problem:
We're going to build the beginnings of a markdown processor. Markdown is a markup language that allows you to easily create HTML.
We ll provide some sample input and desired output. Dont worry too much about edge cases, but feel free to ask if you re unsure or think there s something we ought to consider.

Part 1:  A markdown processor is capable of handling a multitude of string to html tag formats. For now, we just want to focus on supporting <p/>, <br/>, <blockquote/>, and <del/> tags.  

Input:
String input = "This is a paragraph with a soft\n" + "line break.\n\n" + "This is another paragraph that has\n" + 
               "> Some text that\n" + "> is in a\n" + "> block quote.\n\n" + 
			   "This is another paragraph with a ~~strikethrough~~ word.";  

Expected Output:
"<p>This is a paragraph with a soft<br />line break.</p> 
<p>This is another paragraph that has <br />
<blockquote.>Some text that<br />is in a<b.r />
block quote</blockquote.> </p> <p>This is another paragraph with a
<del>strikethrough</del.> word.</p>"'''


def markdown(input):
    i = 0
    res = '<p>'
    block_is_active, is_new_para, strikethrough_began = False, True, False

    while i < len(input):
        ch = input[i: i+2]
        new_line = input[i:i + 1]

        if new_line == '\n':
            if input[i + 1: i + 2] == '\n':
                if block_is_active:
                    res += '</blockquote>'
                    block_is_active = False
                res += '</p>'
                res += '<p>'
                i += 2
            else:
                res += '<br />'
                i += 1

        elif ch == '> ':
            if not block_is_active:
                res += '<blockquote>'
                block_is_active = True
            i += 2
        elif ch == '~~':
            if not strikethrough_began:
                res += '<del>'
                strikethrough_began = True
            else:
                res += '</del>'
            i += 2
        else:
            res += input[i]
            i += 1
        
        # print(repr(res))
    res += '</p>'
    return res
