from django.shortcuts import render
from .models import Feed, Comment, Like
from django.shortcuts import redirect
from tag.models import Tag
from django.http import JsonResponse

def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        tags = Tag.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds, 'tags': tags})
    
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        feed = Feed.objects.create(title=title, content=content, author=request.user)
        for tag_id in request.POST.getlist('tags'):
            feed.tags.add(tag_id)
        return redirect('feedpage:index')
    
def new(request):
    tags = Tag.objects.all()
    return render(request, 'feedpage/new.html', {'tags': tags})

def show(request, id):
    feed = Feed.objects.get(id=id)
    tags = Tag.objects.filter(feeds=feed)
    return render(request, 'feedpage/show.html', {'feed': feed, 'tags': tags})

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return JsonResponse({});

def edit(request, id):
    if request.method == 'GET':
        feed = Feed.objects.get(id=id)
        tags = Tag.objects.all()
        return render(request, 'feedpage/edit.html', {'feed': feed, 'tags': tags})
    
    elif request.method == 'POST':
        feed = Feed.objects.get(id=id)
        feed.title=request.POST['title']
        feed.content=request.POST['content']
        feed.save()
        
        feed.tags.clear()
        for tag_id in request.POST.getlist('tags'): 	# 추가
            feed.tags.add(tag_id)
        return redirect(f'/feeds/{id}')
    
    
class CommentView:
    def create(request, id):
        content = request.POST['content']
        comment = Comment.objects.create(feed_id=id, content=content, author=request.user)
        return JsonResponse({'commentId': comment.id})
        
    def delete(request, id, cid):
        c = Comment.objects.get(id=cid)
        c.delete()
        return JsonResponse({})     
class LikeView:
    def create(request, id):
        feed = Feed.objects.get(id=id)
        like_list = feed.like_set.filter(user=request.user)
        if like_list.count() > 0:
            feed.like_set.get(user_id=request.user.id).delete()
        else:
            Like.objects.create(user=request.user, feed=feed)
        return JsonResponse({'feedLikeCount': feed.like_set.count(), 'userLikeCount': request.user.like_feeds.count()})
