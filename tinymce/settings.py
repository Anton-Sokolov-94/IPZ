import os
from django.conf import settings

DEFAULT_CONFIG = {
    #'mode': "textareas",
    'theme': "advanced",
    'plugins': '''pagebreak, style, layer, table, save, advhr, advimage, advlink,
               emotions, iespell, inlinepopups, insertdatetime, preview, media,
               searchreplace, print, contextmenu, paste, directionality,
               fullscreen, noneditable, visualchars, nonbreaking, xhtmlxtras,
               template, wordcount, advlist, autosave''',

    'theme_advanced_buttons1': '''bold, italic, underline, strikethrough, |,
                               justifyleft, justifycenter, justifyright,
                               justifyfull, fontselect, fontsizeselect,
                               fullscreen, code''',
    'theme_advanced_buttons2': '''bullist, numlist, |, outdent, indent,
                               blockquote, |, undo, redo, |, link, unlink, |,
                               forecolor, backcolor''',
    'theme_advanced_buttons3': '''tablecontrols, |, hr, sub, sup, |, charmap''',

    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': "true",

    'template_external_list_url': "lists/template_list.js",
    'external_link_list_url': "lists/link_list.js",
    'external_image_list_url': "lists/image_list.js",
    'media_external_list_url': "lists/media_list.js",

    'style_formats': [
      {'title': 'Bold text', 'inline': 'strong'},
      {'title': 'Red text', 'inline': 'span', 'styles': {'color' : '#ff0000'}},
      {'title': 'Help', 'inline': 'strong', 'classes': 'help'},
      {'title': 'Table styles'},
      {'title': 'Table row 1', 'selector': 'tr', 'classes': 'tablerow'}
    ],

    'width': '700',
    'height': '400'
}



USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)

USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)

USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER',
        'filebrowser' in settings.INSTALLED_APPS)

if 'staticfiles' in settings.INSTALLED_APPS or 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL',os.path.join(settings.STATIC_URL, 'tiny_mce/tiny_mce.js'))
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT',os.path.join(settings.STATIC_ROOT, 'tiny_mce'))
else:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL','%sjs/tiny_mce/tiny_mce.js' % settings.MEDIA_URL)
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', os.path.join(settings.MEDIA_ROOT, 'js/tiny_mce'))

JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]
