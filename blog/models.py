from wagtail.models import Page
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from wagtail.admin.panels import FieldPanel


class BlogIndexPage(Page):
    max_count = 1
    subpage_types = ["blog.BlogPostPage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["blog_posts"] = BlogPostPage.objects.live()
        return context


class BlogPostPage(Page):
    parent_page_types = ["blog.BlogIndexPage"]

    body = StreamField(
        [
            (
                "title",
                blocks.CharBlock(
                    form_classname="full title", template="blocks/title_block.html"
                ),
            ),
            ("richtext", blocks.RichTextBlock()),
            ("image", ImageChooserBlock(template="blocks/image_block.html")),
        ],
        use_json_field=True,
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [FieldPanel("body")]
