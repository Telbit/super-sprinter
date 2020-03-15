from flask import Flask, render_template, request, redirect, url_for
from _collections import OrderedDict

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()

    return render_template('list.html', user_stories=user_stories, headers=data_handler.DATA_HEADER)


@app.route('/story', methods=['GET', 'POST'])
def story_page():
    new_data = OrderedDict()
    user_stories = data_handler.get_all_user_story()
    if request.method == 'POST':
        new_data['id'] = len(user_stories) + 1
        new_data['title'] = request.form['story_title']
        new_data['user_story'] = str(request.form["user_story"]).replace('\n', '<br>')
        new_data['acceptance_criteria'] = str(request.form["acceptance_criteria"]).replace('\n', '<br>')
        new_data['business_value'] = request.form['business_value']
        new_data['estimation'] = request.form['estimation']
        new_data['status'] = 'no status'
        user_stories.append(new_data)
        data_handler.write_data(user_stories)
    return render_template('story.html', statuses=data_handler.STATUSES,
                           status_visibility='hidden', button_text='Add new User Story')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
