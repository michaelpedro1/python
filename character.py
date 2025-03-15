text=input('enter  your text')
char=input('eter the character to check')
x=0
count=0
while (x<len(text)):
    if (text[x] == char):
        count=count+1
    x=x+1
print('the letter', char, 'occurs',count,'in the text',text)        