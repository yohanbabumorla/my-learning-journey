
# 📅 **Day 4 — Sorting Algorithms (Step-by-Step with Python + Dry Runs)**

---

## 🧠 **Concept: What is Sorting?**

**Sorting** means arranging data in a specific order — ascending or descending.

Example:

```
Input: [5, 3, 8, 6, 2]
Output: [2, 3, 5, 6, 8]
```

### 💡 Real-life Analogy:

Imagine organizing exam papers by marks —
you repeatedly **compare two papers** and **swap** them until all are sorted.

---

## ⚙️ **Sorting Types by Method**

| Type                     | Description      | Example                      |
| ------------------------ | ---------------- | ---------------------------- |
| **Comparison-based**     | Compare elements | Bubble, Insertion, Selection |
| **Non-comparison-based** | Use math logic   | Counting, Radix, Bucket      |

---

We’ll cover the **3 foundational algorithms** today 👇

---

## 🫧 **1️⃣ Bubble Sort**

### 🧠 Concept:

* Repeatedly compare **adjacent elements**
* Swap if they’re in the wrong order
* “Largest element bubbles up” to the end each pass

---

### 💻 Code:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

nums = [5, 3, 8, 6, 2]
print("Sorted array:", bubble_sort(nums))
```

### 🧮 Output:

```
Sorted array: [2, 3, 5, 6, 8]
```

---

### 🔍 **Dry Run Visualization**

| Pass | Comparisons             | Array after pass |
| ---- | ----------------------- | ---------------- |
| 1    | (5,3),(3,8),(8,6),(6,2) | [3,5,6,2,8]      |
| 2    | (3,5),(5,6),(6,2)       | [3,5,2,6,8]      |
| 3    | (3,5),(5,2)             | [3,2,5,6,8]      |
| 4    | (3,2)                   | [2,3,5,6,8]      |

✅ Time Complexity:

* Worst/Average → **O(n²)**
* Best (already sorted) → **O(n)**
  💾 Space → **O(1)**

---

## 🧩 **2️⃣ Selection Sort**

### 🧠 Concept:

* Repeatedly find the **minimum element** in the unsorted part
* Swap it with the first unsorted element
* Shrinks the unsorted region each time

---

### 💻 Code:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

nums = [64, 25, 12, 22, 11]
print("Sorted array:", selection_sort(nums))
```

### 🧮 Output:

```
Sorted array: [11, 12, 22, 25, 64]
```

---

### 🔍 **Dry Run Visualization**

| Step | Unsorted Part    | Min Found | Swap Result      |
| ---- | ---------------- | --------- | ---------------- |
| 1    | [64,25,12,22,11] | 11        | [11,25,12,22,64] |
| 2    | [25,12,22,64]    | 12        | [11,12,25,22,64] |
| 3    | [25,22,64]       | 22        | [11,12,22,25,64] |

✅ Time → O(n²)
✅ Space → O(1)
🧠 Fewer swaps than Bubble Sort, but still slow for large n.

---

## ✋ **3️⃣ Insertion Sort**

### 🧠 Concept:

* Divide the array into **sorted** and **unsorted** parts
* Pick each element from unsorted, and **insert** it in the correct place in sorted part
* Works great for **small or nearly sorted** data

---

### 💻 Code:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

nums = [12, 11, 13, 5, 6]
print("Sorted array:", insertion_sort(nums))
```

### 🧮 Output:

```
Sorted array: [5, 6, 11, 12, 13]
```

---

### 🔍 **Dry Run Visualization**

| Step | Key | Result after Insertion |
| ---- | --- | ---------------------- |
| 1    | 11  | [11,12,13,5,6]         |
| 2    | 13  | [11,12,13,5,6]         |
| 3    | 5   | [5,11,12,13,6]         |
| 4    | 6   | [5,6,11,12,13]         |

✅ Time → O(n²)
✅ Best case (already sorted) → O(n)
✅ Space → O(1)

---

## ⚔️ **Comparison Table**

| Algorithm | Best  | Worst | Stable? | Use Case                      |
| --------- | ----- | ----- | ------- | ----------------------------- |
| Bubble    | O(n)  | O(n²) | ✅ Yes   | Teaching concept              |
| Selection | O(n²) | O(n²) | ❌ No    | Fewer swaps                   |
| Insertion | O(n)  | O(n²) | ✅ Yes   | Small or nearly sorted arrays |

---

## 🎯 **Mini Challenge**

Write a Python function to:

* Accept a list of numbers
* Sort them using **insertion sort**
* Print the number of **comparisons and swaps** made

💡 *Hint:* Use counters inside your loops.

---

## 🧩 **Practice Problems**

1️⃣ [LeetCode #912 — Sort an Array](https://leetcode.com/problems/sort-an-array/)
2️⃣ [GFG — Selection Sort Practice](https://www.geeksforgeeks.org/selection-sort/)
3️⃣ [GFG — Insertion Sort Practice](https://www.geeksforgeeks.org/insertion-sort/)
4️⃣ [HackerRank — Python Sorting Challenge](https://www.hackerrank.com/domains/tutorials/10-days-of-statistics)

---

## 🔗 **Free Resources**

* 🎥 [Apna College – Sorting in Python (YouTube)](https://youtu.be/pkkFqlG0Hds)
* 🧠 [Visualgo.net – Sorting Animations](https://visualgo.net/en/sorting)
* 💻 [Python Tutor – Step Execution Visualizer](https://pythontutor.com/visualize.html)

---

## 🔁 **Quick Recap**

✅ Learned 3 core sorting algorithms
✅ Understood step-by-step dry runs
✅ Learned which one to use and when

**Time Complexities Summary**

| Algorithm      | Best  | Worst | Average |
| -------------- | ----- | ----- | ------- |
| Bubble Sort    | O(n)  | O(n²) | O(n²)   |
| Selection Sort | O(n²) | O(n²) | O(n²)   |
| Insertion Sort | O(n)  | O(n²) | O(n²)   |

---

## 🧠 **Mini Quiz (3 Questions)**

1️⃣ Which sorting algorithm performs the fewest swaps?
A) Bubble B) Selection C) Insertion

2️⃣ Which is best for nearly sorted arrays?
A) Bubble B) Selection C) Insertion

3️⃣ Time complexity of Bubble Sort in worst case?
A) O(n) B) O(n log n) C) O(n²)

*(Answers: 1️⃣ B, 2️⃣ C, 3️⃣ C)*

---


## 🚀 **Tomorrow (Day 5 Preview — Advanced Array Patterns)**

We’ll dive into:

* Prefix Sum (for subarray problems)
* Kadane’s Algorithm (maximum subarray sum)
* Sliding Window Pattern (for performance optimization)
* Real interview problems on arrays

---

Would you like me to include **visual dry runs and prefix-sum diagrams** for tomorrow’s Day 5 (Kadane’s Algorithm + Sliding Window)?
