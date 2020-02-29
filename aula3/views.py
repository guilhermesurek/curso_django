from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import socket


def index(request):
    html = "<h1>Welcome</h1>"
    response = HttpResponse(html)
    response['Data-Atual'] = timezone.localtime(timezone.now())

    return response


# Function to display hostname and
# IP address por cokkie
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname()


def setCookie(request):
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)

    response = HttpResponse()
    response.set_cookie("my_name", value=host_ip)

    return response


def redirect(request):
    return HttpResponseRedirect('https://uol.com.br')


def show_code(resquest, code):
    html = "<h1> 0 codigo é {code} </<h1>"
    response = HttpResponse(html)
    return response


def catting(request, code):
    return HttpResponseRedirect(f'https://http.cat/{code}')


def show_get_status(request):
    nome = request.GET.get("nome", None)
    if nome is None:
        html = f"<h1> welcome user anonymo <h1>"
    else:
        html = f"<h1> Bem vindo {nome} - {teste} </h1>"
    return HttpResponse(html)


@csrf_exempt
def show_post_values(request):
    head = ""
    if request.method == "POST":
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        head += f"<h1> bem vindo {nome} {sobrenome}</h1>"
    html = """
    <form method=POST>
    <label for="nome">First name:</label><br>
    <input type="text" id="nome" name="nome" value=""><br>
    <label for="sobrenome">Last name:</label><br>
    <input type="text" id="sobrenome" name="sobrenome" value=""><br><br>
    <input type="submit" value="Enviar">
    </form> 
    """
    html_to_response = head+html
    return HttpResponse(html_to_response)