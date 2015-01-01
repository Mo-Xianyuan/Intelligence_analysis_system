#coding=utf-8
from django import forms  
from django.contrib.auth.models import User  
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput  

# 创建跟踪表单
class TrackCreationForm(forms.Form):
    symbol = forms.CharField(  
            required=True,  
            label=u"此跟踪的标识符",  
            error_messages={'required': u'请输入标识符'},  
            widget=forms.TextInput(  
                attrs={  
                    'placeholder':u"标志",  
                }  
            ),  
    ) 
    
    start_url = forms.CharField(  
            required=True,  
            label=u"起始URL",  
            error_messages={'required': u'请输入网站链接'},  
            widget=forms.TextInput(  
                attrs={  
                    'placeholder':u"网站",  
                }  
            ),  
    )    

    allowed_domain = forms.CharField(  
            required=True,  
            label=u"限定域名",  
            error_messages={'required': u'请输入域名'},  
            widget=forms.TextInput(  
                attrs={  
                    'placeholder':u"域名",  
                }  
            ),  
    )
    
    keywords = forms.ChoiceField(
        required=True,  
        label=u"信息类型的类型",
        choices=[
            ('auto.sohu.com/', u'汽车'),
            ('business.sohu.com/', u'经济'),
            ('it.sohu.com/', u'IT'),
            ('health.sohu.com/', u'健康'),
            ('sports.sohu.com/', u'体育'),
            ('travel.sohu.com/', u'旅游'),
            ('career.sohu.com/', u'职场'),
            ('cul.sohu.com/', u'cul'),
            ('house.sohu.com/', u'住房'),
            ('yule.sohu.com/', u'娱乐'),
            ('women.sohu.com/', u'女性'),
            ('media.sohu.com/', u'媒体'),
            ('gongyi.sohu.com/', u'公益'),]
    )
    #keywords = forms.CharField(  
    #        required=True,  
    #        label=u"信息类型的关键字",  
    #        error_messages={'required': u'请输入关键字'},  
    #        widget=forms.TextInput(  
    #            attrs={  
    #                'placeholder':u"关键字",  
    #            }  
    #        ),  
    #)
    
    def clean(self):  
        if not self.is_valid():  
            raise forms.ValidationError(u"请重新确认填写是否有误")  
        else:  
            cleaned_data = super(TrackCreationForm, self).clean()
