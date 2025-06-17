from flask import session, request, redirect, url_for

LANGUAGES = {
    'en': 'English', 
    'fr': 'Français', 
    'zh_Hans_CN': 'Chinese', 
    'my_MM' : 'Myanmar',
    'mi' : 'Te Reo Māori'
}

def get_locale():
    lang = session.get('language')
    if lang in LANGUAGES:
        return lang
    #print(lang)
    return request.accept_languages.best_match(LANGUAGES.keys())


def change_language(lang):
    if lang in LANGUAGES:
        session['language'] = lang
        session.permanent = True
    return redirect(request.referrer or url_for('index'))