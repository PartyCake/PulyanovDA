from django.test import TestCase
from .models import Member
import datetime

# Create your tests here.
class MemberTestCase(TestCase):
    def setUp(self):
        Member.objects.create(
                                first_name='Lionel',
                                last_name='Messi',
                                mobile_number='80291879913',
                                email='leomessi10@gmail.com',
                                registration_date='2010-06-16',
                                registration_upto='2020-06-16',
                                dob='2000-06-16',
                                subscription_type='gym',
                                subscription_period='1',
                                amount='500',
                                fee_status='paid',
                                batch='morning',
                                notification='0'
                            )

    def test_member(self):
        check = Member.objects.get(first_name='Lionel')
        print(check)
