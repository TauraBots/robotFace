# Pacote de controle do rosto animatrônico da Doris

- CONSTRUINDO O PACOTE 

Crie um workspace ROS com o nome "faceDoris" na raiz do usuário...

` mkdir -p ~/faceDoris/src `

` cd ~/faceDoris/`

` catkin_make `

Dê um

` git clone https://github.com/TauraBots/robotFace --recursive ` 

dentro do "src" e de ` catkin_make ` no workspace.

- CONFIGURANDO O PACOTE

Precisamos configurar o PyDynamixel manualmente. 

Para fazer isso vá até o endereço `robotFace/src/PyDynamixel/pyjoints.py`

Agora abra e altere o "sys.path.append" apropriadamente para o seu computador.

Precisamos alterar mais um valor manualmente, esse esta no endereço `robotFace/src/PyDynamixel/dynamixel/dynamixel_functions.py`

Dessa vez altere de forma apropriada os parâmetros da função "cdll.LoadLibrary"

**Pronto, tudo configurado!**

- USANDO O PACOTE

Existem dois arquivos .launch para ser executados... o "withMonitor.launch" abre uma janela que possibilita observar o comportamento discretizado dos motores em tempo real. Enquanto o arquivo "withoutMonitor.launch" apenas executa os nodes (sem uma interface gráfica). Para executa-los, respectivamente, use:

` roslaunch robotFace withMonitor.launch  `

` roslaunch robotFace withoutMonitor.launch  `

![alt text](https://i.imgur.com/kBRv57p.png)
