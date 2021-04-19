from django import forms

TOOLS_LIST=("ping", "dig" , "whois")

class ToolForm(forms.Form):
    tool = forms.ChoiceField(label='Tool To Use: ', choices=TOOLS_LIST)
    IP_ADDR = forms.CharField(label = 'IP Addr', max_length=20)