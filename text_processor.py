"""Purpose of this file is to clean data"""
import re

def remove_url(txt):
    p = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    res = re.sub(p, "[URL REMOVED]", txt)
    return res

def remove_special_characters(s):
    res = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    return res

def lowercase(txt):
    lower = txt.lower()
    return lower

def remove_whitespace(txt):
    cleaned = ' '.join(txt.split())
    return cleaned