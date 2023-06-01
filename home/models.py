from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)

    content_panels = Page.content_panels + [FieldPanel("banner_title")]
