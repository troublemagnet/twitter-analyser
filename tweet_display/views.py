from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Graph
from .helper import grant_access, get_current_user, check_graphs

# Create your views here.


def index(request, oh_id=None):
    context = {'section': 'general', 'graph_section': True}
    if oh_id is not None:
        context['link_target'] = oh_id
    if grant_access(request, oh_id):
        context['oh_id'] = grant_access(request, oh_id)
        context['current_user_oh_id'] = get_current_user(request)
        graphs = ['overall_tweets', 'hourly_tweets', 'tweet_types']
        context['graphs'] = check_graphs(graphs, context['oh_id'])
        return render(request, 'tweet_display/index.html', context)
    else:
        return redirect('/users/')


def location(request, oh_id=None):
    context = {'section': 'location', 'graph_section': True}
    if oh_id is not None:
        context['link_target'] = oh_id
    if grant_access(request, oh_id):
        context['oh_id'] = grant_access(request, oh_id)
        context['current_user_oh_id'] = get_current_user(request)
        graphs = ['timeline', 'heatmap']
        context['graphs'] = check_graphs(graphs, context['oh_id'])
        return render(request, 'tweet_display/location.html', context)
    else:
        return redirect('/users/')


def interactions(request, oh_id=None):
    context = {'section': 'interactions', 'graph_section': True}
    if oh_id is not None:
        context['link_target'] = oh_id
    if grant_access(request, oh_id):
        context['oh_id'] = grant_access(request, oh_id)
        context['current_user_oh_id'] = get_current_user(request)
        graphs = ['gender_rt', 'gender_reply', 'top_replies']
        context['graphs'] = check_graphs(graphs, context['oh_id'])
        return render(request, 'tweet_display/interactions.html', context)
    else:
        return redirect('/users/')


def gender_rt(request, oh_id):
    if grant_access(request, oh_id):
        graph = Graph.objects.get(graph_type__exact='gender_rt',
                                  open_humans_member__oh_id=oh_id)
        return HttpResponse(graph.graph_data, content_type='application/json')
    else:
        return redirect('/users/')


def gender_reply(request, oh_id):
    if grant_access(request, oh_id):
        graph = Graph.objects.get(graph_type__exact='gender_reply',
                                  open_humans_member__oh_id=oh_id)
        return HttpResponse(graph.graph_data, content_type='application/json')
    else:
        return redirect('/users')


def hourly_tweets(request, oh_id):
    if grant_access(request, oh_id):
        graph = Graph.objects.get(graph_type__exact='hourly_tweets',
                                  open_humans_member__oh_id=oh_id)
        return HttpResponse(graph.graph_data, content_type='application/json')
    else:
        return redirect('/users/')


def tweet_types(request, oh_id):
    if grant_access(request, oh_id):
        graph = Graph.objects.get(graph_type__exact='tweet_types',
                                  open_humans_member__oh_id=oh_id)
        return HttpResponse(graph.graph_data, content_type='application/json')
    else:
        return redirect('/users/')


def top_replies(request, oh_id):
    if grant_access(request, oh_id):
        graph = Graph.objects.get(graph_type__exact='top_replies',
                                  open_humans_member__oh_id=oh_id)
        return HttpResponse(graph.graph_data, content_type='application/json')
    else:
        return redirect('/users/')


def heatmap(request, oh_id):
    if grant_access(request, oh_id):
        graph = Graph.objects.get(graph_type__exact='heatmap',
                                  open_humans_member__oh_id=oh_id)
        return HttpResponse(graph.graph_data, content_type='application/json')
    else:
        return redirect('/users/')


def timeline(request, oh_id):
    if grant_access(request, oh_id):
        graph = Graph.objects.get(graph_type__exact='timeline',
                                  open_humans_member__oh_id=oh_id)
        return HttpResponse(graph.graph_data, content_type='application/json')
    else:
        return redirect('/users/')


def overall_tweets(request, oh_id):
    if grant_access(request, oh_id):
        graph = Graph.objects.get(graph_type__exact='overall_tweets',
                                  open_humans_member__oh_id=oh_id)
        return HttpResponse(graph.graph_data, content_type='application/json')
    else:
        return redirect('/users/')
