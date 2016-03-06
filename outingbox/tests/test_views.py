from django.core.urlresolvers import reverse
from django.test import TestCase
from outingbox.utils.model_utils import get_fake_box, get_fake_category, get_fake_activity, get_fake_user_and_credentials, get_user_bookmarks, get_user_rating

def assert_base_templates(self, response):        
    self.assertTemplateUsed(response, 'components/base.html')
    self.assertTemplateUsed(response, 'components/nav-base.html')
    self.assertTemplateUsed(response, 'components/footer.html')
    self.assertTemplateUsed(response, 'account/login-modal.html')
    self.assertTemplateUsed(response, 'account/logout-modal.html')

class TestIndexView(TestCase):
    def setUp(self):
        self.url = reverse('index')
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_templates_used(self):
        assert_base_templates(self, self.response)
        self.assertTemplateUsed(self.response, 'outingbox/index.html')
        self.assertTemplateUsed(self.response, 'outingbox/featured.html')
        self.assertTemplateUsed(self.response, 'outingbox/collections.html')
        self.assertTemplateUsed(self.response, 'outingbox/categories.html')
        self.assertTemplateUsed(self.response, 'components/nav-main.html')

    def test_context(self):
        context = self.response.context
        self.assertIn('boxes', context)
        self.assertIn('featured', context)

class TestContactView(TestCase):
    def setUp(self):
        self.url = reverse('contact')
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_templates_used(self):
        assert_base_templates(self, self.response)
        self.assertTemplateUsed(self.response, 'outingbox/contact-us.html')
        self.assertTemplateUsed(self.response, 'components/nav-secondary.html')

    def test_context(self):
        context = self.response.context
        self.assertIn('form', context)
        self.assertNotIn('thanks', context)

class TestContactThanksView(TestCase):
    def setUp(self):
        self.url = reverse('feedback-thanks')
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_templates_used(self):
        assert_base_templates(self, self.response)
        self.assertTemplateUsed(self.response, 'outingbox/contact-us.html')
        self.assertTemplateUsed(self.response, 'components/nav-secondary.html')

    def test_context(self):
        context = self.response.context
        self.assertIn('thanks', context)
        self.assertNotIn('form', context)

class TestAboutView(TestCase):
    def setUp(self):
        self.url = reverse('about')
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_templates_used(self):
        assert_base_templates(self, self.response)
        self.assertTemplateUsed(self.response, 'outingbox/about-us.html')
        self.assertTemplateUsed(self.response, 'components/nav-secondary.html')

class TestActivityView(TestCase):
    def test_none_activity_id(self):
        url = '/activity/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_invalid_activity_id_character(self):
        url = '/activity/xyq/title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_invalid_activity_id_negative(self):
        url = '/activity/-1/title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_fake_activity(self):
        fake_activity = get_fake_activity()

        url = reverse('activity', kwargs={'id': fake_activity.id, 'title': fake_activity.title})
        response = self.client.get(url)

        assert_base_templates(self, response)
        self.assertTemplateUsed(response, 'activity/activity.html')

        self.assertEqual(response.status_code, 200)

        context = response.context
        self.assertEqual(context['activity'], fake_activity)
        self.assertEqual(len(context['reviews']), 0)
        self.assertEqual(context['bookmarks'], None)
        self.assertEqual(len(context['photos']), 0)
        self.assertEqual(context['user_rating'], 0)
        self.assertEqual(context['user_review'], None)

class TestBookmarkView(TestCase):
    def test_user_is_authenticated(self):
        url = reverse('bookmark')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)

    def test_activity_id_is_valid(self):
        url = reverse('bookmark')
        _, username, passwd = get_fake_user_and_credentials()
        self.client.login(username=username, password=passwd)

        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)

    def test_get_not_allowed(self):
        pass

    def test_bookmark_is_working(self):
        url = reverse('bookmark')
        user, username, passwd = get_fake_user_and_credentials()
        self.client.login(username=username, password=passwd)

        fake_activity = get_fake_activity()

        response = self.client.post(url, {'id': fake_activity.id})
        self.assertEqual(response.status_code, 200)

        self.assertIn(fake_activity, get_user_bookmarks(user))

class TestRatingView(TestCase):
    def test_user_is_authenticated(self):
        url = reverse('rate')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)

    def test_activity_id_is_valid(self):
        url = reverse('rate')
        _, username, passwd = get_fake_user_and_credentials()
        self.client.login(username=username, password=passwd)

        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)

    def test_invalid_rating(self):
        url = reverse('rate')
        user, username, passwd = get_fake_user_and_credentials()
        self.client.login(username=username, password=passwd)

        fake_activity = get_fake_activity()

        response = self.client.post(url, {'id': fake_activity.id, 'new_rating': -1})
        self.assertEqual(response.status_code, 400)

        response = self.client.post(url, {'id': fake_activity.id, 'new_rating': 6})
        self.assertEqual(response.status_code, 400)

        response = self.client.post(url, {'id': fake_activity.id, 'new_rating': 'xyz'})
        self.assertEqual(response.status_code, 400)

    def test_delete_rating_with_no_activity(self):
        pass

    def test_delete_rating_with_activity(self):
        pass

    def test_rating_is_working(self):
        url = reverse('rate')
        user, username, passwd = get_fake_user_and_credentials()
        self.client.login(username=username, password=passwd)

        fake_activity = get_fake_activity()

        response = self.client.post(url, {'id': fake_activity.id, 'new_rating': 3})
        self.assertEqual(response.status_code, 200)

        self.assertEqual(3, get_user_rating(user, fake_activity))

class TestBoxView(TestCase):
    def test_none_box_id(self):
        url = '/box/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_invalid_box_id_character(self):
        url = '/box/xyz/title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_invalid_box_id_negative(self):
        url = '/box/-1/title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_fake_box_with_no_activities(self):
        fake_box = get_fake_box()
        
        url = reverse('box', kwargs={'id': fake_box.id, 'title': fake_box.title})
        response = self.client.get(url)

        assert_base_templates(self, response)
        self.assertTemplateUsed(response, 'box/box.html')

        self.assertEqual(response.status_code, 200)

        context = response.context
        self.assertEqual(context['box'], fake_box)
        self.assertEqual(len(context['activities']), 0)
        self.assertEqual(context['url_next_page_number'], None)
        self.assertEqual(context['url_prev_page_number'], None)

    def test_fake_box_with_single_activity(self):
        fake_box = get_fake_box()
        fake_category = get_fake_category(fake_box)
        fake_activity = get_fake_activity(categories=[fake_category])

        url = reverse('box', kwargs={'id': fake_box.id, 'title': fake_box.title})
        response = self.client.get(url)        
        
        self.assertEqual(response.status_code, 200)

        context = response.context
        self.assertEqual(context['box'], fake_box)
        self.assertEqual(len(context['activities']), 1)
        self.assertEqual(context['activities'][0], fake_activity)
        self.assertEqual(context['url_next_page_number'], None)
        self.assertEqual(context['url_prev_page_number'], None)

    def test_fake_box_with_multiple_activities(self):
        fake_box = get_fake_box()
        fake_category = get_fake_category(fake_box)
        fake_activity_1 = get_fake_activity(categories=[fake_category])
        fake_activity_2 = get_fake_activity(categories=[fake_category])

        url = reverse('box', kwargs={'id': fake_box.id, 'title': fake_box.title})
        response = self.client.get(url)        
        
        self.assertEqual(response.status_code, 200)

        context = response.context
        self.assertEqual(context['box'], fake_box)
        self.assertEqual(len(context['activities']), 2)
        self.assertCountEqual(context['activities'], [fake_activity_1, fake_activity_2])
        self.assertEqual(context['url_next_page_number'], None)
        self.assertEqual(context['url_prev_page_number'], None)

    def test_fake_box_with_duplicate_activities(self):
        fake_box = get_fake_box()
        fake_category_1 = get_fake_category(fake_box)
        fake_category_2 = get_fake_category(fake_box)
        fake_activity = get_fake_activity(categories=[fake_category_1, fake_category_2])

        url = reverse('box', kwargs={'id': fake_box.id, 'title': fake_box.title})
        response = self.client.get(url)        
        
        self.assertEqual(response.status_code, 200)

        context = response.context
        self.assertEqual(context['box'], fake_box)
        self.assertEqual(len(context['activities']), 1)
        self.assertEqual(context['activities'][0], fake_activity)
        self.assertEqual(context['url_next_page_number'], None)
        self.assertEqual(context['url_prev_page_number'], None)

class TestSearchView(TestCase):
    def setUp(self):
        self.url = reverse('search')
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_templates_used(self):
        assert_base_templates(self, self.response)
        self.assertTemplateUsed(self.response, 'search/search.html')
        self.assertTemplateUsed(self.response, 'components/nav-secondary.html')
