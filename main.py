from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill
from flask import Flask
from flask import render_template


app = Flask(__name__)

lst_candidates = "candidates.json"

@app.route("/")
def page_index():
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:idx>")
def candidate_page(idx):
    candidate = get_candidate(idx)
    if not candidate:
        return "Кандидат не найден"
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def candidate_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    if not candidates:
        return "Кандидат не найден"
    return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def candidate_skills(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skills.html", skill=skill_name, candidates=candidates)


app.run()
