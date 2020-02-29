from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    twitter = models.URLField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    texto = models.TextField()
    categorias = models.ManyToManyField(Categoria, related_name="posts")

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    autor = models.CharField(max_length=30)
    comentario = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.autor} no post {self.post}"

class Produto(models.Model):
    descricao = models.CharField(max_length=50)
    preco = models.FloatField(null=False)
    
    def __str__(self):
        return self.descricao

class Carrinho(models.Model):
    usuario = models.CharField(max_length=30)
    data_criacao = models.DateField(auto_now_add=True)
    produtos = models.ManyToManyField(Produto, related_name="carrinhos")
    
    def valor_total(self):
        return self.produtos.all().aggregate(models.Sum('preco'))

    def __str__(self):
        return f"Carrinho do usuario {self.usuario} criado em {self.data_criacao}"