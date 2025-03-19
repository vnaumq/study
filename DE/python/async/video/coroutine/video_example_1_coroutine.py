import asyncio

#Courotine function
async def main():
    print('Start of main coroutine')

#Run the main courotine
asyncio.run(main())

'''
Ну кратко в этом примере он рассказал, что при вызове функции async возращается не сам результат
а куротина этой функции и то что эту функцию нужно обязательно выполнять с помощью asyncio.run()
'''

# https://www.youtube.com/watch?v=Qb9s3UiMSTA