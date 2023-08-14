#!/usr/bin/env python3

s = '5TViqGVHMochlusnoGiLTtDWtPaMRtA0f5ARkDldNZquVAdY6pdi8BAzYrS96wMcxCfQ2iDh4iMCxWgpuHgjL5AmfsrH2HliXcUoPgyRU35JhOJ75GSQ805HOQTLTEkgaleatusB6OxW9XsbwggZFe6yJWQFHZbio0U9WYz0sEk.'

a = 8
b = 14
c = 127
d = 134

# Return: The slice of the string s from indices a through b and c through d (with space in between), inclusively. 
# In other words, we should include elements s[b] and s[d] in our slice.

def slicing(s, a, b, c, d):
    return f'{s[a:b+1]} {s[c:d+1]}'

print(slicing(s, a, b, c, d))