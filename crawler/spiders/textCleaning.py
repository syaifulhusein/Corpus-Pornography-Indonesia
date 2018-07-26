import re

with open("convertedToText-1.txt",'r',encoding='utf-8') as f:
    text = f.read()
    f.close()

def normalizeText(text):
    # result = text.lower()
    result = text
    # result = re.sub(r'<(script).*?</\1>(?s)', '', result,1 )
    result = re.sub(r'[^a-z0-9 -]', ' ', result, flags = re.IGNORECASE|re.MULTILINE)
    result = re.sub(r'( +)', ' ', result, flags = re.IGNORECASE|re.MULTILINE)

    return result.strip()

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def remove_jquery(text):
    clean = re.sub(r'jQuery.*','',text,1)
    return clean

def remove_script(text):
    clean = re.sub(r'<script.+?</script>', '', text, flags=re.DOTALL)
    return clean

a = remove_script(text)
b = remove_html_tags(a).lower().strip()

with open('cleanText.txt','w',encoding='utf-8') as f:
    d = f.write(b)
    f.close()
