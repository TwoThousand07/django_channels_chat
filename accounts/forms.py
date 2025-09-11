from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreationForm(forms.ModelForm):
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Enter Password again', widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('email', 'phone_number')

    def clean_password2(self):
      '''Проверка паролей на совпадение'''
      password1 = self.cleaned_data.get('password1')
      password2 = self.cleaned_data.get('password2')

      if password1 and password2 and password1 != password2:
        raise ValidationError("Passwords don't match")
      
      def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
          user.save()
        return user