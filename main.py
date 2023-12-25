from configs import * 
from PIL import Image
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привіт, я бот для перетворення фото png картинку що б створювати скірети. Відправ мені фото і я зроблю все за тебе")



@dp.message_handler(content_types=['photo'])
async def photo(message: types.Message):
    await message.answer("Зачекайте, ваше фото обробляється")
    await message.photo[-1].download(f'./images/image_{message.message_id}.png')

    image = Image.open('./images/image.png')
    resized_image = image.resize((512, 512))

    # Save the resized image
    resized_image.save(f'./images/resized_image_for_{message.message_id}.png')

    await message.answer_photo(photo=open(f'./images/resized_image_for_{message.message_id}.png', 'rb'))
    await message.answer("Ваше фото оброблено")

    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
