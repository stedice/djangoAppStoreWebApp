from django.test import TestCase

# Create your tests here.

from appStore.models import App
from django.core.urlresolvers import reverse

class AppListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 apps for pagination tests
        number_of_apps = 13
        for app_num in range(number_of_apps):
            App.objects.create(name='Foo %s' % app_num, description = 'Bar %s' % app_num, platform = 'a')
    
    def test_view_url_exists_at_desired_location(self):
        print("Method: test_view_url_exists_at_desired_location.")
        resp = self.client.get('/appStore/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        print("Method: test_view_url_accessible_by_name.")
        resp = self.client.get(reverse('appStore:index'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        print("Method: test_view_uses_correct_template.")
        resp = self.client.get(reverse('appStore:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'appStore/base.html')
        self.assertTemplateUsed(resp, 'appStore/index.html')
  
    def test_pagination_is_ten(self):
        print("Method: test_pagination_is_ten.")
        resp = self.client.get(reverse('appStore:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['object_list']) == 10)

    def test_lists_all_apps(self):
        print("Method: test_lists_all_apps.")
        resp = self.client.get(reverse('appStore:index')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['object_list']) == 3)

