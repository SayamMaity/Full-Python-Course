def remove_and_strip(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()


this="   sayam is a good   "
n=remove_and_strip(this, "sayam")
print(n)
# print(this)
# print(this.strip())