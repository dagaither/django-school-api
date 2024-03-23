from django.core.exceptions import ValidationError
import re

def validate_subject_name(subject_name):
    error_message = 'Subject must be in title case format.'
    regex = r'^[A-Z][a-z]* [A-Z][a-z]*$'
    good_name = re.match(regex, subject_name)
    if good_name:
        return subject_name
    else:
        raise ValidationError(error_message)

def validate_professor_name(professor):
    error_message = 'Professor name must be in the format "Professor Adam".'
    regex = r'^Professor [A-Z][a-z]*$'

    good_name = re.match(regex, professor)
    if good_name:
        return professor
    else:
        raise ValidationError(error_message)