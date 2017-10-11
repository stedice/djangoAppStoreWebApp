from django.test import TestCase
from appStore.models import App


class AppModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        App.objects.create(name='appname', description='appdescription', platform='a')

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_name_label(self):
        print("Method: test_name_label.")
        app=App.objects.get(id=1)
        field_label = app._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_description_label(self):
        print("Method: test_description_label.")
        app=App.objects.get(id=1)
        field_label = app._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'description')

    def test_platform_label(self):
        print("Method: test_platform_label.")
        app=App.objects.get(id=1)
        field_label = app._meta.get_field('platform').verbose_name
        self.assertEquals(field_label,'platform')

    def test_created_label(self):
        print("Method: test_created_label.")
        app=App.objects.get(id=1)
        field_label = app._meta.get_field('created_at').verbose_name
        self.assertEquals(field_label,'created at')

    def test_name_max_length(self):
        print("Method: test_name_max_length.")
        app=App.objects.get(id=1)
        max_length = app._meta.get_field('name').max_length
        self.assertEquals(max_length,50)

    def test_description_max_length(self):
        print("Method: test_description_max_length.")
        app=App.objects.get(id=1)
        max_length = app._meta.get_field('description').max_length
        self.assertEquals(max_length,200)

    def test_platform_max_length(self):
        print("Method: test_description_max_length.")
        app=App.objects.get(id=1)
        max_length = app._meta.get_field('platform').max_length
        self.assertEquals(max_length,1)

    def test_created_auto_now_add(self):
        print("Method: test_description_max_length.")
        app=App.objects.get(id=1)
        auto_now_add = app._meta.get_field('created_at').auto_now_add
        self.assertEquals(auto_now_add, True)

    def test_object_str_is_name_slash_platform(self):
        print("Method: test_object_str_is_name.")
        app=App.objects.get(id=1)
        expected_object_name = '%s/%s' % (app.name, app.platform)
        self.assertEquals(expected_object_name,str(app))

    def test_get_absolute_url(self):
        print("Method: test_get_absolute_url.")
        app=App.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(app.get_absolute_url(),'/appstore/1/')

