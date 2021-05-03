from django.test import TestCase, Client
from fitapp.models import User, Logs, Profile, Comment
from django.contrib.auth.models import User
import fitapp.views as views

# Create your tests here.
class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
        self.logs_1 = Logs.objects.create(exercise="running", date="2021-04-11", duration="30", intensity="moderate")
        testuser = User.objects.create(username="test10", email="test10@gmail.com")
        self.comments_1 = Comment.objects.create(name="test", post=self.logs_1, body="test", created_on="2021-04-11", active=True)
        self.c = Client()
        adminuser = User.objects.create_superuser(username='b-08-admin2')

    def test_log(self):
        Test = self.logs_1
        print(Test.__str__())
        self.assertEqual(Test.__str__(), "2021-04-11" + ":" + "running" + "\n")

    def test_comment(self):
        Test = self.comments_1
        print(Test.__str__())
        self.assertEqual(Test.__str__(), "Comment test by test")

    def test_hometab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/').status_code, 200)

    def test_profiletab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/fitapp/progress/').status_code, 302)

    def test_logstab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/fitapp/Logs/').status_code, 302)
    
    def test_viewlogstab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/fitapp/viewLogs/').status_code, 302)

    def test_achievementstab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/fitapp/achievements/').status_code, 302)

    def test_leaderboardtab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/fitapp/leaderboard/').status_code, 302)

    def test_hometab_afterlogin(self):
        TestClient = self.c
        TestAdmin = self.adminuser
        TestClient.force_login(TestAdmin)
        self.assertEqual(Test.get('/').status_code, 200)

