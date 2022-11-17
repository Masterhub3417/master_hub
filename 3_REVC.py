# master_

```
#解答
input_dna = input('DNAを入力してください')

input_dna_reverse = input_dna[::-1]
print(input_dna_reverse)

def reverse (str):
    reverse = []
    for i in range(len(str)-1, -1, -1):
        reverse.append(str[i])
    for i in range(0, len(reverse)):
        if (reverse[i] == "A"):
            reverse[i] = "T"
        elif (reverse[i] == "T"):
            reverse[i] = "A"
        elif (reverse[i] == "C"):
            reverse[i] = "G"
        else:
            reverse[i] = "C"
    return reverse

print(reverse(i))
```


```
#模範解答2
st = "AAAACCCGGT"
st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print(st)
```
```
#模範解答3
s = 'AAAACCCGGT'
print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))
```

```
str = input('input dna alignment')
def reverse (a):
    reverse = []
    for i in range(len(str)-1, -1, -1):
        reverse.append(str[i])
    for i in range(0, len(reverse)):
        if (reverse[i] == "A"):
            reverse[i] = "T"
        elif (reverse[i] == "T"):
            reverse[i] = "A"
        elif (reverse[i] == "C"):
            reverse[i] = "G"
        else:
            reverse[i] = "C"
    return reverse

print(reverse(str)) #reverse()の引数にロザリンドから提示された配列を入力する。

#https://www.headboost.jp/python-strings-into-a-list/#index_id1
#上記サイト参照　#リスト---->文字列　文字列---->リスト
```
