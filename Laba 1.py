import re

another_string_email = "riferman@mail.ru"
string = """"The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

a_long_string = another_string_email + string #Take your personal email as a second string and concatenate it with <text>
print(a_long_string)

print(len(re.findall('[a-zA-Z]', a_long_string)))  #Print the count of all symbols in <text>

print(len(re.findall(r'[aeiou]', a_long_string))) #Print the count all the vowels in <text>

print(sum(a_long_string.count(v) for v in 'aeiou'))

for i in range(18, len(a_long_string), 18):
    print(str(i) + a_long_string[i].swapcase()) #Print each 18th symbol of the string, but do it in case opposite to the original (print A if the letter is a, print a if A etc.) adding the position of that char in the string in format like
