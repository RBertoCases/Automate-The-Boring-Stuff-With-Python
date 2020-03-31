Q:1. What are escape characters?
A: Escape characters let you use characters that otherwise couldn't be used in a string.

Q:2. What do the \n and \t escape characters represent?
A: \n = newline(line break), \t = Tab

Q:3. How can you put a \ backslash character in a string?
A: \\

Q:4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
A:The use of double quotes allows the use of single quote in the string.

Q:5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
A: Use triple quotes around the string.

Q:6. What do the following expressions evaluate to?

'Hello world!'[1]
A: e

'Hello world!'[0:5]
A: Hello

'Hello world!'[:5]
A: Hello

'Hello world!'[3:]
A: lo world!

Q:7. What do the following expressions evaluate to?

'Hello'.upper()
A: 'HELLO'

'Hello'.upper().isupper()
A: True

'Hello'.upper().lower()
'hello'

Q:8. What do the following expressions evaluate to?

'Remember, remember, the fifth of November.'.split()
A: ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

'-'.join('There can be only one.'.split())
A: 'There-can-be-only-one.'

Q:9. What string methods can you use to right-justify, left-justify, and center a string?
A: rjust(), ljust(), center()

Q:10. How can you trim whitespace characters from the beginning or end of a string?
A: strip(), rstrip(), lstrip()
