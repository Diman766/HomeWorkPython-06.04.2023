import view
import model
import logger


def run_work():
    flag = True
    while flag:
        choose = view.user_choose()
        if choose == 1:
            print(logger.get_base())
        elif choose == 2:
            logger.writer(model.add_id(logger.get_base()),
                        input('Заголовок   '), input('текст   '))
        elif choose == 3:
            model.find(logger.get_base())
            base = model.delete(logger.get_base(), input(
                'Введите Id работника для удаления    '))
            logger.rewriter(base)
        elif choose == 4:
            model.find(logger.get_base())
            workerId = input('Введите Id заметки из списка  ')
            logger.rewriter(model.changeWorker(logger.get_base(), workerId))
        elif choose == 5:
            model.find(logger.get_base())
        elif choose == 6:
            flag = False
