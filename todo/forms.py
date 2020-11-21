from django import forms


def validate_len_input_name(value):
    if len(value) < 6:
        raise forms.ValidationError("Name must contain at lest 6 character")


def validate_len_input_description(value):
    if len(value) < 10:
        raise forms.ValidationError("Name must contain at lest 10 character")


class TodoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (field_name, field) in self.fields.items():
            if 'class' in field.widget.attrs:
                value = field.widget.attrs['class'] + 'form-control'
            else:
                value = 'form-control'
            field.widget.attrs['class'] = value

    def clean_bot_catcher(self):
        if len(self.cleaned_data['bot_catcher']):
            raise forms.ValidationError("This is a bot")

    name = forms.CharField(max_length=30, validators=(validate_len_input_name,))
    description = forms.CharField(max_length=100, widget=forms.Textarea(), validators=(validate_len_input_description,))
    bot_catcher = forms.CharField(widget=forms.HiddenInput, required=False, )
