from django.core.management import call_command
from django.test import TestCase
from wagtail.wagtailcore.models import Page
from zpatkydoma.blog.models import BlogPage, BlogTagPage, BlogListPage
from zpatkydoma.base.models import HomePage


class ZpatkydomaTest(TestCase):

    @classmethod
    def setUpTestData(self):
        call_command('load_test_data')

    def test_blog_page(self):
        # get blog page with 3 related posts
        blog_page_with_3 = BlogPage.objects.get(
            slug='blabotovy-rozumy-ceske-lorem-ipsum')
        # get blog page with 2 related posts
        blog_page_with_2 = BlogPage.objects.get(
            slug='where-does-it-come-where-can-i-get-some')
        self.assertEqual(blog_page_with_3.related_pages.all().count(), 3)
        self.assertEqual(blog_page_with_3.related_pages_columns(), 4)
        self.assertEqual(blog_page_with_2.related_pages.all().count(), 2)
        self.assertEqual(blog_page_with_2.related_pages_columns(), 6)

    def test_blog_tag_page(self):
        blog_tag_page = BlogTagPage.objects.get(slug='tags')
        # test tag page without passing any tag - should return all live pages
        response = self.client.get(blog_tag_page.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['searched_tag'])
        self.assertEqual(len(response.context['blogpages']), 6)
        # test tag page passing tag 'jablecne-rohlicky'
        tag = 'jablecne-rohlicky'
        response = self.client.get(blog_tag_page.url, {'tag': tag})
        self.assertEqual(response.status_code, 200)
        # this should test friendly tag name
        self.assertEqual('Jablečné rohlíčky',
                         response.context['searched_tag'].name)
        self.assertEqual(len(response.context['blogpages']), 1)
        for page in response.context['blogpages']:
            self.assertIn(tag, [tag.slug for tag in page.tags.all()])

    def test_blog_list_page(self):
        blog_list_page = BlogListPage.objects.get(slug='o-cesku')
        # check if post per page is 5 (total number of live blog posts is 6)
        self.assertEqual(blog_list_page.posts_per_page, 5)
        response = self.client.get(blog_list_page.url)
        # if no page spcified paginator should return first page with 5 posts
        self.assertEqual(response.context['blogpages'].number, 1)
        self.assertEqual(len(response.context['blogpages']), 5)
        # paginator should return page spcified in parameter page
        response = self.client.get(blog_list_page.url, {'page': 2})
        self.assertEqual(response.context['blogpages'].number, 2)
        self.assertEqual(len(response.context['blogpages']), 1)
        # if page out of range, paginator should return last page -> page 2 wiht 1 blog post should be returned
        response = self.client.get(blog_list_page.url, {'page': 999})
        self.assertEqual(response.context['blogpages'].number, 2)
        self.assertEqual(len(response.context['blogpages']), 1)

    def test_home_page(self):
        home_page = HomePage.objects.first()
        self.assertEqual(home_page.posts_per_page, 25)
        # if no page spcified paginator should return first page with 5 posts (6 is available, 1 has to be promo)
        # promo post is not included in paginator and will be the same on all paginated pages for homepage
        response = self.client.get(home_page.url)
        self.assertEqual(response.context['blogpages'].number, 1)
        self.assertEqual(len(response.context['blogpages']), 5)
        # if page out of range, paginator should return last page, in this it is also first page
        response = self.client.get(home_page.url, {'page': 2})
        self.assertEqual(response.context['blogpages'].number, 1)
        self.assertEqual(len(response.context['blogpages']), 5)
