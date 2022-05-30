from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
IP = env.str("ip")
ADMINS = env.list("ADMINS")
MY_TG_PAGE = env.list("MY_TG_PAGE")


class Messages:
    greetings = "ПРИВЕТ! 👋 Хочешь научится строить структуру в бизнесе, но нет автоматизированной системы рекрутинга??😃\n\nЦена вопроса всего 10 минут твоего времени!\n\n😎Перед тем как ты все узнаешь , помни, шанс приходит всем, но страхи и стереотипы не дают продвинутся дальше!\n\nГотов?"
    start_watching = "Всего 5 коротких роликов. Время пролетит быстро. 🚀\n\nВАЖНО❗️В каждом ролике будет КОДОВОЕ СЛОВО в конце.\n\nЧто бы продвинуться дальше, нужно нажать на кнопку внизу 👇 ПОСЛЕ того как закончится ролик.👇\n\n🤝Договорились?\nСмотри первое видео, НАЖМИ кнопку ниже 👇"
    write_code = "Нажми на КОДОВОЕ СЛОВО 👇"
    reject = "Хорошо. Уважаю твое решение. Можешь отписаться от рассылки."
    first_answer = "Отлично! В этом видео разберемся, подойдет ли тебе наше предложение 👇"
    second_answer = "В этом минутном видео расскажу о том как мы зарабатываем 😎👇"
    third_answer = "В этом видео расскажу откуда деньги 💰😃 👇"
    fourth_answer = "В этом видео познакомлю тебя с нашим генеральным партнером 🤩"
    fifths_answer = "🚀Супер! Осталось последнее самое важное видео!"
    sixth_answer = f"🤩Ты молодец! Давай подведем итог. Ты немного узнал на этом этапе кто мы такие и с какой компанией сотрудничаем.\n\n🤝Выбор безусловно за тобой . Но я знаю точно, если ты прошел все до конца, то ты тот человек который ищет возможности.\n\n✍️Поэтому предлагаю, продолжить наше общение уже в личных сообщениях, что бы познакомиться поближе.\n\n👉Переходи по ссылке {MY_TG_PAGE[0]}\n\n✍️Напиши: Хочу узнать больше."


class Buttons:
    yes = "Да"
    no = "Нет"


class Codes:
    start = "Начать"
    first = "Бизнес"
    second = "Далее"
    third = "Доход"
    fourth = "Компания"


class Videos:
    first: str = "BAACAgIAAxkBAAIgvWKQvWO7pIyGAAFRhsPzxPadAWdBkgACXhoAAvYagUjoWxHX5tO4kiQE"
    second = "BAACAgIAAxkBAAIgv2KQvbxH2Vu4dWouZXQVZs0wtebJAAJnGgAC9hqBSBsnoOkhvD-OJAQ"
    third = "BAACAgIAAxkBAAIgwWKQvkPEOIsDdQxs1bj6NkU3yND9AAJsGgAC9hqBSLcAAQ-5qwg8eSQE"
    fourth = "BAACAgIAAxkBAAIgw2KQvpEnbegZ3KzlHUSt72D8hW3nAAJzGgAC9hqBSONVmUO3hiAmJAQ"
    fifth = "BAACAgIAAxkBAAIgxWKQvpzaHZLL_qgD3HwVvsOEJut2AAJ0GgAC9hqBSO2bizn20y7hJAQ"
    sixth = "BAACAgIAAxkBAAIiFGKQ6FZOC2oGS0lCa2aU7zyf8W8sAALQGQAC9hqJSK2iAnxFkzz3JAQ"

    first_length = 86
    second_length = 86
    third_length = 133
    fourth_length = 88
    fifth_length = 213
    sixth_length = 85

