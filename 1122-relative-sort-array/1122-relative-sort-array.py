class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for n2 in arr2:
            n2_cnt = arr1.count(n2)     # 각 숫자의 개수
            result.extend([n2] * n2_cnt)
        
        arr1.sort()
        
        for n1 in arr1:
            if n1 not in arr2:
                result.append(n1)
        return result