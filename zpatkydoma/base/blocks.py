from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailcore.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    RawHTMLBlock,
    ListBlock
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

    class Meta:
        icon = 'image'


class QuoteBlock(StructBlock):
    text = TextBlock(required=False)
    author = CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        icon = 'fa-quote-left'
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
        icon="fa-paragraph",
        template="blocks/indented_paragraph_block.html",
        features=['ol', 'ul', 'bold', 'italic', 'hr', 'link'],
        label='Indented Text'
    )
    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        template="blocks/paragraph_block.html",
        features=['ol', 'ul', 'bold', 'italic', 'hr', 'link'],
        label='Text'
    )
    image_block = ImageBlock()
    landscape_images_block = ListBlock(SimpleImageBlock(),
                                       label='Landscape Images',
                                       icon='image',
                                       template='blocks/landscape_images_block.html',
                                       help_text='Add even number of images (it inserts 2 images on the line)')
    image_slider_block = ListBlock(SimpleImageBlock(),
                                   label='Image Slider',
                                   icon='image',
                                   template='blocks/image_slider_block.html',
                                   help_text='Full width image slider, add at least 4 images')
    block_quote = QuoteBlock()
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon='fa-s15',
        template='blocks/embed_block.html')
    raw_html = RawHTMLBlock(
        required=False,
        template='blocks/raw_html_block.html',
        label='Raw HTML',
        help_text='A text area for entering raw HTML which will be rendered unescaped')
