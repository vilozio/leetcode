# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

versions = []


def isBadVersion(version: int) -> bool:
    return versions[version - 1]


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        bad_version = -1
        while left <= n:
            mid = (n + left) // 2
            if isBadVersion(mid):
                bad_version = mid
                n = mid - 1
            else:
                left = mid + 1
        return bad_version


def call(arr):
    s = Solution()
    global versions
    versions = arr
    return s.firstBadVersion(len(arr))


def test():
    assert call([False, True, True]) == 2
    assert call([True]) == 1
    assert call([]) == -1
    assert call([True, True, True, True]) == 1
    assert call([False, False, False, False, False, True, True, True, True]) == 6
    assert call([False, False, False, False, False, False, False, False, True]) == 9
