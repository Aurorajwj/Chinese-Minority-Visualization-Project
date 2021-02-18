from flask import render_template,flash
from . import nationality
from .forms import NameForm
from ..model import Nationmain,Area
@nationality.route('/', methods=['GET', 'POST'])
def index():
    name = None
    # 生成实例
    form = NameForm()
    wordc=''
    # 如果用户提交
    if form.validate_on_submit():
        # 用户输入的数据传给name,再置空
        name = form.name.data
        form.name.data = ''
        # name是用户输入的name，是表单的data
        word = Nationmain.query.filter_by(name=name).first()
        if (word):
            wordc = word.comment
        else:
            wordc = '不存在这个民族或输入有误！'
    #气泡图列表
    li= Area.query.with_entities(Area.area,Area.total,Area.han).distinct().all()
    print(li)
    #词云图列表
    li2=Nationmain.query.with_entities(Nationmain.name, Nationmain.overview,Nationmain.clothing).distinct().all()
    print(li2)

    return render_template('index.html', form=form, name=name, wordc=wordc, li=li, li2=li2)

