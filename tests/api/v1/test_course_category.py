
from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin


class CourseCategoryResourceTest(ResourceTestCaseMixin, TestCase):
    def setUp(self):
        super(CourseCategoryResourceTest, self).setUp()
        self.url = '/api/v1/coursetag/'

    # check get not allowed
    def test_get_not_found(self):
        self.assertHttpNotFound(self.api_client.get(self.url, format='json'))

    # check post not allowed
    def test_post_not_found(self):
        self.assertHttpNotFound(self.api_client.post(self.url,
                                                     format='json',
                                                     data={}))
