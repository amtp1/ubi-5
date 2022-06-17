import re
from json import dumps
from datetime import datetime as dt
from datetime import timedelta

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView

from .models import *


class API:
    class CreateUser(ListAPIView):
        serializer_class: UserProfile = UserProfile

        def get(self, request: HttpRequest, user_id: int, username: str, first_name: str, last_name: str):
            user = UserProfile.objects.filter(user_id=user_id)
            if not user.exists():
                UserProfile.objects.create(
                    user_id=user_id, username=username, first_name=first_name, last_name=last_name)
            return HttpResponse(dumps({"response": True}), content_type='application/json')

    class RunAttack(ListAPIView):
        serializer_class = Attack

        def get(self, request: HttpRequest, user_id: int, phone: int):
            attack = Attack.objects.filter(user_id=user_id, phone=phone)
            if not attack.exists():
                return self.create_new_attack(user_id=user_id, phone=phone)
            else:
                attack = attack.first()
                if attack.is_run:
                    return HttpResponse(dumps({"id": ""}), content_type='application/json')
                else:
                    return self.create_new_attack(user_id=user_id, phone=phone)

        def create_new_attack(self, user_id: int, phone: int):
            new_attack = Attack.objects.create(user_id=user_id, phone=phone)
            attack_id = re.sub("-", "", str(new_attack.pk))[:7]
            return HttpResponse(dumps({"id": attack_id, "uuid": str(new_attack.pk)}), content_type='application/json')

    class StopAttack(ListAPIView):
        serializer_class = Attack

        def get(self, request: HttpRequest, pk: str):
            attack = Attack.objects.filter(pk=pk).get()
            attack.is_run = False
            attack.save()
            return HttpResponse(dumps({"response": True}), content_type='application/json')

    class Statistic(ListAPIView):
        serializer_class: UserProfile = UserProfile

        def get(self, request: HttpRequest):
            return HttpResponse(dumps({"statistic": self.generate_statistic()}))

        def generate_statistic(self):
            today = dt.today()
            last_day = today - timedelta(days=1)
            all_users = len(UserProfile.objects.all())
            last_login_users = len(UserProfile.objects.filter(
                last_login__range=(last_day, today)))
            return dict(all_users=all_users, last_login_users=last_login_users)


class Web:
    def index(request):
        return render(request, "index.html")
