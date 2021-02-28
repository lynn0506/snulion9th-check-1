from django.shortcuts import redirect, render
from tag.models import Tag
from feedpage.models import Feed
from django.http import JsonResponse

# Create your views here.
class TagView:
    def create(request):
        content = request.POST.get('content', '')
        tag = Tag.objects.create(content=content)
        return JsonResponse({'tagId':tag.id});

    def read(request, id):
        tag = Tag.objects.get(id=id)
        feeds = Feed.objects.filter(tags=tag)
        return render(request, 'tag/detail.html', {'tag': tag, 'feeds': feeds})
        
    def update(request, id):
        tag = Tag.objects.get(id=id)
        tag.content = request.POST['content']
        tag.save()
        return render(request, 'tag/detail.html', {'tag': tag})
        
    def delete(request, id):
        tag = Tag.objects.get(id=id)
        tag.delete()
        return redirect('feedpage:index')
