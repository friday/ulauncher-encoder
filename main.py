"""
Ulauncher Encoder extension
"""
import base64
import urllib
import html
from ulauncher.api import Extension, ExtensionResult
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction


class EncoderExtension(Extension):
    def on_query_change(self, query):
        if query.keyword == "encode":
            return self.encode(query.argument)
        return self.decode(query.argument)

    def decode(self, text):
        """ Decode a string into multiple formats """

        try:
            decoded_base64 = base64.b64decode(text).decode()
        except: # pylint: disable=bare-except
            decoded_base64 = "Cannot decode input text as base64."

        try:
            decoded_url = urllib.parse.unquote_plus(text)
        except: # pylint: disable=bare-except
            decoded_url = "Cannot decode input text"

        decoded_html = html.unescape(text)

        return [
            ExtensionResult(
                icon='images/decode.svg',
                name=decoded_base64,
                description='Base64 Decoded',
                highlightable=False,
                on_enter=CopyToClipboardAction(decoded_base64)
            ),
            ExtensionResult(
                icon='images/decode.svg',
                name=decoded_url,
                description='URL Decoded',
                highlightable=False,
                on_enter=CopyToClipboardAction(decoded_url)
            ),
            ExtensionResult(
                icon='images/decode.svg',
                name=decoded_html,
                description='HTML Decoded',
                highlightable=False,
                on_enter=CopyToClipboardAction(decoded_html)
            )
        ]

    def encode(self, text):
        """ Encodes a string into multiple formats """

        encoded_base64 = base64.b64encode(bytes(text, "utf-8")).decode("utf-8")
        encoded_url = urllib.parse.quote_plus(text)
        encoded_html = html.escape(text)

        return [
            ExtensionResult(
                icon='images/encode.svg',
                name=encoded_base64,
                description='Base64 Encoded',
                highlightable=False,
                on_enter=CopyToClipboardAction(encoded_base64)
            ),
            ExtensionResult(
                icon='images/encode.svg',
                name=encoded_url,
                description='URL Encoded',
                highlightable=False,
                on_enter=CopyToClipboardAction(encoded_url)
            ),
            ExtensionResult(
                icon='images/encode.svg',
                name=encoded_html,
                description='HTML Encoded',
                highlightable=False,
                on_enter=CopyToClipboardAction(encoded_html)
            )
        ]

if __name__ == '__main__':
    EncoderExtension().run()
