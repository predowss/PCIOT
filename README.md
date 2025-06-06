# 🏫 Sistema de Detecção de Apagão com Reconhecimento de Gestos

Este projeto foi desenvolvido com Python e MediaPipe para **escolas**, com o objetivo de oferecer uma solução prática e acessível para **situações de apagão** em salas de aula e ambientes escolares.

O sistema reconhece ambientes escuros, emite alertas sonoros e permite que alunos ou professores **se comuniquem usando gestos simples**, mesmo na ausência total de luz.

---

## 🎯 Objetivo

Facilitar a resposta da comunidade escolar durante quedas de energia, promovendo **segurança**, **comunicação não verbal** e **acessibilidade**.

---

## 💡 Funcionalidades

- ✅ Detecta **apagões** automaticamente após 5 segundos de ambiente escuro.
- 🔊 Emite **alarme sonoro contínuo** com aviso visual: “APAGÃO DETECTADO!”
- ✋ Reconhece o gesto de **dois dedos levantados** (indicador e médio) como sinal de **socorro**.
- 🖐️ Cancela o alarme automaticamente se a **mão aberta** for mostrada após o retorno da luz.
- 🧑‍🎓 Detecta **rostos** para verificar se há pessoas visíveis no ambiente.
- 🌙 Ativa **modo noturno automático**, invertendo as cores da imagem para facilitar a visualização no escuro.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10**
- **OpenCV** – para acesso à webcam e manipulação de imagem.
- **MediaPipe** – para detecção de mãos e rostos.
- **Pygame** – para execução e controle de som.
- **Numpy** – para análise de brilho da imagem.

---

## 📂 Estrutura do Projeto

```
📁 detector-apagao/
├── main.py           # Código principal do projeto
├── alarme.mp3        # Arquivo de som usado como alarme
└── README.md         # Instruções e documentação
```

---

## ▶️ Como Executar

1. Instale as dependências no terminal:

```bash
pip install opencv-python mediapipe pygame numpy
```

2. Coloque o arquivo `alarme.mp3` (disponível no repositório ou fornecido separadamente) **na mesma pasta do arquivo `main.py`**.

3. Execute o projeto com:

```bash
python main.py
```

---

## 🎬 Vídeo de Demonstração

📺 Link: (https://www.youtube.com/watch?v=dSYspDJohuM)

No vídeo, mostramos:
- A detecção automática do apagão.
- O gesto de socorro com dois dedos.
- A parada do alarme ao detectar mão aberta e retorno da luz.
- O modo noturno e a detecção facial em ação.

---

## 👨‍🏫 Aplicação em Escolas

Este sistema pode ser usado:
- Em **salas de aula**, para auxiliar alunos e professores durante quedas de luz.
- Em **salas de informática, bibliotecas e corredores**, com um computador comum e webcam.
- Em ambientes com alunos com deficiência visual ou auditiva, facilitando a **comunicação visual e sonora** por gestos simples.

---

## 👥 Integrantes

- **[Pedro Henrique Alves Guariente]** – RM550301  
- **[David de Medeiros Pacheco Junior ]** – RM551462  
- **[Orlando Akio Morii Cardoso]** – RM98067

---

## 📌 Observações

- O projeto não exige conexão com internet nem dispositivos externos (Arduino, ESP32, etc.).
- Pode ser instalado em qualquer computador com webcam.
- O som pode ser substituído por arquivos personalizados.
