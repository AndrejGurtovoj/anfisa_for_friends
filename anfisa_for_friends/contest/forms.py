from django import forms


class ContestForm(forms.Form):
    title = forms.CharField(max_length=20, required=True, label='Название')
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        required=True,
        label='Описание'
    )
    price = forms.IntegerField(
        min_value=10,
        max_value=100,
        required=True,
        label='Цена',
        help_text='Рекомендованная розничная цена'
    )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        required=False,
        label='Комментарий'
    )
