import json
from urllib.parse import urlparse
import redis

REDIS_URL = 'rediss://:pf41ce38d95403b8ab2177eb2ffa1cccd20bc15d62923012efaf2548c33e07879@ec2-54-204-192-122.compute-1.amazonaws.com:20860'
url = urlparse(REDIS_URL)
rediska = redis.Redis(host=url.hostname, port=url.port, username=url.username, password=url.password, ssl=True,
                      ssl_cert_reqs=None)


def get_questions(chat_id):
    questions = rediska.get(chat_id)
    if questions is None:
        return False
    return json.loads(questions.decode("utf-8"))


def add_question(chat_id, question_id, answers, correct_answer_id, timeout):
    data = '{"%d": {"answers": {"%s": "%d"}, "timeout": "%d"}}' % (question_id, answers, correct_answer_id, timeout)
    questions = get_questions(chat_id)
    if questions is False:
        rediska.set(chat_id, data, ex=7200)
        return
    else:
        questions.update({f'{question_id}': {"answers": {f"{answers}": f'{correct_answer_id}'},
                                             "timeout": f"{timeout}"}})
    rediska.set(chat_id, str(questions).replace("'", '"'), ex=7200)
    return


def get_question(chat_id):
    questions = get_questions(chat_id)
    if questions is False:
        return False
    elif len(questions) == 0:
        rediska.delete(chat_id)
        return False
    else:
        questions_list = list(questions.keys())
        question_id = questions_list[0]
        question = questions.pop(question_id)
        rediska.set(chat_id, str(questions).replace("'", '"'), ex=7200)
        return question_id, question,


def add_poll_id(poll_id, chat_id, msg_id):
    rediska.set(poll_id, f'{chat_id}, {msg_id}', ex=300)


def get_poll_id(poll_id):
    chat_id = rediska.get(poll_id)
    if chat_id is None:
        return False
    rediska.delete(poll_id)
    return chat_id.decode('utf-8')


def get_result(chat_id):
    question_id = rediska.get(f'{chat_id} - question')
    if question_id is None:
        return False
    rediska.delete(f'{chat_id} - question')
    return question_id.decode('utf-8')


def write_result(chat_id, question_id):
    rediska.set(f'{chat_id} - question', question_id, ex=7200)


def get_usage(chat_id, flag=1):
    usage_id = rediska.get(f'{chat_id} - usage_id')
    if usage_id is None:
        return False
    if flag == 0:
        rediska.delete(f'{chat_id} - usage_id')
    return usage_id.decode('utf-8')


def write_usage(chat_id, usage_id):
    rediska.set(f'{chat_id} - usage_id', usage_id, ex=7200)


def get_quiz_attempt_id(chat_id):
    quiz_attempt_id = rediska.get(f'{chat_id} - quiz_attempt_id')
    if quiz_attempt_id is None:
        return False
    rediska.delete(f'{chat_id} - quiz_attempt_id')
    return quiz_attempt_id.decode('utf-8')


def write_quiz_attempts(chat_id, quiz_attempt_id):
    rediska.set(f'{chat_id} - quiz_attempt_id', quiz_attempt_id, ex=7200)


def get_question_num(chat_id):
    question_num = rediska.get(f'{chat_id} - question_num')
    if question_num is None:
        return False
    return question_num.decode('utf-8')


def write_question_num(chat_id, question_num):
    rediska.set(f'{chat_id} - question_num', question_num, ex=3600)



def get_course_id(chat_id):
    course_id = rediska.get(f'{chat_id} - course_id')
    if course_id is None:
        return False
    rediska.delete(f'{chat_id} - course_id')
    return course_id.decode('utf-8')


def write_course_id(chat_id, course_id):
    rediska.set(f'{chat_id} - course_id', course_id, ex=7200)
