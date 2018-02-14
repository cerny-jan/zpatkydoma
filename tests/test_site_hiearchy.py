from wagtail.tests.utils import WagtailPageTests
from zpatkydoma.blog.models import BlogPage, BlogListPage, BlogTagPage
from zpatkydoma.base.models import StandardPage, HomePage
from wagtail.wagtailcore.models import Page

class HiearchyTest(WagtailPageTests):

    def test_blog_page_can_create_under_blog_list_page(self):
        self.assertCanCreateAt(BlogListPage, BlogPage)

    def test_blog_page_cant_create_under_blog_tag_page(self):
        self.assertCanNotCreateAt(BlogTagPage, BlogPage)

    def test_blog_page_cant_create_under_standard_page(self):
        self.assertCanNotCreateAt(StandardPage, BlogPage)

    def test_blog_page_cant_create_under_home_page(self):
        self.assertCanNotCreateAt(HomePage, BlogPage)

    def test_blog_page_cant_create_under_blog_page(self):
        self.assertCanNotCreateAt(BlogPage, BlogPage)

    def test_blog_list_page_can_create_under_home_page(self):
        self.assertCanCreateAt(HomePage, BlogListPage)

    def test_blog_list_page_cant_create_under_blog_page(self):
        self.assertCanNotCreateAt(BlogPage, BlogListPage)

    def test_blog_list_page_cant_create_under_standard_page(self):
        self.assertCanNotCreateAt(StandardPage, BlogListPage)

    def test_blog_list_page_cant_create_under_blog_tag_page(self):
        self.assertCanNotCreateAt(BlogTagPage, BlogListPage)

    def test_blog_list_page_cant_create_under_blog_list__page(self):
        self.assertCanNotCreateAt(BlogListPage, BlogListPage)

    def test_blog_tag_page_can_create_under_home_page(self):
        self.assertCanCreateAt(HomePage, BlogTagPage)

    def test_blog_tag_page_cant_create_under_standard_page(self):
        self.assertCanNotCreateAt(StandardPage, BlogTagPage)

    def test_blog_tag_page_cant_create_under_blog_page(self):
        self.assertCanNotCreateAt(BlogPage, BlogTagPage)

    def test_blog_tag_page_cant_create_under_blog_tag_page(self):
        self.assertCanNotCreateAt(BlogTagPage, BlogTagPage)

    def test_home_page_can_create_under_root_page(self):
        self.assertCanCreateAt(Page, HomePage)

    def test_home_page_cant_create_under_blog_tag_page(self):
        self.assertCanNotCreateAt(BlogTagPage, HomePage)

    def test_home_page_cant_create_under_blog_list_page(self):
        self.assertCanNotCreateAt(BlogListPage, HomePage)

    def test_home_page_cant_create_under_blog_page(self):
        self.assertCanNotCreateAt(BlogPage, HomePage)

    def test_home_page_cant_create_under_standard_page(self):
        self.assertCanNotCreateAt(StandardPage, HomePage)
