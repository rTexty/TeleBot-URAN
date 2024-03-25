from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(callback_data="Назад", text="Назад", )
        ]
    ]
)

services_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(callback_data="Брендинг", text="Брендинг"),
        InlineKeyboardButton(callback_data="Дизайн приложений", text="Дизайн приложений"),
        InlineKeyboardButton(callback_data="Дизайн презентаций", text="Дизайн презентаций")
        ],
        [
        InlineKeyboardButton(callback_data="Дизайн веб-сайтов", text="Дизайн веб-сайтов"),
        InlineKeyboardButton(callback_data="Превью для ютуба", text="Превью для ютуба", ),
        InlineKeyboardButton(callback_data="Баннеры, постеры", text="Баннеры, постеры"),
        ],
        [
        InlineKeyboardButton(callback_data="Оформление соц.сетей", text="Оформление соц.сетей"),
        InlineKeyboardButton(callback_data="Дизайн брендбуков", text="Дизайн брендбуков"),
        InlineKeyboardButton(callback_data="3D дизайн", text="3D дизайн")
        ],

        [
        InlineKeyboardButton(callback_data="Логотипы", text="Логотипы"),
        InlineKeyboardButton(callback_data="Карточки Wildberris", text="Карточки Wildberris"),
        InlineKeyboardButton(callback_data="Музыкальные обложки", text="Музыкальные обложки")
        ],
        [
            InlineKeyboardButton(callback_data="Другое", text="Другое", )
        ]
        
    ]
)
