class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(result, 0, [], 0, target, candidates)
        return result

    def backtrack(self, result, start, path, total, target, candidates):
        # 如果總和剛好等於 target，加入結果集
        if total == target:
            result.append(path[:])
            return
        # 如果總和超過 target，停止搜索
        if total > target:
            return

        # 從 start 開始遍歷，允許重複使用當前數字
        for i in range(start, len(candidates)):
            # 選擇 candidates[i]
            path.append(candidates[i])
            self.backtrack(result, i, path, total + candidates[i], target, candidates)  # 重複使用同一個數字
            path.pop()  # 回溯