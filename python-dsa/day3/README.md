
# 📅 **Day 3 — Searching Algorithms (Linear + Binary Search)**

---

## 🧠 **Concept: What is Searching?**

When you have a collection of data (like an array), you often need to **find the position of a specific element**.

For example:

> Given `[10, 20, 30, 40, 50]`, find where `30` is.

That’s **searching** — and there are multiple ways to do it.

---

## 🔹 **Two Main Types of Searching Algorithms**

| Type              | Description                            | Time Complexity |
| ----------------- | -------------------------------------- | --------------- |
| **Linear Search** | Check each element one by one          | O(n)            |
| **Binary Search** | Repeatedly divide sorted array in half | O(log n)        |

---

## 💡 **Real-Life Analogy**

Imagine finding a friend’s name in a printed **list of names**:

* If the list is **unsorted**, you start from the top → **Linear Search**.
* If it’s **alphabetically sorted**, you can jump to the middle → **Binary Search**.

---

## ⚙️ **1️⃣ Linear Search**

Linear search is the simplest form of searching —
you check each element one by one until you find the target (or reach the end).

### 💻 Example Code:

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1  # Not found

nums = [10, 20, 30, 40, 50]
print("Index of 30:", linear_search(nums, 30))
print("Index of 99:", linear_search(nums, 99))
```

### 🧮 Output:

```
Index of 30: 2
Index of 99: -1
```

### ⏱️ Time Complexity:

* **Best Case:** O(1) (if found early)
* **Worst Case:** O(n) (if found late or not at all)
* **Space:** O(1)

---

## ⚙️ **2️⃣ Binary Search (Iterative)**

Binary search works **only on sorted arrays**.
Instead of checking every element, it **divides the array in half** each time — making it much faster.

---

### 💡 Concept:

1️⃣ Start with two pointers:
`low = 0`, `high = len(arr) - 1`

2️⃣ Find the middle element:
`mid = (low + high) // 2`

3️⃣ Compare `arr[mid]` with target:

* If equal → found 🎯
* If smaller → search right half
* If greater → search left half

4️⃣ Repeat until found or `low > high`

---

### 💻 Example Code:

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Not found

nums = [10, 20, 30, 40, 50, 60, 70]
print("Index of 50:", binary_search(nums, 50))
print("Index of 25:", binary_search(nums, 25))
```

### 🧮 Output:

```
Index of 50: 4
Index of 25: -1
```

---

### 🔍 **Dry Run Visualization**

Let’s say `arr = [10, 20, 30, 40, 50, 60, 70]`, `target = 50`

| Step | low | high | mid | arr[mid] | Comparison | Action                 |
| ---- | --- | ---- | --- | -------- | ---------- | ---------------------- |
| 1    | 0   | 6    | 3   | 40       | 40 < 50    | Search right → low = 4 |
| 2    | 4   | 6    | 5   | 60       | 60 > 50    | Search left → high = 4 |
| 3    | 4   | 4    | 4   | 50       | 50 == 50   | 🎯 Found!              |

✅ **Found in 3 steps**, not 7 (O(log n) time).

---

## ⚙️ **3️⃣ Binary Search (Recursive)**

Binary search can also be implemented recursively.

```python
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1  # Base case

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)


nums = [2, 4, 6, 8, 10, 12]
print("Index of 8:", binary_search_recursive(nums, 0, len(nums)-1, 8))
```

🧮 **Output:**

```
Index of 8: 3
```

---

## 🎯 **Mini Challenge**

Write a program that:

1. Takes a **sorted list of integers** and a **target** as input.
2. Uses **binary search** to find if the target exists.
3. Prints **"Found"** if present, otherwise **"Not Found"**.

Example:

```
Input: [5, 10, 15, 20, 25], target = 15  
Output: Found
```

💡 *Hint:* Use a while loop, update `low`, `high`, and check `arr[mid]`.

---

## 🧩 **Practice Problems**

1️⃣ [LeetCode #704 — Binary Search](https://leetcode.com/problems/binary-search/)
2️⃣ [GFG — Binary Search Algorithm](https://www.geeksforgeeks.org/binary-search/)
3️⃣ [LeetCode #35 — Search Insert Position](https://leetcode.com/problems/search-insert-position/)
4️⃣ [GFG — Count 1’s in Sorted Binary Array](https://www.geeksforgeeks.org/count-1s-sorted-binary-array/)

---

## 🔗 **Free Resources**

* 🎥 [freeCodeCamp – Binary Search Explained Visually (YouTube)](https://youtu.be/P3YID7liBug)
* 🧠 [Visualgo.net – Binary Search Animation](https://visualgo.net/en/bst)
* 💻 [Python Tutor – Step-by-Step Binary Search Execution](https://pythontutor.com/visualize.html)

---

## 🔁 **Quick Recap**

✅ Linear Search → simple, O(n)
✅ Binary Search → efficient, O(log n)
✅ Works only on sorted data
✅ Implemented both iterative & recursive versions
✅ Learned dry-run logic of mid, low, and high pointers

---

## 🧠 **Mini Quiz (3 Questions)**

1️⃣ Binary search works only on what type of data?
A) Unsorted B) Random C) Sorted

2️⃣ If array size doubles, how many more steps does binary search take (roughly)?
A) +1 B) +n C) +log₂n

3️⃣ Time complexity of binary search?
A) O(n) B) O(log n) C) O(n²)

*(Answers: 1️⃣ C, 2️⃣ A, 3️⃣ B)*


## 🚀 **Tomorrow (Day 4 Preview — Sorting Algorithms)**

We’ll cover:

* Bubble Sort 🫧
* Insertion Sort ✋
* Selection Sort 🧩
* Step-by-step dry runs + comparisons
* Sorting logic visualization

---

Would you like me to include **visual dry runs + swap-trace tables** for each sorting algorithm tomorrow (so you can clearly see how the array changes after every pass)?
