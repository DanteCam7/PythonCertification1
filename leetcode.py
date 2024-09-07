
def mergeAlternately(word1, word2):
    merged = ""

    if len(word1) <= len(word2):
        N = len(word1)
    else:
        N = len(word2)


    i = 0
    while i < N:
        merged += word1[i] + word2[i]
        i += 1

    if len(word1) < len(word2):
        merged += word2[i:len(word2)]
    else:
        merged += word1[i:len(word1)]

    print(merged)

#word1 = input()
#word2 = input()

#mergeAlternately(word1,word2)



def gcdOfStrings1(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    if len(str1) == len(str2):
        return str1
    if len(str1) > len(str2):
        print(gcdOfStrings1(str1[len(str2):], str2))
        return gcdOfStrings1(str1[len(str2):], str2)
    print(gcdOfStrings1(str1, str2[len(str1):]))
    return gcdOfStrings1(str1, str2[len(str1):])

#gcdOfStrings(word1,word2)

class Solution:

    def __init__(self,str1,str2):
        self.str1 = str1
        self.str2 = str2
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])

#leet = Solution("baba","bababa")

#leet.gcdOfStrings("baba","babababa")

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        lista = []
        candies1 = max(candies)
        for c in candies:
            extra = c + extraCandies
            if extra >= candies1:
                lista.append(True)
            else:
                lista.append(False)

        return lista



lista=['a','e','i','o','u']
lista2 = []
s = 'esternocleidomastoideo'
for l in s:
    if l == 'a' or l == 'e' or l == 'i' or l == 'u' or l == 'o':
        lista2.append(l)
length = len(lista2)
#print(lista2[length-1])
i = 0
while length != 0:
    word1 = list(s)
    word1[i] = lista2[length-1]
    length -= 1
#print(word1)

word = list(s)
start = 0
end = len(s) - 1
vowels = list("aeiouAEIOU")

# Loop until the start pointer is no longer less than the end pointer.
while start < end:
    # Move the start pointer towards the end until it points to a vowel.
    while start < end and word[start] not in vowels:
        start += 1
        #print(word[start])
        #print(start)
    #print('-'*25)
    # Move the end pointer towards the start until it points to a vowel.
    while start < end and word[end] not in vowels:
        end -= 1
        #print(end)
        #print(word[end])

    # Swap the vowels found at the start and end positions.
    word[start], word[end] = word[end], word[start]

    # Move the pointers towards each other for the next iteration.
    start += 1
    #print(f"iteracion{start}")
    end -= 1
    #print(f"iteracion{end}" )

#print("".join(word))


s = " the sky is blue "
phrase = list(s)
reverse = s.split(" ")
print(reverse)
reverse2 = []
for l in reverse:
    if l == "":
        pass
    else:
        reverse2.insert(0,l)
print(" ".join(reverse2))

