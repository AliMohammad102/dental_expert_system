"""Simple inference engine for the dental expert system."""

from typing import Dict, List, Optional

import knowledge_base


def _to_diagnostic_fact(disease: str) -> str:
    mapping = {
        "Dental Caries": "possible_caries",
        "Tooth Sensitivity": "possible_sensitivity",
        "Pulpitis": "possible_pulpitis",
        "Gingivitis": "possible_gingivitis",
        "Dental Abscess": "possible_abscess",
        "Bruxism": "possible_bruxism",
        "Gum Recession": "possible_recession",
    }
    return mapping.get(disease, f"possible_{disease.lower().replace(' ', '_')}")


def _positive_facts(working_memory: Dict[str, bool]) -> List[str]:
    return [symptom for symptom, value in working_memory.items() if value]


def evaluate_rule(rule: Dict, working_memory: Dict[str, bool]) -> Dict:
    conditions = rule["conditions"]
    matched_positive_symptoms = []
    full_match = True

    for symptom, expected_value in conditions.items():
        actual_value = working_memory.get(symptom, False)

        if actual_value != expected_value:
            full_match = False

        if expected_value and actual_value:
            matched_positive_symptoms.append(symptom)

    return {
        "rule_id": rule["id"],
        "disease": rule["disease"],
        "matched_symptoms": matched_positive_symptoms,
        "full_match": full_match,
    }


def diagnose(working_memory: Dict[str, bool]) -> Dict:
    positive_facts = _positive_facts(working_memory)
    fired_rules_by_disease = {}
    matched_symptoms_by_disease = {}
    fired_rule_ids = []
    diagnostic_facts = []

    for rule in knowledge_base.RULES:
        result = evaluate_rule(rule, working_memory)
        if result["full_match"]:
            disease = result["disease"]
            fired_rule_ids.append(result["rule_id"])
            diagnostic_facts.append(_to_diagnostic_fact(disease))

            fired_rules_by_disease.setdefault(disease, []).append(result["rule_id"])
            matched_symptoms_by_disease.setdefault(disease, []).extend(result["matched_symptoms"])

    if not fired_rules_by_disease:
        return {
            "diagnosis": None,
            "confidence": None,
            "match_type": "No reliable diagnosis",
            "score": 0.0,
            "matched_rule": None,
            "fired_rules": [],
            "matched_symptoms": [],
            "diagnostic_facts": [],
        }

    best_disease: Optional[str] = None
    best_rule_count = 0
    best_matched_symptom_count = 0

    for disease, rules in fired_rules_by_disease.items():
        rule_count = len(rules)
        symptom_count = len(matched_symptoms_by_disease.get(disease, []))

        if rule_count > best_rule_count or (
            rule_count == best_rule_count and symptom_count > best_matched_symptom_count
        ):
            best_disease = disease
            best_rule_count = rule_count
            best_matched_symptom_count = symptom_count

    disease_rule_count = sum(1 for rule in knowledge_base.RULES if rule["disease"] == best_disease)
    fired_rule_ids_for_disease = fired_rules_by_disease[best_disease]
    matched_positive_symptoms = matched_symptoms_by_disease.get(best_disease, [])
    unique_matched_symptoms = list(dict.fromkeys(matched_positive_symptoms))

    if best_rule_count == disease_rule_count:
        confidence = "High"
    elif best_rule_count > 1:
        confidence = "Medium"
    else:
        confidence = "Low"

    return {
        "diagnosis": best_disease,
        "confidence": confidence,
        "match_type": confidence,
        "score": 0.0,
        "matched_rule": fired_rule_ids_for_disease[0] if fired_rule_ids_for_disease else None,
        "fired_rules": fired_rule_ids_for_disease,
        "matched_symptoms": unique_matched_symptoms,
        "diagnostic_facts": [_to_diagnostic_fact(best_disease)],
        "positive_facts": positive_facts,
    }
