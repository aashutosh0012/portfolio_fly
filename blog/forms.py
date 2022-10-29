from django import forms
from .models import Post, Tag

class createPostForm(forms.ModelForm):
	# summary	= forms.CharField(label='A short summary', required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
	# summary	= forms.CharField(label='A short summary', required=False)
	class Meta:
		model = Post
		fields = ('title',"body",'tag','summary')
		tag = forms.ModelChoiceField(queryset=Tag.objects.all())
		widgets = {
			'title'		: forms.TextInput(attrs={'class':'form-control'}),
			'body'		: forms.Textarea(attrs={'class':'form-control'}),
			'tag'		: forms.SelectMultiple(attrs={'class':'form-control'}),
			'summary'	: forms.TextInput(attrs={'class':'form-control'}),
		}


class editPostForm(forms.ModelForm):
	# summary	= forms.CharField(label='A short summary', required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
	# summary	= forms.CharField(label='A short summary', required=False)
	class Meta:
		model = Post		
		fields = ('title',"body",'tag','summary')
		tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
		widgets = {
			'title'		: forms.TextInput(attrs={'class':'form-control'}),
			'body'		: forms.Textarea(attrs={'class':'form-control'}),
			'tag'		: forms.SelectMultiple(attrs={'class':'form-control'}),
			'summary'	: forms.Textarea(attrs={'class':'form-control'}),
		}