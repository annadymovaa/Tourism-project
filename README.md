# Tourism-project

Для сохранения датасета, найденного на kaggle.com, я решила воспользоваться API и написать bash скрипт (kaggle.sh) для автоматизации процесса. Кто смотрит это на винде, простите
https://github.com/Kaggle/kaggle-cli/tree/main

Чтобы запустить мой скрипт kaggle.sh, нужно было добавить разрешение на исполнение файла и добавить в директорию ~/.kaggle/ .json файл с моим логином и API токеном. В терминале использовала такие команды (не стала писать отдельный скрипт):

  chmod +x kaggle.sh
  cd ~/.kaggle/
  touch kaggle.json
  nano kaggle.json
