import json
def load_candidates_from_json():
    with open ("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    for candidate in load_candidates_from_json():
        if candidate_id == candidate["id"]:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    candidate_lst = []
    for candidate in load_candidates_from_json():
        if candidate["name"] == candidate_name:
            candidate_lst.append(candidate)
    return candidate_lst


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    candidate_lst = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate["skills"].lower().split(", "):
            candidate_lst.append(candidate)
    return candidate_lst






# print(get_candidates_by_skill(candidates, "python"))