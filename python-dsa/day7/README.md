Week 2 – Day 1: Strings (Foundations for DSA)
🧠 Concept: What is a String?

A string is a sequence of characters stored in order.

name = "yohan"


Think of a string as:

📦 An array of characters where each character has an index

Index	0	1	2	3	4
Char	y	o	h	a	n

So:

print(name[0])   # y
print(name[4])   # n

⚠️ Important Rule (Very Interview-Relevant)

👉 Strings are IMMUTABLE in Python

That means:

s = "hello"
# s[0] = "H"  ❌ ERROR


You cannot change characters directly.
You must create a new string.

💡 Real-Life Analogy

Think of a string like a printed exam hall ticket 🎫

You can read it

You can copy & modify a new one

But you cannot overwrite characters on the original

⚙️ Basic String Operations
🔹 1️⃣ Length of a String
s = "python"
print(len(s))  # 6


⏱️ Time: O(1)

🔹 2️⃣ Traversing a String
for ch in "yohan":
    print(ch)


⏱️ Time: O(n)

🔹 3️⃣ String Slicing (VERY IMPORTANT)
s = "datastructures"

print(s[0:4])   # data
print(s[4:9])   # struc
print(s[:4])    # data
print(s[4:])    # structures
print(s[::-1])  # serutcurtsatad (reverse)


🧠 Slicing creates a new string → O(n) time & space

🔄 Common String Operations Used in DSA
Operation	Example	Use Case
Convert case	s.lower()	Case-insensitive compare
Count chars	s.count('a')	Frequency problems
Find index	s.find('o')	Substring search
Replace	s.replace('a','@')	Transform string
Split	"a b c".split()	Word problems
Join	"".join(list)	Efficient string build

Example:

s = "banana"
print(s.count('a'))   # 3
print(s.find('n'))    # 2
print(s.replace('a', '@'))  # b@n@n@

🧩 Core DSA String Problems (Day 1 Level)
✅ Problem 1: Reverse a String
Method 1: Slicing (Pythonic)
def reverse_string(s):
    return s[::-1]

print(reverse_string("yohan"))  # nahoY


⏱️ Time: O(n)
💾 Space: O(n)

✅ Problem 2: Reverse a String (Manual – Interview Friendly)
def reverse_string_manual(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

print(reverse_string_manual("python"))


🧠 Shows logic (preferred in interviews)

✅ Problem 3: Count Vowels & Consonants
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = c = 0

    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c

print(count_vowels_consonants("Yohan Babu"))


Output:

(4, 5)

✅ Problem 4: Check Palindrome

A palindrome reads the same forward & backward.

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))   # True
print(is_palindrome("python"))  # False

🎯 Try It Yourself (Mini Challenges)

1️⃣ Print every character of a string with its index
2️⃣ Reverse a string without slicing
3️⃣ Count how many times each vowel appears
4️⃣ Remove spaces from a sentence
5️⃣ Convert "hello world" → "HELLO_WORLD"

🧠 Mini Quiz (3 Questions)

1️⃣ Are strings mutable in Python?
A) Yes B) No

2️⃣ Time complexity of reversing a string of length n?
A) O(1) B) O(n) C) O(log n)

3️⃣ What does s[::-1] do?
A) Sort string
B) Reverse string
C) Remove duplicates

Answers: 1️⃣ B, 2️⃣ B, 3️⃣ B

🔁 Quick Recap

✅ Strings are sequences of characters
✅ They are immutable
✅ Learned indexing, slicing, traversal
✅ Solved reverse, palindrome, vowel count problems
✅ Prepared base for string DSA patterns

🧩 Practice Problems (Easy – Must Do)

LeetCode #344 — Reverse String

LeetCode #125 — Valid Palindrome

LeetCode #709 — To Lower Case

🔗 Optional Free Resources

🎥 YouTube: Apna College – Strings in Python

🧠 Blog: GeeksforGeeks – String Data Structure

💻 Tool: pythontutor.com (visualize string operations)

🚀 Tomorrow (Week 2 – Day 2 Preview)

We’ll level up with:

Two-pointer technique on strings

Palindrome using two pointers

String comparison problems

First real interview-style string logic
