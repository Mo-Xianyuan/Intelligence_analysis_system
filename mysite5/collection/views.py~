#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext 
from django.utils import timezone

from collection.models import user_behavior
from WebPage.models import webpage, Favour
from collection.models import user_behavior
from django.contrib.auth.models import User 
import math

def create_user_item_list():
    user_items = []
    for record in user_behavior.objects.all():
        user_items.append([record.user_id, record.link_id])
    return user_items

# 建立用户-物品表，该表索引为用户，值为用户产生过行为的物品集合
def create_user_items():
    user_items = dict()
    for record in user_behavior.objects.all():
        if record.user_id not in user_items:
             user_items[record.user_id] = set()
        user_items[record.user_id].add(record.link_id)
   
    return user_items

# 建立物品-用户表，该表索引为物品，值为用户产生过行为的用户集合
def create_item_users():
    item_users = dict()
    for record in user_behavior.objects.all():
        if record.link_id not in item_users:
             item_users[record.link_id] = set()
        item_users[record.link_id].add(record.user_id)
   
    return item_users

def UserSimilarity():
    item_users = create_item_users()
    print item_users  

    C = dict()
    N = dict()
    for i, users in item_users.items():
        for u in users:
            if u not in N:
                N[u] = 1
            else:
                N[u] += 1
            for v in users:
                if u == v:
                    continue
                if u not in C:
                    C[u] = dict()
                if v not in C[u]:
                    C[u][v] = 0
                C[u][v] += 1 / math.log(1 + len(users))

    W = dict()
    for u, releated_users in C.items():
        for v, cuv in releated_users.items():
            if u not in W:
                W[u] = dict()
            W[u][v] = cuv / math.sqrt(N[u] * N[v])
    return W
    
def recommended(request):
    W = UserSimilarity()
    username = request.user.username
    favours = Favour.objects.filter(user=request.user) 

    if W:
        user_items = create_user_items()
        item_users = create_item_users()

        u_id = User.objects.get(username=username).pk
        
        print W[u_id]
        Wu = sorted(W[u_id].iteritems(), key=lambda d:d[1], reverse = True)

        recommendation = []
        # 选了相似度最高的用户v
        vid = Wu[0][0]  
        for i in user_items[vid]:
            if u_id not in item_users[i]:
                page = webpage.objects.get(pk=i)
                recommendation.append(page)    
       
        return render_to_response('recommendation.html', 
            RequestContext(request, {'mypages': recommendation, 
                                     'username': username, 
                                     'favours':favours}))
    else:
        # 对于还没有点击任何链接的新用户,进行随机推荐
        print "p3"
        recommendation = webpage.objects.all().order_by('?')[0:10]
        return render_to_response('recommendation.html', 
            RequestContext(request, {'mypages': recommendation, 
                                     'username': username, 
                                     'favours':favours}))
        
def mark_down(request):
    if request.method == 'GET':
        user = request.user.username
        link = request.GET.get('link', '')

        user_obj = request.user        
        web_obj = webpage.objects.get(link=link)        
                
        ub = user_behavior(user=user_obj, link=web_obj, time = timezone.now())
        ub.save()

        return HttpResponse(u'收集信息')
