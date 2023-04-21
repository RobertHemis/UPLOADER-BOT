

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Button(object):

      BUTTONS01 = InlineKeyboardMarkup( [ [ InlineKeyboardButton(text="YTS", callback_data='00'),
                                            InlineKeyboardButton(text="Search", switch_inline_query_current_chat="1 ") ],
                                          [ InlineKeyboardButton(text="Anime", callback_data='00'),
                                            InlineKeyboardButton(text="Search", switch_inline_query_current_chat="2 ") ],
                                          [ InlineKeyboardButton(text="1337x", callback_data='00'),
                                            InlineKeyboardButton(text="Search", switch_inline_query_current_chat="3 " ) ],
                                          [ InlineKeyboardButton(text="ThePirateBay", callback_data='00'),
                                            InlineKeyboardButton(text="Search", switch_inline_query_current_chat="4 ") ],
                                          [ InlineKeyboardButton(text="Cancel", callback_data="X0") ] ] )
