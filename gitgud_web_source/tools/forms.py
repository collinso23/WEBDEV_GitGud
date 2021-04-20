from django import forms
"""
form is used to define the form elements which are called in the view. 
It can use statically assigned vars like TOOLS_LIST or it can pull information from the DB using models.py
"""
TOOLS_LIST=(("ping","ping"), ("dig", "dig") , ("whois", "whois"), ("mtr","mtr"))

class ToolForm(forms.Form):
    tool = forms.ChoiceField(label='Tool:', choices=TOOLS_LIST)
    ip_address = forms.CharField(label = 'IP Address', max_length=100)
