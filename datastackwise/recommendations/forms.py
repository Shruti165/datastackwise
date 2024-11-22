# from django import forms
# from .models import Database
#
# class DatabaseForm(forms.Form):
#     SCALE_CHOICES = [
#         ('enterprise', 'Enterprise'),
#         ('medium', 'Medium'),
#         ('small', 'Small'),
#         ('POC', 'POC')
#     ]
#     BUDGET_CHOICES = [
#         ('high', 'High'),
#         ('medium', 'Medium'),
#         ('low', 'Low')
#     ]
#     QUERY_COMPLEXITY_CHOICES = [
#         ('simple', 'Simple'),
#         ('complex', 'Complex')
#     ]
#     TRAFFIC_CHOICES = [
#         ('high', 'High'),
#         ('medium', 'Medium'),
#         ('low', 'Low')
#     ]
#     GEOGRAPHIC_DISTRIBUTION_CHOICES = [
#         ('multi', 'Multi-region'),
#         ('single', 'Single region')
#     ]
#     COMPLIANCE_NEEDS_CHOICES = [
#         ('high', 'High'),
#         ('medium', 'Medium'),
#         ('low', 'Low')
#     ]
#
#     scale = forms.ChoiceField(choices=SCALE_CHOICES)
#     budget = forms.ChoiceField(choices=BUDGET_CHOICES)
#     query_complexity = forms.ChoiceField(choices=QUERY_COMPLEXITY_CHOICES)
#     traffic = forms.ChoiceField(choices=TRAFFIC_CHOICES)
#     geographic_distribution = forms.ChoiceField(choices=GEOGRAPHIC_DISTRIBUTION_CHOICES)
#     compliance_needs = forms.ChoiceField(choices=COMPLIANCE_NEEDS_CHOICES)

from django import forms

class DatabaseForm(forms.Form):
    application_type = forms.ChoiceField(
        choices=[
            ('analytics', 'Analytics'),
            ('transactional', 'Transactional'),
            ('hybrid', 'Hybrid'),
        ],
        widget=forms.RadioSelect,
    )
    scale = forms.ChoiceField(
        choices=[
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('enterprise', 'Enterprise'),
        ],
        widget=forms.RadioSelect,
    )
    read_write_operations = forms.ChoiceField(
        choices=[
            ('heavy_reads', 'Heavy Reads'),
            ('balanced', 'Balanced'),
            ('heavy_writes', 'Heavy Writes'),
        ],
        widget=forms.RadioSelect,
    )
    query_complexity = forms.ChoiceField(
        choices=[
            ('simple', 'Simple'),
            ('moderate', 'Moderate'),
            ('complex', 'Complex'),
        ],
        widget=forms.RadioSelect,
    )
    traffic = forms.ChoiceField(
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        widget=forms.RadioSelect,
    )
    budget = forms.ChoiceField(
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        widget=forms.RadioSelect,
    )
    compliance_needs = forms.ChoiceField(
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        widget=forms.RadioSelect,
    )
