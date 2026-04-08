from django  import forms
from deploy_app.models import employee
class emp_form(forms.ModelForm):
    class Meta:
        model=employee
        fields="__all__"