from bs4 import BeautifulSoup


# get unformatted text content from all the html tags in the html string that satisfy the tag_filter condition
def get_content_from_tags(html_string, tag_filter):
    soup = BeautifulSoup(html_string, 'html.parser')
    tag_content = []
    for tag in soup.findAll(name=tag_filter['name'], attrs=tag_filter['attrs']):
        tag_content.append(tag.get_text())

    return tag_content
