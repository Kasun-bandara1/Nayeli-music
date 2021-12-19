from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""
Hey🥀..I am Nayeli ,I'm here to Play Audio▶️ in Telegram Voice Chats 🔊.

How to use me :- @HowToUse_Nayeli

♻️I cool project by @SANTA_R1 🚶 2021.""",
        reply_markup=InlineKeyboardMarkup(
            [
                    [
                        InlineKeyboardButton(
                             text=" Support🚶‍♂",
                             url="https://t.me/nayelisupport"),
                         InlineKeyboardButton(
                             text="Updates 🙋‍♀",
                             url="https://t.me/name")
                    ],
                    [
                        InlineKeyboardButton(
     text="source owner📲",
                             url="https://t.me/SANTA_R1"),
                         InlineKeyboardButton(
                             text=" 😚",
                             url="https://t.me/yakkaadaviya")
                    ],
                    [
                        InlineKeyboardButton(
                            text=" ⚡️ Developer ",
                             url="https://t.me/hirunaofficial") 
                    
                    ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""
        Nayeli🥀\n\nTelegram UserBot to Play Audio in Telegram Voice Chats 🔊\n\n©2021 @SANTA_R1 cool project📲
        """,
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "️Start Bot", url="https://t.me/YakkaAdaviyaMusicBot")
                ]
            ]
        )
   )
