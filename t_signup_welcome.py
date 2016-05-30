import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "askdjango.settings")
import django
django.setup()

members = ['철수', '영희', '밥', '스티브']
params = {
    'name': '이진석',
    'group_name': 'AskDjango',
    'members_count': len(members),
    'members': members,
    'site_url': 'http://facebook.com/askdjango/',
}

from django.template.loader import render_to_string

welcome_content = render_to_string('blog/signup_welcome.txt', params)

print(welcome_content)

# render(request, 블라블라)  # HttpResponse

