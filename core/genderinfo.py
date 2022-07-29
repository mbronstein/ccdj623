#mb_utils.py

from django.db import models

# assumptions:
gender_options_dict = {
    "mm": {"label": "Male", "pronoun": "he", "possessive": "his", "objective": "him"},  # Male
    "ff": {"label": "Female", "pronoun": "she", "possessive": "her", "objective": "her"}, # Female
    "mp": {"label": "Male", "pronoun": "they", "possessive": "their","objective": "them"},  # Male
    "fp": {"label": "Female", "pronoun": "they", "possessive": "their","objective": "them"},   # Male
    "nn": {"label": "Male", "pronoun": "they", "possessive": "their","objective": "them"},
    "nf": {"label": "Non-Binary", "pronoun": "she", "possessive": "her","objective": "her"},  # Unknown/Plural
    "nm": {"label": "Non-Binary", "pronoun": "he", "possessive": "his", "objective": "him"}, # Unknown/Plural
    "np": {"label": "Non-Binary", "pronoun": "she", "possessive": "her","objective": "them"},
    "uu": {"label": "Unknown", "pronoun": "they", "possessive": "their","objective": "them"},
    "up": {"label": "Unknown", "pronoun": "they", "possessive": "their","objective": "them"},
}

gender_list = {"m":"Male", "f":"Female", "n":"Non-Binary", "u":"Unknown"}

pronoun_list = {"m":"Male", "f":"Female", "p":"Plural", "u":"Unknown"}

def get_gender_string_dict(g_char:str, p_char:str)-> dict:
    if g_char.lower() not in gender_list:
        raise ValueError("Gender must be m,f,n,p or u")
    else:
        g_char = g_char.lower()

    if p_char.lower() not in pronoun_list:
        raise ValueError(f"{p_char} is not a valid pronoun type. Must be m,f,p or u")
    else:
        p_char = p_char.lower()

    gender_code = str(g_char + p_char)

    if gender_code not in list(gender_options_dict):
        raise ValueError(f"gender code option combo :{gender_code} is not in valid gender codes option combo")
    else:
        return gender_options_dict[gender_code]


def get_personal_pronoun(g_char:str, p_char:str):
    return get_gender_string_dict(g_char,p_char)['pronoun']

def get_possessive_pronoun(g_char:str, p_char:str):
    return get_gender_string_dict(g_char,p_char)['possessive']

def get_gender_label(g_char:str, p_char:str):
    return get_gender_string_dict(g_char,p_char)['label']

def get_objective_pronoun(g_char:str, p_char:str):
    return get_gender_string_dict(g_char,p_char)['objective']


# TODO do we need to add choice for pronoun object like him, them, her

class GenderInfoMixin(models.Model):
    #to do add choices param
    gender_pronoun_code= models.CharField(max_length=1, default = "u")
    gender_code = models.CharField(max_length=1, default = "u")

    @property
    def gender_string(self):
        return get_gender_label(self.gender_code, self.gender_pronoun_code)

    @property
    def get_possessive_pronoun_string(self):
        return get_possessive_pronoun(self.gender_code, self.gender_pronoun_code)

    @property
    def object_pronoun_string(self):
        return get_objective_pronoun(self.gender_code, self.gender_pronoun_code)

    @property
    def personal_pronoun_string(self):
        return get_personal_pronoun(self.gender_code, self.gender_pronoun_code)

    class Meta:
        abstract = True
