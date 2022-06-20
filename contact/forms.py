from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'phone':forms.TextInput(attrs={
                'class':'form-control'
            }),
             'mobile':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'company':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control'
            }),
            'date':forms.DateInput(attrs={
                'class':'form-control'
            }),
            'company':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'notes':forms.Textarea(attrs={
                'class':'form-control'
            }),
        
        }
    def clean_name(self):
        name=self.cleaned_data['name']
        if len(Contact.objects.filter(name=name))>0:
            raise forms.ValidationError(f"EL contacto {name} existe Elija Otro")
        else:
            return name
  
      