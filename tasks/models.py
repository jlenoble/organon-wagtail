from wagtail.models import Page
from wagtail import blocks
from wagtail.fields import StreamField

from wagtail.admin.panels import FieldPanel


class TaskIndexPage(Page):
    max_count = 1
    subpage_types = ["tasks.TaskDetailPage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["tasks"] = TaskDetailPage.objects.live()
        return context


class TaskDetailPage(Page):
    parent_page_types = ["tasks.TaskIndexPage"]

    body = StreamField(
        [
            (
                "title",
                blocks.CharBlock(
                    form_classname="full title", template="blocks/title_block.html"
                ),
            ),
            ("richtext", blocks.RichTextBlock()),
        ],
        use_json_field=True,
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [FieldPanel("body")]
