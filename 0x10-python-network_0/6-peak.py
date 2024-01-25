#!/usr/bin/python3
""" find_peak funtion to get max number """


def peak(nums, start, end):
    """helper for find_peak"""
    if start == end:
        return nums[start]
    mid = int((end - start) / 2) + start

    if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
        return nums[mid]
    if nums[mid + 1] > nums[mid]:
        return peak(nums, mid + 1, end)
    return peak(nums, start, mid)


def find_peak(list_of_integers):
    """ finds the peak in the list if list is empty return None"""

    if list_of_integers is None or list_of_integers == []:
        return None

    return peak(list_of_integers, 0, len(list_of_integers) - 1)
