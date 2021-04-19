from django import forms

TOOLS_LIST=(("ping","ping"), ("dig", "dig") , ("whois", "whois"))

class ToolForm(forms.Form):
    tool = forms.ChoiceField(label='Tool:', choices=TOOLS_LIST)
    ip_address = forms.CharField(label = 'IP Addr', max_length=20)


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)