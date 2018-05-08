from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    RawHTMLBlock,
    ListBlock,
    StaticBlock
)


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    caption = CharBlock(blank=True, required=False)

    class Meta:
        icon = 'image'
        template = 'blocks/image_block.html'
        label = 'Image'


class SimpleImageBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    caption = CharBlock(blank=True, required=False)

    class Meta:
        icon = 'image'


class SliderImageBlock(StructBlock):
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = 'image'


class QuoteBlock(StructBlock):
    text = TextBlock(required=False)
    author = CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        icon = 'openquote'
        template = 'blocks/quote_block.html'
        label = 'Quote'


class HeadingBlock(StructBlock):
    heading_text = CharBlock(required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('title-small', 'Small'),
        ('title-med', 'Medium'),
        ('title-large', 'Large'),
        ('title-extra-large', 'Extra Large')
    ], blank=True, required=False)

    class Meta:
        icon = 'title'
        template = 'blocks/heading_block.html'
        label = 'Heading'


class BaseStreamBlock(StreamBlock):
    heading_block = HeadingBlock()
    indented_paragraph_block = RichTextBlock(
        icon='pilcrow',
        template='blocks/indented_paragraph_block.html',
        features=['ol', 'ul', 'bold', 'italic', 'strikethrough', 'hr', 'link'],
        label='Indented Text'
    )
    paragraph_block = RichTextBlock(
        icon='pilcrow',
        template='blocks/paragraph_block.html',
        features=['ol', 'ul', 'bold', 'italic', 'strikethrough', 'hr', 'link'],
        label='Text'
    )
    image_block = ImageBlock()
    landscape_images_block = ListBlock(SimpleImageBlock(),
                                       label='Landscape Images',
                                       icon='image',
                                       template='blocks/landscape_images_block.html',
                                       help_text='Add even number of images (it inserts 2 horizontal images on the line)')
    portrait_images_block = ListBlock(SimpleImageBlock(),
                                      label='Portrait Images',
                                      icon='image',
                                      template='blocks/portrait_images_block.html',
                                      help_text='Add 2 images (it inserts 2 vertical images on the line)')
    image_slider_block = ListBlock(SliderImageBlock(),
                                   label='Image Slider',
                                   icon='image',
                                   template='blocks/image_slider_block.html',
                                   help_text='Full width image slider, add at least 4 images')
    block_quote = QuoteBlock()
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='media',
        template='blocks/embed_block.html')
    raw_html = RawHTMLBlock(
        required=False,
        template='blocks/raw_html_block.html',
        label='Raw HTML',
        help_text='A text area for entering raw HTML which will be rendered unescaped')


class StandardPageHeadingBlock(StructBlock):
    heading_text = CharBlock(required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('title-small', 'Small'),
        ('title-med', 'Medium'),
        ('title-large', 'Large'),
        ('title-extra-large', 'Extra Large')
    ], blank=True, required=False)

    class Meta:
        icon = 'title'
        template = 'blocks/standard_page_heading_block.html'
        label = 'Heading'


class StandardPageImageBlock(StructBlock):
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = 'image'
        template = 'blocks/standard_page_image_block.html'
        label = 'Image'


class SeparatorLineStaticBlock(StaticBlock):
    class Meta:
        label = 'Separator Line'
        admin_text = 'Automaticaly inserts separator line into the template'
        template = 'blocks/separator_line_static_block.html'


class ColumnStreamBlock(StreamBlock):
    heading = StandardPageHeadingBlock()
    paragraph = RichTextBlock(
        icon='pilcrow',
        features=['ol', 'ul', 'bold', 'italic', 'hr', 'link'],
        label='Text'
    )
    image = StandardPageImageBlock()
    raw_html = RawHTMLBlock(
        required=False,
        template='blocks/raw_html_block.html',
        label='Raw HTML',
        help_text='A text area for entering raw HTML which will be rendered unescaped')


class TwoColumnsBlock(StructBlock):
    left_column = ColumnStreamBlock(
        icon='arrow-left', label='Left column content')
    right_column = ColumnStreamBlock(
        icon='arrow-right', label='Right column content')

    class Meta:
        label = 'Two Columns Layout'
        template = 'blocks/two_columns_layout.html'


class OneColumnsBlock(StructBlock):
    column = ColumnStreamBlock()

    class Meta:
        label = 'One Column Layout'
        template = 'blocks/one_column_layout.html'


class StandardPageStreamBlock(StreamBlock):
    one_columng_block = OneColumnsBlock()
    two_column_block = TwoColumnsBlock()
    separator_line_block = SeparatorLineStaticBlock()
