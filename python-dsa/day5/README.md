
# 📅 **Day 5 — Prefix Sum, Kadane’s Algorithm & Sliding Window**

---

## 🧠 **Concept 1: Prefix Sum**

### ❓What is a Prefix Sum?

A **Prefix Sum** is a running total of array elements.
Each element at index `i` stores the **sum of all elements from 0 to i**.

---

### 💡 Example:

Array: `[2, 4, 6, 8]`

| Index      | 0 | 1 | 2  | 3  |
| ---------- | - | - | -- | -- |
| Value      | 2 | 4 | 6  | 8  |
| Prefix Sum | 2 | 6 | 12 | 20 |

So,
`prefix[i] = prefix[i-1] + arr[i]`

---

### 💻 **Code: Create Prefix Sum Array**

```python
def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix

nums = [2, 4, 6, 8, 10]
print("Prefix Sum:", prefix_sum(nums))
```

🧮 **Output:**

```
Prefix Sum: [2, 6, 12, 20, 30]
```

---

### ⚙️ **Use Case: Subarray Sum in O(1)**

If we have prefix sums,
we can find the sum of any subarray `[L…R]` using:

```
sum(L…R) = prefix[R] - prefix[L-1]
```

Example:

```
nums = [2,4,6,8,10]
prefix = [2,6,12,20,30]
Sum(1…3) = prefix[3] - prefix[0] = 20 - 2 = 18
```

✅ **Time Complexity:**

* Normal subarray sum: O(n)
* Prefix method: O(1)

💾 Space: O(n)

---

## ⚡ **Concept 2: Kadane’s Algorithm (Maximum Subarray Sum)**

### ❓Problem:

Find the **maximum sum of any contiguous subarray**.

Example:

```
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6   # (4 + -1 + 2 + 1)
```

---

### 💡 Intuition:

We keep adding elements — if the sum becomes negative, we **reset** it to 0.

---

### 💻 **Code: Kadane’s Algorithm**

```python
def max_subarray_sum(arr):
    max_sum = arr[0]
    curr_sum = 0

    for num in arr:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)

        # Reset current sum if it becomes negative
        if curr_sum < 0:
            curr_sum = 0

    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", max_subarray_sum(nums))
```

🧮 **Output:**

```
Maximum Subarray Sum: 6
```

---

### 🔍 **Dry Run Visualization**

| Step | num | curr_sum | max_sum |
| ---- | --- | -------- | ------- |
| 1    | -2  | -2       | -2      |
| 2    | 1   | 1        | 1       |
| 3    | -3  | -2       | 1       |
| 4    | 4   | 4        | 4       |
| 5    | -1  | 3        | 4       |
| 6    | 2   | 5        | 5       |
| 7    | 1   | 6        | 6       |
| 8    | -5  | 1        | 6       |
| 9    | 4   | 5        | 6       |

✅ **Max Subarray Sum = 6**

---

### ⚙️ **Time & Space**

* ⏱️ Time: O(n)
* 💾 Space: O(1)

💡 Used in financial analysis (max profit streaks) or AI signal smoothing.

---

## 🔄 **Concept 3: Sliding Window Technique**

### ❓What is it?

Instead of recalculating sums or counts every time,
we **slide a window** of fixed size across the array —
updating results efficiently as the window moves.

---

### 💡 Example Problem:

Find the **maximum sum of a subarray of size `k`**.

```
Input: [2, 1, 5, 1, 3, 2], k = 3
Output: 9  # (5 + 1 + 3)
```

---

### 💻 **Code: Sliding Window**

```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Slide window
        max_sum = max(max_sum, window_sum)

    return max_sum

nums = [2, 1, 5, 1, 3, 2]
print("Max sum of subarray of size 3:", max_sum_subarray(nums, 3))
```

🧮 **Output:**

```
Max sum of subarray of size 3: 9
```

---

### 🔍 **Dry Run Visualization**

| Window | Elements | Window Sum | Max Sum |
| ------ | -------- | ---------- | ------- |
| 1      | [2,1,5]  | 8          | 8       |
| 2      | [1,5,1]  | 7          | 8       |
| 3      | [5,1,3]  | 9          | 9       |
| 4      | [1,3,2]  | 6          | 9       |

✅ **Efficient O(n) time** — no nested loops.

---

## ⚔️ **Prefix vs Sliding Window**

| Feature | Prefix Sum                       | Sliding Window    |
| ------- | -------------------------------- | ----------------- |
| Type    | Cumulative pattern               | Fixed-size window |
| Problem | Range queries                    | Subarray analysis |
| Time    | O(n) preprocessing, O(1) queries | O(n) single-pass  |
| Space   | O(n)                             | O(1)              |

---

## 🎯 **Mini Challenge**

Write a Python program to:

* Input: `arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]`, `k = 4`
* Output: **maximum sum of subarray of size 4**

💡 Hint: Use the **sliding window** technique.

✅ Expected Output: `39` (subarray `[4, 2, 10, 23]`)

---

## 🧩 **Practice Problems**

1️⃣ [LeetCode #53 — Maximum Subarray (Kadane’s Algorithm)](https://leetcode.com/problems/maximum-subarray/)
2️⃣ [GFG — Maximum of All Subarrays of Size K](https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/)
3️⃣ [LeetCode #560 — Subarray Sum Equals K (Prefix Sum)](https://leetcode.com/problems/subarray-sum-equals-k/)

---

## 🔗 **Free Resources**

* 🎥 [Striver – Kadane’s Algorithm Explained](https://youtu.be/86CQq3pKSUw)
* 🧠 [GeeksforGeeks – Prefix Sum & Sliding Window](https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/)
* 💻 [Visualize Prefix & Window Movement – Python Tutor](https://pythontutor.com/visualize.html)

---

## 🔁 **Quick Recap**

✅ **Prefix Sum** — helps calculate subarray sums in O(1)
✅ **Kadane’s Algorithm** — finds the largest contiguous sum efficiently
✅ **Sliding Window** — efficient for fixed-size subarray problems
✅ All O(n) time — powerful optimization patterns

---

## 🧠 **Mini Quiz (3 Questions)**

1️⃣ Kadane’s Algorithm works for what type of array?
A) Sorted B) Only positive numbers C) Any array

2️⃣ Sliding window is best for subarrays of?
A) Fixed size B) Variable size C) Random length

3️⃣ Prefix sum helps to compute what faster?
A) Average B) Range sum C) Multiplication

*(Answers: 1️⃣ C, 2️⃣ A, 3️⃣ B)*

---


## 🚀 **Tomorrow (Day 6 Preview — Array Interview Patterns & Revision)**

We’ll cover:

* Merging sorted arrays
* Rotating arrays by `k` positions
* Removing duplicates
* Real interview-style array problems
* Week 1 recap quiz 🧠

---

Would you like me to include **array rotation & merge visuals (with step-by-step movement diagrams)** for tomorrow’s final array class (Day 6 + Week 1 Recap)?
