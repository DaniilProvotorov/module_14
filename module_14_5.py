from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup()
kb2 = InlineKeyboardMarkup()
kb3 = InlineKeyboardMarkup()
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
button5 = KeyboardButton(text='Купить')
button6 = InlineKeyboardButton(text='Product1', callback_data= 'product_buying')
button7 = InlineKeyboardButton(text='Product2', callback_data= 'product_buying')
button8 = InlineKeyboardButton(text='Product3', callback_data= 'product_buying')
button9 = InlineKeyboardButton(text='Product4', callback_data= 'product_buying')
button10 = KeyboardButton(text='Регистрация')
kb.row(button, button2, button5, button10)
kb.resize_keyboard = True
kb2.row(button3, button4)
kb3.row(button6, button7, button8, button9)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    check_user = crud_functions.is_included(message.text)
    if check_user is False:
        await state.update_data(username=message.text)
        await message.answer(text='Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    crud_functions.add_user(username=data['username'], email=data['email'], age=data['age'])
    await message.answer(text='Регистрация прошла успешно!')
    await state.finish()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open('картинки/1.jpg', 'rb') as img1:
        await message.answer_photo(img1, f'Название: {crud_functions.prod[0][0]}| Описание: {crud_functions.prod[0][1]} | Цена:{crud_functions.prod[0][2]}')
    with open('картинки/2.jpg', 'rb') as img2:
        await message.answer_photo(img2, f'Название: {crud_functions.prod[1][0]}| Описание: {crud_functions.prod[1][1]} | Цена:{crud_functions.prod[1][2]}')
    with open('картинки/3.jpg', 'rb') as img3:
        await message.answer_photo(img3, f'Название: {crud_functions.prod[2][0]}| Описание: {crud_functions.prod[2][1]} | Цена:{crud_functions.prod[2][2]}')
    with open('картинки/4.jpg', 'rb') as img4:
        await message.answer_photo(img4, f'Название: {crud_functions.prod[3][0]}| Описание: {crud_functions.prod[3][1]} | Цена:{crud_functions.prod[3][2]}')
    await message.answer('Выберите продукт для покупки:', reply_markup = kb3)

@dp.callback_query_handler(text= 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text= 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup= kb2)

@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer('10 * вес (кг) + 6,25 * рост (см) – 5 * возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f"Ваша норма калорий: {10*int(data['weight'])+6.25*int(data['growth'])-5*int(data['age'])+5}")

    await state.finish()

@dp.message_handler(text= 'Информация')
async def info(message):
    await message.answer('На данный момент у меня одна функция, но стоит немного подождать!')

@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb )

@dp.message_handler()
async def start(message):
    await message.answer('Введите команду /start, чтобы начать общение.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)