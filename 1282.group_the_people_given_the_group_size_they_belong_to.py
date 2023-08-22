class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        curr_group = [None] * (len(groupSizes) + 1)
        group_map = {}
        for i, size in enumerate(groupSizes):
            if (
                curr_group[size] not in group_map
                or len(group_map[curr_group[size]]) == size
            ):
                group_map[i] = [i]
                curr_group[size] = i
            else:
                group_map[curr_group[size]].append(i)
        return group_map.values()
