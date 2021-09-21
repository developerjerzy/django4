from django.test import TestCase
from myfinishproject.bboard import models


class BbModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Bb.object.create(
            title='Bike',
            content='good look',
            price='200',
            phone='+375000000000'
        )

    def test_title_label(self):
        title_example = Bb.object.get(id=1)
        field_label = title_example._meta.get.field('title').verbose.name
        self.assertEqual(field_label, 'title')
