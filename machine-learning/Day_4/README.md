Today I learned 

**Calculate key statistical measures (mean, median, std, etc.)

Reshape and flatten arrays

Combine and split arrays efficiently**

**Basic Statistical Operations**

**Axis Parameter (Important for ML Data)** 
When working with 2D arrays (matrices), you can compute stats row-wise or column-wise using the axis parameter.
**Hint** Think of axis=0 as “vertical operations” (columns) and axis=1 as “horizontal operations” (rows).

**Reshaping Arrays**
🧠 In ML, reshaping is often used for feature and label preparation, or when transforming image pixel arrays.

 **Stacking & Splitting Arrays**
Combining or separating data is common in preprocessing steps.
💡 Use case:
Splitting train/test datasets or combining different feature arrays before model training.

**Useful Utility Functions**

''A few more handy tools:
arr = np.array([1, 2, 3, 4, 5])
print("Unique elements:", np.unique(arr))
print("Clipped between 2 and 4:", np.clip(arr, 2, 4))  # Limit values
print("Sorted array:", np.sort(arr))
print("Indices of sorted array:", np.argsort(arr))''

