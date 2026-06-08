"""Dental expert system knowledge base."""

SYMPTOM_QUESTIONS = [
    ("tooth_pain", "Do you feel pain in one of your teeth?"),
    ("severe_throbbing_pain", "Is the pain severe or throbbing?"),
    ("cold_sensitivity", "Do you feel pain or discomfort when drinking cold beverages?"),
    ("hot_sensitivity", "Do you feel pain or discomfort when drinking hot beverages?"),
    ("visible_cavity", "Do you notice a visible cavity or hole in the tooth?"),
    ("gum_bleeding", "Do your gums bleed while brushing or spontaneously?"),
    ("gum_redness", "Do your gums appear red or inflamed?"),
    ("gum_face_swelling", "Is there swelling in your gums or face?"),
    ("bad_breath", "Do you suffer from persistent bad breath?"),
    ("pus_bad_taste", "Do you notice pus or a bad taste coming from the gum or tooth?"),
    ("pain_while_chewing", "Do you feel pain while chewing?"),
    ("grinding_sleep", "Has anyone told you that you grind your teeth while sleeping?"),
    ("jaw_pain_fatigue", "Do you wake up with jaw pain or fatigue?"),
    ("receding_gums", "Do you notice gum recession or exposed tooth roots?"),
    ("pain_after_stimulus", "Does the pain continue after removing the trigger such as cold or hot drinks?"),
    ("night_pain", "Does the pain become worse at night or wake you up from sleep?"),
]

RULES = [
    {
        "id": "Dental Caries Rule 1",
        "disease": "Dental Caries",
        "conditions": {
            "tooth_pain": True,
            "cold_sensitivity": True,
            "visible_cavity": True,
        },
    },
    {
        "id": "Dental Caries Rule 2",
        "disease": "Dental Caries",
        "conditions": {
            "visible_cavity": True,
            "cold_sensitivity": True,
        },
    },
    {
        "id": "Dental Caries Rule 3",
        "disease": "Dental Caries",
        "conditions": {
            "pain_while_chewing": True,
            "visible_cavity": True,
        },
    },
    {
        "id": "Tooth Sensitivity Rule 1",
        "disease": "Tooth Sensitivity",
        "conditions": {
            "cold_sensitivity": True,
            "severe_throbbing_pain": False,
            "visible_cavity": False,
        },
    },
    {
        "id": "Tooth Sensitivity Rule 2",
        "disease": "Tooth Sensitivity",
        "conditions": {
            "cold_sensitivity": True,
            "hot_sensitivity": True,
            "visible_cavity": False,
        },
    },
    {
        "id": "Pulpitis Rule 1",
        "disease": "Pulpitis",
        "conditions": {
            "severe_throbbing_pain": True,
            "pain_after_stimulus": True,
            "night_pain": True,
        },
    },
    {
        "id": "Pulpitis Rule 2",
        "disease": "Pulpitis",
        "conditions": {
            "severe_throbbing_pain": True,
            "cold_sensitivity": True,
            "night_pain": True,
        },
    },
    {
        "id": "Pulpitis Rule 3",
        "disease": "Pulpitis",
        "conditions": {
            "severe_throbbing_pain": True,
            "hot_sensitivity": True,
            "pain_after_stimulus": True,
        },
    },
    {
        "id": "Gingivitis Rule 1",
        "disease": "Gingivitis",
        "conditions": {
            "gum_bleeding": True,
            "gum_redness": True,
        },
    },
    {
        "id": "Gingivitis Rule 2",
        "disease": "Gingivitis",
        "conditions": {
            "gum_bleeding": True,
            "gum_redness": True,
            "bad_breath": True,
        },
    },
    {
        "id": "Gingivitis Rule 3",
        "disease": "Gingivitis",
        "conditions": {
            "gum_bleeding": True,
            "gum_redness": True,
            "gum_face_swelling": True,
        },
    },
    {
        "id": "Dental Abscess Rule 1",
        "disease": "Dental Abscess",
        "conditions": {
            "gum_face_swelling": True,
            "severe_throbbing_pain": True,
            "pus_bad_taste": True,
        },
    },
    {
        "id": "Dental Abscess Rule 2",
        "disease": "Dental Abscess",
        "conditions": {
            "gum_face_swelling": True,
            "severe_throbbing_pain": True,
            "pain_while_chewing": True,
        },
    },
    {
        "id": "Dental Abscess Rule 3",
        "disease": "Dental Abscess",
        "conditions": {
            "gum_face_swelling": True,
            "bad_breath": True,
            "pus_bad_taste": True,
        },
    },
    {
        "id": "Bruxism Rule 1",
        "disease": "Bruxism",
        "conditions": {
            "grinding_sleep": True,
            "jaw_pain_fatigue": True,
        },
    },
    {
        "id": "Bruxism Rule 2",
        "disease": "Bruxism",
        "conditions": {
            "grinding_sleep": True,
            "tooth_pain": True,
            "jaw_pain_fatigue": True,
        },
    },
    {
        "id": "Gum Recession Rule 1",
        "disease": "Gum Recession",
        "conditions": {
            "receding_gums": True,
            "cold_sensitivity": True,
        },
    },
    {
        "id": "Gum Recession Rule 2",
        "disease": "Gum Recession",
        "conditions": {
            "receding_gums": True,
            "cold_sensitivity": True,
            "hot_sensitivity": True,
        },
    },
    {
        "id": "Gum Recession Rule 3",
        "disease": "Gum Recession",
        "conditions": {
            "receding_gums": True,
            "tooth_pain": True,
            "cold_sensitivity": True,
        },
    },
]

DISEASES = [
    "Dental Caries",
    "Tooth Sensitivity",
    "Pulpitis",
    "Gingivitis",
    "Dental Abscess",
    "Bruxism",
    "Gum Recession",
]
