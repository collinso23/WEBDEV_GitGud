from django import forms

TOOLS_LIST=(("ping","ping"), ("dig", "dig") , ("whois", "whois"), ("mtr","mtr"))

class ToolForm(forms.Form):
    tool = forms.ChoiceField(label='Tool:', choices=TOOLS_LIST)
    ip_address = forms.CharField(label = 'IP Address', max_length=100)
