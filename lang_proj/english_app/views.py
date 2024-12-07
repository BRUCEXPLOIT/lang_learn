from django.shortcuts import render

# Create your views here.
def learn(request):
    return render(request,'learning_path.html')
#nationalites
def n_b_quiz(request):
    return render(request,'nat_L1.html')
def n_m_quiz(request):
    return render(request,'nat_L2.html')
def n_a_quiz(request):
    return render(request,'nat_L3.html')
#proffesional
def prof_b_quiz(request):
    return render(request,'prof_L1.html')
def prof_m_quiz(request):
    return render(request,'prof_L2.html')
def prof_a_quiz(request):
    return render(request,'prof_L3.html')
#people
def ppl_b_quiz(request):
    return render(request,'ppl_L1.html')
def ppl_m_quiz(request):
    return render(request,'ppl_L2.html')
def ppl_a_quiz(request):
    return render(request,'ppl_L3.html')
#places
def plc_b_quiz(request):
    return render(request,'plc_L1.html')
def plc_m_quiz(request):
    return render(request,'plc_L2.html')
def plc_a_quiz(request):
    return render(request,'plc_L3.html')
#food
def fod_b_quiz(request):
    return render(request,'fod_L1.html')
def fod_m_quiz(request):
    return render(request,'fod_L2.html')
def fod_a_quiz(request):
    return render(request,'fod_L3.html')
#color
def clr_b_quiz(request):
    return render(request,'clr_L1.html')
def clr_m_quiz(request):
    return render(request,'clr_L2.html')
def clr_a_quiz(request):
    return render(request,'clr_L3.html')
#weather
def wth_b_quiz(request):
    return render(request,'wth_L1.html')
def wth_m_quiz(request):
    return render(request,'wth_L2.html')
def wth_a_quiz(request):
    return render(request,'wth_L3.html')
#technology
def tec_b_quiz(request):
    return render(request,'tec_L1.html')
def tec_m_quiz(request):
    return render(request,'tec_L2.html')
def tec_a_quiz(request):
    return render(request,'tec_L3.html')
