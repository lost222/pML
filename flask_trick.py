#一些FLask个人经验

# 路由
# 上面写应对的请求地址和请求类型，下面写应对方式， render_template函数能返回自己写的HTML模板
            #要传递到jinja2模板的数据写入render_template 函数
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print('login')
    if form.validate_on_submit():
        print(form.email.data)
    return render_template('login.html', form=form)
    
#    jinja2 模板  主要有两种不同于HTML的东西
#     1， 语句{% extends "bootstrap/base.html" %}  继承
#         {% block head %}{% endblock %} 板块
#      逻辑    {% for i in Data.keys() %}
#       {% if i!='Album' %}
#           <div class="Datarow" style="height: 30px; margin: 0; padding: 3px; background:#96c2f1; font-weight: 500 ;color: cornsilk;border:1px solid lavenderblush;"><td class="dataitem">{{ i }}  :  </td>
#           {%-for j in Data.get(i)-%}
#               <td>{{ j }}  ||  </td>
#          注意end     {%-endfor-%}
#               {% endif %}

#    2. 数据， 由路由函数传入
#        {{ i }}  符合python语法， 但是似乎不能定义



# 扩展往往通过如下的方法实现


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


# 表单的提交要定义对应的类， 而且这个类定义了就必须用，不然会报错

class LoginForm(FlaskForm):
    select = StringField(u'select', validators=[
                DataRequired(), Length(1, 64)]
                )
    table = StringField(u'from',
                  validators=[DataRequired()])
    where = StringField(u'where', validators=[
        DataRequired(), Length(1, 64)
        ])

    submit = SubmitField(u'search')
    
#用法
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print('login')
    if form.validate_on_submit():
        print(form.email.data)
    return render_template('login.html', form=form)
