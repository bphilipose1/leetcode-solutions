class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        iter1 = 0
        iter2 = 0
        combinedList = []
        while iter1 < len(nums1) and iter2 < len(nums2):
            if nums1[iter1] < nums2[iter2]:
                combinedList.append(nums1[iter1])
                iter1 = iter1 + 1
            else:
                combinedList.append(nums2[iter2])
                iter2 = iter2 + 1
        while iter1 < len(nums1):
            combinedList.append(nums1[iter1])
            iter1 = iter1 + 1
        while iter2 < len(nums2):
            combinedList.append(nums2[iter2])
            iter2 = iter2 + 1

        if len(combinedList) % 2 == 0:
            mid = int(len(combinedList) / 2)
            median = (combinedList[mid] + combinedList[mid - 1]) / 2
        else:
            mid = int(len(combinedList) / 2)
            median = combinedList[mid]
        return median