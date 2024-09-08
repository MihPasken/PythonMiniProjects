import difflib

def similarity(str1, str2):
    return difflib.SequenceMatcher(None, str1.lower(), str2.lower()).ratio() * 100

print(similarity('gre', 'gbe'))