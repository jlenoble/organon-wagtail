from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail import blocks
from wagtail.fields import StreamField

from wagtail.admin.panels import FieldPanel, InlinePanel


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

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        InlinePanel("subtasks", label="Subtasks"),
    ]


class Subtasks(Orderable):
    page = ParentalKey("tasks.TaskDetailPage", related_name="subtasks")
    task = models.ForeignKey(
        "tasks.TaskDetailPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [FieldPanel("task")]
