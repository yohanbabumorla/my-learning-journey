

# 📅 **Day 6 — Array Interview Patterns + Week 1 Recap**

---

## 🧠 **Goal for Today**

You’ll learn:
1️⃣ Merge two sorted arrays
2️⃣ Rotate an array by *k* positions
3️⃣ Remove duplicates from a sorted array
4️⃣ Weekly recap (key takeaways + quiz + coding tasks)

---

## ⚙️ **1️⃣ Merge Two Sorted Arrays (Two-Pointer Approach)**

### 💡 Concept:

You’re given two sorted arrays — your task is to merge them into one sorted array without using built-in functions.

**Example:**

```
Input: arr1 = [1,3,5], arr2 = [2,4,6]
Output: [1,2,3,4,5,6]
```

---

### 💻 **Code:**

```python
def merge_sorted_arrays(arr1, arr2):
    i = j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

print(merge_sorted_arrays([1,3,5,7], [2,4,6,8]))
```

### 🧮 **Output:**

```
[1, 2, 3, 4, 5, 6, 7, 8]
```

---

### 🔍 **Visualization**

| i   | j   | arr1[i] | arr2[j] | Merged    |
| --- | --- | ------- | ------- | --------- |
| 0   | 0   | 1       | 2       | [1]       |
| 1   | 0   | 3       | 2       | [1,2]     |
| 1   | 1   | 3       | 4       | [1,2,3,4] |
| ... | ... | ...     | ...     | ...       |

✅ **Time:** O(n + m)
✅ **Space:** O(n + m)

---

## 🔁 **2️⃣ Rotate an Array by K Positions**

### 💡 Concept:

Rotate array elements to the **right** by `k` positions.

**Example:**

```
Input: [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

---

### 💻 **Code (Using Slicing):**

```python
def rotate_array(arr, k):
    k = k % len(arr)  # Handle k > n
    return arr[-k:] + arr[:-k]

print(rotate_array([1,2,3,4,5,6,7], 3))
```

### 🧮 **Output:**

```
[5, 6, 7, 1, 2, 3, 4]
```

---

### 🔍 **Visualization**

**Before:** [1,2,3,4,5,6,7]
**After 3 rotations:** [5,6,7,1,2,3,4]

✅ Time: O(n)
✅ Space: O(n)

---

### 💪 **Code (In-place Rotation using Reverse Logic):**

```python
def rotate_in_place(arr, k):
    n = len(arr)
    k %= n

    # Helper function to reverse part of array
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse entire array
    reverse(arr, 0, n - 1)
    # Step 2: Reverse first k elements
    reverse(arr, 0, k - 1)
    # Step 3: Reverse remaining elements
    reverse(arr, k, n - 1)
    return arr

print(rotate_in_place([1,2,3,4,5,6,7], 3))
```

### 🧮 **Output:**

```
[5, 6, 7, 1, 2, 3, 4]
```

✅ Time: O(n)
✅ Space: O(1)

---

## 🔢 **3️⃣ Remove Duplicates from a Sorted Array**

**Example:**

```
Input: [1,1,2,2,3,4,4]
Output: [1,2,3,4]
```

---

### 💻 **Code:**

```python
def remove_duplicates(arr):
    if not arr:
        return 0

    unique = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[unique]:
            unique += 1
            arr[unique] = arr[i]
    return arr[:unique + 1]

print(remove_duplicates([1,1,2,2,3,4,4]))
```

### 🧮 **Output:**

```
[1, 2, 3, 4]
```

✅ **Time:** O(n)
✅ **Space:** O(1)

---

## 💪 **Mini Challenge**

Write a Python function to:
1️⃣ Merge two sorted arrays
2️⃣ Remove duplicates from the merged result
3️⃣ Rotate the final array by `k` positions

**Example:**

```
Input:
arr1 = [1,2,3,4]
arr2 = [3,4,5,6]
k = 2

Output: [5,6,1,2,3,4]
```

💡 *Hint:* Combine the three techniques we learned today.

---

## 🧩 **Practice Problems**

1️⃣ [LeetCode #88 — Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
2️⃣ [LeetCode #189 — Rotate Array](https://leetcode.com/problems/rotate-array/)
3️⃣ [LeetCode #26 — Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

---

## 🔗 **Free Resources**

* 🎥 [Striver – Rotate Array & Two Pointer Merge](https://youtu.be/BHr381Guz3Y)
* 🧠 [GFG – Array Rotation & Duplicate Removal](https://www.geeksforgeeks.org/python-program-to-remove-duplicates-from-sorted-array/)
* 💻 [Visualizer – Python Tutor (step-by-step execution)](https://pythontutor.com/visualize.html)

---

## 🧾 **WEEK 1 QUICK RECAP — Arrays Mastered ✅**

| Topic | Concept Learned       | Key Skill                          |
| ----- | --------------------- | ---------------------------------- |
| Day 1 | Arrays Basics         | Create, insert, delete, traverse   |
| Day 2 | Two-Pointer Technique | Reverse, move zeros, pair sum      |
| Day 3 | Searching             | Linear & Binary search             |
| Day 4 | Sorting               | Bubble, Selection, Insertion       |
| Day 5 | Advanced Patterns     | Prefix sum, Kadane, Sliding Window |
| Day 6 | Interview Patterns    | Merge, Rotate, Remove duplicates   |

---

## 🧠 **Mini Quiz (5 Questions)**

1️⃣ Accessing an array element takes:
A) O(1) B) O(n) C) O(log n)

2️⃣ Kadane’s algorithm helps find:
A) Prefix sum B) Max subarray sum C) Median

3️⃣ Binary search works only on:
A) Unsorted array B) Sorted array C) Random data

4️⃣ Rotating an array by `n` elements gives:
A) Same array B) Reversed array C) Empty array

5️⃣ Which algorithm sorts with the fewest swaps?
A) Bubble B) Selection C) Insertion

*(Answers: 1️⃣ A, 2️⃣ B, 3️⃣ B, 4️⃣ A, 5️⃣ B)*

---

## 💾 **GitHub Task**

🗂 Folder: `week1_arrays/day6_interview_patterns.py`
📤 Commit message:
`"Day 6: Merging, rotation, duplicate removal + Week 1 recap complete"`

---

## 🧠 **Weekend Practice (Sunday – Week 1 Review)**

✅ Solve 10–15 array problems from LeetCode or GFG (Easy → Medium)
✅ Revisit your notes from Day 1–6
✅ Watch 1 sorting or searching visualization video
✅ Commit all your work with `"Week 1: Arrays completed ✅"`

---

## 🚀 **Next Week (Week 2 Preview — Strings & Tuples)**

You’ll learn:

* String operations & slicing
* Palindrome, anagram, frequency counter
* Two-pointer & sliding window on strings
* Substrings & pattern matching
* Interview questions like "Valid Anagram", "Longest Substring without Repeating Characters"

---

