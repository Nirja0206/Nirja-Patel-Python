a="Janvi is not poor"
b=0
c=0
if 'not' in a:
    b=a.index("not")
    if 'poor' in a:
        c=a.index("poor")
if c-b==4:
    print(a.replace("not poor","good"))

    
