from unittest import TestCase

from command_executor.semantic_proximity import SemanticController


class TestSemanticController(TestCase):
    def test_get_closest(self):
        controller = SemanticController()
        pattern = controller.get_embedding('Тест шаблон')
        variants = [
            controller.get_embedding('Просто текст'),
            controller.get_embedding('Тестируем шаблон'),
            controller.get_embedding('Проверочный паттерн')
        ]

        closest, dist = controller.get_closest(pattern, variants)

        self.assertEqual(closest.sentence, 'Тестируем шаблон')
        self.assertLess(dist, 0.2)
