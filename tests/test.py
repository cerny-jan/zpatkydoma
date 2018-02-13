from django.core.management import call_command
from django.test import TestCase
from wagtail.wagtailcore.models import Page
from zpatkydoma.blog.models import BlogPage, BlogTagPage


class ZpatkydomaTest(TestCase):

    @classmethod
    def setUpTestData(self):
        call_command('load_test_data')

    def test_blog_page(self):
        blog_page_with_3 = BlogPage.objects.get(
            slug='blabotovy-rozumy-ceske-lorem-ipsum')
        blog_page_with_2 = BlogPage.objects.get(
            slug='where-does-it-come-where-can-i-get-some')
        self.assertEqual(blog_page_with_3.related_pages.all().count(), 3)
        self.assertEqual(blog_page_with_3.related_pages_columns(), 4)
        self.assertEqual(blog_page_with_2.related_pages.all().count(), 2)
        self.assertEqual(blog_page_with_2.related_pages_columns(), 6)

    def test_blog_tag_page(self):
        blog_tag_page = BlogTagPage.objects.get(slug='tags')
        # test tag page without passing any tag
        response = self.client.get(blog_tag_page.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['searched_tag'])
        self.assertEqual(len(response.context['blogpages']), 3)
        # test tag page passing tag 'english'
        tag = 'english'
        response = self.client.get(blog_tag_page.url, {'tag': tag})
        self.assertEqual(response.status_code, 200)
        # this should test friendly tag name
        # self.assertContains('english', response.context['searched_tag'])
        self.assertEqual(len(response.context['blogpages']), 1)
        # for page in response.context['blogpages']:
        #     self.assertIn(tag, page.tags.all())
