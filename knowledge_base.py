SYMPTOM_QUESTIONS = [
    ("tooth_pain", "Do you feel pain in one of your teeth?"),
    ("severe_throbbing_pain", "Is the pain severe, throbbing, or spontaneous (occurs without any trigger)?"),
    ("cold_sensitivity", "Do you feel brief pain or discomfort when drinking cold beverages?"),
    ("hot_sensitivity", "Do you feel pain or discomfort when drinking hot beverages?"),
    ("sweet_sensitivity", "Do you feel pain or discomfort when eating sweet foods?"),
    ("visible_cavity", "Do you notice a visible cavity, hole, or dark spot on the tooth?"),
    ("gum_bleeding", "Do your gums bleed while brushing or spontaneously?"),
    ("gum_redness", "Do your gums appear red, swollen, or inflamed?"),
    ("gum_tenderness", "Are your gums tender or painful to touch?"),
    ("gum_face_swelling", "Is there noticeable swelling in your gums, face, or jaw?"),
    ("bad_breath", "Do you suffer from persistent bad breath?"),
    ("pus_bad_taste", "Do you notice pus, drainage, or a bad taste coming from the gum or tooth?"),
    ("pain_while_chewing", "Do you feel pain while chewing or biting?"),
    ("grinding_sleep", "Has anyone told you that you grind or clench your teeth while sleeping?"),
    ("jaw_pain_fatigue", "Do you wake up with jaw pain, fatigue, or stiffness?"),
    ("morning_headache", "Do you frequently wake up with headaches?"),
    ("earache", "Do you experience earache or facial pain without ear infection?"),
    ("worn_teeth", "Have you noticed your teeth becoming flat, worn down, or chipped?"),
    ("receding_gums", "Do you notice gum recession or exposed tooth roots?"),
    ("lingering_pain", "Does the pain continue for more than 30 seconds after removing the trigger (cold/hot/sweet)?"),
    ("night_pain", "Does the pain become worse at night or wake you up from sleep?"),
    ("pain_on_tapping", "Do you feel pain when tapping or pressing on the affected tooth?"),
    ("fever", "Do you have a fever or feel generally unwell?"),
    ("difficulty_opening_mouth", "Do you have difficulty opening your mouth fully (jaw stiffness)?"),
    ("swollen_lymph_nodes", "Do you have swollen or tender lymph nodes in your neck or jaw area?"),
    ("loose_teeth", "Do you notice any of your teeth feeling loose or shifting?"),
    ("gum_pockets", "Have you been told you have deep gum pockets or periodontal disease?"),
    ("plaque_tartar", "Do you notice heavy plaque or tartar buildup on your teeth?"),
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
        "id": "Dental Caries Rule 4",
        "disease": "Dental Caries",
        "conditions": {
            "sweet_sensitivity": True,
            "visible_cavity": True,
        },
    },
    {
        "id": "Dental Caries Rule 5",
        "disease": "Dental Caries",
        "conditions": {
            "sweet_sensitivity": True,
            "cold_sensitivity": True,
        },
    },

    {
        "id": "Tooth Sensitivity Rule 1",
        "disease": "Tooth Sensitivity",
        "conditions": {
            "cold_sensitivity": True,
            "lingering_pain": False,
            "visible_cavity": False,
            "severe_throbbing_pain": False,
            "pain_on_tapping": False,
            "night_pain": False,
        },
    },
    {
        "id": "Tooth Sensitivity Rule 2",
        "disease": "Tooth Sensitivity",
        "conditions": {
            "cold_sensitivity": True,
            "hot_sensitivity": True,
            "lingering_pain": False,
            "visible_cavity": False,
            "severe_throbbing_pain": False,
        },
    },
    {
        "id": "Tooth Sensitivity Rule 3",
        "disease": "Tooth Sensitivity",
        "conditions": {
            "sweet_sensitivity": True,
            "lingering_pain": False,
            "visible_cavity": False,
            "severe_throbbing_pain": False,
            "night_pain": False,
        },
    },
    {
        "id": "Tooth Sensitivity Rule 4",
        "disease": "Tooth Sensitivity",
        "conditions": {
            "receding_gums": True,
            "cold_sensitivity": True,
            "lingering_pain": False,
            "visible_cavity": False,
            "severe_throbbing_pain": False,
        },
    },

    {
        "id": "Reversible Pulpitis Rule 1",
        "disease": "Reversible Pulpitis",
        "conditions": {
            "cold_sensitivity": True,
            "pain_while_chewing": True,
            "lingering_pain": False,
            "night_pain": False,
            "severe_throbbing_pain": False,
        },
    },
    {
        "id": "Reversible Pulpitis Rule 2",
        "disease": "Reversible Pulpitis",
        "conditions": {
            "sweet_sensitivity": True,
            "pain_on_tapping": True,
            "lingering_pain": False,
            "night_pain": False,
            "severe_throbbing_pain": False,
        },
    },
    {
        "id": "Reversible Pulpitis Rule 3",
        "disease": "Reversible Pulpitis",
        "conditions": {
            "cold_sensitivity": True,
            "sweet_sensitivity": True,
            "lingering_pain": False,
            "night_pain": False,
            "pain_on_tapping": False,
        },
    },
    {
        "id": "Reversible Pulpitis Rule 4",
        "disease": "Reversible Pulpitis",
        "conditions": {
            "cold_sensitivity": True,
            "hot_sensitivity": True,
            "lingering_pain": False,
            "night_pain": False,
            "severe_throbbing_pain": False,
        },
    },

    {
        "id": "Irreversible Pulpitis Rule 1",
        "disease": "Irreversible Pulpitis",
        "conditions": {
            "severe_throbbing_pain": True,
            "lingering_pain": True,
            "night_pain": True,
        },
    },
    {
        "id": "Irreversible Pulpitis Rule 2",
        "disease": "Irreversible Pulpitis",
        "conditions": {
            "severe_throbbing_pain": True,
            "hot_sensitivity": True,
            "lingering_pain": True,
        },
    },
    {
        "id": "Irreversible Pulpitis Rule 3",
        "disease": "Irreversible Pulpitis",
        "conditions": {
            "hot_sensitivity": True,
            "lingering_pain": True,
            "night_pain": True,
        },
    },
    {
        "id": "Irreversible Pulpitis Rule 4",
        "disease": "Irreversible Pulpitis",
        "conditions": {
            "severe_throbbing_pain": True,
            "lingering_pain": True,
            "pain_on_tapping": True,
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
            "gum_tenderness": True,
        },
    },
    {
        "id": "Gingivitis Rule 4",
        "disease": "Gingivitis",
        "conditions": {
            "gum_bleeding": True,
            "gum_redness": True,
            "plaque_tartar": True,
        },
    },

    {
        "id": "Periodontitis Rule 1",
        "disease": "Periodontitis",
        "conditions": {
            "gum_bleeding": True,
            "gum_pockets": True,
            "loose_teeth": True,
        },
    },
    {
        "id": "Periodontitis Rule 2",
        "disease": "Periodontitis",
        "conditions": {
            "receding_gums": True,
            "gum_pockets": True,
            "loose_teeth": True,
        },
    },
    {
        "id": "Periodontitis Rule 3",
        "disease": "Periodontitis",
        "conditions": {
            "gum_bleeding": True,
            "bad_breath": True,
            "gum_pockets": True,
            "loose_teeth": True,
        },
    },
    {
        "id": "Periodontitis Rule 4",
        "disease": "Periodontitis",
        "conditions": {
            "gum_redness": True,
            "receding_gums": True,
            "gum_pockets": True,
            "pain_while_chewing": True,
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
            "pus_bad_taste": True,
            "fever": True,
        },
    },
    {
        "id": "Dental Abscess Rule 4",
        "disease": "Dental Abscess",
        "conditions": {
            "severe_throbbing_pain": True,
            "pus_bad_taste": True,
            "fever": True,
            "swollen_lymph_nodes": True,
        },
    },
    {
        "id": "Dental Abscess Rule 5",
        "disease": "Dental Abscess",
        "conditions": {
            "gum_face_swelling": True,
            "difficulty_opening_mouth": True,
            "fever": True,
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
        "id": "Bruxism Rule 3",
        "disease": "Bruxism",
        "conditions": {
            "grinding_sleep": True,
            "morning_headache": True,
        },
    },
    {
        "id": "Bruxism Rule 4",
        "disease": "Bruxism",
        "conditions": {
            "worn_teeth": True,
            "jaw_pain_fatigue": True,
            "morning_headache": True,
        },
    },
    {
        "id": "Bruxism Rule 5",
        "disease": "Bruxism",
        "conditions": {
            "grinding_sleep": True,
            "earache": True,
            "morning_headache": True,
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
    {
        "id": "Gum Recession Rule 4",
        "disease": "Gum Recession",
        "conditions": {
            "receding_gums": True,
            "gum_pockets": False,
            "loose_teeth": False,
        },
    },
]

DISEASES = [
    "Dental Caries",
    "Tooth Sensitivity",
    "Reversible Pulpitis",
    "Irreversible Pulpitis",
    "Gingivitis",
    "Periodontitis",
    "Dental Abscess",
    "Bruxism",
    "Gum Recession",
]
