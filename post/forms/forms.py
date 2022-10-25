from django import forms
from django.forms import TextInput

from ..models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content')
        #agregar clases al label
        widgets = {
            'title': TextInput(attrs={'class': 'input is-primary m-5',
                                          'placeholder': 'e.g. Learn Python'}),
                                    

                      
            'content': TextInput(attrs={'class': 'textarea is-primary m-5 is-medium',
                                        'placeholder': 'type your content here'
                                        }),
                                        
                                    
                                

        }

       