from django.test import TestCase

# Create your tests here.

class IndexPageTests(TestCase):
    def test_index_contains_Most_Liked_Characters(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'Most Liked Characters', response.content)

    def Test_using_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'ChaRate/index.html')

    def test_Image_Displayed(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'img src="/static/images', response.content)

    def title_is_included(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)

    def most_disscussed_char(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'Most Discussed Character:', response.content)

    def Search_Links(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'Charate/tvpage')
        self.assertTemplateUsed(response, 'Charate/movpage')
        self.assertTemplateUsed(response, 'Charate/character_browser')

    def nav_working_with_hidden_obj(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'Charate/add_mov')
        self.assertTemplateUsed(response, 'Charate/about')
        self.assertTemplateUsed(response, 'auth_logout')
        self.assertTemplateUsed(response, 'login')


    class AboutPageTests(TestCase):
        def title_is_included(self):
            response = self.client.get(reverse('about'))
            self.assertIn(b'<title>', response.content)
            self.assertIn(b'</title>', response.content)

        def test_about_using_template(self):
            response = self.client.get(reverse('about'))
            self.assertTemplateUsed(response, 'ChaRate/about.html')

        def test_about_contains_(self):
            response = self.client.get(reverse('about'))
            self.assertIn(b'This website has been created for our WAD2', response.content)
            self.assertIn(b'We can be contacted via email at the', response.content)


    #class  ModelTests(TestCase):


    class View_tests(TestCase):
        def test_login_using_template(self):
            response = self.client.get(reverse('login'))
            self.assertTemplateUsed(response, 'login')

        def test_logout_using_template(self):
            response = self.client.get(reverse('auth_logout'))
            self.assertTemplateUsed(response, 'auth_logout')

        def test_register_using_temp(self):
            response = self.client.get(reverse('registration_register'))
            self.assertTemplateUsed(response, 'registration_register')

        def test_character_using_temp(self):
            response = self.client.get(reverse('character'))
            self.assertTemplateUsed(response, 'ChaRate/character')




