#coding=utf-8
from django.shortcuts import render
from WebPage.forms import TrackCreationForm
from django.shortcuts import render_to_response
from django.template.context import RequestContext 
from django.http import HttpResponse, HttpResponseRedirect
from WebPage.models import Website, Favour
from urllib2 import Request, urlopen, URLError, HTTPError

def website_valid(someurl): 
    req = Request(someurl)
    try:
        response = urlopen(req)
    except Exception:
        return False
    else:
        # everything is fine
        return True

#根据网页获取allowed_domain,爬虫部分需要使用
import re
def get_allowed_domain(url):
    return re.findall('https?://(.*)/', url)[0]
    
def create(request):
    if request.method == 'GET':  
        form = TrackCreationForm()  
        return render_to_response('create.html', 
               RequestContext(request, {'form': form,'username': request.user.username }))  
    else:
        flag = False  
        form = TrackCreationForm(request.POST)  
        if form.is_valid():
            try:
                start_url = request.POST.get('start_url', '')
                allowed_domain = request.POST.get('allowed_domain', '')
                website = Website.objects.get(allowed_domain=allowed_domain)
            except Website.DoesNotExist:
                website = Website(start_url = start_url, allowed_domain = allowed_domain, user=request.user)
                if website_valid(start_url):
                    website.save()
                else:
                    return HttpResponse(u'网站地址链接有误，创建失败')
            else:
                pass
            symbol = request.POST.get('symbol','')
            keywords = request.POST.get('keywords','')
            try:
                favours_set = Favour.objects.filter(user=request.user)
            except Favour.DoesNotExist:
                flag = True
            else:
                pass
            
            has_this_favour = False
            for favour in favours_set:
                if favour.symbol == symbol:
                    has_this_favour = True

            if flag or not has_this_favour:
                favour = Favour(symbol=symbol,
                                keywords=keywords,
                                user=request.user)
                favour.save()
            return render_to_response('create_success.html', RequestContext(request))
