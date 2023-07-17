class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        skill_count = len(req_skills)
        people_count = len(people)
        skill_map = {}
        for i in range(skill_count):
            skill_map[req_skills[i]] = i
        person_skill_mask = [0] * people_count
        for i in range(people_count):
            for skill in people[i]:
                person_skill_mask[i] |= 1 << skill_map[skill]
        dp = [2**people_count - 1] * (2**skill_count)
        dp[0] = 0
        for skills_combo in range(1, 2**skill_count):
            for i in range(people_count):
                remaining_skills = skills_combo & ~person_skill_mask[i]
                if skills_combo != remaining_skills:
                    people_mask = dp[remaining_skills] | (2**i)
                    if dp[skills_combo].bit_count() > people_mask.bit_count():
                        dp[skills_combo] = people_mask
        res = []
        for i in range(people_count):
            if dp[2**skill_count - 1] >> i & 1:
                res.append(i)
        return res
