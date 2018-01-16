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
)


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = "blocks/image_block.html"


class BlockQuote(StructBlock):
    text = TextBlock(required=False)
    author = CharBlock(
        blank=True, required=False, label='e.g. Mary Berry')

    class Meta:
        icon = "fa-quote-left"
        template = "blocks/blockquote.html"


class BaseStreamBlock(StreamBlock):
    paragraph_block = RichTextBlock(
        icon="fa-paragraph",
        template="blocks/paragraph_block.html",
        features=['h2', 'h3', 'h4', 'h5', 'h6', 'ol',
                  'ul', 'bold', 'italic', 'hr', 'link']
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon="fa-s15",
        template="blocks/embed_block.html")
    raw_html = RawHTMLBlock(
        required=False,
        help_text='A text area for entering raw HTML which will be rendered unescaped')
