import unittest
from htmlparser import htmlparser


class HTMLParserTest(unittest.TestCase):
    # test extraction of simple content
    def test_get_content_from_tags(self):
        tag_filter = {
            'name': 'div',
            'attrs': {
                'id': 'simple_test'
            }
        }
        content = htmlparser.get_content_from_tags(open('test/test.html').read(), tag_filter)
        self.assertTrue(content[0] == 'Test String')

    # test extraction of formatted content
    def test_get_formatted_content_from_tags(self):
        tag_filter = {
            'name': 'div',
            'attrs': {
                'id': 'formatting_test'
            }
        }
        content = htmlparser.get_formatted_text_from_tags(open('test/test.html').read(), tag_filter)
        self.assertTrue(content[0] == '  * one\n  * two\n\n')

    # test extraction of links
    def test_get_href_from_tags(self):
        tag_filter = {
            'name': 'div',
            'attrs': {
                'id': 'href_test'
            }
        }
        links = htmlparser.get_href_from_tags(open('test/test.html').read(), tag_filter)
        self.assertTrue(links == ['test1.com', 'test2.com'])

    # test extraction of attributes
    def test_get_attr_from_tags(self):
        tag_filter = {
            'name': 'div',
            'attrs': {
                'id': 'attr_test'
            },
            'type': 'name'
        }
        attributes = htmlparser.get_attr_from_tags(open('test/test.html').read(), tag_filter)
        self.assertEqual(attributes, ["div name"])


if __name__ == '__main__':
    unittest.main()
