from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Group


@login_required
def home_view(request):
    groups = Group.objects.all()
    user = request.user

    return render(request, template_name='chat/home.html', context={'groups': groups, 'user': user})

@login_required
def group_chat_view(request, uuid):
    group = get_object_or_404(Group, uuid=uuid)
    if not group.members.filter(id=request.user.id).exists():
        return HttpResponseForbidden('You are not member of this group')
    
    messages = group.message_set.all()
    events = group.event_set.all()

    message_and_event_list = [*messages, *events]
    sorted_message_and_event_list = sorted(message_and_event_list, key=lambda x: x.timestamp)

    group_members = group.members.all()

    return render(request, template_name='chat/groupchat.html', context={'message_and_event_list': sorted_message_and_event_list, 'group_members': group_members})