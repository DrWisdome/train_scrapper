from train.train_delay import TrainDelay


with TrainDelay(teardown=True) as bot:
    for i in range(0, 8):
        bot.land_first_page()
        bot.find_train(i)
        bot.find_delay_time()
    bot.print_array()

