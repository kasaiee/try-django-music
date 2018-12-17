from django import template

register = template.Library()


@register.filter
def date_splitter_1(date, separator='-'):
    return date.strftime(f'%Y{separator}%m{separator}%d')
    # return date.strftime('%Y{separator}%m{separator}%d'.format(separator=separator))

@register.filter
def render_rating(rating):
    html = '<fieldset class="rating">'
    for i in range(5, 0, -1):
        active = None
        if rating > i:
            active = 'style="color: #FFD700;"'
        html += f'''
        <input type="radio" id="star{i}" name="rating" value="{i}" /><label class = "full" {active} for="star{i}" title="Sucks big time - 1 star"></label>
        <input type="radio" id="starhalf" name="rating" value="half" /><label class="half" {active} for="starhalf" title="Sucks big time - 0.5 stars"></label>
        '''
    html += '</fieldset>'
    return html

