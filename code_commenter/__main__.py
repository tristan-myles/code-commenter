# *============================= code commenter ==============================*
import argparse
import pyperclip
import math
from enum import Enum

class LanguageCommentSymbol(Enum):
    """Defines the code comment symbol for each supported language"""
    PYTHON = "#"
    SQL = "--"
    GO = "//"

# *--------------------------------- helpers ---------------------------------*
def create_comment_header(header_text: str, character: str, header_length: int, coding_lang: str) -> str:
    """
    Creates a formatted string header.

     In cases where the decorator strings are unequal lengths, the right
     decorator string will have an extra character.

    :param header_text: the text to be decorated
    :param character: the decoration character
    :param header_length: the length of the header comment

    :return: a formatted header string
    """
    if len(header_text) > header_length:
        raise Exception(
            "The string is longer than the number of required " "characters"
        )

    if header_text == "":
        header = character + character
    else:
        header = character + " " + header_text + " " + character

    pre_post_pad = (header_length / 2 - len(header) / 2) - 2

    for i in range(math.floor(pre_post_pad)):
        header = character + header + character

    if (header_length - len(header_text)) % 2 != 0:
        header = header + character

    header = LanguageCommentSymbol[coding_lang].value +" *" + header + "*\n"

    return header


def parse_arguments() -> argparse.Namespace:
    """
    Argument parser

    :return: An argparse namespace
    """
    parser = argparse.ArgumentParser(
        "Generate stylized code comment headers"
    )

    parser.add_argument(
        "-l",
        "--length",
        metavar="\b",
        type=int,
        default=79,
        help="length of the string",
    )

    parser.add_argument(
        "-lang",
        "--language",
        metavar="\b",
        type=str,
        choices=[e.name for e in LanguageCommentSymbol],
        default="PYTHON",
        help="coding language the comment is for",
    )

    parser.add_argument("-t", "--text", metavar="\b", type=str, help="header text")

    parser.add_argument(
        "-d",
        "--decoration",
        metavar="\b",
        type=str,
        default="=",
        help="character to decorate right and left of header " "text",
    )

    parser.add_argument(
        "-cc",
        "--character",
        metavar="\b",
        type=str,
        default="#",
        help="comment character; default is #",
    )

    parser.add_argument(
        "-c",
        "--copy",
        action="store_true",
        default=False,
        help="should the output be copied to your clipboard; " "default is false",
    )

    args = parser.parse_args()

    return args


# *---------------------------------- main -----------------------------------*
def main():
    ARGS = parse_arguments()

    formatted_text = create_comment_header(
        ARGS.text, character=ARGS.decoration, header_length=ARGS.length, coding_lang=ARGS.language
    )

    if ARGS.copy:
        pyperclip.copy(formatted_text)
    else:
        print(formatted_text)
# *===========================================================================*
