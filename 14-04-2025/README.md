<center><h1>Projeto de cadastro</h1></center>

**Introdução:** A inteção é de fato fazer um sistema de cadastro de usuários mas a inteção é deixar o mais complexo possivel na inteção de mostrar minhas habilidades reais durante o desenvolvimento. 

O projeto inteiro será feito em python e será inclusa libs externas e interna mas ficará limitado a linha de comando por motivos de simplicidade e desafio pessoal.

___

<center><h2>Formas de inicialização</h2></center>
<br>

#### Interpretador do Python
**OBS:** É necessario que seu computador tenha o python instalado de preferencia a versão mais recente.

```bash
python ./index.py
```
<br>

#### Dockerfile
É necessario que sua maquina tenha instalado o docker para fazer isso funcionar.

1) Para compilar a imagem personalizada.
    ```bash
    docker build -t <Name_image> .
    ```

2) Executa o container em modo interativo com a criação de um container.
    ```bash
    docker run -it --name <Name_Container> <Name_Image>
    ```
    - Ou você tabém pode executar pela imagem diretamente com o modo interativo.
        ```bash
        docker run -it <Name_Image>
        ```
___
### Créditos
**Desenvolvido por: Victor Alex Moreira Gouveia**
**Link do perfil no github:** [Perfil do GitHub](https://github.com/VictorAlexMoreiraGouveiaEtec24034/DS)