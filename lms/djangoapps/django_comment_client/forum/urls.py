from django.conf.urls.defaults import url, patterns
import django_comment_client.forum.views

urlpatterns = patterns('django_comment_client.forum.views',
    url(r'users/(?P<user_id>\w+)/following$', 'following_threads', name='following_threads'),
    url(r'users/(?P<user_id>\w+)$', 'user_profile', name='user_profile'),
    url(r'(?P<discussion_id>[\w\-]+)/threads/(?P<thread_id>\w+)$', 'single_thread', name='single_thread'),
    url(r'(?P<discussion_id>[\w\-]+)/inline$', 'inline_discussion', name='inline_discussion'),
    url(r'', 'forum_form_discussion', name='forum_form_discussion'),
)
