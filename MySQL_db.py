import random
import time
from logging import config, getLogger
from mysql.connector import connect, OperationalError, Error
from html2text import HTML2Text


config.fileConfig('log.ini', disable_existing_loggers=False)
logger = getLogger(__name__)


class SQL_db:
	def __init__(self):
		try:
			# устанавливаем подключение к базе данных
			self.connect = connect(
								host='94.247.135.53',
								user='telegramUser',
								password='!QAZ2wsx'
								)

		except OperationalError as e:
			logger.error("can't connect to Mysql")
			logger.error(e)
		try:
			self.cursor = self.connect.cursor()
		except OperationalError as e:
			logger.error("can't get cursor")
			logger.error(e)

	def update_id(self, chat_id, iin):
		try:
			self.cursor.execute(f'''UPDATE moodle_additional.user_add_info 
									SET telgram_id=(%s) 
									WHERE username=(%s);''', (chat_id, iin,))
		except Error as e:
			logger.error("func update_id")
			logger.error(e)
			return
		self.connect.commit()

	def check_user(self, uid):
		try:
			self.cursor.execute(f'''SELECT class, telgram_id, pass_req
									FROM moodle_additional.user_add_info
									WHERE telgram_id={uid}''')
		except Error as e:
			logger.error("func check_user")
			logger.error(e)
			return

		user_ids = self.cursor.fetchall()
		for t_id in user_ids:
			if t_id[1] == str(uid):
				return t_id
		return -1

	def get_iin(self, chat_id):
		try:
			self.cursor.execute(f'''SELECT username 
									FROM moodle_additional.user_add_info 
									WHERE telgram_id={chat_id}''')
		except Error as e:
			logger.error("func get_iin")
			logger.error(e)
			return
		data = self.cursor.fetchall()
		username = data[0][0]
		return username

	def send_the_region(self, callback, region_id=18):
		try:
			self.cursor.execute('''UPDATE moodle_additional.user_add_info
									SET region_id=(%s)
									WHERE telgram_id=(%s)''',
								(region_id, callback.message.chat.id))
		except Error as e:
			logger.error("func send_the_region")
			logger.error(e)
			return
		self.connect.commit()

	def update_class(self, class_num, callback):
		try:
			self.cursor.execute('''UPDATE moodle_additional.user_add_info 
									SET class=(%s), isTeacher=(%s)
									WHERE telgram_id=(%s)''',
								(class_num, 0, callback.message.chat.id))
		except Error as e:
			logger.error("func update_class")
			logger.error(e)
			return
		self.connect.commit()

	def update_teacher(self, callback):
		try:
			self.cursor.execute('''UPDATE moodle_additional.user_add_info 
                          			SET isTeacher=(%s) 
                          			WHERE telgram_id=(%s)''',
								(1, callback.message.chat.id))
		except Error as e:
			logger.error("func update_teacher")
			logger.error(e)
			return
		self.connect.commit()

	def send_number(self, chat_id, number):
		try:
			self.cursor.execute('''INSERT INTO moodle_additional.user_add_info 
									(username, telgram_id, isMale, region_id, second_region_id, school_id,
									custom_school, phone, class, class_type, birth_date, kz, promocode_id, isTeacher) 
									VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
								(chat_id, chat_id, 0, 18, 7777, 7777, 0, number, 0, 0, 0000, 0, 0, 0))
		except Error as e:
			logger.error("func send_number, deleting_number")
			logger.error(e)
			self.delete_number(chat_id, number)
			return
		self.connect.commit()

	def delete_number(self, chat_id, number):
		try:
			self.cursor.execute(f'''DELETE FROM moodle_additional.user_add_info 
									WHERE telgram_id={chat_id}''')
		except Error as e:
			logger.error("func deleting_number")
			logger.error(e)
			return
		self.connect.commit()
		self.send_number(chat_id, number)

	def send_fio(self, lastname, firstname, username, patronymic):
		try:
			if patronymic is not None:
				self.cursor.execute(f'''UPDATE moodle.mdl_user 
										SET lastname=(%s), firstname=(%s) 
										WHERE username=(%s)''',
									(lastname, firstname, username))
			else:
				self.cursor.execute(f'''UPDATE moodle.mdl_user 
										SET lastname=(%s), firstname=(%s), patronymic=(%s)
										WHERE username=(%s)''',
									(lastname, firstname, patronymic, username))
		except Error as e:
			logger.error("func send_fio")
			logger.error(e)
			return
		self.connect.commit()

	def update_iin(self, username, chat_id):
		try:
			self.cursor.execute('''UPDATE moodle_additional.user_add_info 
									SET username=(%s) 
									WHERE telgram_id=(%s)''',
								(username, chat_id))
		except Error as e:
			logger.error("func update_iin")
			logger.error(e)
			return
		self.connect.commit()
		return 1

	def send_iin(self, username):
		time_now = int(time.time())
		try:
			self.cursor.execute('''INSERT INTO moodle.mdl_user 
            						(auth, confirmed, policyagreed, deleted, suspended, mnethostid, username, password, 
            						emailstop, country, lang, calendartype, timezone, firstaccess, lastaccess, 
            						lastlogin, currentlogin, lastip, picture, descriptionformat, mailformat, maildigest,
            						maildisplay, autosubscribe, trackforums, timecreated, timemodified, trustbitmask)
            						VALUES 
									(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
									 %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
								('manual', 1, 0, 0, 0, 1, username, 00000, 0, 'KZ',
								 'en', 'gregorian', 99, time_now, time_now, time_now, time_now, '31.171.166.55', 0,
								 1, 1, 0, 2, 1, 0, time_now,
								 0, 0))
		except Error as e:
			logger.error("func send_iin")
			logger.error(e)
			return
		self.connect.commit()

	def delete_user(self, username):
		try:
			self.cursor.execute(f'''DELETE FROM moodle_additional.user_add_info 
									WHERE username=(%s)''',
								(str(username), ))
		except Error as e:
			logger.error("func deleting_user")
			logger.error(e)
			return
		self.connect.commit()

	def send_password(self, password, username):
		try:
			self.cursor.execute(f'''UPDATE moodle.mdl_user 
									SET password=(%s) 
									WHERE username=(%s)''',
								(password, username))
		except Error as e:
			logger.error("func send_password")
			logger.error(e)
			return
		self.connect.commit()

	def profile(self, chat_id):
		try:
			self.cursor.execute(f'''SELECT username, class 
									FROM moodle_additional.user_add_info 
									WHERE telgram_id={str(chat_id)}''')
		except Error as e:
			logger.error("func profile")
			logger.error(e)
			return
		data = self.cursor.fetchall()
		return data

	def get_sort_order(self, course_id):
		try:
			self.cursor.execute(f'''SELECT sortorder 
									FROM moodle.mdl_enrol 
									WHERE courseid=(%s);''', (course_id, ))
		except Error as e:
			logger.error("func get_sort_order")
			logger.error(e)
			return
		data = len(self.cursor.fetchall())
		return data

	def get_enrol(self, course_id):
		try:
			self.cursor.execute(f'''SELECT id 
									FROM moodle.mdl_enrol
									WHERE courseid=(%s) and enrol=(%s);''',
								(course_id, 'manual'))
		except Error as e:
			logger.error("func get_enrol")
			logger.error(e)
			return
		data = self.cursor.fetchone()[0]
		self.cursor.fetchmany()
		return data

	def get_user_id(self, chat_id):
		username = self.get_iin(chat_id)
		try:
			self.cursor.execute(f'''SELECT id 
									FROM moodle.mdl_user
									WHERE username=(%s);''',
								(username, ))
		except Error as e:
			logger.error("func get_user_id")
			logger.error(e)
			return
		data = self.cursor.fetchone()[0]
		return data

	def set_user_enrolments(self, chat_id, enrol_id):
		time_now = int(time.time())
		user_id = self.get_user_id(chat_id)
		try:
			self.cursor.execute(f'''INSERT INTO moodle.mdl_user_enrolments
									(enrolid, userid, timestart, timeend, modifierid, timecreated, timemodified)
									VALUES (%s, %s, %s, %s, %s, %s, %s);''',
								(enrol_id, user_id, time_now, 0, user_id, time_now, time_now))
		except Error as e:
			logger.error("func set_user_enrolments")
			logger.error(e)
			return
		self.connect.commit()

	def sub_cash(self, chat_id, cash):
		iin = self.get_iin(chat_id)
		cur_cash = self.get_cash_value(chat_id)
		new_cash = cur_cash - cash
		try:
			self.cursor.execute(f'''UPDATE moodle_additional.purse 
									SET current_payment_sum=(%s)
									WHERE username=(%s);''',
								(new_cash, iin))
		except Error as e:
			logger.error("func sub_cash")
			logger.error(e)
			return
		self.connect.commit()

	def insert_purse(self, chat_id):
		userid = self.get_iin(chat_id)
		try:
			self.cursor.execute(f'''INSERT INTO moodle_additional.purse 
									(username, current_payment_sum) 
									VALUES (%s, %s);''',
								(userid, 0))
		except Error as e:
			logger.error("func insert_purse")
			logger.error(e)
			return
		self.connect.commit()

	def get_cash_value(self, chat_id):
		username = self.get_iin(chat_id)
		try:
			self.cursor.execute(f'''SELECT current_payment_sum 
									FROM moodle_additional.purse 
									WHERE username=(%s);''',
								(username,))
		except Error as e:
			logger.error("func get_cash_value")
			logger.error(e)
			return
		data = self.cursor.fetchone()
		if len(data) == 0:
			return 0
		return data[0]

	def update_genre_(self, callback, is_male=1):
		try:
			self.cursor.execute(f'''UPDATE moodle_additional.user_add_info 
									SET isMale=(%s) 
									WHERE telgram_id=(%s);''',
								(is_male, callback.message.chat.id))
		except Error as e:
			logger.error("func update_genre_")
			logger.error(e)
			return
		self.connect.commit()

	def access(self, chat_id):
		try:
			self.cursor.execute(f'''UPDATE moodle_additional.user_add_info 
									SET pass_req=(%s) 
									WHERE telgram_id=(%s);''',
								(1, chat_id))
		except Error as e:
			logger.error("func access")
			logger.error(e)
			return
		self.connect.commit()

	def get_olymp_name(self, chat_id):
		self.cursor.execute(f'''SELECT fullname 
								FROM moodle.mdl_course 
								WHERE id=(%s);''',
							(chat_id, ))
		try:
			pass
		except Error as e:
			logger.error("func get_olymp_name")
			logger.error(e)
			return ' '
		return self.cursor.fetchone()[0]

	def get_certificate(self, u_id, timee):
		self.cursor.execute(f'''SELECT customcertid 
								FROM moodle.mdl_customcert_issues 
								WHERE userid=(%s) and timecreated>(%s);''',
							(u_id, timee))
		try:
			pass
		except Error as e:
			logger.error("func get_certificate")
			logger.error(e)
			return ' '
		return self.cursor.fetchall()

	def get_customcert_one(self, customcert_id):
		try:
			self.cursor.execute(f'''SELECT course, name, id 
								FROM moodle.mdl_customcert 
								WHERE id=(%s);''',
							(customcert_id, ))
		except Error as e:
			logger.error("func get_customcert_one")
			logger.error(e)
			return ' '
		return self.cursor.fetchall()

	def get_customcert_list(self, customcert_ids):

		try:
			self.cursor.execute(f'''SELECT course, name, id 
								FROM moodle.mdl_customcert
								WHERE id in {customcert_ids};''')
		except Error as e:
			logger.error("func get_customcert_list")
			logger.error(e)
			return ' '
		return self.cursor.fetchall()

	def get_instance(self, course_id):
		try:
			self.cursor.execute(f'''SELECT id
                      				FROM moodle.mdl_course_modules
                      				WHERE course=(%s) and module=(%s);''', (course_id, 16))
		except Error as e:
			logger.error("func get_instance")
			logger.error(e)
			return
		data = self.cursor.fetchall()[0][0]
		return data

	def get_context(self, instance_id):
		try:
			self.cursor.execute(f'''SELECT id
                      				FROM moodle.mdl_context
                      				WHERE instanceid=(%s) and contextlevel=(%s);''', (instance_id, 70))
		except Error as e:
			logger.error("func get_context")
			logger.error(e)
			return
		data = self.cursor.fetchall()[0][0]
		return data

	def get_context_category(self, course_id):
		try:
			self.cursor.execute(f'''SELECT id
                      				FROM moodle.mdl_context
                      				WHERE instanceid=(%s) and contextlevel=(%s);''', (course_id, 50))
		except Error as e:
			logger.error("func get_context_category")
			logger.error(e)
			return
		data = self.cursor.fetchall()[0][0]
		return data

	def get_quiz(self, course_id):
		try:
			self.cursor.execute(f'''SELECT id, questionsperpage, timelimit
                      				FROM moodle.mdl_quiz
                      				WHERE course=(%s);''', (course_id, ))
		except Error as e:
			logger.error("func get_quiz")
			logger.error(e)
			return
		data = self.cursor.fetchall()[0]
		return data

	def get_category(self, context_id):
		try:
			self.cursor.execute(f'''SELECT id
                      				FROM moodle.mdl_question_categories
                      				WHERE contextid=(%s) and sortorder=(%s);''', (context_id, 999))
		except Error as e:
			logger.error("func get_category")
			logger.error(e)
			return
		data = self.cursor.fetchall()[0][0]
		return data

	def get_questions(self, category_id):
		try:
			self.cursor.execute(f'''SELECT id
                      				FROM moodle.mdl_question
                      				WHERE category=(%s);''', (category_id, ))
		except Error as e:
			logger.error("func get_questions")
			logger.error(e)
			return
		data = self.cursor.fetchall()
		ids = []
		for item in data:
			ids.append(item[0])
		random.shuffle(ids)
		return ids

	def get_fucking_questions(self, category_id):
		try:
			self.cursor.execute(f'''SELECT id
                      				FROM moodle.mdl_question
                      				WHERE category=(%s) and parent=(%s);''', (category_id, 0))
		except Error as e:
			logger.error("func get_questions")
			logger.error(e)
			return
		data = self.cursor.fetchall()
		ids = []
		i = 0
		for item in data:
			if i == 30:
				break
			ids.append(item[0])
			i += 1
		random.shuffle(ids)
		return ids

	def get_questiontext(self, question):
		try:
			self.cursor.execute(f'''SELECT questiontext
                          			FROM moodle.mdl_question
                          			WHERE id=(%s);''', (question,))
		except Error as e:
			logger.error("func get_questionstext")
			logger.error(e)
			return
		data = self.cursor.fetchall()
		html = HTML2Text()
		html.ignore_emphasis = True
		questiontext = html.handle(data[0][0]).lstrip()
		return questiontext

	def get_answers(self, question):
		try:
			self.cursor.execute(f'''SELECT id, answer, fraction
                          			FROM moodle.mdl_question_answers
                          			WHERE question=(%s);''', (question,))
		except Error as e:
			logger.error("func get_answers")
			logger.error(e)
			return
		data = self.cursor.fetchall()
		return data

	def get_answers_text(self, ans_id, flag=1):
		try:
			self.cursor.execute(f'''SELECT answer
                          			FROM moodle.mdl_question_answers
                          			WHERE id=(%s);''', (ans_id,))
		except Error as e:
			logger.error("func get_answers_text")
			logger.error(e)
			return
		data = self.cursor.fetchone()
		html = HTML2Text()
		if flag == 0:
			return html.handle(data[0]).strip()
		html.ignore_emphasis = True
		text = html.handle(data[0]).strip()
		return text

	def set_attempts_step_data(self, attemptstepid, name, value):
		if type(value) is list:
			str_value = ''
			for num in value:
				str_value += f'{num}, '
			value = str_value[:-2]
		try:
			self.cursor.execute(f'''INSERT INTO moodle.mdl_question_attempt_step_data
                      				(attemptstepid, name, value)
                      				VALUES (%s, %s, %s)''',
								(attemptstepid, name, value))
		except Error as e:
			logger.error("func set_attempts_step_data")
			logger.error(e)
			return
		self.connect.commit()

	def set_attempts_step(self, attempt_id, userid, answers):
		time_ = int(time.time())
		try:
			self.cursor.execute(f'''INSERT INTO moodle.mdl_question_attempt_steps
                  					(questionattemptid, sequencenumber, state, timecreated, userid)
                  					VALUES (%s, %s, %s, %s, %s)''',
								(attempt_id, 0, 'todo', time_, userid))
		except Error as e:
			logger.error("func set_attempts_step")
			logger.error(e)
			return
		lastrowid = self.cursor.lastrowid
		self.set_attempts_step_data(lastrowid, '_order', answers)

		try:
			self.cursor.execute(f'''INSERT INTO moodle.mdl_question_attempt_steps
                  					(questionattemptid, sequencenumber, state, timecreated, userid)
                  					VALUES (%s, %s, %s, %s, %s)''',
								(attempt_id, 1, 'complete', time_, userid))
		except Error as e:
			logger.error("func set_attempts_step")
			logger.error(e)
			return
		lastrowid = self.cursor.lastrowid
		self.set_attempts_step_data(lastrowid, 'answer', 0)

		try:
			self.cursor.execute(f'''INSERT INTO moodle.mdl_question_attempt_steps
                  					(questionattemptid, sequencenumber, state, fraction, timecreated, userid)
                  					VALUES (%s, %s, %s, %s, %s, %s)''',
								(attempt_id, 2, 'gradedright', 1.0000000, time_, userid))
		except Error as e:
			logger.error("func set_attempts_step")
			logger.error(e)
			return
		lastrowid = self.cursor.lastrowid
		self.set_attempts_step_data(lastrowid, '-finish', 1)
		self.connect.commit()

	def set_question_attempts(self, questionusageid, j, question, questionsummary, rightanswer):
		try:
			self.cursor.execute(f'''INSERT INTO moodle.mdl_question_attempts
                         			(questionusageid, slot, behaviour, questionid, variant, maxmark, minfraction, 
                         			maxfraction, flagged, questionsummary, rightanswer, responsesummary, timemodified)
                         			VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',
								(questionusageid, j, 'deferredfeedback', question, 1, 1.0000000, 0.0000000, 1.0000000,
								 0, questionsummary, rightanswer, rightanswer, int(time.time())))
		except Error as e:
			logger.error("func set_question_attempts")
			logger.error(e)
			return
		self.connect.commit()
		return self.cursor.lastrowid

	def set_question_usages(self, context_id):
		try:
			self.cursor.execute(f'''INSERT INTO moodle.mdl_question_usages
                    				(contextid, component, preferredbehaviour) 
                    				VALUES (%s, %s, %s);''',
								(context_id, 'mod_quiz', 'deferredfeedback'))
		except Error as e:
			logger.error("func set_question_usages")
			logger.error(e)
			return
		self.connect.commit()
		return self.cursor.lastrowid

	def set_quiz_attempts(self, quiz, userid, uniqueid, layout, timestart):
		try:
			self.cursor.execute(f'''INSERT INTO moodle.mdl_quiz_attempts
                    				(quiz, userid, attempt, uniqueid, layout, currentpage, preview, state, timestart, 
                    				timemodifiedoffline, sumgrades) 
                    				VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',
								(quiz[0], userid, 1, uniqueid, layout, 0, 0, 'finished', timestart, 0, 0.00000))
		except Error as e:
			logger.error("func set_quiz_attempts")
			logger.error(e)
			return
		self.connect.commit()
		return self.cursor.lastrowid

	def update_quiz_attempts(self, overall, quiz_attempt_id):
		time_ = int(time.time())
		try:
			self.cursor.execute(f'''UPDATE moodle.mdl_quiz_attempts
                    				SET sumgrades=(%s), timemodified=(%s), timefinish=(%s)
                    				WHERE id=(%s);''',
								(overall, time_, time_, quiz_attempt_id))
		except Error as e:
			logger.error("func update_quiz_attempts")
			logger.error(e)
			return
		self.connect.commit()

	def get_enrol_id(self, userid):
		try:
			self.cursor.execute(f'''SELECT enrolid 
                  					FROM moodle.mdl_user_enrolments
                  					WHERE userid=(%s);''',
								(userid, ))
		except Error as e:
			logger.error("func get_enrol_id")
			logger.error(e)
			return
		return self.cursor.fetchall()

	def select_course_id(self, enrol_id):
		try:
			self.cursor.execute(f'''SELECT courseid 
									FROM moodle.mdl_enrol 
									WHERE id=(%s);''',
								(enrol_id,))
		except Error as e:
			logger.error("func select_course_id")
			logger.error(e)
			return
		return self.cursor.fetchall()

	def select_course_ids(self, enrol_id):
		try:
			self.cursor.execute(f'''SELECT courseid 
									FROM moodle.mdl_enrol 
									WHERE id in {enrol_id};''')
		except Error as e:
			logger.error("func select_course_ids")
			logger.error(e)
			return
		return self.cursor.fetchall()

	def delete_enrol_id(self, enrol_id):
		try:
			self.cursor.execute(f'''DELETE FROM moodle.mdl_user_enrolments 
                            		WHERE enrolid=(%s);''',
								(enrol_id, ))
		except Error as e:
			logger.error("func delete_enrol_id")
			logger.error(e)
			return
		self.connect.commit()

	def delete_quiz_attempt(self, quiz_id, user_id):
		try:
			self.cursor.execute(f'''DELETE FROM moodle.mdl_quiz_attempts 
                            		WHERE quiz=(%s) and userid=(%s);''',
								(quiz_id, user_id))
		except Error as e:
			logger.error("func delete_quiz_attempt")
			logger.error(e)
			return
		self.connect.commit()

	def update_question_attempts(self, question_id, usage_id, answer):
		time_ = int(time.time())
		if answer is not None:
			answer += '\n'
		try:
			self.cursor.execute(f'''UPDATE moodle.mdl_question_attempts 
									SET responsesummary=(%s), timemodified=(%s) 
									WHERE questionid=(%s) and questionusageid=(%s);''',
								(answer, time_, question_id, usage_id))
		except Error as e:
			logger.error("func update_question_attempts")
			logger.error(e)
			return
		self.connect.commit()

	def update_question_attempt_step(self, questionattemptid):
		time_ = int(time.time())
		try:
			self.cursor.execute('''UPDATE moodle.mdl_question_attempt_steps
								   SET state=(%s), fraction=(%s), timecreated=(%s)
								   WHERE questionattemptid=(%s) and sequencenumber=(%s);''',
								("gradedwrong", 0.0000000, time_, questionattemptid, 2))
		except Error as e:
			logger.error("func update_question_attempt_step")
			logger.error(e)
			return
		self.connect.commit()

	def update_question_attempt_step_data(self, value, attemptstepid):
		try:
			self.cursor.execute(f'''UPDATE moodle.mdl_question_attempt_step_data
									SET value=(%s)
									WHERE attemptstepid=(%s);''',
								(value, attemptstepid))
		except Error as e:
			logger.error("func update_question_attempt_step_data")
			logger.error(e)
			return
		self.connect.commit()

	def get_attempt_step(self, attemptid):
		try:
			self.cursor.execute(f'''SELECT id 
									FROM moodle.mdl_question_attempt_steps
									WHERE questionattemptid=(%s) and sequencenumber=(%s);''',
								(attemptid, 2))
		except Error as e:
			logger.error("func get_attempt_step")
			logger.error(e)
			return
		return self.cursor.fetchone()[0]

	def select_grade_attempt_step(self, attemptid):
		try:
			self.cursor.execute(f'''SELECT fraction 
									FROM moodle.mdl_question_attempt_steps
									WHERE questionattemptid=(%s) and sequencenumber=(%s);''',
								(attemptid, 2))
		except Error as e:
			logger.error("func select_grade_attempt_step")
			logger.error(e)
			return
		return self.cursor.fetchone()[0]

	def select_all_question_attempts(self, usage_id):
		try:
			self.cursor.execute(f'''SELECT id 
									FROM moodle.mdl_question_attempts
									WHERE questionusageid=(%s);''',
								(usage_id, ))
		except Error as e:
			logger.error("func select_all_question_attempts")
			logger.error(e)
			return
		return self.cursor.fetchall()

	def select_id_question_attempts(self, question_id, usage_id):
		try:
			self.cursor.execute(f'''SELECT id 
									FROM moodle.mdl_question_attempts
									WHERE questionid=(%s) and questionusageid=(%s);''',
								(question_id, usage_id))
		except Error as e:
			logger.error("func select_all_question_attempts")
			logger.error(e)
			return
		return self.cursor.fetchone()[0]

	def select_code_customcert(self, code):
		try:
			self.cursor.execute('''SELECT * 
									FROM moodle.mdl_customcert_issues
									WHERE code=(%s);''', (code, ))
		except Error as e:
			logger.error('func select_code_customcert')
			logger.error(e)
			return
		result = self.cursor.fetchall()
		if len(result) == 0:
			return None
		return result

	def insert_customcert(self, userid, customcertid, code):
		time_ = int(time.time())
		try:
			self.cursor.execute(f'''INSERT INTO moodle.mdl_customcert_issues
		                    		(userid, customcertid, code, emailed, timecreated) 
		                    		VALUES (%s, %s, %s, %s, %s);''',
								(userid, customcertid, code, 0, time_))
		except Error as e:
			logger.error("func insert_customcert")
			logger.error(e)
			return
		self.connect.commit()

	def select_customcertid(self, course, level):
		try:
			self.cursor.execute(f'''SELECT customcert_id
									FROM moodle_additional.customcert_additional
									WHERE course=(%s) and level=(%s);''',
								(course, level))
		except Error as e:
			logger.error("func select_customcertid")
			logger.error(e)
			return
		return self.cursor.fetchone()[0]

	def select_customcertid_all(self, course):
		try:
			self.cursor.execute(f'''SELECT customcert_id
									FROM moodle_additional.customcert_additional
									WHERE course=(%s)''',
								(course, ))
		except Error as e:
			logger.error("func select_customcertid_all")
			logger.error(e)
			return
		return self.cursor.fetchall()

	def select_customcertid_userid_to_delete(self, userid, customcert_id):
		try:
			self.cursor.execute(f'''SELECT id
									FROM moodle.mdl_customcert_issues
									WHERE userid=(%s) and customcertid=(%s);''',
								(userid, customcert_id))
		except Error as e:
			logger.error("func select_customcertid_all")
			logger.error(e)
			return
		return self.cursor.fetchall()

	def check_quiz_aatem(self, userid, quiz):
		try:
			self.cursor.execute(f'''SELECT id
									FROM moodle.mdl_quiz_attempts
									WHERE userid=(%s) and quiz=(%s);''',
								(userid, quiz))
		except Error as e:
			logger.error("func check_quiz_aatem")
			logger.error(e)
			return
		result = self.cursor.fetchall()
		if len(result) == 0:
			return None
		return result

	def delete_customcert(self, is_id):
		try:
			self.cursor.execute(f'''DELETE FROM moodle.mdl_customcert_issues
									WHERE id=(%s);''',
								(is_id, ))
		except Error as e:
			logger.error("func delete_customcert")
			logger.error(e)
			return
		self.connect.commit()


def main():
	sql = SQL_db()


if __name__ == "__main__":
	main()
