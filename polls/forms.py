from django import forms
from .models import Question


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text"]

    def save(self, commit=True):
        instance = super(AddQuestionForm, self).save(commit=False)
        instance.field1 = "Modified Value"

        if commit:
            instance.save()

        return instance
