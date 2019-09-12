# Pacote de controle do rosto animatrônico da Doris

Crie um workspace ROS com o nome "faceDoris" na raiz do usuário

``` mkdir -p ~/faceDoris/src ```

``` cd ~/faceDoris/```

``` catkin_make ```

Dê um ``` git clone https://github.com/TauraBots/robotFace ``` dentro do "src" e de ``` catkin_make ``` no workspace

Use  ``` rosrun ... ``` para executar os nós um por um (vou criar os launchs logo).

Com o comando ``` rosrun robotFace faceMonitoring.py ``` você pode observar o comportamento discretizado dos motores em tempo real.

![alt text](https://i.imgur.com/kBRv57p.png)
