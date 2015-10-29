from bs4 import BeautifulSoup
import html2text


# get unformatted text content from all the html tags in the html string that satisfy the tag_filter condition
def get_content_from_tags(html_string, tag_filter):
    soup = BeautifulSoup(html_string, 'html.parser')
    tag_content = []
    for tag in soup.findAll(name=tag_filter['name'], attrs=tag_filter['attrs']):
        tag_content.append(tag.get_text())

    return tag_content


# get formatted text from all the html tags in the html string that satisfy the tag_filter condition
# maintains the structure of the extracted text
def get_formatted_text_from_tags(html_string, tag_filter):
    soup = BeautifulSoup(html_string, 'html.parser')
    tag_content = []
    for element in soup.findAll(name=tag_filter['name'], attrs=tag_filter['attrs']):
        tag_content.append(html2text.HTML2Text().handle(str(element)))

    return tag_content


# get all links from all the html tags in the html string that satisfy the tag_filter condition
def get_href_from_tags(html_string, tag_filter):
    soup = BeautifulSoup(html_string, 'html.parser')
    links = []
    for element in soup.findAll(name=tag_filter['name'], attrs=tag_filter['attrs']):
        for a in element.findAll('a'):
            links.append(a.attrs['href'])

    return links


# get specific attributes from all the html tags in the html string that satisfy the tag_filter condition
def get_attr_from_tags(html_string, tag_filter):
    soup = BeautifulSoup(html_string, 'html.parser')
    attr = []
    for element in soup.findAll(name=tag_filter['name'], attrs=tag_filter['attrs']):
        attr.append(element.attrs[tag_filter['type']])

    return attr
