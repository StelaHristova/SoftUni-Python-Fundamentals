sub_text = input()
text = input()

while sub_text in text:
    text = text.replace(sub_text, "")
    
print(text)