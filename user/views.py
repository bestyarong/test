from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password

from .forms import RegisterForm
from .models import User
# Create your views here.

# 注册账号
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            # 创建 User 对象，并修改密码
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            # 写入 session 数据
            request.session['uid'] = user.id
            request.session['nickname'] = user.nickname
            return redirect('/user/info/')
        else:
            return render(request, 'register.html', {'errors':form.errors})
    return render(request,'register.html')


# 登录账号
def user_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        try:
            user = User.objects.get(nickname=nickname)
        except User.DoesNotExist as e:
            return render(request,'login.html',{'errors':'账号错误'})
        if check_password(password,user.password):
            request.session['uid'] = user.id
            request.session['nickname'] = user.nickname
            return redirect('/user/info/')
        else:
            return render(request, 'login.html', {'error': '密码错误'})




# 显示主页
def user_info(request):
    uid = request.session.get('uid')
    if uid:
        user = User.objects.get(id=uid)
        return render(request, 'info.html', {'user': user})
    else:
        return render(request, 'login.html', {})


# 退出
def logout(request):
    request.session.flush()
    return redirect('/')

