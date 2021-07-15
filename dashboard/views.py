import os
from django.shortcuts import render
from googleAdsDashboard import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages  # import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render


TEMPLATE_DIR_WEBSITE = os.path.join(settings.TEMPLATES_DIR)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):

    return render(request, os.path.join(TEMPLATE_DIR_WEBSITE, 'index.html'))