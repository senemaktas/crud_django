from django import forms
from .models import userModel


# creating a form
class userForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used , call the model
		model = userModel

		# specify fields to be used  or '__all__'
		fields = [
			"id",
			"name",
			"email",
			"phone", ]
    
	def __init__(self, *args, **kwargs):
		super(userForm,self).__init__(*args, **kwargs)
	    #self.fields['name'].empty_label = "Select"
		#self.fields['id'].required = True #zorunlu==True
