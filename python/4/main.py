# three lines O(m+n)
def findMedianSortedArrays(self, nums1, nums2):
    nums = sorted(nums1 + nums2)
    l = len(nums)
    return (nums[l // 2] + nums[l // 2 - (l + 1) % 2]) / 2


# O(log(m+n)) Kth method
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def getKth(array1, i, array2, x, k):
            if i == len(array1):
                return array2[x + k]
            elif x == len(array2):
                return array1[i + k]
            elif k == 0:
                return min(array1[i], array2[x])

            mid1 = min(len(array1) - i, (k + 1) // 2)
            mid2 = min(len(array2) - x, (k + 1) // 2)
            a = array1[i + mid1 - 1]
            b = array2[x + mid2 - 1]

            if a < b:
                return getKth(array1, i + mid1, array2, x, k - mid1)
            return getKth(array1, i, array2, x + mid2, k - mid2)

        total_nums = len(nums1) + len(nums2)
        midpoint = total_nums // 2 + 1

        if total_nums % 2 == 0:
            first = getKth(nums1, 0, nums2, 0, total_nums // 2 - 1)
            second = getKth(nums1, 0, nums2, 0, total_nums // 2)
            return (first + second) / 2
        else:
            return getKth(nums1, 0, nums2, 0, total_nums // 2)  
        
# O(log(min(m,n)))
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        median = (m + n - 1) // 2
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) // 2
            if median - i - 1 < 0 or a[i] >= b[median-i-1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i+2] + b[median-i:median-i+2])
        return (nextfew[0] + nextfew[1 - (m+n) % 2]) / 2.0
