from django.test import TestCase
from django.urls import reverse, resolve

from ..models import Board
from ..views import BoardsListView


class IndexTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('index')
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/boards/')

        self.assertEquals(view.func.view_class, BoardsListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})

        self.assertContains(self.response, f'href="{board_topics_url}"')